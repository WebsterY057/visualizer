# app.py 逐行注释对照

- 源文件: `/Users/yy/.hermes/workspace/db/visualizer/app.py`
- 说明: 该文件逐行解释 `app.py` 代码作用，不改动原始 Python 文件。

| 行号 | 原代码 | 注释 |
|---:|---|---|
| 1 | `&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 2 | `K12 可视化分析平台` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 3 | `启动方式: python3 app.py` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 4 | `访问地址: http://localhost:5050` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 5 | `&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 6 | `` | 空行，用于逻辑分段与可读性。 |
| 7 | `import sqlite3` | 导入依赖模块。 |
| 8 | `import json` | 导入依赖模块。 |
| 9 | `from flask import Flask, request, render_template, jsonify` | 导入依赖模块。 |
| 10 | `from datetime import datetime, timedelta` | 导入依赖模块。 |
| 11 | `` | 空行，用于逻辑分段与可读性。 |
| 12 | `app = Flask(__name__)` | 创建 Flask 应用实例。 |
| 13 | `app.template_folder = &#x27;templates&#x27;` | 设置模板目录路径。 |
| 14 | `app.static_folder = &#x27;static&#x27;` | 设置静态资源目录路径。 |
| 15 | `` | 空行，用于逻辑分段与可读性。 |
| 16 | `DB_PATH = &#x27;/Users/yy/.hermes/workspace/db/analysis.db&#x27;` | 定义全局常量或配置项。 |
| 17 | `ORDERS_DB_PATH = &#x27;/Users/yy/.hermes/workspace/db/orders.db&#x27;` | 定义全局常量或配置项。 |
| 18 | `SUMMARY_DB_PATH = &#x27;/Users/yy/.hermes/workspace/db/summary.db&#x27;` | 定义全局常量或配置项。 |
| 19 | `MAX_ROWS = 50000` | 定义全局常量或配置项。 |
| 20 | `` | 空行，用于逻辑分段与可读性。 |
| 21 | `DATABASES = {` | 定义全局常量或配置项。 |
| 22 | `    &#x27;analysis&#x27;: {&#x27;name&#x27;: &#x27;分析数据库&#x27;, &#x27;path&#x27;: DB_PATH},` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 23 | `    &#x27;orders&#x27;: {&#x27;name&#x27;: &#x27;订单数据库&#x27;, &#x27;path&#x27;: ORDERS_DB_PATH},` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 24 | `    &#x27;summary&#x27;: {&#x27;name&#x27;: &#x27;汇总数据库&#x27;, &#x27;path&#x27;: SUMMARY_DB_PATH},` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 25 | `}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 26 | `` | 空行，用于逻辑分段与可读性。 |
| 27 | `def get_db_path(table=None, db=None):` | 定义函数 `get_db_path`。 |
| 28 | `    &quot;&quot;&quot;根据表名或数据库参数选择数据库&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 29 | `    if db == &#x27;orders&#x27;:` | 条件分支控制。 |
| 30 | `        return ORDERS_DB_PATH` | 函数返回结果。 |
| 31 | `    if db == &#x27;analysis&#x27;:` | 条件分支控制。 |
| 32 | `        return DB_PATH` | 函数返回结果。 |
| 33 | `    if db == &#x27;summary&#x27;:` | 条件分支控制。 |
| 34 | `        return SUMMARY_DB_PATH` | 函数返回结果。 |
| 35 | `    if table and table.startswith(&#x27;orders&#x27;):` | 条件分支控制。 |
| 36 | `        return ORDERS_DB_PATH` | 函数返回结果。 |
| 37 | `    return DB_PATH` | 函数返回结果。 |
| 38 | `` | 空行，用于逻辑分段与可读性。 |
| 39 | `# ============================================================` | 注释行，用于说明模块或逻辑分区。 |
| 40 | `# 数据库查询` | 注释行，用于说明模块或逻辑分区。 |
| 41 | `# ============================================================` | 注释行，用于说明模块或逻辑分区。 |
| 42 | `` | 空行，用于逻辑分段与可读性。 |
| 43 | `def get_tables_meta(db_name=None):` | 定义函数 `get_tables_meta`。 |
| 44 | `    &quot;&quot;&quot;获取所有表及其字段信息，可按数据库过滤&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 45 | `    meta = {}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 46 | `    if db_name == &#x27;orders&#x27;:` | 条件分支控制。 |
| 47 | `        db_paths = [ORDERS_DB_PATH]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 48 | `    elif db_name == &#x27;summary&#x27;:` | 条件分支控制。 |
| 49 | `        db_paths = [SUMMARY_DB_PATH]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 50 | `    elif db_name == &#x27;analysis&#x27;:` | 条件分支控制。 |
| 51 | `        db_paths = [DB_PATH]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 52 | `    else:` | 条件分支控制。 |
| 53 | `        db_paths = [DB_PATH, ORDERS_DB_PATH, SUMMARY_DB_PATH]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 54 | `    db_key = db_name if db_name else &#x27;all&#x27;` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 55 | `` | 空行，用于逻辑分段与可读性。 |
| 56 | `    for db_path in db_paths:` | 循环遍历集合或结果集。 |
| 57 | `        conn = sqlite3.connect(db_path)` | 连接 SQLite 数据库。 |
| 58 | `        cur = conn.cursor()` | 创建数据库游标对象。 |
| 59 | `        cur.execute(&quot;SELECT name FROM sqlite_master WHERE type=&#x27;table&#x27; AND name NOT LIKE &#x27;sqlite_%&#x27; ORDER BY name&quot;)` | 执行 SQL 语句。 |
| 60 | `        tables = [r[0] for r in cur.fetchall()]` | 读取 SQL 查询结果。 |
| 61 | `` | 空行，用于逻辑分段与可读性。 |
| 62 | `        for t in tables:` | 循环遍历集合或结果集。 |
| 63 | `            cur.execute(f&quot;PRAGMA table_info({t})&quot;)` | 执行 SQL 语句。 |
| 64 | `            cols = [{&#x27;name&#x27;: c[1], &#x27;type&#x27;: c[2]} for c in cur.fetchall()]` | 读取 SQL 查询结果。 |
| 65 | `            col_names = [c[&#x27;name&#x27;] for c in cols]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 66 | `` | 空行，用于逻辑分段与可读性。 |
| 67 | `            date_range = None` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 68 | `            for dc in [&#x27;date&#x27;, &#x27;Date&#x27;, &#x27;created_at&#x27;]:` | 循环遍历集合或结果集。 |
| 69 | `                if dc in col_names:` | 条件分支控制。 |
| 70 | `                    try:` | 异常处理：尝试执行可能失败的逻辑。 |
| 71 | `                        cur.execute(f&quot;SELECT MIN({dc}), MAX({dc}) FROM {t} WHERE {dc} IS NOT NULL&quot;)` | 执行 SQL 语句。 |
| 72 | `                        r = cur.fetchone()` | 读取 SQL 查询结果。 |
| 73 | `                        if r and r[0]:` | 条件分支控制。 |
| 74 | `                            date_range = [r[0], r[1]]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 75 | `                            break` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 76 | `                    except:` | 异常处理：捕获错误分支。 |
| 77 | `                        pass` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 78 | `` | 空行，用于逻辑分段与可读性。 |
| 79 | `            cur.execute(f&quot;SELECT COUNT(*) FROM {t}&quot;)` | 执行 SQL 语句。 |
| 80 | `            count = cur.fetchone()[0]` | 读取 SQL 查询结果。 |
| 81 | `            meta[t] = {` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 82 | `                &#x27;columns&#x27;: cols,` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 83 | `                &#x27;date_range&#x27;: date_range,` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 84 | `                &#x27;row_count&#x27;: count,` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 85 | `                &#x27;db&#x27;: &#x27;analysis&#x27; if db_path == DB_PATH else (&#x27;orders&#x27; if db_path == ORDERS_DB_PATH else &#x27;summary&#x27;),` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 86 | `                &#x27;db_name&#x27;: DATABASES[&#x27;analysis&#x27;][&#x27;name&#x27;] if db_path == DB_PATH else (DATABASES[&#x27;orders&#x27;][&#x27;name&#x27;] if db_path == ORDERS_DB_PATH else DATABASES[&#x27;summary&#x27;][&#x27;name&#x27;])` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 87 | `            }` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 88 | `        conn.close()` | 关闭数据库连接，释放资源。 |
| 89 | `    return meta` | 函数返回结果。 |
| 90 | `` | 空行，用于逻辑分段与可读性。 |
| 91 | `def detect_date_col(cur, table):` | 定义函数 `detect_date_col`。 |
| 92 | `    date_cols = [&#x27;date&#x27;, &#x27;Date&#x27;, &#x27;DATE&#x27;, &#x27;日期&#x27;, &#x27;created_at&#x27;]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 93 | `    for col in date_cols:` | 循环遍历集合或结果集。 |
| 94 | `        try:` | 异常处理：尝试执行可能失败的逻辑。 |
| 95 | `            cur.execute(f&quot;SELECT {col} FROM {table} LIMIT 1&quot;)` | 执行 SQL 语句。 |
| 96 | `            return col` | 函数返回结果。 |
| 97 | `        except:` | 异常处理：捕获错误分支。 |
| 98 | `            pass` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 99 | `    return None` | 函数返回结果。 |
| 100 | `` | 空行，用于逻辑分段与可读性。 |
| 101 | `def query_data(table, x_field, y_fields, date_from=None, date_to=None, group_by=None, filters=None, db=None, tables=None):` | 定义函数 `query_data`。 |
| 102 | `    &quot;&quot;&quot;通用数据查询&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 103 | `    db_path = get_db_path(table, db)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 104 | `    conn = sqlite3.connect(db_path)` | 连接 SQLite 数据库。 |
| 105 | `    conn.row_factory = sqlite3.Row` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 106 | `    cur = conn.cursor()` | 创建数据库游标对象。 |
| 107 | `` | 空行，用于逻辑分段与可读性。 |
| 108 | `    # 多表支持` | 注释行，用于说明模块或逻辑分区。 |
| 109 | `    if tables and len(tables) &gt; 1:` | 条件分支控制。 |
| 110 | `        # 获取每个表的字段` | 注释行，用于说明模块或逻辑分区。 |
| 111 | `        table_cols = {}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 112 | `        for t in tables:` | 循环遍历集合或结果集。 |
| 113 | `            try:` | 异常处理：尝试执行可能失败的逻辑。 |
| 114 | `                cur.execute(f&quot;PRAGMA table_info({t})&quot;)` | 执行 SQL 语句。 |
| 115 | `                table_cols[t] = [c[1] for c in cur.fetchall()]` | 读取 SQL 查询结果。 |
| 116 | `            except:` | 异常处理：捕获错误分支。 |
| 117 | `                table_cols[t] = []` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 118 | `` | 空行，用于逻辑分段与可读性。 |
| 119 | `        # 找出每个表特有的后缀模式` | 注释行，用于说明模块或逻辑分区。 |
| 120 | `        # 如小乌龟汇总用_龟1/_龟2/_龟12，跨所汇总用_跨1/_跨2/_跨12` | 注释行，用于说明模块或逻辑分区。 |
| 121 | `        table_suffixes = {}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 122 | `        for t in tables:` | 循环遍历集合或结果集。 |
| 123 | `            suffixes = set()` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 124 | `            for c in table_cols[t]:` | 循环遍历集合或结果集。 |
| 125 | `                parts = c.rsplit(&#x27;_&#x27;, 1)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 126 | `                if len(parts) == 2 and parts[1] not in [&#x27;id&#x27;, &#x27;date&#x27;, &#x27;日期&#x27;]:` | 条件分支控制。 |
| 127 | `                    suffixes.add(parts[1])` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 128 | `            table_suffixes[t] = suffixes` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 129 | `` | 空行，用于逻辑分段与可读性。 |
| 130 | `        # 为每个字段找到在各表中的实际列名` | 注释行，用于说明模块或逻辑分区。 |
| 131 | `        # 用户选&quot;今日总盈亏&quot;，小乌龟应该匹配&quot;今日总盈亏_龟1&quot;等，跨所匹配&quot;今日总盈亏_跨1&quot;等` | 注释行，用于说明模块或逻辑分区。 |
| 132 | `        # 也支持格式&quot;今日总盈亏_小乌龟&quot;表示只从特定表获取` | 注释行，用于说明模块或逻辑分区。 |
| 133 | `        field_map = {}         # f -&gt; t -&gt; 实际列名` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 134 | `        all_field_suffixes = {}  # f -&gt; t -&gt; [所有匹配的后缀]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 135 | `` | 空行，用于逻辑分段与可读性。 |
| 136 | `        # 解析字段名，提取基础字段和目标表` | 注释行，用于说明模块或逻辑分区。 |
| 137 | `        parsed_fields = {}  # f -&gt; {base_field, target_table}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 138 | `        for f in y_fields:` | 循环遍历集合或结果集。 |
| 139 | `            base_field = f` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 140 | `            target_table = None` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 141 | `            # 检查是否有表名后缀（格式：field_表名缩写）` | 注释行，用于说明模块或逻辑分区。 |
| 142 | `            for t in tables:` | 循环遍历集合或结果集。 |
| 143 | `                table_short = t.replace(&#x27;汇总&#x27;, &#x27;&#x27;).replace(&#x27;大币&#x27;, &#x27;&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 144 | `                if f.endswith(&#x27;_&#x27; + table_short):` | 条件分支控制。 |
| 145 | `                    base_field = f[:-len(table_short)-1]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 146 | `                    target_table = t` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 147 | `                    break` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 148 | `            parsed_fields[f] = {&#x27;base_field&#x27;: base_field, &#x27;target_table&#x27;: target_table}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 149 | `` | 空行，用于逻辑分段与可读性。 |
| 150 | `        for f in y_fields:` | 循环遍历集合或结果集。 |
| 151 | `            field_map[f] = {}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 152 | `            all_field_suffixes[f] = {}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 153 | `            base_field = parsed_fields[f][&#x27;base_field&#x27;]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 154 | `            target_table = parsed_fields[f][&#x27;target_table&#x27;]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 155 | `            for t in tables:` | 循环遍历集合或结果集。 |
| 156 | `                if target_table and t != target_table:` | 条件分支控制。 |
| 157 | `                    continue` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 158 | `                # 精确匹配（优先精确匹配）` | 注释行，用于说明模块或逻辑分区。 |
| 159 | `                exact = [c for c in table_cols[t] if c == base_field]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 160 | `                if exact:` | 条件分支控制。 |
| 161 | `                    field_map[f][t] = exact[0]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 162 | `                    all_field_suffixes[f][t] = [exact[0]]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 163 | `                    continue` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 164 | `                # 按后缀匹配（按长度降序，优先更长的后缀如龟12/跨12）` | 注释行，用于说明模块或逻辑分区。 |
| 165 | `                sorted_suffixes = sorted(table_suffixes[t], key=lambda s: len(s), reverse=True)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 166 | `                matched = []` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 167 | `                for suffix in sorted_suffixes:` | 循环遍历集合或结果集。 |
| 168 | `                    candidate = f&#x27;{base_field}_{suffix}&#x27;` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 169 | `                    if candidate in table_cols[t]:` | 条件分支控制。 |
| 170 | `                        matched.append(candidate)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 171 | `                all_field_suffixes[f][t] = matched if matched else []` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 172 | `                # Bug fix: 只取最长的那个后缀，不要 SUM 所有匹配的后缀` | 注释行，用于说明模块或逻辑分区。 |
| 173 | `                if matched:` | 条件分支控制。 |
| 174 | `                    field_map[f][t] = matched[0]  # 取最长后缀` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 175 | `` | 空行，用于逻辑分段与可读性。 |
| 176 | `        date_col = detect_date_col(cur, tables[0]) or &#x27;日期&#x27;` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 177 | `` | 空行，用于逻辑分段与可读性。 |
| 178 | `        # 先查每个表的数据` | 注释行，用于说明模块或逻辑分区。 |
| 179 | `        table_data = {}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 180 | `        for t in tables:` | 循环遍历集合或结果集。 |
| 181 | `            select_fields_t = [date_col]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 182 | `            if group_by:` | 条件分支控制。 |
| 183 | `                select_fields_t.append(group_by)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 184 | `            orig_fields_t = []` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 185 | `            actual_cols_t = []` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 186 | `            sum_exprs = []` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 187 | `            for f in y_fields:` | 循环遍历集合或结果集。 |
| 188 | `                if t in field_map.get(f, {}) and field_map[f][t]:` | 条件分支控制。 |
| 189 | `                    # field_map[f][t] 已是单列（精确匹配或最长后缀）` | 注释行，用于说明模块或逻辑分区。 |
| 190 | `                    actual_col = field_map[f][t]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 191 | `                    base_field = parsed_fields[f][&#x27;base_field&#x27;]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 192 | `                    # 多后缀场景（len &gt; 1）只取最长后缀单列，不 SUM` | 注释行，用于说明模块或逻辑分区。 |
| 193 | `                    if &#x27;_&#x27; in actual_col and actual_col != base_field:` | 条件分支控制。 |
| 194 | `                        # 后缀列 → 不聚合，直接取单列` | 注释行，用于说明模块或逻辑分区。 |
| 195 | `                        select_fields_t.append(actual_col)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 196 | `                    else:` | 条件分支控制。 |
| 197 | `                        # 精确匹配 → 也不聚合` | 注释行，用于说明模块或逻辑分区。 |
| 198 | `                        select_fields_t.append(actual_col)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 199 | `                    orig_fields_t.append(f)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 200 | `                    actual_cols_t.append(actual_col)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 201 | `` | 空行，用于逻辑分段与可读性。 |
| 202 | `            if len(select_fields_t) &lt;= 1:` | 条件分支控制。 |
| 203 | `                print(f&quot;[DEBUG] SKIP {t}: select_fields_t={select_fields_t} (no fields matched)&quot;)` | 打印调试或启动信息。 |
| 204 | `                continue` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 205 | `` | 空行，用于逻辑分段与可读性。 |
| 206 | `            where_parts = []` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 207 | `            params_t = []` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 208 | `            if date_from:` | 条件分支控制。 |
| 209 | `                where_parts.append(f&quot;{date_col} &gt;= ?&quot;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 210 | `                params_t.append(date_from)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 211 | `            if date_to:` | 条件分支控制。 |
| 212 | `                where_parts.append(f&quot;{date_col} &lt;= ?&quot;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 213 | `                params_t.append(date_to)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 214 | `            where_sql = &quot; AND &quot;.join(where_parts) if where_parts else &quot;1=1&quot;` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 215 | `` | 空行，用于逻辑分段与可读性。 |
| 216 | `            select_sql = &quot;, &quot;.join(select_fields_t)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 217 | `            if group_by:` | 条件分支控制。 |
| 218 | `                group_expr = field_map[y_fields[0]][t] if y_fields and t in field_map.get(y_fields[0], {}) else &#x27;1&#x27;` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 219 | `                sql = f&quot;SELECT {select_sql}, SUM({group_expr}) as _val FROM {t} WHERE {where_sql} GROUP BY {group_by}, {date_col} ORDER BY {group_by}, {date_col} LIMIT {MAX_ROWS}&quot;` | 构建 SQL 查询字符串。 |
| 220 | `            elif sum_exprs:` | 条件分支控制。 |
| 221 | `                sql = f&quot;SELECT {select_sql} FROM {t} WHERE {where_sql} GROUP BY {date_col} ORDER BY {date_col} LIMIT {MAX_ROWS}&quot;` | 构建 SQL 查询字符串。 |
| 222 | `            else:` | 条件分支控制。 |
| 223 | `                sql = f&quot;SELECT {select_sql} FROM {t} WHERE {where_sql} ORDER BY {date_col} LIMIT {MAX_ROWS}&quot;` | 构建 SQL 查询字符串。 |
| 224 | `            print(f&quot;[DEBUG] SQL for {t}: {sql}, params={params_t}&quot;)` | 打印调试或启动信息。 |
| 225 | `            cur.execute(sql, params_t)` | 执行 SQL 语句。 |
| 226 | `            rows = cur.fetchall()` | 读取 SQL 查询结果。 |
| 227 | `            cols = list(dict(rows[0]).keys()) if rows else []` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 228 | `            print(f&quot;[DEBUG] {t}: got {len(rows)} rows, cols={cols}&quot;)` | 打印调试或启动信息。 |
| 229 | `            table_data[t] = {` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 230 | `                &#x27;orig_fields&#x27;: orig_fields_t,` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 231 | `                &#x27;actual_cols&#x27;: actual_cols_t,` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 232 | `                &#x27;rows&#x27;: [dict(r) for r in rows],` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 233 | `                &#x27;has_group_by&#x27;: group_by is not None,` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 234 | `                &#x27;sum_exprs&#x27;: sum_exprs` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 235 | `            }` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 236 | `` | 空行，用于逻辑分段与可读性。 |
| 237 | `        # 合并数据` | 注释行，用于说明模块或逻辑分区。 |
| 238 | `        print(f&quot;[DEBUG] table_data before merge: {[(t, len(d[&#x27;rows&#x27;]), d[&#x27;orig_fields&#x27;], d[&#x27;actual_cols&#x27;]) for t, d in table_data.items()]}&quot;)` | 打印调试或启动信息。 |
| 239 | `        merged = {}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 240 | `        for t, data in table_data.items():` | 循环遍历集合或结果集。 |
| 241 | `            for r in data[&#x27;rows&#x27;]:` | 循环遍历集合或结果集。 |
| 242 | `                if group_by:` | 条件分支控制。 |
| 243 | `                    key = r.get(group_by, &#x27;总计&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 244 | `                else:` | 条件分支控制。 |
| 245 | `                    key = r.get(date_col, &#x27;&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 246 | `                if key not in merged:` | 条件分支控制。 |
| 247 | `                    merged[key] = {date_col if not group_by else group_by: key}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 248 | `                for i, f in enumerate(data[&#x27;orig_fields&#x27;]):` | 循环遍历集合或结果集。 |
| 249 | `                    base_field = parsed_fields.get(f, {}).get(&#x27;base_field&#x27;, f)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 250 | `                    # Bug fix: 每个表的列名必须唯一，用表名全称做后缀避免冲突` | 注释行，用于说明模块或逻辑分区。 |
| 251 | `                    # v4_2_今日总盈亏 vs v4_23_今日总盈亏 不会冲突` | 注释行，用于说明模块或逻辑分区。 |
| 252 | `                    col_name = f&#x27;{t}_{base_field}&#x27;` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 253 | `                    actual_col = data[&#x27;actual_cols&#x27;][i]` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 254 | `                    val = r.get(actual_col) or 0` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 255 | `                    if col_name not in merged[key]:` | 条件分支控制。 |
| 256 | `                        merged[key][col_name] = val` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 257 | `                    else:` | 条件分支控制。 |
| 258 | `                        merged[key][col_name] = merged[key].get(col_name, 0) + val` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 259 | `                    print(f&quot;[DEBUG] merge {t}: key={key}, col_name={col_name}, actual_col={actual_col}, val={val}&quot;)` | 打印调试或启动信息。 |
| 260 | `` | 空行，用于逻辑分段与可读性。 |
| 261 | `        conn.close()` | 关闭数据库连接，释放资源。 |
| 262 | `` | 空行，用于逻辑分段与可读性。 |
| 263 | `        # 构建所有表×字段的完整列名，确保每个日期行都有所有列` | 注释行，用于说明模块或逻辑分区。 |
| 264 | `        all_col_names = set()` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 265 | `        for t in tables:` | 循环遍历集合或结果集。 |
| 266 | `            for f in y_fields:` | 循环遍历集合或结果集。 |
| 267 | `                base_field = parsed_fields.get(f, {}).get(&#x27;base_field&#x27;, f)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 268 | `                col_name = f&#x27;{t}_{base_field}&#x27;` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 269 | `                all_col_names.add(col_name)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 270 | `` | 空行，用于逻辑分段与可读性。 |
| 271 | `        for row in merged.values():` | 循环遍历集合或结果集。 |
| 272 | `            for col in all_col_names:` | 循环遍历集合或结果集。 |
| 273 | `                if col not in row:` | 条件分支控制。 |
| 274 | `                    row[col] = 0` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 275 | `` | 空行，用于逻辑分段与可读性。 |
| 276 | `        result = sorted(merged.values(), key=lambda x: str(x.get(group_by or date_col, &#x27;&#x27;)))` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 277 | `        print(f&quot;[DEBUG] query_data multi-table: tables={tables}, y_fields={y_fields}, merged_count={len(result)}, first_row_keys={list(result[0].keys()) if result else []}&quot;)` | 打印调试或启动信息。 |
| 278 | `        return result` | 函数返回结果。 |
| 279 | `` | 空行，用于逻辑分段与可读性。 |
| 280 | `    # 单表查询` | 注释行，用于说明模块或逻辑分区。 |
| 281 | `    date_col = detect_date_col(cur, table)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 282 | `    if x_field == &#x27;date&#x27; and date_col and date_col != &#x27;date&#x27;:` | 条件分支控制。 |
| 283 | `        x_field = date_col` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 284 | `` | 空行，用于逻辑分段与可读性。 |
| 285 | `    select_fields = [x_field] + list(y_fields)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 286 | `    select_fields_sql = &quot;, &quot;.join(select_fields)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 287 | `` | 空行，用于逻辑分段与可读性。 |
| 288 | `    where_clauses = []` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 289 | `    params = []` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 290 | `` | 空行，用于逻辑分段与可读性。 |
| 291 | `    if date_from and date_col:` | 条件分支控制。 |
| 292 | `        where_clauses.append(f&quot;{date_col} &gt;= ?&quot;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 293 | `        params.append(date_from)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 294 | `    if date_to and date_col:` | 条件分支控制。 |
| 295 | `        where_clauses.append(f&quot;{date_col} &lt;= ?&quot;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 296 | `        params.append(date_to)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 297 | `` | 空行，用于逻辑分段与可读性。 |
| 298 | `    if filters:` | 条件分支控制。 |
| 299 | `        for col, val in filters.items():` | 循环遍历集合或结果集。 |
| 300 | `            if val and val != &#x27;all&#x27;:` | 条件分支控制。 |
| 301 | `                where_clauses.append(f&quot;{col} = ?&quot;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 302 | `                params.append(val)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 303 | `` | 空行，用于逻辑分段与可读性。 |
| 304 | `    where_sql = &quot; AND &quot;.join(where_clauses) if where_clauses else &quot;1=1&quot;` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 305 | `` | 空行，用于逻辑分段与可读性。 |
| 306 | `    if group_by:` | 条件分支控制。 |
| 307 | `        sql = f&quot;SELECT {group_by}, &quot; + &quot;, &quot;.join([f&quot;SUM({f}) as {f}_sum&quot; for f in y_fields]) + f&quot;, COUNT(*) as __count FROM {table} WHERE {where_sql} GROUP BY {group_by} ORDER BY {group_by} LIMIT {MAX_ROWS}&quot;` | 构建 SQL 查询字符串。 |
| 308 | `    else:` | 条件分支控制。 |
| 309 | `        sql = f&quot;SELECT {select_fields_sql} FROM {table} WHERE {where_sql} ORDER BY {x_field} LIMIT {MAX_ROWS}&quot;` | 构建 SQL 查询字符串。 |
| 310 | `` | 空行，用于逻辑分段与可读性。 |
| 311 | `    cur.execute(sql, params)` | 执行 SQL 语句。 |
| 312 | `    rows = cur.fetchall()` | 读取 SQL 查询结果。 |
| 313 | `    conn.close()` | 关闭数据库连接，释放资源。 |
| 314 | `    ` | 空行，用于逻辑分段与可读性。 |
| 315 | `    print(f&quot;[DEBUG] query_data single-table: table={table}, y_fields={y_fields}, row_count={len(rows)}, first_row_keys={list(dict(rows[0]).keys()) if rows else []}&quot;)` | 打印调试或启动信息。 |
| 316 | `    return [dict(r) for r in rows]` | 函数返回结果。 |
| 317 | `` | 空行，用于逻辑分段与可读性。 |
| 318 | `def get_distinct_values(table, field, db=None):` | 定义函数 `get_distinct_values`。 |
| 319 | `    &quot;&quot;&quot;获取某字段的所有不重复值（用于下拉筛选）&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 320 | `    conn = sqlite3.connect(get_db_path(table, db))` | 连接 SQLite 数据库。 |
| 321 | `    cur = conn.cursor()` | 创建数据库游标对象。 |
| 322 | `    try:` | 异常处理：尝试执行可能失败的逻辑。 |
| 323 | `        cur.execute(f&quot;SELECT DISTINCT {field} FROM {table} WHERE {field} IS NOT NULL ORDER BY {field}&quot;)` | 执行 SQL 语句。 |
| 324 | `        values = [r[0] for r in cur.fetchall()]` | 读取 SQL 查询结果。 |
| 325 | `        conn.close()` | 关闭数据库连接，释放资源。 |
| 326 | `        return values` | 函数返回结果。 |
| 327 | `    except:` | 异常处理：捕获错误分支。 |
| 328 | `        conn.close()` | 关闭数据库连接，释放资源。 |
| 329 | `        return []` | 函数返回结果。 |
| 330 | `` | 空行，用于逻辑分段与可读性。 |
| 331 | `def get_date_range(table, db=None):` | 定义函数 `get_date_range`。 |
| 332 | `    &quot;&quot;&quot;获取表的最大最小日期&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 333 | `    conn = sqlite3.connect(get_db_path(table, db))` | 连接 SQLite 数据库。 |
| 334 | `    cur = conn.cursor()` | 创建数据库游标对象。 |
| 335 | `    cur.execute(f&quot;PRAGMA table_info({table})&quot;)` | 执行 SQL 语句。 |
| 336 | `    col_names = [c[1] for c in cur.fetchall()]` | 读取 SQL 查询结果。 |
| 337 | `    for dc in [&#x27;date&#x27;, &#x27;Date&#x27;, &#x27;created_at&#x27;]:` | 循环遍历集合或结果集。 |
| 338 | `        if dc in col_names:` | 条件分支控制。 |
| 339 | `            try:` | 异常处理：尝试执行可能失败的逻辑。 |
| 340 | `                cur.execute(f&quot;SELECT MIN({dc}), MAX({dc}) FROM {table} WHERE {dc} IS NOT NULL&quot;)` | 执行 SQL 语句。 |
| 341 | `                r = cur.fetchone()` | 读取 SQL 查询结果。 |
| 342 | `                if r and r[0]:` | 条件分支控制。 |
| 343 | `                    conn.close()` | 关闭数据库连接，释放资源。 |
| 344 | `                    return r[0], r[1]` | 函数返回结果。 |
| 345 | `            except:` | 异常处理：捕获错误分支。 |
| 346 | `                pass` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 347 | `    conn.close()` | 关闭数据库连接，释放资源。 |
| 348 | `    return None, None` | 函数返回结果。 |
| 349 | `` | 空行，用于逻辑分段与可读性。 |
| 350 | `# ============================================================` | 注释行，用于说明模块或逻辑分区。 |
| 351 | `# 路由` | 注释行，用于说明模块或逻辑分区。 |
| 352 | `# ============================================================` | 注释行，用于说明模块或逻辑分区。 |
| 353 | `` | 空行，用于逻辑分段与可读性。 |
| 354 | `@app.route(&#x27;/&#x27;)` | Flask 路由装饰器，声明接口路径。 |
| 355 | `def index():` | 定义函数 `index`。 |
| 356 | `    &quot;&quot;&quot;主页 - 数据选择界面&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 357 | `    meta = get_tables_meta()` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 358 | `    return render_template(&#x27;index.html&#x27;, meta=meta)` | 函数返回结果。 |
| 359 | `` | 空行，用于逻辑分段与可读性。 |
| 360 | `@app.route(&#x27;/api/databases&#x27;)` | Flask 路由装饰器，声明接口路径。 |
| 361 | `def api_databases():` | 定义函数 `api_databases`。 |
| 362 | `    &quot;&quot;&quot;获取所有数据库及其表&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 363 | `    result = {}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 364 | `    for db_key, db_info in DATABASES.items():` | 循环遍历集合或结果集。 |
| 365 | `        conn = sqlite3.connect(db_info[&#x27;path&#x27;])` | 连接 SQLite 数据库。 |
| 366 | `        cur = conn.cursor()` | 创建数据库游标对象。 |
| 367 | `        cur.execute(&quot;SELECT name FROM sqlite_master WHERE type=&#x27;table&#x27; AND name NOT LIKE &#x27;sqlite_%&#x27; ORDER BY name&quot;)` | 执行 SQL 语句。 |
| 368 | `        tables = [r[0] for r in cur.fetchall()]` | 读取 SQL 查询结果。 |
| 369 | `        conn.close()` | 关闭数据库连接，释放资源。 |
| 370 | `        result[db_key] = {&#x27;name&#x27;: db_info[&#x27;name&#x27;], &#x27;tables&#x27;: tables}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 371 | `    return jsonify(result)` | 函数返回结果。 |
| 372 | `` | 空行，用于逻辑分段与可读性。 |
| 373 | `@app.route(&#x27;/api/tables&#x27;)` | Flask 路由装饰器，声明接口路径。 |
| 374 | `def api_tables():` | 定义函数 `api_tables`。 |
| 375 | `    &quot;&quot;&quot;获取所有表信息&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 376 | `    db = request.args.get(&#x27;db&#x27;)` | 读取 HTTP 请求参数或体。 |
| 377 | `    meta = get_tables_meta(db)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 378 | `    return jsonify(meta)` | 函数返回结果。 |
| 379 | `` | 空行，用于逻辑分段与可读性。 |
| 380 | `@app.route(&#x27;/api/query&#x27;, methods=[&#x27;POST&#x27;])` | Flask 路由装饰器，声明接口路径。 |
| 381 | `def api_query():` | 定义函数 `api_query`。 |
| 382 | `    &quot;&quot;&quot;执行查询&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 383 | `    body = request.json` | 读取 HTTP 请求参数或体。 |
| 384 | `    table = body.get(&#x27;table&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 385 | `    db = body.get(&#x27;db&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 386 | `    x_field = body.get(&#x27;x_field&#x27;, &#x27;date&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 387 | `    y_fields = body.get(&#x27;y_fields&#x27;, [])` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 388 | `    date_from = body.get(&#x27;date_from&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 389 | `    date_to = body.get(&#x27;date_to&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 390 | `    group_by = body.get(&#x27;group_by&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 391 | `    filters = body.get(&#x27;filters&#x27;, {})` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 392 | `    tables = body.get(&#x27;tables&#x27;, [table])` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 393 | `` | 空行，用于逻辑分段与可读性。 |
| 394 | `    if not tables or not y_fields:` | 条件分支控制。 |
| 395 | `        return jsonify({&#x27;error&#x27;: &#x27;请选择表和字段&#x27;}), 400` | 函数返回结果。 |
| 396 | `` | 空行，用于逻辑分段与可读性。 |
| 397 | `    try:` | 异常处理：尝试执行可能失败的逻辑。 |
| 398 | `        print(f&quot;[DEBUG] api_query: tables={tables}, y_fields={y_fields}&quot;)` | 打印调试或启动信息。 |
| 399 | `        data = query_data(tables[0], x_field, y_fields, date_from, date_to, group_by, filters, db, tables)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 400 | `        return jsonify({&#x27;success&#x27;: True, &#x27;data&#x27;: data, &#x27;count&#x27;: len(data)})` | 函数返回结果。 |
| 401 | `    except Exception as e:` | 异常处理：捕获错误分支。 |
| 402 | `        return jsonify({&#x27;error&#x27;: str(e)}), 500` | 函数返回结果。 |
| 403 | `` | 空行，用于逻辑分段与可读性。 |
| 404 | `@app.route(&#x27;/api/values/&lt;table&gt;/&lt;field&gt;&#x27;)` | Flask 路由装饰器，声明接口路径。 |
| 405 | `def api_values(table, field):` | 定义函数 `api_values`。 |
| 406 | `    &quot;&quot;&quot;获取某字段的不重复值&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 407 | `    try:` | 异常处理：尝试执行可能失败的逻辑。 |
| 408 | `        db = request.args.get(&#x27;db&#x27;)` | 读取 HTTP 请求参数或体。 |
| 409 | `        values = get_distinct_values(table, field, db)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 410 | `        return jsonify(values)` | 函数返回结果。 |
| 411 | `    except Exception as e:` | 异常处理：捕获错误分支。 |
| 412 | `        return jsonify({&#x27;error&#x27;: str(e)}), 500` | 函数返回结果。 |
| 413 | `` | 空行，用于逻辑分段与可读性。 |
| 414 | `@app.route(&#x27;/api/daterange/&lt;table&gt;&#x27;)` | Flask 路由装饰器，声明接口路径。 |
| 415 | `def api_daterange(table):` | 定义函数 `api_daterange`。 |
| 416 | `    &quot;&quot;&quot;获取表的日期范围&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 417 | `    db = request.args.get(&#x27;db&#x27;)` | 读取 HTTP 请求参数或体。 |
| 418 | `    dmin, dmax = get_date_range(table, db)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 419 | `    return jsonify({&#x27;min&#x27;: dmin, &#x27;max&#x27;: dmax})` | 函数返回结果。 |
| 420 | `` | 空行，用于逻辑分段与可读性。 |
| 421 | `@app.route(&#x27;/api/heatmap&#x27;, methods=[&#x27;POST&#x27;])` | Flask 路由装饰器，声明接口路径。 |
| 422 | `def api_heatmap():` | 定义函数 `api_heatmap`。 |
| 423 | `    &quot;&quot;&quot;热力图数据 - spread_range × size_range&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 424 | `    body = request.json` | 读取 HTTP 请求参数或体。 |
| 425 | `    table = body.get(&#x27;table&#x27;, &#x27;k12_token_spread_size_daily_v2&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 426 | `    date_from = body.get(&#x27;date_from&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 427 | `    date_to = body.get(&#x27;date_to&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 428 | `    metric = body.get(&#x27;metric&#x27;, &#x27;alpha&#x27;)  # alpha / pnl / theo / bundle` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 429 | `` | 空行，用于逻辑分段与可读性。 |
| 430 | `    conn = sqlite3.connect(get_db_path(table))` | 连接 SQLite 数据库。 |
| 431 | `    conn.row_factory = sqlite3.Row` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 432 | `    cur = conn.cursor()` | 创建数据库游标对象。 |
| 433 | `` | 空行，用于逻辑分段与可读性。 |
| 434 | `    where = &quot;1=1&quot;` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 435 | `    params = []` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 436 | `    if date_from:` | 条件分支控制。 |
| 437 | `        where += &quot; AND date &gt;= ?&quot;` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 438 | `        params.append(date_from)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 439 | `    if date_to:` | 条件分支控制。 |
| 440 | `        where += &quot; AND date &lt;= ?&quot;` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 441 | `        params.append(date_to)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 442 | `` | 空行，用于逻辑分段与可读性。 |
| 443 | `    sql = f&quot;&quot;&quot;` | 构建 SQL 查询字符串。 |
| 444 | `        SELECT spread_range, size_range,` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 445 | `               SUM({metric}) as value,` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 446 | `               SUM(order_count) as cnt` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 447 | `        FROM {table}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 448 | `        WHERE {where}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 449 | `        GROUP BY spread_range, size_range` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 450 | `        ORDER BY spread_range, size_range` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 451 | `    &quot;&quot;&quot;` | 多行文档字符串边界。 |
| 452 | `    cur.execute(sql, params)` | 执行 SQL 语句。 |
| 453 | `    rows = [dict(r) for r in cur.fetchall()]` | 读取 SQL 查询结果。 |
| 454 | `    conn.close()` | 关闭数据库连接，释放资源。 |
| 455 | `    return jsonify(rows)` | 函数返回结果。 |
| 456 | `` | 空行，用于逻辑分段与可读性。 |
| 457 | `@app.route(&#x27;/api/daily&#x27;, methods=[&#x27;POST&#x27;])` | Flask 路由装饰器，声明接口路径。 |
| 458 | `def api_daily():` | 定义函数 `api_daily`。 |
| 459 | `    &quot;&quot;&quot;每日趋势数据&quot;&quot;&quot;` | 多行文档字符串边界。 |
| 460 | `    body = request.json` | 读取 HTTP 请求参数或体。 |
| 461 | `    table = body.get(&#x27;table&#x27;, &#x27;k12_token_spread_size_daily_v2&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 462 | `    date_from = body.get(&#x27;date_from&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 463 | `    date_to = body.get(&#x27;date_to&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 464 | `    metric = body.get(&#x27;metric&#x27;, &#x27;alpha&#x27;)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 465 | `    group_by = body.get(&#x27;group_by&#x27;)  # spread_range, size_range, token` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 466 | `` | 空行，用于逻辑分段与可读性。 |
| 467 | `    conn = sqlite3.connect(get_db_path(table))` | 连接 SQLite 数据库。 |
| 468 | `    conn.row_factory = sqlite3.Row` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 469 | `    cur = conn.cursor()` | 创建数据库游标对象。 |
| 470 | `    ` | 空行，用于逻辑分段与可读性。 |
| 471 | `    where = &quot;1=1&quot;` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 472 | `    params = []` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 473 | `    if date_from:` | 条件分支控制。 |
| 474 | `        where += &quot; AND date &gt;= ?&quot;` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 475 | `        params.append(date_from)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 476 | `    if date_to:` | 条件分支控制。 |
| 477 | `        where += &quot; AND date &lt;= ?&quot;` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 478 | `        params.append(date_to)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 479 | `    ` | 空行，用于逻辑分段与可读性。 |
| 480 | `    if group_by:` | 条件分支控制。 |
| 481 | `        sql = f&quot;&quot;&quot;` | 构建 SQL 查询字符串。 |
| 482 | `            SELECT date, {group_by},` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 483 | `                   SUM({metric}) as value,` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 484 | `                   SUM(order_count) as cnt` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 485 | `            FROM {table}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 486 | `            WHERE {where}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 487 | `            GROUP BY date, {group_by}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 488 | `            ORDER BY date, {group_by}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 489 | `        &quot;&quot;&quot;` | 多行文档字符串边界。 |
| 490 | `    else:` | 条件分支控制。 |
| 491 | `        sql = f&quot;&quot;&quot;` | 构建 SQL 查询字符串。 |
| 492 | `            SELECT date,` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 493 | `                   SUM({metric}) as value,` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 494 | `                   SUM(order_count) as cnt` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 495 | `            FROM {table}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 496 | `            WHERE {where}` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 497 | `            GROUP BY date` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 498 | `            ORDER BY date` | 业务逻辑代码（数据处理/组装/控制流程）。 |
| 499 | `        &quot;&quot;&quot;` | 多行文档字符串边界。 |
| 500 | `    ` | 空行，用于逻辑分段与可读性。 |
| 501 | `    cur.execute(sql, params)` | 执行 SQL 语句。 |
| 502 | `    rows = [dict(r) for r in cur.fetchall()]` | 读取 SQL 查询结果。 |
| 503 | `    conn.close()` | 关闭数据库连接，释放资源。 |
| 504 | `    return jsonify(rows)` | 函数返回结果。 |
| 505 | `` | 空行，用于逻辑分段与可读性。 |
| 506 | `if __name__ == &#x27;__main__&#x27;:` | 脚本入口判断，直接运行时启动服务。 |
| 507 | `    print(&quot;=&quot; * 50)` | 打印调试或启动信息。 |
| 508 | `    print(&quot;K12 可视化分析平台&quot;)` | 打印调试或启动信息。 |
| 509 | `    print(&quot;访问地址: http://localhost:5050&quot;)` | 打印调试或启动信息。 |
| 510 | `    print(&quot;按 Ctrl+C 停止服务&quot;)` | 打印调试或启动信息。 |
| 511 | `    print(&quot;=&quot; * 50)` | 打印调试或启动信息。 |
| 512 | `    app.run(host=&#x27;0.0.0.0&#x27;, port=5050, debug=False)` | 业务逻辑代码（数据处理/组装/控制流程）。 |
