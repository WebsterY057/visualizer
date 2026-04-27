"""
K12 可视化分析平台
启动方式: python3 app.py
访问地址: http://localhost:5050
"""

import sqlite3
import json
from flask import Flask, request, render_template, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)
app.template_folder = 'templates'
app.static_folder = 'static'

DB_PATH = '/Users/yy/.hermes/workspace/db/analysis.db'
ORDERS_DB_PATH = '/Users/yy/.hermes/workspace/db/orders.db'
SUMMARY_DB_PATH = '/Users/yy/.hermes/workspace/db/summary.db'
MAX_ROWS = 1000

DATABASES = {
    'analysis': {'name': '分析数据库', 'path': DB_PATH},
    'orders': {'name': '订单数据库', 'path': ORDERS_DB_PATH},
    'summary': {'name': '汇总数据库', 'path': SUMMARY_DB_PATH},
}

def get_db_path(table=None, db=None):
    """根据表名或数据库参数选择数据库"""
    if db == 'orders':
        return ORDERS_DB_PATH
    if db == 'analysis':
        return DB_PATH
    if db == 'summary':
        return SUMMARY_DB_PATH
    if table and table.startswith('orders'):
        return ORDERS_DB_PATH
    return DB_PATH

# ============================================================
# 数据库查询
# ============================================================

def get_tables_meta(db_name=None):
    """获取所有表及其字段信息，可按数据库过滤"""
    meta = {}
    if db_name == 'orders':
        db_paths = [ORDERS_DB_PATH]
    elif db_name == 'summary':
        db_paths = [SUMMARY_DB_PATH]
    elif db_name == 'analysis':
        db_paths = [DB_PATH]
    else:
        db_paths = [DB_PATH, ORDERS_DB_PATH, SUMMARY_DB_PATH]
    db_key = db_name if db_name else 'all'

    for db_path in db_paths:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")
        tables = [r[0] for r in cur.fetchall()]

        for t in tables:
            cur.execute(f"PRAGMA table_info({t})")
            cols = [{'name': c[1], 'type': c[2]} for c in cur.fetchall()]
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

            cur.execute(f"SELECT COUNT(*) FROM {t}")
            count = cur.fetchone()[0]
            meta[t] = {
                'columns': cols,
                'date_range': date_range,
                'row_count': count,
                'db': 'analysis' if db_path == DB_PATH else ('orders' if db_path == ORDERS_DB_PATH else 'summary'),
                'db_name': DATABASES['analysis']['name'] if db_path == DB_PATH else (DATABASES['orders']['name'] if db_path == ORDERS_DB_PATH else DATABASES['summary']['name'])
            }
        conn.close()
    return meta

def detect_date_col(cur, table):
    date_cols = ['date', 'Date', 'DATE', '日期', 'created_at']
    for col in date_cols:
        try:
            cur.execute(f"SELECT {col} FROM {table} LIMIT 1")
            return col
        except:
            pass
    return None

def query_data(table, x_field, y_fields, date_from=None, date_to=None, group_by=None, filters=None, db=None, tables=None):
    """通用数据查询"""
    db_path = get_db_path(table, db)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    # 多表支持
    if tables and len(tables) > 1:
        # 获取所有表都有的字段
        all_cols = set()
        table_cols = {}
        for t in tables:
            try:
                cur.execute(f"PRAGMA table_info({t})")
                cols = [c[1] for c in cur.fetchall()]
                table_cols[t] = set(cols)
                all_cols.update(cols)
            except:
                pass

        # 找出所有表都有的公共字段
        common_cols = set(y_fields)
        for t in tables:
            if t in table_cols:
                common_cols = common_cols.intersection(table_cols[t])
        common_cols = list(common_cols)

        if not common_cols:
            conn.close()
            return []

        # 构建多表 UNION 查询
        date_col = detect_date_col(cur, tables[0])
        if not date_col:
            date_col = 'date'
        select_fields = [date_col] + common_cols
        select_sql = ", ".join(select_fields)

        subqueries = []
        for t in tables:
            sub_col = detect_date_col(cur, t) or date_col
            if sub_col != date_col:
                select_sql_t = select_sql.replace(date_col, sub_col)
            else:
                select_sql_t = select_sql

            where_parts = []
            params_t = []
            if date_from:
                where_parts.append(f"{sub_col} >= ?")
                params_t.append(date_from)
            if date_to:
                where_parts.append(f"{sub_col} <= ?")
                params_t.append(date_to)
            where_sql = " AND ".join(where_parts) if where_parts else "1=1"

            subqueries.append(f"SELECT {select_sql_t} FROM {t} WHERE {where_sql}")

        sql = " UNION ALL ".join(subqueries) + f" ORDER BY {date_col} LIMIT {MAX_ROWS}"
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return [dict(r) for r in rows]

    # 单表查询
    date_col = detect_date_col(cur, table)
    if x_field == 'date' and date_col and date_col != 'date':
        x_field = date_col

    select_fields = [x_field] + list(y_fields)
    select_fields_sql = ", ".join(select_fields)

    where_clauses = []
    params = []

    if date_from and date_col:
        where_clauses.append(f"{date_col} >= ?")
        params.append(date_from)
    if date_to and date_col:
        where_clauses.append(f"{date_col} <= ?")
        params.append(date_to)

    if filters:
        for col, val in filters.items():
            if val and val != 'all':
                where_clauses.append(f"{col} = ?")
                params.append(val)

    where_sql = " AND ".join(where_clauses) if where_clauses else "1=1"

    if group_by:
        sql = f"SELECT {group_by}, " + ", ".join([f"SUM({f}) as {f}_sum" for f in y_fields]) + f", COUNT(*) as __count FROM {table} WHERE {where_sql} GROUP BY {group_by} ORDER BY {group_by} LIMIT {MAX_ROWS}"
    else:
        sql = f"SELECT {select_fields_sql} FROM {table} WHERE {where_sql} ORDER BY {x_field} LIMIT {MAX_ROWS}"

    cur.execute(sql, params)
    rows = cur.fetchall()
    conn.close()
    
    return [dict(r) for r in rows]

