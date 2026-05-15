# 可视化分析平台

全栈数据可视化平台，用于加密货币量化回测结果的分析与管理。后端 Flask + SQLite，前端原生 HTML/CSS/JS + Chart.js。

## 功能

### 数据分析
- 多数据库切换（汇总、K12订单、小乌龟订单、跨K1K2综合订单）
- 多字段组合图表（折线图/柱状图/散点图/饼图/热力图/雷达图）
- SQL 原生查询，支持跨库查询（`库名.表名` 语法）
- 自然语言→SQL（集成 MiniMax API）

### 回测实验
- 本地回测实验列表（排序、筛选、版本管理）
- 组合净值曲线 + 统计指标卡片
- 详情弹窗：JSON参数、参数摘要、改动说明
- 交易分析热力图：X/Y轴可选的指标散点密度图，基于FIFO买卖配对计算每笔盈亏

### 服务器回测
- 服务端回测实验管理
- 净值曲线与汇总指标

### 参数优化
- 交易级热力图分析
  - X/Y轴可选：成交价、盈亏USDT、快慢VWAP差%
  - 网格密度着色（绿盈红亏）
  - FIFO配对逐笔盈亏计算

## 技术栈

| 层       | 技术                          |
|----------|-------------------------------|
| 后端     | Python Flask + SQLite         |
| 前端     | 原生 HTML/CSS/JavaScript      |
| 图表     | Chart.js 4.x                  |
| 回测引擎 | 自定义 Python 回测模块         |
| 版本管理 | Git + GitHub + 内网 GitLab    |

## 快速启动

```bash
# 克隆仓库
git clone https://github.com/WebsterY057/visualizer.git
cd visualizer

# 安装依赖
pip install flask pandas numpy

# 启动
python app.py
```

访问 `http://localhost:5050`

> 内置演示数据，开箱即用。如需重新回测，参考 `save_*.py` 脚本。

## 数据架构

```
backtest_experiments.db     # 回测实验主库
  ├── backtest_experiments  # 实验记录（版本/数据集/收益率/回撤等）
  ├── equity_curves          # 净值曲线（逐 bar 净值+回撤）
  ├── bar_data              # 分钟级 K 线数据
  ├── trade_markers         # 交易标记（买卖点）
  └── trade_records         # 交易明细

summary.db                   # 汇总数据库
orders_k12.db                # K12 订单数据
orders_turtle.db             # 小乌龟订单数据
orders_bigcoin.db            # 大币订单数据
k1k2_token_orders.db         # K1K2 综合订单
```

## 目录结构

```
visualizer/
├── app.py                  # Flask 主应用（路由 + API）
├── config.py               # 数据库路径等配置
├── templates/
│   └── index.html          # 前端单页应用（HTML+CSS+JS）
├── save_*.py               # 各种版本的回测保存脚本
└── README.md
```

## API 概览

| 端点 | 说明 |
|------|------|
| `GET  /api/databases` | 获取数据库列表 |
| `GET  /api/tables` | 获取表及其字段 |
| `POST /api/query` | 通用数据查询 |
| `POST /api/sql_query` | 原生 SQL 查询 |
| `GET  /api/backtest/list` | 本地回测列表 |
| `GET  /api/backtest/detail/<id>` | 回测详情 |
| `GET  /api/backtest/equity_curve/<id>` | 净值曲线 |
| `GET  /api/backtest/trade_analysis/<id>` | 交易分析（含 FIFO 盈亏） |
| `GET  /api/server_backtest/experiments` | 服务器回测列表 |

## Git 提交历史

```
ccbda38 数据分析中版基本无错
291c628 数据分析查询矫正，历史回测梳理
1af8003 参数优化初版
e4072c1 可视化平台首次推送
b1d68b0 服务器回测初版
20c5525 回测实验最大回撤校正
8d92f39 回测实验字段修改
1601e32 回测实验初版
b68616a 数据分析字段修改
9f1c231 数据分析板块初版
```

## 许可证

MIT
