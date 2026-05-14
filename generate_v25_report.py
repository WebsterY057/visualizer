import json
from datetime import datetime

with open('/Users/yy/.hermes/workspace/db/visualizer/V25_backtest_report.json', 'r') as f:
    data = json.load(f)

md = f"""# V25 回测报告

## 策略概述

**策略名称**: V25 - FIFO Pyramid + Cash Constraint + 3% Stop Loss
**回测时间**: 2026-05-09
**交易品种**: ALPHA (7 个币种: 41, 154, 356, 428, 442, 474, 497)
**初始资金**: $3,000 / 币种 = $21,000 总计
**数据周期**: Train / Test / Holdout

## 策略逻辑

```
while buy_signal:
    if cash >= $30:
        buy $30 of token (add to FIFO queue)

while sell_signal:
    sell 1 FIFO queue item (oldest first)

if total_position_loss > 3%:
    liquidate entire position (stop loss)
```

## 核心参数

| 参数 | 值 |
|------|-----|
| 每次买入金额 | $30 固定 |
| 卖出方式 | FIFO 队列，先进先出，每次 1 个队列项 |
| 现金约束 | cash >= $30 才能执行买入 |
| 止损阈值 | 整体持仓亏损 > 3% 时全部清仓 |
| 滑点 | 5 bps |
| 手续费 | 5 bps (双向) |
| 成交概率 | 85% |
| VWAP Fast Window | 40 |
| VWAP Slow Window | 120 |
| Trend VWAP Windows | 120 / 240 |
| QV Range | 100 - 1000 |

---

## 组合整体表现 (7 币种合并计算)

| Period | Total Return | Max Drawdown | Sharpe | Sortino | Win Rate | Profit Factor | Total Trades |
|--------|-------------|--------------|--------|---------|----------|--------------|--------------|
| **Train** | {data['train']['portfolio']['total_return']:.2f}% | {data['train']['portfolio']['max_drawdown']:.2f}% | {data['train']['portfolio']['sharpe_ratio']:.2f} | {data['train']['portfolio']['sortino_ratio']:.2f} | {data['train']['portfolio']['win_rate']:.1f}% | {data['train']['portfolio']['profit_factor']:.2f} | {data['train']['portfolio']['total_trades']} |
| **Test** | {data['test']['portfolio']['total_return']:.2f}% | {data['test']['portfolio']['max_drawdown']:.2f}% | {data['test']['portfolio']['sharpe_ratio']:.2f} | {data['test']['portfolio']['sortino_ratio']:.2f} | {data['test']['portfolio']['win_rate']:.1f}% | {data['test']['portfolio']['profit_factor']:.2f} | {data['test']['portfolio']['total_trades']} |
| **Holdout** | {data['holdout']['portfolio']['total_return']:.2f}% | {data['holdout']['portfolio']['max_drawdown']:.2f}% | {data['holdout']['portfolio']['sharpe_ratio']:.2f} | {data['holdout']['portfolio']['sortino_ratio']:.2f} | {data['holdout']['portfolio']['win_rate']:.1f}% | {data['holdout']['portfolio']['profit_factor']:.2f} | {data['holdout']['portfolio']['total_trades']} |

---

## 各币种详情

### Train (训练集)

| Token | Final Equity | Return | Max Drawdown |
|-------|-------------|--------|--------------|
"""

for tok, m in data['train']['tokens'].items():
    md += f"| {tok} | ${m['final_equity']:,.2f} | {m['return']:.2f}% | {m['max_drawdown']:.2f}% |\n"

md += f"""
### Test (测试集)

| Token | Final Equity | Return | Max Drawdown |
|-------|-------------|--------|--------------|
"""

for tok, m in data['test']['tokens'].items():
    md += f"| {tok} | ${m['final_equity']:,.2f} | {m['return']:.2f}% | {m['max_drawdown']:.2f}% |\n"

md += f"""
### Holdout (留置集)

| Token | Final Equity | Return | Max Drawdown |
|-------|-------------|--------|--------------|
"""

for tok, m in data['holdout']['tokens'].items():
    md += f"| {tok} | ${m['final_equity']:,.2f} | {m['return']:.2f}% | {m['max_drawdown']:.2f}% |\n"

md += f"""
---

## 指标说明

| 指标 | 说明 |
|------|------|
| Total Return | 组合总收益率 = (最终 Equity - 初始资金 $21,000) / 初始资金 × 100% |
| Max Drawdown | 最大回撤 = 组合 Equity 从最高点到最低点的跌幅 |
| Sharpe Ratio | 夏普比率 = (平均收益 / 收益标准差) × √年化倍数 |
| Sortino Ratio | 索提诺比率 = (平均收益 / 下行收益标准差) × √年化倍数 |
| Win Rate | 胜率 = 盈利卖出次数 / 总卖出次数 |
| Profit Factor | 利润因子 = 盈利总额 / 亏损总额 |
| Total Trades | 总交易次数 = 所有币种的买入 + 卖出次数之和 |

---

*报告生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

with open('/Users/yy/.hermes/workspace/db/visualizer/V25_backtest_report.md', 'w') as f:
    f.write(md)

print('Updated V25_backtest_report.md with portfolio-level metrics')