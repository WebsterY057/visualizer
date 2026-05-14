"""
配置模块 - 集中管理数据库路径和常量配置
"""

import os

BASE_DIR = '/Users/yy/.hermes/workspace/db'

DATABASES = {
    'k1k2_token': {'name': 'K1K2综合订单库(唯一)', 'path': os.path.join(BASE_DIR, 'k1k2_token_orders.db')},
    'summary': {'name': '汇总数据库', 'path': os.path.join(BASE_DIR, 'summary.db')},
    'backtest': {'name': '回测数据库', 'path': os.path.join(BASE_DIR, 'backtest_experiments.db')},
}

BACKTEST_REPORT_ROOT = os.path.join(BASE_DIR, '回测项目/量价关系信号_alpha市场/报告')
MAX_ROWS = 50000
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5050

# MiniMax API配置（自然语言查询用）
MINIMAX_API_KEY = 'sk-cp-a7Scx1OB2BfewT37DDJATWDXL8WtdnJvQKF4rjpSaZwcNj6csLlWUm0mSBmNntc8nhr53CAdsBGx0U3SQkbe07HlQ0yOtOItEZGlrqte09Yxdu28zKTTkjI'
MINIMAX_BASE_URL = 'https://api.minimax.chat/v1'
MINIMAX_MODEL = 'minimax-m2.7-highspeed'
