#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/yy/.hermes/workspace/db/回测项目/量价关系信号_alpha市场/代码')
from backtest_v26_next_open import DATA_DIR, PERIODS, TOKENS_11
import pandas as pd
import sqlite3

DB_PATH = '/Users/yy/.hermes/workspace/db/backtest_experiments.db'

ID_MAP = {'train': 27258, 'test': 27259, 'holdout': 27260}

def save_bar_data():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS bar_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        exp_id INTEGER, token TEXT, timestamp TEXT,
        open REAL, high REAL, low REAL, close REAL,
        volume REAL, quote_volume REAL, bar_index INTEGER,
        FOREIGN KEY (exp_id) REFERENCES backtest_experiments(编号))''')
    conn.commit()

    for period in ['train', 'test', 'holdout']:
        exp_id = ID_MAP[period]
        subdir, start, end = PERIODS[period]

        rows = []
        for tok in TOKENS_11:
            bar_index = 0
            fp = list((DATA_DIR / subdir).glob(f'{tok}_aggTrades_*.csv'))
            if not fp:
                continue

            df = pd.read_csv(fp[0]).sort_values('trade_ts_ms').copy()
            df['ts'] = pd.to_datetime(df['trade_ts_ms'], unit='ms', utc=True)
            df['minute'] = df['ts'].dt.floor('1min')
            tc = 'trade_id' if 'trade_id' in df.columns else 'agg_trade_id'

            bars = df.groupby('minute').agg(
                open=('price', 'first'),
                high=('price', 'max'),
                low=('price', 'min'),
                close=('price', 'last'),
                volume=('qty', 'sum'),
                quote_volume=('quote_qty', 'sum')
            ).reset_index()

            bars = bars[(bars['minute'] >= start) & (bars['minute'] <= f'{end} 23:59:59')].copy()
            if bars.empty:
                continue
            bars = bars.reset_index(drop=True)

            for i, (_, row) in enumerate(bars.iterrows()):
                if i % 10 == 0:
                    rows.append((
                        exp_id, tok.replace('USDT', ''), str(row['minute']),
                        row['open'], row['high'], row['low'], row['close'],
                        row['volume'], row['quote_volume'], bar_index
                    ))
                    bar_index += 1

        cur.executemany('''INSERT INTO bar_data
            (exp_id, token, timestamp, open, high, low, close, volume, quote_volume, bar_index)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            rows)

        conn.commit()
        print(f'V23 {period}: {len(rows)} bars saved for {len(TOKENS_11)} tokens, exp_id={exp_id}')

    conn.close()
    print('Done!')

if __name__ == '__main__':
    save_bar_data()