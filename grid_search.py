import sys
sys.path.insert(0, '/Users/yy/.hermes/workspace/db/回测项目/量价关系信号_alpha市场/代码')
print("Starting...", flush=True)
from backtest_v23_fifo_pyramid import add_signals, run_backtest, DATA_DIR, PERIODS
import pandas as pd
import numpy as np
import time
print("Imports done", flush=True)

tokens = ['ALPHA_41USDT', 'ALPHA_154USDT', 'ALPHA_356USDT', 'ALPHA_428USDT',
          'ALPHA_442USDT', 'ALPHA_474USDT', 'ALPHA_497USDT']

sell_confirms = [0, 1, 2, 3, 5]
stop_losses = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0]

period = 'train'
subdir, start, end = PERIODS[period]

print(f'Grid Search on TRAIN: sell_confirm x stop_loss')
print('='*80)

results = []

for sc in sell_confirms:
    row = f'{sc:>5}'
    for sl in stop_losses:
        all_equities = []

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

            res, _ = run_backtest(sig,
                initial_capital_usd=3000.0, fee_bps=5.0,
                position_size_pct=0.01, max_position_pct=0.90,
                min_order_notional=0.0, fill_probability=0.85, seed=42,
                max_consecutive_losses=0, single_loss_stop_pct=0.0,
                sell_vol_pct=0.05, stop_loss_pct=sl, sell_confirm_bars=sc)

            all_equities.append(res['equity'].values)

        combined = np.concatenate(all_equities)
        total_ret = (sum(eq[-1] for eq in all_equities) / 21000 - 1) * 100
        mdd = ((combined / np.maximum.accumulate(combined)) - 1).min() * 100
        row += f'{total_ret:>7.1f}%'
        results.append((sc, sl, total_ret, mdd))

    print(row)

print('='*80)

print('\nTop 5 (Train Return):')
results.sort(key=lambda x: x[2], reverse=True)
for sc, sl, ret, mdd in results[:5]:
    print(f'  SC={sc}, SL={sl}% => Return={ret:.2f}%, MDD={mdd:.2f}%')