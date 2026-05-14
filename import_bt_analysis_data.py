#!/usr/bin/env python3
"""
导入回测分析数据到 backtest_experiments.db
从CSV构建 bar_data + trade_markers 表，与原表结构一致（中文列名）
"""
import sys
sys.path.insert(0, '/Users/yy/.hermes/workspace/db/回测项目/量价关系信号_alpha市场/代码')
from backtest_v29_next_open import add_signals, DATA_DIR, PERIODS, TOKENS_V29
import pandas as pd
import sqlite3

DB_PATH = '/Users/yy/.hermes/workspace/db/backtest_experiments.db'


def get_exp_info():
    """查询数据库获取实验的版本和周期信息"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT 编号, 策略版本, 数据集 FROM backtest_experiments WHERE 来源='本地'")
    rows = cur.fetchall()
    conn.close()
    info = {}
    for exp_id, version, dataset in rows:
        info[exp_id] = {'version': version, 'dataset': dataset}
    return info


def ensure_columns():
    """确保bar_data和trade_markers表有所需的列"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # bar_data: 确保有signal列
    try:
        cur.execute("ALTER TABLE bar_data ADD COLUMN signal INTEGER DEFAULT 0")
        conn.commit()
        print("  -> 添加 bar_data.signal 列")
    except:
        pass
    conn.close()


def import_for_version(version_key, exp_ids_by_period):
    """为一个策略版本导入所有周期的bar_data"""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for period in ['train', 'test', 'holdout']:
        exp_id = exp_ids_by_period.get(period)
        if not exp_id:
            continue

        # 清空旧数据
        cur.execute('DELETE FROM bar_data WHERE exp_id = ?', (exp_id,))
        cur.execute('DELETE FROM trade_markers WHERE exp_id = ?', (exp_id,))

        subdir, start, end = PERIODS[period]
        print(f"  处理 {version_key}/{period} (exp_id={exp_id})...")

        total_bars = 0
        total_trades = 0

        for tok in TOKENS_V29:
            fp = list((DATA_DIR / subdir).glob(f'{tok}_aggTrades_*.csv'))
            if not fp:
                continue

            df = pd.read_csv(fp[0]).sort_values('trade_ts_ms').copy()
            df['ts'] = pd.to_datetime(df['trade_ts_ms'], unit='ms', utc=True)
            df['minute'] = df['ts'].dt.floor('1min')
            tc = 'trade_id' if 'trade_id' in df.columns else 'agg_trade_id'

            bars = df.groupby('minute').agg(
                open=('price', 'first'), high=('price', 'max'),
                low=('price', 'min'), close=('price', 'last'),
                volume=('qty', 'sum'), quote_volume=('quote_qty', 'sum'),
                trades=(tc, 'count')
            ).reset_index()

            bars = bars[(bars['minute'] >= start) & (bars['minute'] <= f'{end} 23:59:59')].copy()
            if bars.empty:
                continue
            bars = bars.sort_values('minute').reset_index(drop=True)

            # 生成signal
            sig = add_signals(bars,
                vwap_sustain=1, vwap_type='rolling', vwap_window=60,
                vwap_signal_mode='dual_vwap_cross', vwap_fast_window=40, vwap_slow_window=120,
                buy_trend_strength_threshold=0.0, qv_floor_window=60, qv_floor_quantile=0.0,
                qv_min=100.0, qv_max=1000.0, enable_trend_vwap_filter=True,
                trend_vwap_fast_window=120, trend_vwap_slow_window=240)

            token_name = tok.replace('USDT', '')

            # 保存bar_data（所有行）- signal: 1=buy, -1=sell, 0=none
            bar_rows = []
            for i, row in sig.iterrows():
                if row.get('buy_signal'):
                    sig_val = 1
                elif row.get('sell_signal'):
                    sig_val = -1
                else:
                    sig_val = 0
                bar_rows.append((
                    exp_id, version_key, period, i,
                    str(row['minute']),
                    row['open'], row['high'], row['low'], row['close'],
                    row['volume'], row['quote_volume'], int(row['trades']),
                    sig_val
                ))

            if bar_rows:
                cur.executemany('''INSERT INTO bar_data
                    (exp_id, 策略版本, 数据集, bar_index, timestamp, open, high, low, close, volume, quote_volume, trades, signal)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', bar_rows)

            # 保存trade_markers（买入/卖出信号变化点）
            trade_rows = []
            prev_buy = False
            prev_sell = False
            for i, row in sig.iterrows():
                cur_buy = bool(row.get('buy_signal', False))
                cur_sell = bool(row.get('sell_signal', False))
                # 买入信号出现
                if cur_buy and not prev_buy:
                    trade_rows.append((
                        exp_id, version_key, period, token_name, str(row['minute']),
                        'buy', row['close'], row['volume'],
                        row['quote_volume'], 'buy', 'signal_entry'
                    ))
                # 卖出信号出现
                elif cur_sell and not prev_sell:
                    trade_rows.append((
                        exp_id, version_key, period, token_name, str(row['minute']),
                        'sell', row['close'], row['volume'],
                        row['quote_volume'], 'sell', 'signal_exit'
                    ))
                prev_buy = cur_buy
                prev_sell = cur_sell

            if trade_rows:
                cur.executemany('''INSERT INTO trade_markers
                    (exp_id, 策略版本, 数据集, token, timestamp, signal_type, price, quantity, notional_usd, side, exit_reason)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', trade_rows)
                total_trades += len(trade_rows)

            total_bars += len(bar_rows)

        conn.commit()
        print(f"    -> {total_bars} bars, {total_trades} trades")

    conn.close()


def main():
    print('开始导入回测分析数据...')
    ensure_columns()

    # 查询实验信息
    exp_info = get_exp_info()
    by_version = {}
    for exp_id, info in exp_info.items():
        ver = (info['version'] or '').lower()
        ds = (info['dataset'] or '').lower()
        if ver and ds in ['train', 'test', 'holdout']:
            if ver not in by_version:
                by_version[ver] = {}
            by_version[ver][ds] = exp_id

    print(f'查询到的实验版本: {list(by_version.keys())}')

    for ver, periods in by_version.items():
        if any(v for v in periods.values()):
            import_for_version(ver.upper(), periods)

    # 验证
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM bar_data')
    bar_count = cur.fetchone()[0]
    cur.execute('SELECT COUNT(*) FROM trade_markers')
    trade_count = cur.fetchone()[0]
    cur.execute('SELECT DISTINCT 策略版本, 数据集, COUNT(*) FROM bar_data GROUP BY 1,2')
    breakdown = cur.fetchall()
    conn.close()
    print(f'\n导入完成: bar_data={bar_count}, trade_markers={trade_count}')
    print('各版本分布:')
    for row in breakdown:
        print(f'  {row}')


if __name__ == '__main__':
    main()
