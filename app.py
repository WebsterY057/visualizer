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
MAX_ROWS = 50000

DATABASES = {
    'analysis': {'name': '分析数据库', 'path': DB_PATH},
    'orders': {'name': '订单数据库', 'path': ORDERS_DB_PATH},
    'summary': {'name': '汇总数据库', 'path': SUMMARY_DB_PATH},
}

# 启动时扫描所有表所在的数据库，建立映射
TABLE_TO_DB = {}
for db_key, db_info in DATABASES.items():
    try:
        conn = sqlite3.connect(db_info['path'])
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
        for (t,) in cur.fetchall():
            TABLE_TO_DB[t] = db_key
        conn.close()
    except:
        pass

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
    # 自动判断：查表名映射
    if table and table in TABLE_TO_DB:
        db_key = TABLE_TO_DB[table]
        if db_key == 'orders':
            return ORDERS_DB_PATH
        if db_key == 'analysis':
            return DB_PATH
        if db_key == 'summary':
            return SUMMARY_DB_PATH
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
        # 获取每个表的字段
        table_cols = {}
        for t in tables:
            try:
                cur.execute(f"PRAGMA table_info({t})")
                table_cols[t] = [c[1] for c in cur.fetchall()]
            except:
                table_cols[t] = []

        # 找出每个表特有的后缀模式
        # 如小乌龟汇总用_龟1/_龟2/_龟12，跨所汇总用_跨1/_跨2/_跨12
        table_suffixes = {}
        for t in tables:
            suffixes = set()
            for c in table_cols[t]:
                parts = c.rsplit('_', 1)
                if len(parts) == 2 and parts[1] not in ['id', 'date', '日期']:
                    suffixes.add(parts[1])
            table_suffixes[t] = suffixes

        # 为每个字段找到在各表中的实际列名
        # 用户选"今日总盈亏"，小乌龟应该匹配"今日总盈亏_龟1"等，跨所匹配"今日总盈亏_跨1"等
        # 也支持格式"今日总盈亏_小乌龟"表示只从特定表获取
        field_map = {}         # f -> t -> 实际列名
        all_field_suffixes = {}  # f -> t -> [所有匹配的后缀]

        # 解析字段名，提取基础字段和目标表
        parsed_fields = {}  # f -> {base_field, target_table}
        for f in y_fields:
            base_field = f
            target_table = None
            # 检查是否有表名后缀（格式：field_表名缩写）
            for t in tables:
                table_short = t.replace('汇总', '').replace('大币', '')
                if f.endswith('_' + table_short):
                    base_field = f[:-len(table_short)-1]
                    target_table = t
                    break
            parsed_fields[f] = {'base_field': base_field, 'target_table': target_table}

        for f in y_fields:
            field_map[f] = {}
            all_field_suffixes[f] = {}
            base_field = parsed_fields[f]['base_field']
            target_table = parsed_fields[f]['target_table']
            for t in tables:
                if target_table and t != target_table:
                    continue
                # 精确匹配（优先精确匹配）
                exact = [c for c in table_cols[t] if c == base_field]
                if exact:
                    field_map[f][t] = exact[0]
                    all_field_suffixes[f][t] = [exact[0]]
                    continue
                # 按后缀匹配（按长度降序，优先更长的后缀如龟12/跨12）
                # 但如果 base_field 本身已经带下划线（如今日总盈亏_龟12），说明用户已指定后缀，不再加后缀
                if '_' not in base_field:
                    sorted_suffixes = sorted(table_suffixes[t], key=lambda s: len(s), reverse=True)
                    matched = []
                    for suffix in sorted_suffixes:
                        candidate = f'{base_field}_{suffix}'
                        if candidate in table_cols[t]:
                            matched.append(candidate)
                    all_field_suffixes[f][t] = matched if matched else []
                    if matched:
                        field_map[f][t] = matched[0]
                else:
                    all_field_suffixes[f][t] = []

        date_col = detect_date_col(cur, tables[0]) or '日期'

        # 先查每个表的数据（每个表用自己的数据库连接）
        table_data = {}
        table_conns = {}
        for t in tables:
            conn_t = sqlite3.connect(get_db_path(t, db))
            conn_t.row_factory = sqlite3.Row
            cur_t = conn_t.cursor()
            table_conns[t] = {'conn': conn_t, 'cur': cur_t}

            select_fields_t = [date_col]
            if group_by:
                select_fields_t.append(group_by)
            orig_fields_t = []
            actual_cols_t = []
            sum_exprs = []
            for f in y_fields:
                if t in field_map.get(f, {}) and field_map[f][t]:
                    # field_map[f][t] 已是单列（精确匹配或最长后缀）
                    actual_col = field_map[f][t]
                    base_field = parsed_fields[f]['base_field']
                    # 多后缀场景（len > 1）只取最长后缀单列，不 SUM
                    if '_' in actual_col and actual_col != base_field:
                        # 后缀列 → 不聚合，直接取单列
                        select_fields_t.append(actual_col)
                    else:
                        # 精确匹配 → 也不聚合
                        select_fields_t.append(actual_col)
                    orig_fields_t.append(f)
                    actual_cols_t.append(actual_col)

            if len(select_fields_t) <= 1:
                print(f"[DEBUG] SKIP {t}: select_fields_t={select_fields_t} (no fields matched)")
                continue

            where_parts = []
            params_t = []
            if date_from:
                where_parts.append(f"{date_col} >= ?")
                params_t.append(date_from)
            if date_to:
                where_parts.append(f"{date_col} <= ?")
                params_t.append(date_to)
            if filters:
                for col, val in filters.items():
                    if val and val != 'all':
                        where_parts.append(f"{col} = ?")
                        params_t.append(val)
            where_sql = " AND ".join(where_parts) if where_parts else "1=1"

            select_sql = ", ".join(select_fields_t)
            if group_by:
                group_expr = field_map[y_fields[0]][t] if y_fields and t in field_map.get(y_fields[0], {}) else '1'
                sql = f"SELECT {select_sql}, SUM({group_expr}) as _val FROM {t} WHERE {where_sql} GROUP BY {group_by}, {date_col} ORDER BY {group_by}, {date_col} LIMIT {MAX_ROWS}"
            elif filters and any(v and v != 'all' for v in filters.values()):
                agg_fields = [date_col] + [f"SUM({c}) as {c}" for c in actual_cols_t]
                sql = f"SELECT {', '.join(agg_fields)} FROM {t} WHERE {where_sql} GROUP BY {date_col} ORDER BY {date_col} LIMIT {MAX_ROWS}"
            else:
                agg_fields = [date_col] + [f"SUM({c}) as {c}" for c in actual_cols_t]
                sql = f"SELECT {', '.join(agg_fields)} FROM {t} WHERE {where_sql} GROUP BY {date_col} ORDER BY {date_col} LIMIT {MAX_ROWS}"
            print(f"[DEBUG] SQL for {t}: {sql}, params={params_t}")
            # 使用该表自己的连接
            cur_t = table_conns[t]['cur']
            cur_t.execute(sql, params_t)
            rows = cur_t.fetchall()
            cols = list(dict(rows[0]).keys()) if rows else []
            print(f"[DEBUG] {t}: got {len(rows)} rows, cols={cols}")
            table_data[t] = {
                'orig_fields': orig_fields_t,
                'actual_cols': actual_cols_t,
                'rows': [dict(r) for r in rows],
                'has_group_by': group_by is not None,
                'sum_exprs': sum_exprs
            }

        # 合并数据
        print(f"[DEBUG] table_data before merge: {[(t, len(d['rows']), d['orig_fields'], d['actual_cols']) for t, d in table_data.items()]}")
        merged = {}
        all_col_names = set()
        for t, data in table_data.items():
            for r in data['rows']:
                if group_by:
                    key = r.get(group_by, '总计')
                else:
                    key = r.get(date_col, '')
                if key not in merged:
                    merged[key] = {date_col if not group_by else group_by: key}
                for i, f in enumerate(data['orig_fields']):
                    t_short = t.replace('汇总', '').replace('大币', '')
                    col_name = f
                    all_col_names.add(col_name)
                    actual_col = data['actual_cols'][i]
                    val = r.get(actual_col) or 0
                    if col_name not in merged[key]:
                        merged[key][col_name] = val
                    else:
                        merged[key][col_name] = merged[key].get(col_name, 0) + val
                    print(f"[DEBUG] merge {t}: key={key}, col_name={col_name}, actual_col={actual_col}, val={val}")

        for key in merged:
            for col in all_col_names:
                if col not in merged[key]:
                    merged[key][col] = 0

        # 关闭所有per-table连接
        for t, item in table_conns.items():
            try:
                item['conn'].close()
            except:
                pass
        conn.close()

        result = sorted(merged.values(), key=lambda x: str(x.get(group_by or date_col, '')))
        print(f"[DEBUG] query_data multi-table: tables={tables}, y_fields={y_fields}, merged_count={len(result)}, first_row_keys={list(result[0].keys()) if result else []}")
        return result

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

    # 如果有筛选条件且没有指定group_by，按x_field和筛选的维度列聚合（避免返回多条同一日期的数据）
    if group_by:
        sql = f"SELECT {group_by}, " + ", ".join([f"SUM({f}) as {f}_sum" for f in y_fields]) + f", COUNT(*) as __count FROM {table} WHERE {where_sql} GROUP BY {group_by} ORDER BY {group_by} LIMIT {MAX_ROWS}"
    elif filters and any(v and v != 'all' for v in filters.values()):
        # 找出有筛选值的维度列，按x_field和这些维度列聚合
        active_dim_cols = [col for col, val in filters.items() if val and val != 'all']
        if active_dim_cols:
            group_cols = f"{x_field}, {', '.join(active_dim_cols)}"
            sql = f"SELECT {group_cols}, " + ", ".join([f"SUM({f}) as {f}" for f in y_fields]) + f" FROM {table} WHERE {where_sql} GROUP BY {group_cols} ORDER BY {x_field} LIMIT {MAX_ROWS}"
        else:
            sql = f"SELECT {select_fields_sql} FROM {table} WHERE {where_sql} ORDER BY {x_field} LIMIT {MAX_ROWS}"
    else:
        sql = f"SELECT {select_fields_sql} FROM {table} WHERE {where_sql} ORDER BY {x_field} LIMIT {MAX_ROWS}"

    cur.execute(sql, params)
    rows = cur.fetchall()
    conn.close()
    
    print(f"[DEBUG] query_data single-table: table={table}, y_fields={y_fields}, row_count={len(rows)}, first_row_keys={list(dict(rows[0]).keys()) if rows else []}")
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
# 工具函数
# ============================================================

def round_numeric_fields(data, decimals=4):
    """将数据中的数值字段四舍五入到指定小数位"""
    if not data:
        return data
    result = []
    for row in data:
        new_row = {}
        for k, v in row.items():
            if isinstance(v, float):
                new_row[k] = round(v, decimals)
            else:
                new_row[k] = v
        result.append(new_row)
    return result

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
        print(f"[DEBUG] api_query: tables={tables}, y_fields={y_fields}")
        data = query_data(tables[0], x_field, y_fields, date_from, date_to, group_by, filters, db, tables)
        data = round_numeric_fields(data)
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
