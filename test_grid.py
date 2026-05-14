#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/yy/.hermes/workspace/db/回测项目/量价关系信号_alpha市场/代码')
print("Starting", flush=True)
from backtest_v23_fifo_pyramid import add_signals, run_backtest, DATA_DIR, PERIODS
print("Imported", flush=True)
import pandas as pd
import numpy as np
print("Starting grid search", flush=True)

tokens = ['ALPHA_41USDT']
sell_confirms = [0]
stop_losses = [0.0]

period = 'train'
subdir, start, end = PERIODS[period]

fp = list((DATA_DIR / subdir).glob(f'{tokens[0]}_aggTrades_*.csv'))
df = pd.read_csv(fp[0]).sort_values('trade_ts_ms').copy()
df['ts'] = pd.to_datetime(df['trade_ts_ms'], unit='ms', utc=True)
df['minute'] = df['ts'].dt.floor('1min')
bars = df.groupby('minute').agg(
    close=('price', 'last'), volume=('qty', 'sum'),
    quote_volume=('quote_qty', 'sum'), trades=('agg_trade_id', 'count')
).reset_index()
bars = bars[(bars['minute'] >= start) & (bars['minute'] <= f'{end} 23:59:59')].copy()
bars = bars.reset_index(drop=True)
print(f"Bars: {len(bars)}", flush=True)

sig = add_signals(bars,
    vwap_sustain=1, vwap_type='rolling', vwap_window=60,
    vwap_signal_mode='dual_vwap_cross', vwap_fast_window=40, vwap_slow_window=120,
    buy_trend_strength_threshold=0.0, qv_floor_window=60, qv_floor_quantile=0.0,
    qv_min=100.0, qv_max=1000.0, enable_trend_vwap_filter=True,
    trend_vwap_fast_window=120, trend_vwap_slow_window=240)
print("Signals added", flush=True)

res, trd = run_backtest(sig,
    initial_capital_usd=3000.0, fee_bps=5.0,
    position_size_pct=0.01, max_position_pct=0.90,
    min_order_notional=0.0, fill_probability=0.85, seed=42,
    max_consecutive_losses=0, single_loss_stop_pct=0.0,
    sell_vol_pct=0.05, stop_loss_pct=0.0, sell_confirm_bars=0)
print("Backtest done", flush=True)