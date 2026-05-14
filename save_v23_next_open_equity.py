#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/yy/.hermes/workspace/db/回测项目/量价关系信号_alpha市场/代码')
from backtest_v23_next_open import add_signals, run_backtest, DATA_DIR, PERIODS, TOKENS_11
import numpy as np
import sqlite3
import pandas as pd

DB_PATH = '/Users/yy/.hermes/workspace/db/backtest_experiments.db'

ID_MAP = {'train': 27261, 'test': 27262, 'holdout': 27263}

def save_equity_curves():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS equity_curves (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        exp_id INTEGER, 策略版本 TEXT, 数据集 TEXT, bar_index INTEGER,
        timestamp TEXT, equity REAL, position REAL, price REAL,
        cash REAL, drawdown REAL,
        FOREIGN KEY (exp_id) REFERENCES backtest_experiments(编号))''')
    conn.commit()

    for period in ['train', 'test', 'holdout']:
        exp_id = ID_MAP[period]
        subdir, start, end = PERIODS[period]

        rows = []
        for tok in TOKENS_11:
            fp = list((DATA_DIR / subdir).glob(f'{tok}_aggTrades_*.csv'))
            if not fp:
                continue

            df = pd.read_csv(fp[0]).sort_values('trade_ts_ms').copy()
            df['ts'] = pd.to_datetime(df['trade_ts_ms'], unit='ms', utc=True)
            df['minute'] = df['ts'].dt.floor('1min')
            tc = 'trade_id' if 'trade_id' in df.columns else 'agg_trade_id'
            bars = df.groupby('minute').agg(
                open=('price', 'first'), close=('price', 'last'), volume=('qty', 'sum'),
                quote_volume=('quote_qty', 'sum'), trades=(tc, 'count')
            ).reset_index()
            bars = bars[(bars['minute'] >= start) & (bars['minute'] <= f'{end} 23:59:59')].copy()
            if bars.empty:
                continue
            bars = bars.reset_index(drop=True)

            sig = add_signals(bars,
                vwap_sustain=1, vwap_type='rolling', vwap_window=60,
                vwap_signal_mode='dual_vwap_cross', vwap_fast_window=40, vwap_slow_window=120,
                buy_trend_strength_threshold=0.0, qv_floor_window=60, qv_floor_quantile=0.0,
                qv_min=100.0, qv_max=1000.0, enable_trend_vwap_filter=True,
                trend_vwap_fast_window=120, trend_vwap_slow_window=240)

            res, trd = run_backtest(sig,
                initial_capital_usd=3000.0, fee_bps=5.0,
                position_size_pct=0.01, max_position_pct=0.90,
                min_order_notional=0.0, fill_probability=0.85, seed=42,
                max_consecutive_losses=0, single_loss_stop_pct=0.0,
                sell_vol_pct=0.05)

            r = res.copy()
            r['token'] = tok
            rows.append(r)

        combined = pd.concat(rows, ignore_index=True).sort_values('minute').reset_index(drop=True)

        # 创建统一的时间索引（所有token的完整时间并集）
        all_minutes = combined['minute'].unique()
        all_minutes = sorted(all_minutes)
        minute_idx = pd.DatetimeIndex(all_minutes)

        # 对每个token的equity做前向填充，然后重新索引到统一时间轴
        portfolio_equity = pd.Series(0.0, index=minute_idx, dtype=float)

        for tok in combined['token'].unique():
            tok_data = combined[combined['token'] == tok].copy()
            tok_data = tok_data.sort_values('minute').set_index('minute')['equity']
            # 前向填充确保每个token在每个时刻都有一个equity值
            tok_data = tok_data.reindex(minute_idx).ffill().fillna(3000.0)  # 初始资金3000
            portfolio_equity = portfolio_equity + tok_data.values

        # 构建结果DataFrame
        result_df = pd.DataFrame({
            'minute': minute_idx,
            'equity': portfolio_equity.values
        })

        result_rows = []
        for bar_index, (_, row) in enumerate(result_df.iterrows()):
            running_max = result_df['equity'].iloc[:bar_index+1].max()
            drawdown = (row['equity'] / running_max - 1) * 100 if running_max > 0 else 0
            result_rows.append((
                exp_id, 'V23', period, bar_index,
                str(row['minute']), row['equity'],
                0, 0, 0, drawdown
            ))

        cur.executemany('''INSERT INTO equity_curves
            (exp_id, 策略版本, 数据集, bar_index, timestamp, equity, position, price, cash, drawdown)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', result_rows)

        conn.commit()
        print(f'V23 {period}: {len(result_rows)} minute bars saved, initial={result_df["equity"].iloc[0]:.0f}, final={result_df["equity"].iloc[-1]:.0f}, exp_id={exp_id}')

    conn.close()
    print('Done!')

if __name__ == '__main__':
    save_equity_curves()