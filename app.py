"""
K12 可视化分析平台
启动方式: python3 app.py
访问地址: http://localhost:5050
"""

import sqlite3
import json
import os
import csv
from flask import Flask, request, render_template, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)
app.template_folder = 'templates'
app.static_folder = 'static'

DB_PATH = '/Users/yy/.hermes/workspace/db/analysis.db'
ORDERS_DB_PATH = '/Users/yy/.hermes/workspace/db/orders.db'
SUMMARY_DB_PATH = '/Users/yy/.hermes/workspace/db/summary.db'
BACKTEST_DB_PATH = '/Users/yy/.hermes/workspace/db/backtest_experiments.db'
BACKTEST_REPORT_ROOT = '/Users/yy/.hermes/workspace/db/回测项目/量价关系信号_alpha市场/报告'
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


def init_backtest_db():
    """初始化回测实验记录库（独立于现有分析库）"""
    conn = sqlite3.connect(BACKTEST_DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS backtest_experiments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            experiment_name TEXT NOT NULL,
            strategy_version TEXT,
            split_name TEXT,
            total_return_pct REAL,
            max_drawdown_pct REAL,
            trades INTEGER,
            trade_volume_usd REAL,
            win_rate_pct REAL,
            sharpe REAL,
            change_summary TEXT,
            param_summary TEXT,
            direction TEXT,
            tags TEXT,
            metric_version TEXT,
            metrics_json TEXT,
            metric_formula_text TEXT,
            params_json TEXT,
            notes TEXT
        )
        """
    )
    cur.execute("PRAGMA table_info(backtest_experiments)")
    exists_cols = {r[1] for r in cur.fetchall()}
    add_cols = []
    if "metric_version" not in exists_cols:
        add_cols.append("ALTER TABLE backtest_experiments ADD COLUMN metric_version TEXT")
    if "metrics_json" not in exists_cols:
        add_cols.append("ALTER TABLE backtest_experiments ADD COLUMN metrics_json TEXT")
    if "metric_formula_text" not in exists_cols:
        add_cols.append("ALTER TABLE backtest_experiments ADD COLUMN metric_formula_text TEXT")
    if "trade_volume_usd" not in exists_cols:
        add_cols.append("ALTER TABLE backtest_experiments ADD COLUMN trade_volume_usd REAL")
    if "change_summary" not in exists_cols:
        add_cols.append("ALTER TABLE backtest_experiments ADD COLUMN change_summary TEXT")
    if "param_summary" not in exists_cols:
        add_cols.append("ALTER TABLE backtest_experiments ADD COLUMN param_summary TEXT")
    for sql in add_cols:
        cur.execute(sql)
    conn.commit()
    conn.close()

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


@app.route('/backtest')
def backtest():
    """回测实验工作台（独立页面）"""
    return render_template('backtest.html')

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


@app.route('/api/backtest/experiments', methods=['GET'])
def api_backtest_experiments():
    """查询回测实验记录"""
    split = request.args.get('split')
    keyword = request.args.get('keyword')
    limit = min(int(request.args.get('limit', 500)), 2000)

    conn = sqlite3.connect(BACKTEST_DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    where_parts = []
    params = []
    if split:
        where_parts.append("split_name = ?")
        params.append(split)
    if keyword:
        where_parts.append("(experiment_name LIKE ? OR direction LIKE ? OR notes LIKE ? OR tags LIKE ?)")
        like_kw = f"%{keyword}%"
        params.extend([like_kw, like_kw, like_kw, like_kw])

    where_sql = ("WHERE " + " AND ".join(where_parts)) if where_parts else ""
    sql = f"""
        SELECT *
        FROM backtest_experiments
        {where_sql}
        ORDER BY datetime(created_at) DESC, id DESC
        LIMIT ?
    """
    params.append(limit)
    cur.execute(sql, params)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return jsonify({"success": True, "data": rows, "count": len(rows)})


@app.route('/api/backtest/experiments', methods=['POST'])
def api_backtest_insert_experiment():
    """新增回测实验记录"""
    body = request.json or {}
    experiment_name = (body.get('experiment_name') or '').strip()
    if not experiment_name:
        return jsonify({"error": "experiment_name 不能为空"}), 400

    created_at = body.get('created_at') or datetime.now().isoformat(timespec='seconds')
    params_obj = body.get('params', {})
    params_json = json.dumps(params_obj, ensure_ascii=False) if isinstance(params_obj, dict) else str(params_obj)
    metrics_obj = body.get('metrics', {})
    metrics_json = json.dumps(metrics_obj, ensure_ascii=False) if isinstance(metrics_obj, dict) else str(metrics_obj)

    conn = sqlite3.connect(BACKTEST_DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO backtest_experiments (
            created_at, experiment_name, strategy_version, split_name,
            total_return_pct, max_drawdown_pct, trades, trade_volume_usd, win_rate_pct, sharpe,
            change_summary, param_summary, direction, tags, metric_version, metrics_json, metric_formula_text, params_json, notes
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            created_at,
            experiment_name,
            body.get('strategy_version'),
            body.get('split_name'),
            body.get('total_return_pct'),
            body.get('max_drawdown_pct'),
            body.get('trades'),
            body.get('trade_volume_usd'),
            body.get('win_rate_pct'),
            body.get('sharpe'),
            body.get('change_summary'),
            body.get('param_summary'),
            body.get('direction'),
            body.get('tags'),
            body.get('metric_version') or 'factor_detection_metric_library_v1',
            metrics_json,
            body.get('metric_formula_text'),
            params_json,
            body.get('notes'),
        ),
    )
    new_id = cur.lastrowid
    conn.commit()
    conn.close()
    return jsonify({"success": True, "id": new_id})


@app.route('/api/backtest/experiments/<int:exp_id>', methods=['PUT'])
def api_backtest_update_experiment(exp_id: int):
    """更新回测实验记录（便于迭代复盘）"""
    body = request.json or {}
    allowed = {
        "experiment_name", "strategy_version", "split_name", "total_return_pct",
        "max_drawdown_pct", "trades", "trade_volume_usd", "win_rate_pct", "sharpe",
        "change_summary", "param_summary", "direction", "tags", "notes",
        "params_json", "metric_version", "metrics_json", "metric_formula_text"
    }
    updates = []
    params = []

    for k, v in body.items():
        if k not in allowed:
            continue
        if k == "params_json" and isinstance(v, dict):
            v = json.dumps(v, ensure_ascii=False)
        updates.append(f"{k} = ?")
        params.append(v)

    if not updates:
        return jsonify({"error": "没有可更新字段"}), 400

    params.append(exp_id)
    conn = sqlite3.connect(BACKTEST_DB_PATH)
    cur = conn.cursor()
    cur.execute(f"UPDATE backtest_experiments SET {', '.join(updates)} WHERE id = ?", params)
    conn.commit()
    affected = cur.rowcount
    conn.close()
    return jsonify({"success": True, "updated": affected})


@app.route('/api/backtest/experiments/clear', methods=['POST'])
def api_backtest_clear_experiments():
    """清空回测实验记录（谨慎操作）"""
    conn = sqlite3.connect(BACKTEST_DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM backtest_experiments")
    deleted = cur.rowcount
    conn.commit()
    conn.close()
    return jsonify({"success": True, "deleted": deleted})


def _safe_float(v):
    try:
        return float(v)
    except Exception:
        return None


def _read_equity_curve_csv(csv_path: str) -> list[dict]:
    rows = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            x = r.get("minute") or r.get("date") or r.get("ts") or r.get("time")
            eq = _safe_float(r.get("equity"))
            if x is None or eq is None:
                continue
            rows.append({"x": x, "equity": eq})
    if not rows:
        return []
    peak = rows[0]["equity"]
    for item in rows:
        if item["equity"] > peak:
            peak = item["equity"]
        item["drawdown_pct"] = (item["equity"] / peak - 1.0) * 100.0 if peak > 0 else 0.0
    return rows


def _read_trade_events_csv(csv_path: str) -> list[dict]:
    events = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            et = r.get("entry_time")
            xt = r.get("exit_time")
            ep = _safe_float(r.get("entry_price"))
            xp = _safe_float(r.get("exit_price"))
            if et and ep is not None:
                events.append({"x": et, "price": ep, "side": "buy"})
            if xt and xp is not None:
                events.append({"x": xt, "price": xp, "side": "sell"})
    return events


def _read_trade_curve_csv(trade_csv_path: str, equity_csv_path: str | None = None, initial_capital: float | None = None) -> list[dict]:
    """按交易笔数构建收益曲线（每笔交易一个点）。

    优先使用组合净值曲线在交易退出时刻的净值，避免直接连乘交易收益带来的口径偏差。
    """
    trade_rows = []
    with open(trade_csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            et = r.get("exit_time") or r.get("entry_time") or r.get("time")
            if not et:
                continue
            trade_rows.append({"time": et})
    if not trade_rows:
        return []

    eq_index = {}
    first_curve_eq = None
    if equity_csv_path and os.path.exists(equity_csv_path):
        with open(equity_csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                x = r.get("minute") or r.get("date") or r.get("ts") or r.get("time")
                eq = _safe_float(r.get("equity"))
                if not x or eq is None:
                    continue
                # minute-level key
                key = str(x)[:16]
                eq_index[key] = eq
                if first_curve_eq is None:
                    first_curve_eq = eq

    out = []
    peak = None
    last_eq = None
    first_eq = None
    if initial_capital is not None:
        first_eq = float(initial_capital)
    elif first_curve_eq is not None:
        first_eq = first_curve_eq

    if first_eq is not None and trade_rows:
        out.append({"x": f"{trade_rows[0]['time']} [start]", "equity": first_eq, "drawdown_pct": 0.0, "trade_idx": 0})
        peak = first_eq

    for i, tr in enumerate(trade_rows, start=1):
        key = str(tr["time"])[:16]
        eq = eq_index.get(key, last_eq)
        if eq is None:
            # 找不到映射时跳过，避免引入错误口径
            continue
        last_eq = eq
        if first_eq is None:
            first_eq = eq
        if peak is None or eq > peak:
            peak = eq
        dd = (eq / peak - 1.0) * 100.0 if peak and peak > 0 else 0.0
        out.append({"x": tr["time"], "equity": eq, "drawdown_pct": dd, "trade_idx": i})
    return out


@app.route('/api/backtest/experiments/<int:exp_id>/curve', methods=['GET'])
def api_backtest_experiment_curve(exp_id: int):
    """根据实验记录返回对应净值/回撤曲线"""
    conn = sqlite3.connect(BACKTEST_DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM backtest_experiments WHERE id = ?", (exp_id,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return jsonify({"error": "实验不存在"}), 404
    rec = dict(row)

    split = (rec.get("split_name") or "").strip()
    direction = (rec.get("direction") or "").strip()
    params_json = rec.get("params_json") or "{}"
    notes = rec.get("notes") or ""
    report_root = BACKTEST_REPORT_ROOT
    curve_mode = (request.args.get("mode") or "trade").strip().lower()

    candidates = []
    if direction and split:
        candidates.append(os.path.join(report_root, direction, split, "组合净值曲线.csv"))
    if direction:
        candidates.append(os.path.join(report_root, direction, "组合净值曲线.csv"))

    try:
        params_obj = json.loads(params_json) if isinstance(params_json, str) else {}
    except Exception:
        params_obj = {}
    source_curve_csv = params_obj.get("source_curve_csv")
    if isinstance(source_curve_csv, str) and source_curve_csv:
        if os.path.isabs(source_curve_csv):
            candidates.append(source_curve_csv)
        else:
            candidates.append(os.path.join(report_root, source_curve_csv))
    src_file = params_obj.get("source_file")
    if isinstance(src_file, str) and src_file:
        src_abs = os.path.join(report_root, src_file)
        candidates.append(os.path.join(os.path.dirname(src_abs), "组合净值曲线.csv"))
    source_report = params_obj.get("source_report")
    if isinstance(source_report, str) and source_report:
        rep_abs = os.path.join(report_root, source_report)
        candidates.append(os.path.join(os.path.dirname(rep_abs), f"{split}_组合净值曲线.csv"))

    if "from " in notes:
        p = notes.split("from ", 1)[1].strip()
        notes_abs = os.path.join(report_root, p)
        candidates.append(os.path.join(os.path.dirname(notes_abs), "组合净值曲线.csv"))

    dedup = []
    seen = set()
    for c in candidates:
        cc = os.path.normpath(c)
        if cc not in seen:
            seen.add(cc)
            dedup.append(cc)

    for c in dedup:
        if os.path.exists(c):
            trade_candidates = []
            if c.endswith("组合净值曲线.csv"):
                trade_candidates.append(c.replace("组合净值曲线.csv", "组合交易明细.csv"))
            source_trade_csv = params_obj.get("source_trade_csv")
            if isinstance(source_trade_csv, str) and source_trade_csv:
                if os.path.isabs(source_trade_csv):
                    trade_candidates.append(source_trade_csv)
                else:
                    trade_candidates.append(os.path.join(report_root, source_trade_csv))

            init_cap = _safe_float(params_obj.get("total_nominal_capital_usd"))
            if init_cap is None:
                init_cap = _safe_float(params_obj.get("initial_capital_normalized"))

            trades = []
            trade_curve = []
            for tc in trade_candidates:
                if os.path.exists(tc):
                    trades = _read_trade_events_csv(tc)
                    trade_curve = _read_trade_curve_csv(tc, c, init_cap)
                    if trades or trade_curve:
                        break

            # 默认优先交易级曲线，点数与交易次数同量级
            if curve_mode == "trade" and trade_curve:
                return jsonify({"success": True, "source": c, "mode": "trade", "data": trade_curve, "trades": trades})

            data = _read_equity_curve_csv(c)
            if data:
                return jsonify({"success": True, "source": c, "mode": "bar", "data": data, "trades": trades})

    return jsonify({"error": "未找到该实验对应的净值曲线文件", "candidates": dedup}), 404

if __name__ == '__main__':
    init_backtest_db()
    print("=" * 50)
    print("K12 可视化分析平台")
    print("访问地址: http://localhost:5050")
    print("按 Ctrl+C 停止服务")
    print("=" * 50)
    app.run(host='0.0.0.0', port=5050, debug=False)
