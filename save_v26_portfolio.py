#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/yy/.hermes/workspace/db/回测项目/量价关系信号_alpha市场/代码')
from backtest_v23_fifo_pyramid import add_signals, run_backtest, DATA_DIR, PERIODS
import pandas as pd
import numpy as np
import sqlite3
import json
from datetime import datetime

tokens = ['ALPHA_41USDT', 'ALPHA_154USDT', 'ALPHA_356USDT', 'ALPHA_428USDT',
          'ALPHA_442USDT', 'ALPHA_474USDT', 'ALPHA_497USDT']

db_path = '/Users/yy/.hermes/workspace/db/backtest_experiments.db'

def save_portfolio_with_equity(version_label, strategy_name, stop_loss_pct, sell_confirm_bars, initial_capital=3000.0):
    """Save portfolio-level results with equity curve and comprehensive metrics"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create equity_curves table if not exists
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS equity_curves (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        exp_id INTEGER,
        策略版本 TEXT,
        数据集 TEXT,
        bar_index INTEGER,
        timestamp TEXT,
        equity REAL,
        position REAL,
        price REAL,
        cash REAL,
        drawdown REAL,
        FOREIGN KEY (exp_id) REFERENCES backtest_experiments(编号)
    )
    ''')
    conn.commit()

    for period in ['train', 'test', 'holdout']:
        subdir, start, end = PERIODS[period]

        all_equities = []
        all_positions = []
        all_prices = []
        all_cash = []
        all_timestamps = []
        all_trades = []

        # Run backtest for each token
        for tok in tokens:
            fp = list((DATA_DIR / subdir).glob(f'{tok}_aggTrades_*.csv'))
            if not fp:
                continue

            df = pd.read_csv(fp[0]).sort_values('trade_ts_ms').copy()
            df['ts'] = pd.to_datetime(df['trade_ts_ms'], unit='ms', utc=True)
            df['minute'] = df['ts'].dt.floor('1min')
            bars = df.groupby('minute').agg(
                close=('price', 'last'), volume=('qty', 'sum'),
                quote_volume=('quote_qty', 'sum'), trades=('agg_trade_id', 'count')
            ).reset_index()
            bars = bars[(bars['minute'] >= start) & (bars['minute'] <= f'{end} 23:59:59')].copy()
            bars = bars.reset_index(drop=True)

            sig = add_signals(bars,
                vwap_sustain=1, vwap_type='rolling', vwap_window=60,
                vwap_signal_mode='dual_vwap_cross', vwap_fast_window=40, vwap_slow_window=120,
                buy_trend_strength_threshold=0.0, qv_floor_window=60, qv_floor_quantile=0.0,
                qv_min=100.0, qv_max=1000.0, enable_trend_vwap_filter=True,
                trend_vwap_fast_window=120, trend_vwap_slow_window=240)

            res, trd = run_backtest(sig,
                initial_capital_usd=initial_capital, fee_bps=5.0,
                position_size_pct=0.01, max_position_pct=0.90,
                min_order_notional=0.0, fill_probability=0.85, seed=42,
                max_consecutive_losses=0, single_loss_stop_pct=0.0,
                sell_vol_pct=0.05, stop_loss_pct=stop_loss_pct, sell_confirm_bars=sell_confirm_bars)

            all_equities.append(res['equity'].values)
            all_positions.append(res['position'].values)
            all_prices.append(res['close'].values)
            all_timestamps.append(res['minute'].values)
            all_trades.append(trd)

        # Calculate portfolio-level metrics
        combined_eq = np.concatenate(all_equities)
        total_initial = initial_capital * len(tokens)
        total_ret = (sum(eq[-1] for eq in all_equities) / total_initial - 1) * 100
        mdd = ((combined_eq / np.maximum.accumulate(combined_eq)) - 1).min() * 100

        returns = np.diff(combined_eq) / combined_eq[:-1]
        returns = returns[~np.isnan(returns)]
        sharpe = np.mean(returns) / np.std(returns) * np.sqrt(525600) if len(returns) > 0 and np.std(returns) > 0 else 0

        # Trade-level metrics
        all_sells = pd.concat(all_trades)
        all_sells = all_sells[all_sells['trade_type'] == 'sell']

        wins = all_sells[all_sells['return_pct'] > 0]
        losses = all_sells[all_sells['return_pct'] <= 0]

        win_rate = len(wins) / len(all_sells) * 100 if len(all_sells) > 0 else 0
        gross_profit = wins['return_pct'].sum() if len(wins) > 0 else 0
        gross_loss = abs(losses['return_pct'].sum()) if len(losses) > 0 else 0
        net_profit = gross_profit - gross_loss
        fee_total = len(all_sells) * 10 * 2 if len(all_sells) > 0 else 0  # 5 bps each direction * 2
        fee_adjusted_profit = net_profit - fee_total

        profit_factor = gross_profit / gross_loss if gross_loss > 0 else 0
        total_trades = sum(len(trd) for trd in all_trades)

        # Volume metrics
        total_buy_vol = sum(trd[trd['trade_type']=='buy']['notional_usd'].sum() for trd in all_trades)
        total_sell_vol = sum(trd[trd['trade_type']=='sell']['notional_usd'].sum() for trd in all_trades)
        total_volume = total_buy_vol + total_sell_vol
        volume_ratio = net_profit / total_volume * 10000 if total_volume > 0 else 0  # bp
        fee_adjusted_volume_ratio = fee_adjusted_profit / total_volume * 10000 if total_volume > 0 else 0

        params = {
            'mode': 'fifo_pyramid',
            'stop_loss_pct': stop_loss_pct,
            'sell_confirm_bars': sell_confirm_bars,
            'cash_constraint': True,
            'tokens': tokens
        }

        # Save to backtest_experiments
        cursor.execute('''INSERT INTO backtest_experiments
            (创建时间, 实验名, 策略版本, 数据集, 总收益率, 最大回撤, 交易次数, 胜率, 夏普比率,
             方向, 标签, 参数JSON, 备注, 成交量USD,
             毛利润, 净利润, 费后利润, 成交额比率, 费后成交额比率)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (datetime.now().strftime('%Y-%m-%d %H:%M:%S'), strategy_name, version_label, period,
             total_ret, mdd, total_trades, win_rate, sharpe,
             'long', version_label, json.dumps(params, ensure_ascii=False),
             f'FIFO pyramid, SC={sell_confirm_bars}, SL={stop_loss_pct}%, portfolio',
             total_volume, gross_profit, net_profit, fee_adjusted_profit,
             volume_ratio, fee_adjusted_volume_ratio))

        exp_id = cursor.lastrowid

        # Save equity curve (downsampled to every 10th bar to save space)
        combined_positions = np.concatenate(all_positions)
        combined_prices = np.concatenate(all_prices)
        combined_timestamps = np.concatenate(all_timestamps)

        equity_curve = []
        for i in range(0, len(combined_eq), 10):  # Every 10th bar
            pos_val = combined_positions[i] * combined_prices[i]
            cash = combined_eq[i] - pos_val
            running_max = np.maximum.accumulate(combined_eq[:i+1])[-1] if i > 0 else combined_eq[0]
            drawdown = (combined_eq[i] / running_max - 1) * 100 if running_max > 0 else 0

            equity_curve.append({
                'exp_id': exp_id,
                '策略版本': version_label,
                '数据集': period,
                'bar_index': i,
                'timestamp': str(combined_timestamps[i]),
                'equity': combined_eq[i],
                'position': combined_positions[i],
                'price': combined_prices[i],
                'cash': cash,
                'drawdown': drawdown
            })

        cursor.executemany('''INSERT INTO equity_curves
            (exp_id, 策略版本, 数据集, bar_index, timestamp, equity, position, price, cash, drawdown)
            VALUES (:exp_id, :策略版本, :数据集, :bar_index, :timestamp, :equity, :position, :price, :cash, :drawdown)''',
            equity_curve)

        conn.commit()
        print(f'  {period}: Ret={total_ret:.2f}%, MDD={mdd:.2f}%, Sharpe={sharpe:.2f}, '
              f'NetProfit={net_profit:.2f}%, Volume={total_volume:,.0f}, '
              f'VolumeRatio={volume_ratio:.2f}bp, exp_id={exp_id}')

    conn.close()
    print(f'{version_label} saved with equity curves!')

if __name__ == '__main__':
    # V26: SC=3, SL=3.0%
    save_portfolio_with_equity('V26', 'V26_FIFO_SC3_SL3_portfolio', 3.0, 3)