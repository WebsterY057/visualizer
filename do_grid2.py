#!/usr/bin/env python3
import sys
import os

log_file = open('/tmp/grid_results.log', 'w')
def log(msg):
    log_file.write(msg + '\n')
    log_file.flush()

log('Starting grid search')

sys.path.insert(0, '/Users/yy/.hermes/workspace/db/回测项目/量价关系信号_alpha市场/代码')
from backtest_v23_fifo_pyramid import add_signals, run_backtest, DATA_DIR, PERIODS
import pandas as pd
import numpy as np

tokens = ['ALPHA_41USDT', 'ALPHA_154USDT', 'ALPHA_356USDT', 'ALPHA_428USDT',
          'ALPHA_442USDT', 'ALPHA_474USDT', 'ALPHA_497USDT']

period = 'train'
subdir, start, end = PERIODS[period]

# Pre-load all signals
log('Loading signals for all tokens...')
all_sigs = {}
for tok in tokens:
    fp = list((DATA_DIR / subdir).glob(f'{tok}_aggTrades_*.csv'))
    df = pd.read_csv(fp[0]).sort_values('trade_ts_ms').copy()
    df['ts'] = pd.to_datetime(df['trade_ts_ms'], unit='ms', utc=True)
    df['minute'] = df['ts'].dt.floor('1min')
    bars = df.groupby('minute').agg(close=('price','last'), volume=('qty','sum'), quote_volume=('quote_qty','sum'), trades=('agg_trade_id','count')).reset_index()
    bars = bars[(bars['minute'] >= start) & (bars['minute'] <= f'{end} 23:59:59')].copy().reset_index(drop=True)
    sig = add_signals(bars, vwap_sustain=1, vwap_type='rolling', vwap_window=60, vwap_signal_mode='dual_vwap_cross', vwap_fast_window=40, vwap_slow_window=120, buy_trend_strength_threshold=0.0, qv_floor_window=60, qv_floor_quantile=0.0, qv_min=100.0, qv_max=1000.0, enable_trend_vwap_filter=True, trend_vwap_fast_window=120, trend_vwap_slow_window=240)
    all_sigs[tok] = sig
    log(f'  {tok} loaded')

log('')
log('Grid search (7 tokens portfolio, train):')
log('SC\SL     ')
for sl in [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]:
    log(f'{sl:>8.1f}%', end='')
log('')

results = []
for sc in [0, 1, 2, 3, 5]:
    log(f'{sc:>6}', end='')
    for sl in [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]:
        all_eq = []
        for tok in tokens:
            res, _ = run_backtest(all_sigs[tok], initial_capital_usd=3000.0, fee_bps=5.0, position_size_pct=0.01, max_position_pct=0.90, min_order_notional=0.0, fill_probability=0.85, seed=42, max_consecutive_losses=0, single_loss_stop_pct=0.0, sell_vol_pct=0.05, stop_loss_pct=sl, sell_confirm_bars=sc)
            all_eq.append(res['equity'].values)
        combined = np.concatenate(all_eq)
        total_ret = (sum(eq[-1] for eq in all_eq) / 21000 - 1) * 100
        mdd = ((combined / np.maximum.accumulate(combined)) - 1).min() * 100
        log(f'{total_ret:>7.1f}%', end='')
        results.append((sc, sl, total_ret, mdd))
    log('')

log('')
log('Top 5 by Return:')
for r in sorted(results, key=lambda x: x[2], reverse=True)[:5]:
    log(f'  SC={r[0]}, SL={r[1]}% => Return={r[2]:.2f}%, MDD={r[3]:.2f}%')

log('')
log('Top 5 by lowest MDD:')
for r in sorted(results, key=lambda x: x[3])[:5]:
    log(f'  SC={r[0]}, SL={r[1]}% => Return={r[2]:.2f}%, MDD={r[3]:.2f}%')

log_file.close()
print('Done - see /tmp/grid_results.log')