def get_distinct_values(table, field, db=None):
    """获取某字段的所有不重复值（用于下拉筛选）"""
    conn = sqlite3.connect(get_db_path(table, db))
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT DISTINCT {field} FROM {table} WHERE {field} IS NOT NULL ORDER BY {field}")
        values = [r[0] for r in cur.fetchall()]
        conn.close()
        return values
    except:
        conn.close()
        return []

def get_date_range(table, db=None):
    """获取表的最大最小日期"""
    conn = sqlite3.connect(get_db_path(table, db))
    cur = conn.cursor()
    cur.execute(f"PRAGMA table_info({table})")
    col_names = [c[1] for c in cur.fetchall()]
    for dc in ['date', 'Date', 'created_at']:
        if dc in col_names:
            try:
                cur.execute(f"SELECT MIN({dc}), MAX({dc}) FROM {table} WHERE {dc} IS NOT NULL")
                r = cur.fetchone()
                if r and r[0]:
                    conn.close()
                    return r[0], r[1]
            except:
                pass
    conn.close()
    return None, None

# ============================================================
# 路由
# ============================================================

@app.route('/')
def index():
    """主页 - 数据选择界面"""
    meta = get_tables_meta()
    return render_template('index.html', meta=meta)

@app.route('/api/databases')
def api_databases():
    """获取所有数据库及其表"""
    result = {}
    for db_key, db_info in DATABASES.items():
        conn = sqlite3.connect(db_info['path'])
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")
        tables = [r[0] for r in cur.fetchall()]
        conn.close()
        result[db_key] = {'name': db_info['name'], 'tables': tables}
    return jsonify(result)

@app.route('/api/tables')
def api_tables():
    """获取所有表信息"""
    db = request.args.get('db')
    meta = get_tables_meta(db)
    return jsonify(meta)

@app.route('/api/query', methods=['POST'])
def api_query():
    """执行查询"""
    body = request.json
    table = body.get('table')
    db = body.get('db')
    x_field = body.get('x_field', 'date')
    y_fields = body.get('y_fields', [])
    date_from = body.get('date_from')
    date_to = body.get('date_to')
    group_by = body.get('group_by')
    filters = body.get('filters', {})
    tables = body.get('tables', [table])

    if not tables or not y_fields:
        return jsonify({'error': '请选择表和字段'}), 400

    try:
        data = query_data(tables[0], x_field, y_fields, date_from, date_to, group_by, filters, db, tables)
        return jsonify({'success': True, 'data': data, 'count': len(data)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/values/<table>/<field>')
def api_values(table, field):
    """获取某字段的不重复值"""
    try:
        db = request.args.get('db')
        values = get_distinct_values(table, field, db)
        return jsonify(values)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/daterange/<table>')
def api_daterange(table):
    """获取表的日期范围"""
    db = request.args.get('db')
    dmin, dmax = get_date_range(table, db)
    return jsonify({'min': dmin, 'max': dmax})

@app.route('/api/heatmap', methods=['POST'])
def api_heatmap():
    """热力图数据 - spread_range × size_range"""
    body = request.json
    table = body.get('table', 'k12_token_spread_size_daily_v2')
    date_from = body.get('date_from')
    date_to = body.get('date_to')
    metric = body.get('metric', 'alpha')  # alpha / pnl / theo / bundle

    conn = sqlite3.connect(get_db_path(table))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    where = "1=1"
    params = []
    if date_from:
        where += " AND date >= ?"
        params.append(date_from)
    if date_to:
        where += " AND date <= ?"
        params.append(date_to)

    sql = f"""
        SELECT spread_range, size_range,
               SUM({metric}) as value,
               SUM(order_count) as cnt
        FROM {table}
        WHERE {where}
        GROUP BY spread_range, size_range
        ORDER BY spread_range, size_range
    """
    cur.execute(sql, params)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return jsonify(rows)

@app.route('/api/daily', methods=['POST'])
def api_daily():
    """每日趋势数据"""
    body = request.json
    table = body.get('table', 'k12_token_spread_size_daily_v2')
    date_from = body.get('date_from')
    date_to = body.get('date_to')
    metric = body.get('metric', 'alpha')
    group_by = body.get('group_by')  # spread_range, size_range, token

    conn = sqlite3.connect(get_db_path(table))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    
    where = "1=1"
    params = []
    if date_from:
        where += " AND date >= ?"
        params.append(date_from)
    if date_to:
        where += " AND date <= ?"
        params.append(date_to)
    
    if group_by:
        sql = f"""
            SELECT date, {group_by},
                   SUM({metric}) as value,
                   SUM(order_count) as cnt
            FROM {table}
            WHERE {where}
            GROUP BY date, {group_by}
            ORDER BY date, {group_by}
        """
    else:
        sql = f"""
            SELECT date,
                   SUM({metric}) as value,
                   SUM(order_count) as cnt
            FROM {table}
            WHERE {where}
            GROUP BY date
            ORDER BY date
        """
    
    cur.execute(sql, params)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    print("=" * 50)
    print("K12 可视化分析平台")
    print("访问地址: http://localhost:5050")
    print("按 Ctrl+C 停止服务")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5050, debug=False)
