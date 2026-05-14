"""
配置模块 - 集中管理数据库路径和常量配置
"""

import os

BASE_DIR = '/Users/yy/.hermes/workspace/db'

# 「数据查询」Tab 仅允许这 5 个库（与 visualizer/app.py 中 QUERY_DATABASES 一致）
QUERY_DATABASES = {
    'summary': {'name': '汇总数据库 summary.db', 'path': os.path.join(BASE_DIR, 'summary.db')},
    'orders_bigcoin': {'name': '大币订单 orders_bigcoin.db', 'path': os.path.join(BASE_DIR, 'orders_bigcoin.db')},
    'orders_k12': {'name': 'K12 订单 orders_k12.db', 'path': os.path.join(BASE_DIR, 'orders_k12.db')},
    'orders_turtle': {'name': '小乌龟订单 orders_turtle.db', 'path': os.path.join(BASE_DIR, 'orders_turtle.db')},
    'k1k2_token': {'name': 'K1K2 综合订单 k1k2_token_orders.db', 'path': os.path.join(BASE_DIR, 'k1k2_token_orders.db')},
}

# 「数据分析」等：在查询库之外可附加回测库
DATABASES = {
    **QUERY_DATABASES,
    'backtest': {'name': '回测实验 backtest_experiments.db', 'path': os.path.join(BASE_DIR, 'backtest_experiments.db')},
}

BACKTEST_REPORT_ROOT = os.path.join(BASE_DIR, '回测项目/量价关系信号_alpha市场/报告')
MAX_ROWS = 50000
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5050

# MiniMax API配置（自然语言查询用）
MINIMAX_API_KEY = 'sk-cp-a7Scx1OB2BfewT37DDJATWDXL8WtdnJvQKF4rjpSaZwcNj6csLlWUm0mSBmNntc8nhr53CAdsBGx0U3SQkbe07HlQ0yOtOItEZGlrqte09Yxdu28zKTTkjI'
MINIMAX_BASE_URL = 'https://api.minimax.chat/v1'
MINIMAX_MODEL = 'minimax-m2.7-highspeed'
