#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/yy/.hermes/workspace/db/回测项目/量价关系信号_alpha市场/代码')
from backtest_v29_next_open import (
    add_signals, run_backtest, DATA_DIR, PERIODS, TOKENS_V29,
    FILL_PROBABILITY, SEED, POSITION_SIZE_PCT, MAX_POSITION_PCT,
    MIN_ORDER_NOTIONAL, SELL_CONFIRM_BARS, MAX_CONSECUTIVE_LOSSES,
    SINGLE_LOSS_STOP_PCT, STOP_LOSS_PCT, SELL_VOL_PCT,
    USE_TIERED_SLIPPAGE, FIXED_SLIPPAGE_BPS
)
import sqlite3
import pandas as pd

DB_PATH = '/Users/yy/.hermes/workspace/db/backtest_experiments.db'

ID_MAP = {'train': 27378, 'test': 27379, 'holdout': 27380}

def save_trade_markers():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for period in ['train', 'test', 'holdout']:
        exp_id = ID_MAP[period]
        subdir, start, end = PERIODS[period]

        trade_markers = []
        for tok in TOKENS_V29:
            fp = list((DATA_DIR / subdir).glob(f'{tok}_aggTrades_*.csv'))
            if not fp:
                continue

            df = pd.read_csv(str(fp[0])).sort_values('trade_ts_ms').copy()
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
                buy_trend_strength_threshold=0.0, qv_min=None, qv_max=None,
                enable_trend_vwap_filter=True,
                trend_vwap_fast_window=120, trend_vwap_slow_window=240)

            res, trd = run_backtest(sig,
                initial_capital_usd=3000.0, fee_bps=5.0,
                position_size_pct=POSITION_SIZE_PCT, max_position_pct=MAX_POSITION_PCT,
                min_order_notional=MIN_ORDER_NOTIONAL, fill_probability=FILL_PROBABILITY, seed=SEED,
                max_consecutive_losses=MAX_CONSECUTIVE_LOSSES, single_loss_stop_pct=SINGLE_LOSS_STOP_PCT,
                sell_vol_pct=SELL_VOL_PCT, stop_loss_pct=STOP_LOSS_PCT,
                sell_confirm_bars=SELL_CONFIRM_BARS)

            for _, t in trd.iterrows():
                ts = t['entry_time'] if t['trade_type'] == 'buy' else t['exit_time']
                ts = str(ts) if ts else ''
                trade_markers.append((
                    exp_id, tok, t['trade_type'], float(t['price']),
                    ts, float(t.get('return_pct', 0) or 0), str(t.get('exit_reason', '')),
                    float(t.get('units', 0) or 0), float(t.get('notional_usd', 0) or 0)
                ))

        cur.executemany('''INSERT INTO trade_markers
            (exp_id, token, trade_type, price, timestamp, return_pct, exit_reason, units, notional_usd)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', trade_markers)

        conn.commit()
        print(f'V29 {period}: trades={len(trade_markers)}, exp_id={exp_id}')

    conn.close()
    print('Done!')

if __name__ == '__main__':
    save_trade_markers()