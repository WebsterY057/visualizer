"""
数据库工具模块 - 连接管理、schema缓存
"""

import sqlite3
from functools import lru_cache
from config import DATABASES, MAX_ROWS


def get_db_path(table=None, db=None):
    """根据表名或数据库参数选择数据库"""
    if db and db in DATABASES:
        return DATABASES[db]['path']
    if table:
        if table.startswith('orders'):
            return DATABASES['orders']['path']
        for db_key, db_info in DATABASES.items():
            if table in TABLE_TO_DB.get(db_key, set()):
                return db_info['path']
    return DATABASES['orders']['path']


def get_table_db_key(table):
    """获取表所在的数据库key"""
    for db_key, tables in TABLE_TO_DB.items():
        if table in tables:
            return db_key
    return 'orders'


TABLE_TO_DB = {}
for db_key, db_info in DATABASES.items():
    try:
        conn = sqlite3.connect(db_info['path'])
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
        TABLE_TO_DB[db_key] = {t[0] for t in cur.fetchall()}
        conn.close()
    except:
        TABLE_TO_DB[db_key] = set()


@lru_cache(maxsize=128)
def get_table_columns_cached(db_path, table):
    """缓存表字段信息，避免频繁查询PRAGMA"""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table})")
    cols = [{'name': c[1], 'type': c[2]} for c in cur.fetchall()]
    conn.close()
    return cols


@lru_cache(maxsize=32)
def get_table_row_count(db_path, table):
    """缓存表行数"""
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM {table}")
    count = cur.fetchone()[0]
    conn.close()
    return count


def get_tables_meta(db_name=None):
    """获取所有表及其字段信息，可按数据库过滤"""
    meta = {}
    db_paths = [DATABASES[k]['path'] for k in DATABASES] if not db_name else [DATABASES[db_name]['path']]

    for db_path in db_paths:
        db_key = next((k for k, v in DATABASES.items() if v['path'] == db_path), 'orders')
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")
        tables = [r[0] for r in cur.fetchall()]

        for t in tables:
            cols = get_table_columns_cached(db_path, t)
            col_names = [c['name'] for c in cols]

            date_range = None
            for dc in ['date', 'Date', 'created_at']:
                if dc in col_names:
                    try:
                        cur.execute(f"SELECT MIN({dc}), MAX({dc}) FROM {t} WHERE {dc} IS NOT NULL")
                        r = cur.fetchone()
                        if r and r[0]:
                            date_range = [r[0], r[1]]
                            break
                    except:
                        pass

            count = get_table_row_count(db_path, t)
            meta[t] = {
                'columns': cols,
                'date_range': date_range,
                'row_count': count,
                'db': db_key,
                'db_name': DATABASES[db_key]['name']
            }
        conn.close()

    return meta


def detect_date_col(cur, table):
    """自动检测日期列"""
    try:
        cur.execute(f"PRAGMA table_info({table})")
        cols = [c[1] for c in cur.fetchall()]
        for dc in ['date', 'Date', '日期', 'created_at']:
            if dc in cols:
                return dc
    except:
        pass
    return None


def query_safe(db_path, sql, params=None):
    """安全的查询执行，自动关闭连接"""
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(sql, params or [])
        rows = cur.fetchall()
        cols = list(dict(rows[0]).keys()) if rows else []
        conn.close()
        return rows, cols, None
    except Exception as e:
        return [], [], str(e)
