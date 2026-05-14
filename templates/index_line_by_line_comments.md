# index.html 逐行注释对照

- 源文件: `/Users/yy/.hermes/workspace/db/visualizer/templates/index.html`
- 说明: 为避免破坏原始 CSS/JS 语法，本文件提供逐行注释对照，不改动原文件。

| 行号 | 原代码 | 注释 |
|---:|---|---|
| 1 | `&lt;!DOCTYPE html&gt;` | 声明HTML5文档类型。 |
| 2 | `&lt;html lang=&quot;zh-CN&quot;&gt;` | HTML根节点，设置文档语言。 |
| 3 | `&lt;head&gt;` | 头部开始，放置元信息、样式和标题。 |
| 4 | `&lt;meta charset=&quot;UTF-8&quot;&gt;` | 页面元信息（编码、视口等）。 |
| 5 | `&lt;meta name=&quot;viewport&quot; content=&quot;width=device-width, initial-scale=1.0&quot;&gt;` | 页面元信息（编码、视口等）。 |
| 6 | `&lt;title&gt;跨所可视化分析平台&lt;/title&gt;` | 浏览器标签页标题。 |
| 7 | `&lt;style&gt;` | 内联CSS样式开始。 |
| 8 | `  /* ============================================================` | CSS注释，说明主题或分区。 |
| 9 | `     天蓝色 + 灰色 专业主题` | CSS样式声明。 |
| 10 | `     主色: #4FA8D7 (天蓝色), 辅色: #8A8A8A (灰色)` | CSS样式声明。 |
| 11 | `     ============================================================ */` | CSS注释，说明主题或分区。 |
| 12 | `  :root {` | CSS规则块开始。 |
| 13 | `    --sky:       #4FA8D7;` | CSS样式声明。 |
| 14 | `    --sky-light: #7EC4E8;` | CSS样式声明。 |
| 15 | `    --sky-dark:  #3A8AB8;` | CSS样式声明。 |
| 16 | `    --gray-1:    #2A2A2E;` | CSS样式声明。 |
| 17 | `    --gray-2:    #353538;` | CSS样式声明。 |
| 18 | `    --gray-3:    #404044;` | CSS样式声明。 |
| 19 | `    --gray-4:    #888888;` | CSS样式声明。 |
| 20 | `    --gray-5:    #BBBBBB;` | CSS样式声明。 |
| 21 | `    --bg:        #1E1E22;` | CSS样式声明。 |
| 22 | `    --pos:       #4CAF82;` | CSS样式声明。 |
| 23 | `    --neg:       #E05C5C;` | CSS样式声明。 |
| 24 | `  }` | CSS规则块结束。 |
| 25 | `  * { margin: 0; padding: 0; box-sizing: border-box; }` | CSS规则，定义选择器样式。 |
| 26 | `  body { font-family: -apple-system, BlinkMacSystemFont, &#x27;Segoe UI&#x27;, sans-serif; background: var(--bg); color: var(--gray-5); min-height: 100vh; }` | CSS规则，定义选择器样式。 |
| 27 | `  .header { background: var(--gray-1); border-bottom: 1px solid var(--gray-3); padding: 16px 32px; display: flex; align-items: center; gap: 24px; }` | CSS规则，定义选择器样式。 |
| 28 | `  .header h1 { font-size: 18px; font-weight: 600; color: var(--sky); }` | CSS规则，定义选择器样式。 |
| 29 | `  .header .subtitle { font-size: 12px; color: var(--gray-4); }` | CSS规则，定义选择器样式。 |
| 30 | `  .main { display: flex; min-height: calc(100vh - 60px); }` | CSS规则，定义选择器样式。 |
| 31 | `` | 空行，用于提升可读性。 |
| 32 | `  /* 左侧控制面板 */` | CSS注释，说明主题或分区。 |
| 33 | `  .sidebar { width: 320px; background: var(--gray-1); border-right: 1px solid var(--gray-3); padding: 20px; overflow-y: auto; flex-shrink: 0; }` | CSS规则，定义选择器样式。 |
| 34 | `  .panel-section { margin-bottom: 24px; }` | CSS规则，定义选择器样式。 |
| 35 | `  .panel-title { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: var(--gray-4); margin-bottom: 10px; font-weight: 600; }` | CSS规则，定义选择器样式。 |
| 36 | `` | 空行，用于提升可读性。 |
| 37 | `  /* 选择器样式 */` | CSS注释，说明主题或分区。 |
| 38 | `  .ctrl-group { margin-bottom: 12px; }` | CSS规则，定义选择器样式。 |
| 39 | `  .ctrl-label { font-size: 12px; color: var(--gray-4); margin-bottom: 4px; display: block; }` | CSS规则，定义选择器样式。 |
| 40 | `  select, input[type=&quot;text&quot;], input[type=&quot;date&quot;] { width: 100%; background: var(--gray-2); border: 1px solid var(--gray-3); border-radius: 6px; color: var(--gray-5); padding: 8px 10px; font-size: 13px; outline: none; transition: border-color 0.2s; }` | CSS规则，定义选择器样式。 |
| 41 | `  select:focus, input:focus { border-color: var(--sky); }` | CSS规则，定义选择器样式。 |
| 42 | `  select[multiple] { height: 120px; }` | CSS规则，定义选择器样式。 |
| 43 | `` | 空行，用于提升可读性。 |
| 44 | `  /* 图表类型按钮 */` | CSS注释，说明主题或分区。 |
| 45 | `  .chart-types { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px; }` | CSS规则，定义选择器样式。 |
| 46 | `  .chart-type-btn { background: var(--gray-2); border: 1px solid var(--gray-3); border-radius: 6px; padding: 8px 4px; text-align: center; font-size: 11px; cursor: pointer; transition: all 0.2s; color: var(--gray-4); }` | CSS规则，定义选择器样式。 |
| 47 | `  .chart-type-btn:hover { border-color: var(--sky); color: var(--sky); }` | CSS规则，定义选择器样式。 |
| 48 | `  .chart-type-btn.active { background: var(--sky); border-color: var(--sky); color: var(--bg); font-weight: 600; }` | CSS规则，定义选择器样式。 |
| 49 | `` | 空行，用于提升可读性。 |
| 50 | `  /* 快捷卡片 */` | CSS注释，说明主题或分区。 |
| 51 | `  .quick-cards { display: grid; grid-template-columns: 1fr 1fr; gap: 6px; }` | CSS规则，定义选择器样式。 |
| 52 | `  .quick-card { background: var(--gray-2); border: 1px solid var(--gray-3); border-radius: 6px; padding: 10px 8px; cursor: pointer; transition: all 0.2s; font-size: 12px; }` | CSS规则，定义选择器样式。 |
| 53 | `  .quick-card:hover { border-color: var(--sky); }` | CSS规则，定义选择器样式。 |
| 54 | `  .quick-card.active { border-color: var(--sky); background: var(--gray-3); }` | CSS规则，定义选择器样式。 |
| 55 | `  .quick-card .qc-title { color: var(--sky); font-weight: 600; font-size: 11px; }` | CSS规则，定义选择器样式。 |
| 56 | `  .quick-card .qc-desc { color: var(--gray-4); font-size: 10px; margin-top: 2px; }` | CSS规则，定义选择器样式。 |
| 57 | `` | 空行，用于提升可读性。 |
| 58 | `  /* 主图表区域 */` | CSS注释，说明主题或分区。 |
| 59 | `  .content { flex: 1; padding: 20px; overflow: auto; }` | CSS规则，定义选择器样式。 |
| 60 | `  .chart-container { background: var(--gray-1); border-radius: 8px; border: 1px solid var(--gray-3); padding: 20px; margin-bottom: 16px; }` | CSS规则，定义选择器样式。 |
| 61 | `  .chart-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; }` | CSS规则，定义选择器样式。 |
| 62 | `  .chart-title { font-size: 14px; font-weight: 600; color: var(--sky); }` | CSS规则，定义选择器样式。 |
| 63 | `  .chart-meta { font-size: 11px; color: var(--gray-4); }` | CSS规则，定义选择器样式。 |
| 64 | `` | 空行，用于提升可读性。 |
| 65 | `  canvas { width: 100% !important; }` | CSS规则，定义选择器样式。 |
| 66 | `` | 空行，用于提升可读性。 |
| 67 | `  /* 数据表格 */` | CSS注释，说明主题或分区。 |
| 68 | `  .data-table { width: 100%; border-collapse: collapse; font-size: 12px; }` | CSS规则，定义选择器样式。 |
| 69 | `  .data-table th { background: var(--gray-2); color: var(--sky); padding: 8px 12px; text-align: left; font-weight: 600; border-bottom: 1px solid var(--gray-3); position: sticky; top: 0; }` | CSS规则，定义选择器样式。 |
| 70 | `  .data-table td { padding: 7px 12px; border-bottom: 1px solid var(--gray-2); color: var(--gray-5); }` | CSS规则，定义选择器样式。 |
| 71 | `  .data-table tr:hover td { background: var(--gray-2); }` | CSS规则，定义选择器样式。 |
| 72 | `  .data-table .num { text-align: right; font-variant-numeric: tabular-nums; }` | CSS规则，定义选择器样式。 |
| 73 | `  .data-table .pos { color: var(--pos); }` | CSS规则，定义选择器样式。 |
| 74 | `  .data-table .neg { color: var(--neg); }` | CSS规则，定义选择器样式。 |
| 75 | `` | 空行，用于提升可读性。 |
| 76 | `  /* 按钮 */` | CSS注释，说明主题或分区。 |
| 77 | `  .btn { background: var(--sky); color: var(--bg); border: none; border-radius: 6px; padding: 10px 20px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all 0.2s; }` | CSS规则，定义选择器样式。 |
| 78 | `  .btn:hover { background: var(--sky-light); }` | CSS规则，定义选择器样式。 |
| 79 | `  .btn-secondary { background: var(--gray-2); color: var(--gray-5); border: 1px solid var(--gray-3); }` | CSS规则，定义选择器样式。 |
| 80 | `  .btn-secondary:hover { border-color: var(--sky); color: var(--sky); }` | CSS规则，定义选择器样式。 |
| 81 | `` | 空行，用于提升可读性。 |
| 82 | `  .btn-row { display: flex; gap: 8px; margin-top: 12px; }` | CSS规则，定义选择器样式。 |
| 83 | `` | 空行，用于提升可读性。 |
| 84 | `  /* 筛选标签 */` | CSS注释，说明主题或分区。 |
| 85 | `  .filter-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px; }` | CSS规则，定义选择器样式。 |
| 86 | `  .filter-tag { background: var(--gray-2); border: 1px solid var(--gray-3); border-radius: 4px; padding: 3px 8px; font-size: 11px; color: var(--gray-4); display: flex; align-items: center; gap: 4px; }` | CSS规则，定义选择器样式。 |
| 87 | `  .filter-tag span { color: var(--sky); }` | CSS规则，定义选择器样式。 |
| 88 | `  .filter-tag button { background: none; border: none; color: var(--gray-4); cursor: pointer; font-size: 12px; padding: 0; line-height: 1; }` | CSS规则，定义选择器样式。 |
| 89 | `  .filter-tag button:hover { color: var(--neg); }` | CSS规则，定义选择器样式。 |
| 90 | `` | 空行，用于提升可读性。 |
| 91 | `  /* 加载状态 */` | CSS注释，说明主题或分区。 |
| 92 | `  .loading { text-align: center; padding: 40px; color: var(--gray-4); }` | CSS规则，定义选择器样式。 |
| 93 | `  .loading::after { content: &#x27;...&#x27;; animation: dots 1.5s infinite; }` | CSS规则，定义选择器样式。 |
| 94 | `  @keyframes dots { 0%,20%{content:&#x27;.&#x27;} 40%{content:&#x27;..&#x27;} 60%,100%{content:&#x27;...&#x27;} }` | 定义CSS关键帧动画。 |
| 95 | `` | 空行，用于提升可读性。 |
| 96 | `  /* 错误提示 */` | CSS注释，说明主题或分区。 |
| 97 | `  .error-msg { background: #2A1A1A; border: 1px solid var(--neg); border-radius: 6px; padding: 12px; color: var(--neg); font-size: 13px; margin-top: 12px; }` | CSS规则，定义选择器样式。 |
| 98 | `` | 空行，用于提升可读性。 |
| 99 | `  /* 无数据 */` | CSS注释，说明主题或分区。 |
| 100 | `  .no-data { text-align: center; padding: 40px; color: var(--gray-4); font-size: 13px; }` | CSS规则，定义选择器样式。 |
| 101 | `` | 空行，用于提升可读性。 |
| 102 | `  /* 分隔线 */` | CSS注释，说明主题或分区。 |
| 103 | `  .divider { border: none; border-top: 1px solid var(--gray-3); margin: 16px 0; }` | CSS规则，定义选择器样式。 |
| 104 | `` | 空行，用于提升可读性。 |
| 105 | `  /* 统计卡片 */` | CSS注释，说明主题或分区。 |
| 106 | `  .stat-cards { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px; }` | CSS规则，定义选择器样式。 |
| 107 | `  .stat-card { background: var(--gray-1); border: 1px solid var(--gray-3); border-radius: 8px; padding: 14px 16px; }` | CSS规则，定义选择器样式。 |
| 108 | `  .stat-card .sc-label { font-size: 11px; color: var(--gray-4); margin-bottom: 4px; }` | CSS规则，定义选择器样式。 |
| 109 | `  .stat-card .sc-value { font-size: 20px; font-weight: 700; font-variant-numeric: tabular-nums; }` | CSS规则，定义选择器样式。 |
| 110 | `  .stat-card .sc-value.pos { color: var(--pos); }` | CSS规则，定义选择器样式。 |
| 111 | `  .stat-card .sc-value.neg { color: var(--neg); }` | CSS规则，定义选择器样式。 |
| 112 | `  .stat-card .sc-value.neu { color: var(--gray-5); }` | CSS规则，定义选择器样式。 |
| 113 | `` | 空行，用于提升可读性。 |
| 114 | `  /* 复选框组 */` | CSS注释，说明主题或分区。 |
| 115 | `  .checkbox-group { display: flex; flex-direction: column; gap: 4px; max-height: 180px; overflow-y: auto; background: var(--gray-2); border-radius: 6px; padding: 8px; }` | CSS规则，定义选择器样式。 |
| 116 | `  .checkbox-item { display: flex; align-items: center; gap: 8px; font-size: 12px; color: var(--gray-5); cursor: pointer; }` | CSS规则，定义选择器样式。 |
| 117 | `  .checkbox-item input { accent-color: var(--sky); }` | CSS规则，定义选择器样式。 |
| 118 | `  .checkbox-item:hover { color: var(--sky); }` | CSS规则，定义选择器样式。 |
| 119 | `&lt;/style&gt;` | 内联CSS样式结束。 |
| 120 | `&lt;/head&gt;` | 头部结束。 |
| 121 | `&lt;body&gt;` | 页面主体开始。 |
| 122 | `` | 空行，用于提升可读性。 |
| 123 | `&lt;div class=&quot;header&quot;&gt;` | 容器节点，用于布局与分区。 |
| 124 | `  &lt;div&gt;` | 容器节点，用于布局与分区。 |
| 125 | `    &lt;h1&gt;跨所可视化分析平台&lt;/h1&gt;` | 一级标题。 |
| 126 | `  &lt;/div&gt;` | 容器节点结束。 |
| 127 | `&lt;/div&gt;` | 容器节点结束。 |
| 128 | `` | 空行，用于提升可读性。 |
| 129 | `&lt;div class=&quot;main&quot;&gt;` | 容器节点，用于布局与分区。 |
| 130 | `  &lt;!-- ========== 左侧控制面板 ========== --&gt;` | HTML注释，用于分区或说明。 |
| 131 | `  &lt;div class=&quot;sidebar&quot;&gt;` | 容器节点，用于布局与分区。 |
| 132 | `` | 空行，用于提升可读性。 |
| 133 | `    &lt;!-- 1. 数据库选择 --&gt;` | HTML注释，用于分区或说明。 |
| 134 | `    &lt;div class=&quot;panel-section&quot;&gt;` | 容器节点，用于布局与分区。 |
| 135 | `      &lt;div class=&quot;panel-title&quot;&gt;1. 选择数据库&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 136 | `      &lt;div class=&quot;ctrl-group&quot;&gt;` | 容器节点，用于布局与分区。 |
| 137 | `        &lt;select id=&quot;dbSelect&quot; onchange=&quot;onDbChange()&quot;&gt;` | 下拉框控件，用于参数选择。 |
| 138 | `          &lt;option value=&quot;&quot;&gt;-- 选择数据库 --&lt;/option&gt;` | 下拉项。 |
| 139 | `        &lt;/select&gt;` | 页面结构或文本内容。 |
| 140 | `      &lt;/div&gt;` | 容器节点结束。 |
| 141 | `    &lt;/div&gt;` | 容器节点结束。 |
| 142 | `` | 空行，用于提升可读性。 |
| 143 | `    &lt;hr class=&quot;divider&quot;&gt;` | 分隔线元素。 |
| 144 | `` | 空行，用于提升可读性。 |
| 145 | `    &lt;!-- 2. 数据表选择 --&gt;` | HTML注释，用于分区或说明。 |
| 146 | `    &lt;div class=&quot;panel-section&quot;&gt;` | 容器节点，用于布局与分区。 |
| 147 | `      &lt;div class=&quot;panel-title&quot;&gt;2. 选择数据表&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 148 | `      &lt;div class=&quot;ctrl-group&quot;&gt;` | 容器节点，用于布局与分区。 |
| 149 | `        &lt;select id=&quot;tableSelect&quot; multiple size=&quot;8&quot; onchange=&quot;onTableChange()&quot; disabled&gt;` | 下拉框控件，用于参数选择。 |
| 150 | `          &lt;option value=&quot;&quot;&gt;-- 先选择数据库 --&lt;/option&gt;` | 下拉项。 |
| 151 | `        &lt;/select&gt;` | 页面结构或文本内容。 |
| 152 | `      &lt;/div&gt;` | 容器节点结束。 |
| 153 | `      &lt;div id=&quot;tableInfo&quot; style=&quot;font-size: 11px; color: #666; margin-top: 4px;&quot;&gt;&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 154 | `      &lt;div style=&quot;margin-top:8px;&quot;&gt;` | 容器节点，用于布局与分区。 |
| 155 | `        &lt;div style=&quot;font-size:11px;color:#888;margin-bottom:4px;&quot;&gt;已选表：&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 156 | `        &lt;div id=&quot;selectedTables&quot; class=&quot;filter-tags&quot;&gt;&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 157 | `      &lt;/div&gt;` | 容器节点结束。 |
| 158 | `    &lt;/div&gt;` | 容器节点结束。 |
| 159 | `` | 空行，用于提升可读性。 |
| 160 | `    &lt;hr class=&quot;divider&quot;&gt;` | 分隔线元素。 |
| 161 | `` | 空行，用于提升可读性。 |
| 162 | `    &lt;!-- 3. 字段选择 --&gt;` | HTML注释，用于分区或说明。 |
| 163 | `    &lt;div class=&quot;panel-section&quot;&gt;` | 容器节点，用于布局与分区。 |
| 164 | `      &lt;div class=&quot;panel-title&quot;&gt;3. 选择字段&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 165 | `      &lt;div class=&quot;ctrl-group&quot;&gt;` | 容器节点，用于布局与分区。 |
| 166 | `        &lt;input type=&quot;text&quot; id=&quot;yFieldSearch&quot; placeholder=&quot;搜索字段...&quot; oninput=&quot;filterYFields()&quot; style=&quot;margin-bottom:6px;&quot;&gt;` | 输入控件（文本/日期等）。 |
| 167 | `      &lt;/div&gt;` | 容器节点结束。 |
| 168 | `      &lt;div style=&quot;margin-bottom:6px;&quot;&gt;` | 容器节点，用于布局与分区。 |
| 169 | `        &lt;button class=&quot;btn-secondary&quot; onclick=&quot;selectAllFields()&quot; style=&quot;padding:4px 10px;font-size:11px;&quot;&gt;全选&lt;/button&gt;` | 按钮控件，触发交互事件。 |
| 170 | `        &lt;button class=&quot;btn-secondary&quot; onclick=&quot;clearAllFields()&quot; style=&quot;padding:4px 10px;font-size:11px;&quot;&gt;清空&lt;/button&gt;` | 按钮控件，触发交互事件。 |
| 171 | `      &lt;/div&gt;` | 容器节点结束。 |
| 172 | `      &lt;div class=&quot;checkbox-group&quot; id=&quot;yFieldGroup&quot; style=&quot;max-height:200px;&quot;&gt;` | 容器节点，用于布局与分区。 |
| 173 | `        &lt;!-- 动态填充 --&gt;` | HTML注释，用于分区或说明。 |
| 174 | `      &lt;/div&gt;` | 容器节点结束。 |
| 175 | `      &lt;div style=&quot;margin-top:8px;&quot;&gt;` | 容器节点，用于布局与分区。 |
| 176 | `        &lt;div style=&quot;font-size:11px;color:#888;margin-bottom:4px;&quot;&gt;已选字段：&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 177 | `        &lt;div id=&quot;selectedFields&quot; class=&quot;filter-tags&quot;&gt;&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 178 | `      &lt;/div&gt;` | 容器节点结束。 |
| 179 | `    &lt;/div&gt;` | 容器节点结束。 |
| 180 | `` | 空行，用于提升可读性。 |
| 181 | `    &lt;hr class=&quot;divider&quot;&gt;` | 分隔线元素。 |
| 182 | `` | 空行，用于提升可读性。 |
| 183 | `    &lt;!-- 4. 日期范围 --&gt;` | HTML注释，用于分区或说明。 |
| 184 | `    &lt;div class=&quot;panel-section&quot;&gt;` | 容器节点，用于布局与分区。 |
| 185 | `      &lt;div class=&quot;panel-title&quot;&gt;4. 日期范围&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 186 | `      &lt;div class=&quot;ctrl-group&quot;&gt;` | 容器节点，用于布局与分区。 |
| 187 | `        &lt;input type=&quot;date&quot; id=&quot;dateFrom&quot; style=&quot;width:100%;margin-bottom:4px;&quot;&gt;` | 输入控件（文本/日期等）。 |
| 188 | `        &lt;span style=&quot;font-size:11px;color:#888;&quot;&gt;至&lt;/span&gt;` | 页面结构或文本内容。 |
| 189 | `        &lt;input type=&quot;date&quot; id=&quot;dateTo&quot; style=&quot;width:100%;margin-top:4px;&quot;&gt;` | 输入控件（文本/日期等）。 |
| 190 | `      &lt;/div&gt;` | 容器节点结束。 |
| 191 | `    &lt;/div&gt;` | 容器节点结束。 |
| 192 | `` | 空行，用于提升可读性。 |
| 193 | `    &lt;hr class=&quot;divider&quot;&gt;` | 分隔线元素。 |
| 194 | `` | 空行，用于提升可读性。 |
| 195 | `    &lt;!-- 5. 图表类型 --&gt;` | HTML注释，用于分区或说明。 |
| 196 | `    &lt;div class=&quot;panel-section&quot;&gt;` | 容器节点，用于布局与分区。 |
| 197 | `      &lt;div class=&quot;panel-title&quot;&gt;5. 图表类型&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 198 | `      &lt;div class=&quot;chart-types&quot;&gt;` | 容器节点，用于布局与分区。 |
| 199 | `        &lt;div class=&quot;chart-type-btn active&quot; onclick=&quot;setChartType(&#x27;line&#x27;, this)&quot;&gt;折线图&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 200 | `        &lt;div class=&quot;chart-type-btn&quot; onclick=&quot;setChartType(&#x27;bar&#x27;, this)&quot;&gt;柱状图&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 201 | `        &lt;div class=&quot;chart-type-btn&quot; onclick=&quot;setChartType(&#x27;pie&#x27;, this)&quot;&gt;饼图&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 202 | `        &lt;div class=&quot;chart-type-btn&quot; onclick=&quot;setChartType(&#x27;heatmap&#x27;, this)&quot;&gt;热力图&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 203 | `        &lt;div class=&quot;chart-type-btn&quot; onclick=&quot;setChartType(&#x27;scatter&#x27;, this)&quot;&gt;散点图&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 204 | `        &lt;div class=&quot;chart-type-btn&quot; onclick=&quot;setChartType(&#x27;radar&#x27;, this)&quot;&gt;雷达图&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 205 | `      &lt;/div&gt;` | 容器节点结束。 |
| 206 | `    &lt;/div&gt;` | 容器节点结束。 |
| 207 | `` | 空行，用于提升可读性。 |
| 208 | `    &lt;hr class=&quot;divider&quot;&gt;` | 分隔线元素。 |
| 209 | `` | 空行，用于提升可读性。 |
| 210 | `    &lt;!-- 6. 查询按钮 --&gt;` | HTML注释，用于分区或说明。 |
| 211 | `    &lt;div class=&quot;panel-section&quot;&gt;` | 容器节点，用于布局与分区。 |
| 212 | `      &lt;button class=&quot;btn&quot; onclick=&quot;renderChart()&quot; style=&quot;width:100%;margin-bottom:8px;&quot;&gt;生成图表&lt;/button&gt;` | 按钮控件，触发交互事件。 |
| 213 | `      &lt;button class=&quot;btn-secondary&quot; onclick=&quot;showTable()&quot; style=&quot;width:100%;&quot;&gt;查看数据&lt;/button&gt;` | 按钮控件，触发交互事件。 |
| 214 | `    &lt;/div&gt;` | 容器节点结束。 |
| 215 | `` | 空行，用于提升可读性。 |
| 216 | `    &lt;div id=&quot;errorBox&quot;&gt;&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 217 | `  &lt;/div&gt;` | 容器节点结束。 |
| 218 | `  ` | 空行，用于提升可读性。 |
| 219 | `  &lt;!-- ========== 右侧内容区 ========== --&gt;` | HTML注释，用于分区或说明。 |
| 220 | `  &lt;div class=&quot;content&quot;&gt;` | 容器节点，用于布局与分区。 |
| 221 | `    &lt;div class=&quot;stat-cards&quot; id=&quot;statCards&quot; style=&quot;display:none;&quot;&gt;&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 222 | `` | 空行，用于提升可读性。 |
| 223 | `    &lt;!-- 数据表格 --&gt;` | HTML注释，用于分区或说明。 |
| 224 | `    &lt;div class=&quot;chart-container&quot; id=&quot;tableContainer&quot; style=&quot;display:none;&quot;&gt;` | 容器节点，用于布局与分区。 |
| 225 | `      &lt;div class=&quot;chart-header&quot;&gt;` | 容器节点，用于布局与分区。 |
| 226 | `        &lt;div class=&quot;chart-title&quot;&gt;数据明细&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 227 | `        &lt;button class=&quot;btn-secondary&quot; style=&quot;padding:5px 12px; font-size:11px;&quot; onclick=&quot;exportCSV()&quot;&gt;导出 CSV&lt;/button&gt;` | 按钮控件，触发交互事件。 |
| 228 | `      &lt;/div&gt;` | 容器节点结束。 |
| 229 | `      &lt;div style=&quot;max-height: 500px; overflow: auto;&quot;&gt;` | 容器节点，用于布局与分区。 |
| 230 | `        &lt;table class=&quot;data-table&quot; id=&quot;dataTable&quot;&gt;` | 表格结构节点，用于数据展示。 |
| 231 | `          &lt;thead id=&quot;tableHead&quot;&gt;&lt;/thead&gt;` | 表格结构节点，用于数据展示。 |
| 232 | `          &lt;tbody id=&quot;tableBody&quot;&gt;&lt;/tbody&gt;` | 表格结构节点，用于数据展示。 |
| 233 | `        &lt;/table&gt;` | 页面结构或文本内容。 |
| 234 | `      &lt;/div&gt;` | 容器节点结束。 |
| 235 | `    &lt;/div&gt;` | 容器节点结束。 |
| 236 | `` | 空行，用于提升可读性。 |
| 237 | `    &lt;!-- 图表区域 --&gt;` | HTML注释，用于分区或说明。 |
| 238 | `    &lt;div class=&quot;chart-container&quot; id=&quot;chartContainer&quot; style=&quot;display:none;&quot;&gt;` | 容器节点，用于布局与分区。 |
| 239 | `      &lt;div class=&quot;chart-header&quot;&gt;` | 容器节点，用于布局与分区。 |
| 240 | `        &lt;div class=&quot;chart-title&quot; id=&quot;chartTitle&quot;&gt;图表&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 241 | `        &lt;div class=&quot;chart-meta&quot; id=&quot;chartMeta&quot;&gt;&lt;/div&gt;` | 容器节点，用于布局与分区。 |
| 242 | `      &lt;/div&gt;` | 容器节点结束。 |
| 243 | `      &lt;canvas id=&quot;mainChart&quot;&gt;&lt;/canvas&gt;` | 图表绘制画布（Chart.js挂载点）。 |
| 244 | `    &lt;/div&gt;` | 容器节点结束。 |
| 245 | `` | 空行，用于提升可读性。 |
| 246 | `    &lt;div class=&quot;no-data&quot; id=&quot;noData&quot;&gt;` | 容器节点，用于布局与分区。 |
| 247 | `      ← 请从左侧选择数据表和字段，然后点击「生成图表」` | 页面结构或文本内容。 |
| 248 | `    &lt;/div&gt;` | 容器节点结束。 |
| 249 | `  &lt;/div&gt;` | 容器节点结束。 |
| 250 | `&lt;/div&gt;` | 容器节点结束。 |
| 251 | `` | 空行，用于提升可读性。 |
| 252 | `&lt;script src=&quot;https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js&quot;&gt;&lt;/script&gt;` | 脚本资源或脚本块开始。 |
| 253 | `&lt;script&gt;` | 脚本资源或脚本块开始。 |
| 254 | `const DB_PATH = &#x27;/Users/yy/.hermes/workspace/db/analysis.db&#x27;;` | 定义变量或常量，保存页面状态。 |
| 255 | `let meta = {};` | 定义变量或常量，保存页面状态。 |
| 256 | `let dbList = {};` | 定义变量或常量，保存页面状态。 |
| 257 | `let currentChart = null;` | 定义变量或常量，保存页面状态。 |
| 258 | `let chartType = &#x27;line&#x27;;` | 定义变量或常量，保存页面状态。 |
| 259 | `let currentData = [];` | 定义变量或常量，保存页面状态。 |
| 260 | `let currentTable = &#x27;&#x27;;` | 定义变量或常量，保存页面状态。 |
| 261 | `let currentDb = &#x27;&#x27;;` | 定义变量或常量，保存页面状态。 |
| 262 | `let activeFilters = {};` | 定义变量或常量，保存页面状态。 |
| 263 | `let tableColumns = [];` | 定义变量或常量，保存页面状态。 |
| 264 | `let yFieldsOptions = [];` | 定义变量或常量，保存页面状态。 |
| 265 | `let selectedTables = [];` | 定义变量或常量，保存页面状态。 |
| 266 | `let selectedFields = [];` | 定义变量或常量，保存页面状态。 |
| 267 | `` | 空行，用于提升可读性。 |
| 268 | `// ============================================================` | JavaScript注释，用于分区和说明。 |
| 269 | `// 初始化` | JavaScript注释，用于分区和说明。 |
| 270 | `// ============================================================` | JavaScript注释，用于分区和说明。 |
| 271 | `document.addEventListener(&#x27;DOMContentLoaded&#x27;, async () =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 272 | `  const resp = await fetch(&#x27;/api/databases&#x27;);` | 定义变量或常量，保存页面状态。 |
| 273 | `  dbList = await resp.json();` | JavaScript业务逻辑或DOM操作。 |
| 274 | `` | 空行，用于提升可读性。 |
| 275 | `  const dbSel = document.getElementById(&#x27;dbSelect&#x27;);` | 定义变量或常量，保存页面状态。 |
| 276 | `  Object.entries(dbList).forEach(([key, info]) =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 277 | `    const opt = document.createElement(&#x27;option&#x27;);` | 定义变量或常量，保存页面状态。 |
| 278 | `    opt.value = key;` | JavaScript业务逻辑或DOM操作。 |
| 279 | `    opt.textContent = info.name;` | JavaScript业务逻辑或DOM操作。 |
| 280 | `    dbSel.appendChild(opt);` | JavaScript业务逻辑或DOM操作。 |
| 281 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 282 | `});` | JavaScript业务逻辑或DOM操作。 |
| 283 | `` | 空行，用于提升可读性。 |
| 284 | `async function onDbChange() {` | 定义异步函数，用于请求后端数据。 |
| 285 | `  const dbKey = document.getElementById(&#x27;dbSelect&#x27;).value;` | 定义变量或常量，保存页面状态。 |
| 286 | `  currentDb = dbKey;` | JavaScript业务逻辑或DOM操作。 |
| 287 | `  const tableSel = document.getElementById(&#x27;tableSelect&#x27;);` | 定义变量或常量，保存页面状态。 |
| 288 | `  tableSel.innerHTML = &#x27;&lt;option value=&quot;&quot;&gt;-- 加载中 --&lt;/option&gt;&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 289 | `  tableSel.disabled = !dbKey;` | JavaScript业务逻辑或DOM操作。 |
| 290 | `` | 空行，用于提升可读性。 |
| 291 | `  if (!dbKey) {` | 条件分支，控制逻辑流程。 |
| 292 | `    tableSel.innerHTML = &#x27;&lt;option value=&quot;&quot;&gt;-- 先选择数据库 --&lt;/option&gt;&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 293 | `    return;` | JavaScript业务逻辑或DOM操作。 |
| 294 | `  }` | JavaScript业务逻辑或DOM操作。 |
| 295 | `` | 空行，用于提升可读性。 |
| 296 | `  const resp = await fetch(`/api/tables?db=${dbKey}`);` | 定义变量或常量，保存页面状态。 |
| 297 | `  meta = await resp.json();` | JavaScript业务逻辑或DOM操作。 |
| 298 | `` | 空行，用于提升可读性。 |
| 299 | `  tableSel.innerHTML = &#x27;&lt;option value=&quot;&quot;&gt;-- 选择数据表 --&lt;/option&gt;&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 300 | `  const tables = Object.keys(meta);` | 定义变量或常量，保存页面状态。 |
| 301 | `  tables.forEach(t =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 302 | `    const opt = document.createElement(&#x27;option&#x27;);` | 定义变量或常量，保存页面状态。 |
| 303 | `    opt.value = t;` | JavaScript业务逻辑或DOM操作。 |
| 304 | `    opt.textContent = t;` | JavaScript业务逻辑或DOM操作。 |
| 305 | `    tableSel.appendChild(opt);` | JavaScript业务逻辑或DOM操作。 |
| 306 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 307 | `` | 空行，用于提升可读性。 |
| 308 | `  if (tables.length &gt; 0) {` | 条件分支，控制逻辑流程。 |
| 309 | `    const defaultTable = tables.find(t =&gt; t.includes(&#x27;k12_token&#x27;)) \|\| tables[0];` | 定义变量或常量，保存页面状态。 |
| 310 | `    currentTable = defaultTable;` | JavaScript业务逻辑或DOM操作。 |
| 311 | `    tableSel.value = defaultTable;` | JavaScript业务逻辑或DOM操作。 |
| 312 | `    await onTableChange();` | JavaScript业务逻辑或DOM操作。 |
| 313 | `  }` | JavaScript业务逻辑或DOM操作。 |
| 314 | `}` | JavaScript业务逻辑或DOM操作。 |
| 315 | `` | 空行，用于提升可读性。 |
| 316 | `// ============================================================` | JavaScript注释，用于分区和说明。 |
| 317 | `// 事件处理` | JavaScript注释，用于分区和说明。 |
| 318 | `// ============================================================` | JavaScript注释，用于分区和说明。 |
| 319 | `` | 空行，用于提升可读性。 |
| 320 | `async function onTableChange() {` | 定义异步函数，用于请求后端数据。 |
| 321 | `  const tableSel = document.getElementById(&#x27;tableSelect&#x27;);` | 定义变量或常量，保存页面状态。 |
| 322 | `  selectedTables = Array.from(tableSel.selectedOptions).map(o =&gt; o.value).filter(v =&gt; v);` | JavaScript业务逻辑或DOM操作。 |
| 323 | `  currentTable = selectedTables[0] \|\| &#x27;&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 324 | `` | 空行，用于提升可读性。 |
| 325 | `  renderSelectedTables();` | JavaScript业务逻辑或DOM操作。 |
| 326 | `` | 空行，用于提升可读性。 |
| 327 | `  if (selectedTables.length === 0) {` | 条件分支，控制逻辑流程。 |
| 328 | `    yFieldsOptions = [];` | JavaScript业务逻辑或DOM操作。 |
| 329 | `    selectedFields = [];` | JavaScript业务逻辑或DOM操作。 |
| 330 | `    renderSelectedFields();` | JavaScript业务逻辑或DOM操作。 |
| 331 | `    return;` | JavaScript业务逻辑或DOM操作。 |
| 332 | `  }` | JavaScript业务逻辑或DOM操作。 |
| 333 | `` | 空行，用于提升可读性。 |
| 334 | `  // 收集所有选中表的字段` | JavaScript注释，用于分区和说明。 |
| 335 | `  const allColumns = new Map();` | 定义变量或常量，保存页面状态。 |
| 336 | `  let dateInfo = [];` | 定义变量或常量，保存页面状态。 |
| 337 | `  let totalRows = 0;` | 定义变量或常量，保存页面状态。 |
| 338 | `` | 空行，用于提升可读性。 |
| 339 | `  selectedTables.forEach(t =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 340 | `    if (meta[t]) {` | 条件分支，控制逻辑流程。 |
| 341 | `      const info = meta[t];` | 定义变量或常量，保存页面状态。 |
| 342 | `      totalRows += info.row_count \|\| 0;` | JavaScript业务逻辑或DOM操作。 |
| 343 | `      if (info.date_range) dateInfo = info.date_range;` | 条件分支，控制逻辑流程。 |
| 344 | `      info.columns.forEach(c =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 345 | `        if (!allColumns.has(c.name)) {` | 条件分支，控制逻辑流程。 |
| 346 | `          allColumns.set(c.name, c);` | JavaScript业务逻辑或DOM操作。 |
| 347 | `        }` | JavaScript业务逻辑或DOM操作。 |
| 348 | `      });` | JavaScript业务逻辑或DOM操作。 |
| 349 | `    }` | JavaScript业务逻辑或DOM操作。 |
| 350 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 351 | `` | 空行，用于提升可读性。 |
| 352 | `  document.getElementById(&#x27;tableInfo&#x27;).textContent =` | JavaScript业务逻辑或DOM操作。 |
| 353 | `    `已选 ${selectedTables.length} 表 \| 共 ${totalRows.toLocaleString()} 条`;` | JavaScript业务逻辑或DOM操作。 |
| 354 | `` | 空行，用于提升可读性。 |
| 355 | `  // 填充字段复选框` | JavaScript注释，用于分区和说明。 |
| 356 | `  const yGroup = document.getElementById(&#x27;yFieldGroup&#x27;);` | 定义变量或常量，保存页面状态。 |
| 357 | `  yGroup.innerHTML = &#x27;&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 358 | `  const excludeNames = [&#x27;id&#x27;, &#x27;created_at&#x27;, &#x27;date&#x27;, &#x27;日期&#x27;];` | 定义变量或常量，保存页面状态。 |
| 359 | `  yFieldsOptions = [];` | JavaScript业务逻辑或DOM操作。 |
| 360 | `  const defaultFields = [&#x27;alpha&#x27;, &#x27;pnl&#x27;, &#x27;theo&#x27;, &#x27;bundle&#x27;, &#x27;gas&#x27;, &#x27;order_count&#x27;, &#x27;theoretical_profit&#x27;, &#x27;实际利润&#x27;, &#x27;bundle_fee&#x27;, &#x27;gas_fee&#x27;, &#x27;bnb_pnl&#x27;, &#x27;spread_range&#x27;, &#x27;size_range&#x27;, &#x27;token&#x27;];` | 定义变量或常量，保存页面状态。 |
| 361 | `` | 空行，用于提升可读性。 |
| 362 | `  const fieldTableMap = {};` | 定义变量或常量，保存页面状态。 |
| 363 | `  if (selectedTables.length &gt; 1) {` | 条件分支，控制逻辑流程。 |
| 364 | `    selectedTables.forEach(t =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 365 | `      if (meta[t]?.columns) {` | 条件分支，控制逻辑流程。 |
| 366 | `        meta[t].columns.forEach(c =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 367 | `          if (excludeNames.includes(c.name)) return;` | 条件分支，控制逻辑流程。 |
| 368 | `          const fullName = `${c.name}_${t.replace(&#x27;汇总&#x27;, &#x27;&#x27;).replace(&#x27;大币&#x27;, &#x27;&#x27;)}`;` | 定义变量或常量，保存页面状态。 |
| 369 | `          if (!fieldTableMap[c.name]) fieldTableMap[c.name] = [];` | 条件分支，控制逻辑流程。 |
| 370 | `          fieldTableMap[c.name].push({ fullName, table: t, col: c });` | JavaScript业务逻辑或DOM操作。 |
| 371 | `        });` | JavaScript业务逻辑或DOM操作。 |
| 372 | `      }` | JavaScript业务逻辑或DOM操作。 |
| 373 | `    });` | JavaScript业务逻辑或DOM操作。 |
| 374 | `    Object.keys(fieldTableMap).forEach(baseName =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 375 | `      const entries = fieldTableMap[baseName];` | 定义变量或常量，保存页面状态。 |
| 376 | `      entries.forEach(entry =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 377 | `        const div = document.createElement(&#x27;div&#x27;);` | 定义变量或常量，保存页面状态。 |
| 378 | `        div.className = &#x27;checkbox-item&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 379 | `        const isSelected = selectedFields.includes(entry.fullName);` | 定义变量或常量，保存页面状态。 |
| 380 | `        const checked = isSelected ? &#x27;checked&#x27; : &#x27;&#x27;;` | 定义变量或常量，保存页面状态。 |
| 381 | `        div.innerHTML = `&lt;input type=&quot;checkbox&quot; id=&quot;yf_${entry.fullName}&quot; value=&quot;${entry.fullName}&quot; ${checked} onclick=&quot;onYFieldChange()&quot;&gt;` | JavaScript业务逻辑或DOM操作。 |
| 382 | `                         &lt;label for=&quot;yf_${entry.fullName}&quot;&gt;${entry.fullName}&lt;/label&gt;`;` | JavaScript业务逻辑或DOM操作。 |
| 383 | `        yGroup.appendChild(div);` | JavaScript业务逻辑或DOM操作。 |
| 384 | `      });` | JavaScript业务逻辑或DOM操作。 |
| 385 | `    });` | JavaScript业务逻辑或DOM操作。 |
| 386 | `  } else {` | JavaScript业务逻辑或DOM操作。 |
| 387 | `    Array.from(allColumns.values()).forEach(c =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 388 | `      if (excludeNames.includes(c.name)) return;` | 条件分支，控制逻辑流程。 |
| 389 | `      yFieldsOptions.push(c);` | JavaScript业务逻辑或DOM操作。 |
| 390 | `      const div = document.createElement(&#x27;div&#x27;);` | 定义变量或常量，保存页面状态。 |
| 391 | `      div.className = &#x27;checkbox-item&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 392 | `      const isInDefault = defaultFields.some(f =&gt; c.name.includes(f) \|\| f.includes(c.name));` | 定义变量或常量，保存页面状态。 |
| 393 | `      const isSelected = selectedFields.includes(c.name);` | 定义变量或常量，保存页面状态。 |
| 394 | `      const checked = (isInDefault \|\| isSelected) ? &#x27;checked&#x27; : &#x27;&#x27;;` | 定义变量或常量，保存页面状态。 |
| 395 | `      div.innerHTML = `&lt;input type=&quot;checkbox&quot; id=&quot;yf_${c.name}&quot; value=&quot;${c.name}&quot; ${checked} onclick=&quot;onYFieldChange()&quot;&gt;` | JavaScript业务逻辑或DOM操作。 |
| 396 | `                       &lt;label for=&quot;yf_${c.name}&quot;&gt;${c.name}&lt;/label&gt;`;` | JavaScript业务逻辑或DOM操作。 |
| 397 | `      yGroup.appendChild(div);` | JavaScript业务逻辑或DOM操作。 |
| 398 | `    });` | JavaScript业务逻辑或DOM操作。 |
| 399 | `  }` | JavaScript业务逻辑或DOM操作。 |
| 400 | `` | 空行，用于提升可读性。 |
| 401 | `  // 设置日期范围` | JavaScript注释，用于分区和说明。 |
| 402 | `  if (dateInfo[0]) document.getElementById(&#x27;dateFrom&#x27;).value = dateInfo[0];` | 条件分支，控制逻辑流程。 |
| 403 | `  if (dateInfo[1]) document.getElementById(&#x27;dateTo&#x27;).value = dateInfo[1];` | 条件分支，控制逻辑流程。 |
| 404 | `` | 空行，用于提升可读性。 |
| 405 | `  onYFieldChange();` | JavaScript业务逻辑或DOM操作。 |
| 406 | `}` | JavaScript业务逻辑或DOM操作。 |
| 407 | `` | 空行，用于提升可读性。 |
| 408 | `function renderSelectedTables() {` | 定义函数，封装交互或渲染逻辑。 |
| 409 | `  const container = document.getElementById(&#x27;selectedTables&#x27;);` | 定义变量或常量，保存页面状态。 |
| 410 | `  container.innerHTML = &#x27;&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 411 | `  selectedTables.forEach(t =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 412 | `    const tag = document.createElement(&#x27;div&#x27;);` | 定义变量或常量，保存页面状态。 |
| 413 | `    tag.className = &#x27;filter-tag&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 414 | `    tag.innerHTML = `&lt;span&gt;${t}&lt;/span&gt; &lt;button onclick=&quot;removeTable(&#x27;${t}&#x27;)&quot;&gt;×&lt;/button&gt;`;` | JavaScript业务逻辑或DOM操作。 |
| 415 | `    container.appendChild(tag);` | JavaScript业务逻辑或DOM操作。 |
| 416 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 417 | `}` | JavaScript业务逻辑或DOM操作。 |
| 418 | `` | 空行，用于提升可读性。 |
| 419 | `function removeTable(t) {` | 定义函数，封装交互或渲染逻辑。 |
| 420 | `  selectedTables = selectedTables.filter(x =&gt; x !== t);` | JavaScript业务逻辑或DOM操作。 |
| 421 | `  const tableSel = document.getElementById(&#x27;tableSelect&#x27;);` | 定义变量或常量，保存页面状态。 |
| 422 | `  Array.from(tableSel.options).forEach(o =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 423 | `    if (o.value === t) o.selected = false;` | 条件分支，控制逻辑流程。 |
| 424 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 425 | `  renderSelectedTables();` | JavaScript业务逻辑或DOM操作。 |
| 426 | `  onTableChange();` | JavaScript业务逻辑或DOM操作。 |
| 427 | `}` | JavaScript业务逻辑或DOM操作。 |
| 428 | `` | 空行，用于提升可读性。 |
| 429 | `function renderSelectedFields() {` | 定义函数，封装交互或渲染逻辑。 |
| 430 | `  const container = document.getElementById(&#x27;selectedFields&#x27;);` | 定义变量或常量，保存页面状态。 |
| 431 | `  container.innerHTML = &#x27;&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 432 | `  selectedFields.forEach(f =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 433 | `    const tag = document.createElement(&#x27;div&#x27;);` | 定义变量或常量，保存页面状态。 |
| 434 | `    tag.className = &#x27;filter-tag&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 435 | `    tag.innerHTML = `&lt;span&gt;${f}&lt;/span&gt; &lt;button onclick=&quot;removeField(&#x27;${f}&#x27;)&quot;&gt;×&lt;/button&gt;`;` | JavaScript业务逻辑或DOM操作。 |
| 436 | `    container.appendChild(tag);` | JavaScript业务逻辑或DOM操作。 |
| 437 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 438 | `}` | JavaScript业务逻辑或DOM操作。 |
| 439 | `` | 空行，用于提升可读性。 |
| 440 | `function removeField(f) {` | 定义函数，封装交互或渲染逻辑。 |
| 441 | `  selectedFields = selectedFields.filter(x =&gt; x !== f);` | JavaScript业务逻辑或DOM操作。 |
| 442 | `  const cb = document.getElementById(&#x27;yf_&#x27; + f);` | 定义变量或常量，保存页面状态。 |
| 443 | `  if (cb) cb.checked = false;` | 条件分支，控制逻辑流程。 |
| 444 | `  renderSelectedFields();` | JavaScript业务逻辑或DOM操作。 |
| 445 | `}` | JavaScript业务逻辑或DOM操作。 |
| 446 | `` | 空行，用于提升可读性。 |
| 447 | `function selectAllFields() {` | 定义函数，封装交互或渲染逻辑。 |
| 448 | `  yFieldsOptions.forEach(c =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 449 | `    if (!selectedFields.includes(c.name)) {` | 条件分支，控制逻辑流程。 |
| 450 | `      selectedFields.push(c.name);` | JavaScript业务逻辑或DOM操作。 |
| 451 | `    }` | JavaScript业务逻辑或DOM操作。 |
| 452 | `    const cb = document.getElementById(&#x27;yf_&#x27; + c.name);` | 定义变量或常量，保存页面状态。 |
| 453 | `    if (cb) cb.checked = true;` | 条件分支，控制逻辑流程。 |
| 454 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 455 | `  renderSelectedFields();` | JavaScript业务逻辑或DOM操作。 |
| 456 | `}` | JavaScript业务逻辑或DOM操作。 |
| 457 | `` | 空行，用于提升可读性。 |
| 458 | `function clearAllFields() {` | 定义函数，封装交互或渲染逻辑。 |
| 459 | `  selectedFields = [];` | JavaScript业务逻辑或DOM操作。 |
| 460 | `  document.querySelectorAll(&#x27;#yFieldGroup input&#x27;).forEach(cb =&gt; cb.checked = false);` | JavaScript业务逻辑或DOM操作。 |
| 461 | `  renderSelectedFields();` | JavaScript业务逻辑或DOM操作。 |
| 462 | `}` | JavaScript业务逻辑或DOM操作。 |
| 463 | `` | 空行，用于提升可读性。 |
| 464 | `function filterYFields() {` | 定义函数，封装交互或渲染逻辑。 |
| 465 | `  const search = document.getElementById(&#x27;yFieldSearch&#x27;).value.toLowerCase();` | 定义变量或常量，保存页面状态。 |
| 466 | `  const yGroup = document.getElementById(&#x27;yFieldGroup&#x27;);` | 定义变量或常量，保存页面状态。 |
| 467 | `  yGroup.innerHTML = &#x27;&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 468 | `  const excludeNames = [&#x27;id&#x27;, &#x27;created_at&#x27;, &#x27;date&#x27;, &#x27;日期&#x27;];` | 定义变量或常量，保存页面状态。 |
| 469 | `` | 空行，用于提升可读性。 |
| 470 | `  if (selectedTables.length &gt; 1) {` | 条件分支，控制逻辑流程。 |
| 471 | `    selectedTables.forEach(t =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 472 | `      if (meta[t]?.columns) {` | 条件分支，控制逻辑流程。 |
| 473 | `        meta[t].columns.forEach(c =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 474 | `          if (excludeNames.includes(c.name)) return;` | 条件分支，控制逻辑流程。 |
| 475 | `          const fullName = `${c.name}_${t.replace(&#x27;汇总&#x27;, &#x27;&#x27;).replace(&#x27;大币&#x27;, &#x27;&#x27;)}`;` | 定义变量或常量，保存页面状态。 |
| 476 | `          if (fullName.toLowerCase().includes(search) \|\| c.name.toLowerCase().includes(search)) {` | 条件分支，控制逻辑流程。 |
| 477 | `            const div = document.createElement(&#x27;div&#x27;);` | 定义变量或常量，保存页面状态。 |
| 478 | `            div.className = &#x27;checkbox-item&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 479 | `            const isSelected = selectedFields.includes(fullName);` | 定义变量或常量，保存页面状态。 |
| 480 | `            const checked = isSelected ? &#x27;checked&#x27; : &#x27;&#x27;;` | 定义变量或常量，保存页面状态。 |
| 481 | `            div.innerHTML = `&lt;input type=&quot;checkbox&quot; id=&quot;yf_${fullName}&quot; value=&quot;${fullName}&quot; ${checked} onclick=&quot;onYFieldChange()&quot;&gt;` | JavaScript业务逻辑或DOM操作。 |
| 482 | `                             &lt;label for=&quot;yf_${fullName}&quot;&gt;${fullName}&lt;/label&gt;`;` | JavaScript业务逻辑或DOM操作。 |
| 483 | `            yGroup.appendChild(div);` | JavaScript业务逻辑或DOM操作。 |
| 484 | `          }` | JavaScript业务逻辑或DOM操作。 |
| 485 | `        });` | JavaScript业务逻辑或DOM操作。 |
| 486 | `      }` | JavaScript业务逻辑或DOM操作。 |
| 487 | `    });` | JavaScript业务逻辑或DOM操作。 |
| 488 | `  } else {` | JavaScript业务逻辑或DOM操作。 |
| 489 | `    yFieldsOptions.forEach(c =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 490 | `      if (excludeNames.includes(c.name)) return;` | 条件分支，控制逻辑流程。 |
| 491 | `      if (c.name.toLowerCase().includes(search)) {` | 条件分支，控制逻辑流程。 |
| 492 | `        const div = document.createElement(&#x27;div&#x27;);` | 定义变量或常量，保存页面状态。 |
| 493 | `        div.className = &#x27;checkbox-item&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 494 | `        const isSelected = selectedFields.includes(c.name);` | 定义变量或常量，保存页面状态。 |
| 495 | `        const checked = isSelected ? &#x27;checked&#x27; : &#x27;&#x27;;` | 定义变量或常量，保存页面状态。 |
| 496 | `        div.innerHTML = `&lt;input type=&quot;checkbox&quot; id=&quot;yf_${c.name}&quot; value=&quot;${c.name}&quot; ${checked} onclick=&quot;onYFieldChange()&quot;&gt;` | JavaScript业务逻辑或DOM操作。 |
| 497 | `                         &lt;label for=&quot;yf_${c.name}&quot;&gt;${c.name}&lt;/label&gt;`;` | JavaScript业务逻辑或DOM操作。 |
| 498 | `        yGroup.appendChild(div);` | JavaScript业务逻辑或DOM操作。 |
| 499 | `      }` | JavaScript业务逻辑或DOM操作。 |
| 500 | `    });` | JavaScript业务逻辑或DOM操作。 |
| 501 | `  }` | JavaScript业务逻辑或DOM操作。 |
| 502 | `}` | JavaScript业务逻辑或DOM操作。 |
| 503 | `` | 空行，用于提升可读性。 |
| 504 | `function onYFieldChange() {` | 定义函数，封装交互或渲染逻辑。 |
| 505 | `  selectedFields = [];` | JavaScript业务逻辑或DOM操作。 |
| 506 | `  document.querySelectorAll(&#x27;#yFieldGroup input:checked&#x27;).forEach(cb =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 507 | `    if (!selectedFields.includes(cb.value)) {` | 条件分支，控制逻辑流程。 |
| 508 | `      selectedFields.push(cb.value);` | JavaScript业务逻辑或DOM操作。 |
| 509 | `    }` | JavaScript业务逻辑或DOM操作。 |
| 510 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 511 | `  renderSelectedFields();` | JavaScript业务逻辑或DOM操作。 |
| 512 | `}` | JavaScript业务逻辑或DOM操作。 |
| 513 | `` | 空行，用于提升可读性。 |
| 514 | `function setChartType(type, el) {` | 定义函数，封装交互或渲染逻辑。 |
| 515 | `  chartType = type;` | JavaScript业务逻辑或DOM操作。 |
| 516 | `  document.querySelectorAll(&#x27;.chart-type-btn&#x27;).forEach(b =&gt; b.classList.remove(&#x27;active&#x27;));` | JavaScript业务逻辑或DOM操作。 |
| 517 | `  el.classList.add(&#x27;active&#x27;);` | JavaScript业务逻辑或DOM操作。 |
| 518 | `  if (currentData.length &gt; 0) renderCurrentChart();` | 条件分支，控制逻辑流程。 |
| 519 | `}` | JavaScript业务逻辑或DOM操作。 |
| 520 | `` | 空行，用于提升可读性。 |
| 521 | `function setDateRange(range) {` | 定义函数，封装交互或渲染逻辑。 |
| 522 | `  const to = new Date();` | 定义变量或常量，保存页面状态。 |
| 523 | `  let from = new Date();` | 定义变量或常量，保存页面状态。 |
| 524 | `  if (range === &#x27;7d&#x27;) from.setDate(to.getDate() - 7);` | 条件分支，控制逻辑流程。 |
| 525 | `  else if (range === &#x27;30d&#x27;) from.setDate(to.getDate() - 30);` | JavaScript业务逻辑或DOM操作。 |
| 526 | `  else { document.getElementById(&#x27;dateFrom&#x27;).value = &#x27;&#x27;; document.getElementById(&#x27;dateTo&#x27;).value = &#x27;&#x27;; return; }` | JavaScript业务逻辑或DOM操作。 |
| 527 | `` | 空行，用于提升可读性。 |
| 528 | `  const fromStr = from.toISOString().split(&#x27;T&#x27;)[0];` | 定义变量或常量，保存页面状态。 |
| 529 | `  const toStr = to.toISOString().split(&#x27;T&#x27;)[0];` | 定义变量或常量，保存页面状态。 |
| 530 | `  document.getElementById(&#x27;dateFrom&#x27;).value = fromStr;` | JavaScript业务逻辑或DOM操作。 |
| 531 | `  document.getElementById(&#x27;dateTo&#x27;).value = toStr;` | JavaScript业务逻辑或DOM操作。 |
| 532 | `}` | JavaScript业务逻辑或DOM操作。 |
| 533 | `` | 空行，用于提升可读性。 |
| 534 | `function getSelectedYFields() {` | 定义函数，封装交互或渲染逻辑。 |
| 535 | `  const fields = [];` | 定义变量或常量，保存页面状态。 |
| 536 | `  document.querySelectorAll(&#x27;#yFieldGroup input:checked&#x27;).forEach(cb =&gt; fields.push(cb.value));` | JavaScript业务逻辑或DOM操作。 |
| 537 | `  return fields;` | 函数返回值。 |
| 538 | `}` | JavaScript业务逻辑或DOM操作。 |
| 539 | `` | 空行，用于提升可读性。 |
| 540 | `// ============================================================` | JavaScript注释，用于分区和说明。 |
| 541 | `// 数据查询 &amp; 渲染` | JavaScript注释，用于分区和说明。 |
| 542 | `// ============================================================` | JavaScript注释，用于分区和说明。 |
| 543 | `` | 空行，用于提升可读性。 |
| 544 | `async function renderChart() {` | 定义异步函数，用于请求后端数据。 |
| 545 | `  const table = currentTable;` | 定义变量或常量，保存页面状态。 |
| 546 | `  const xField = &#x27;date&#x27;;` | 定义变量或常量，保存页面状态。 |
| 547 | `  const yFields = getSelectedYFields();` | 定义变量或常量，保存页面状态。 |
| 548 | `  const dateFrom = document.getElementById(&#x27;dateFrom&#x27;).value;` | 定义变量或常量，保存页面状态。 |
| 549 | `  const dateTo = document.getElementById(&#x27;dateTo&#x27;).value;` | 定义变量或常量，保存页面状态。 |
| 550 | `` | 空行，用于提升可读性。 |
| 551 | `  console.log(&#x27;renderChart called:&#x27;, { table, selectedTables, currentDb, yFields, dateFrom, dateTo });` | JavaScript业务逻辑或DOM操作。 |
| 552 | `` | 空行，用于提升可读性。 |
| 553 | `  document.getElementById(&#x27;errorBox&#x27;).innerHTML = &#x27;&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 554 | `  document.getElementById(&#x27;noData&#x27;).style.display = &#x27;none&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 555 | `  document.getElementById(&#x27;chartContainer&#x27;).style.display = &#x27;none&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 556 | `` | 空行，用于提升可读性。 |
| 557 | `  if (!table) { showError(&#x27;请先选择数据表&#x27;); return; }` | 条件分支，控制逻辑流程。 |
| 558 | `  if (yFields.length === 0) { showError(&#x27;请至少选择一个字段&#x27;); return; }` | 条件分支，控制逻辑流程。 |
| 559 | `  if (!currentDb) { showError(&#x27;请先选择数据库&#x27;); return; }` | 条件分支，控制逻辑流程。 |
| 560 | `` | 空行，用于提升可读性。 |
| 561 | `  try {` | JavaScript业务逻辑或DOM操作。 |
| 562 | `    const resp = await fetch(&#x27;/api/query&#x27;, {` | 定义变量或常量，保存页面状态。 |
| 563 | `      method: &#x27;POST&#x27;,` | JavaScript业务逻辑或DOM操作。 |
| 564 | `      headers: {&#x27;Content-Type&#x27;: &#x27;application/json&#x27;},` | JavaScript业务逻辑或DOM操作。 |
| 565 | `      body: JSON.stringify({ table, tables: selectedTables, db: currentDb, x_field: xField, y_fields: yFields, date_from: dateFrom, date_to: dateTo, filters: activeFilters })` | JavaScript业务逻辑或DOM操作。 |
| 566 | `    });` | JavaScript业务逻辑或DOM操作。 |
| 567 | `    const result = await resp.json();` | 定义变量或常量，保存页面状态。 |
| 568 | `    console.log(&#x27;Query result:&#x27;, result);` | JavaScript业务逻辑或DOM操作。 |
| 569 | `    if (!result.success) { showError(result.error); return; }` | 条件分支，控制逻辑流程。 |
| 570 | `` | 空行，用于提升可读性。 |
| 571 | `    currentData = result.data;` | JavaScript业务逻辑或DOM操作。 |
| 572 | `    tableColumns = result.data.length &gt; 0 ? Object.keys(result.data[0]) : [xField, ...yFields];` | JavaScript业务逻辑或DOM操作。 |
| 573 | `` | 空行，用于提升可读性。 |
| 574 | `    updateStatCards(result.data, yFields);` | JavaScript业务逻辑或DOM操作。 |
| 575 | `    renderCurrentChart();` | JavaScript业务逻辑或DOM操作。 |
| 576 | `` | 空行，用于提升可读性。 |
| 577 | `    document.getElementById(&#x27;chartContainer&#x27;).style.display = &#x27;block&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 578 | `    document.getElementById(&#x27;chartTitle&#x27;).textContent = `${yFields.join(&#x27; + &#x27;)} by ${xField}`;` | JavaScript业务逻辑或DOM操作。 |
| 579 | `    document.getElementById(&#x27;chartMeta&#x27;).textContent = `${result.count} 条数据 \| 表: ${selectedTables.join(&#x27;, &#x27;)}`;` | JavaScript业务逻辑或DOM操作。 |
| 580 | `    document.getElementById(&#x27;errorBox&#x27;).innerHTML = &#x27;&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 581 | `` | 空行，用于提升可读性。 |
| 582 | `  } catch(e) { showError(e.message); console.error(&#x27;renderChart error:&#x27;, e); }` | JavaScript业务逻辑或DOM操作。 |
| 583 | `}` | JavaScript业务逻辑或DOM操作。 |
| 584 | `` | 空行，用于提升可读性。 |
| 585 | `function renderCurrentChart() {` | 定义函数，封装交互或渲染逻辑。 |
| 586 | `  if (currentData.length === 0) return;` | 条件分支，控制逻辑流程。 |
| 587 | `  if (currentChart) currentChart.destroy();` | 条件分支，控制逻辑流程。 |
| 588 | `` | 空行，用于提升可读性。 |
| 589 | `  const yFields = getSelectedYFields();` | 定义变量或常量，保存页面状态。 |
| 590 | `  const dateCols = [&#x27;date&#x27;, &#x27;日期&#x27;, &#x27;Date&#x27;, &#x27;DATE&#x27;];` | 定义变量或常量，保存页面状态。 |
| 591 | `  let xField = &#x27;date&#x27;;` | 定义变量或常量，保存页面状态。 |
| 592 | `  for (let col of tableColumns) {` | 循环处理数据集合。 |
| 593 | `    if (dateCols.includes(col)) {` | 条件分支，控制逻辑流程。 |
| 594 | `      xField = col;` | JavaScript业务逻辑或DOM操作。 |
| 595 | `      break;` | JavaScript业务逻辑或DOM操作。 |
| 596 | `    }` | JavaScript业务逻辑或DOM操作。 |
| 597 | `  }` | JavaScript业务逻辑或DOM操作。 |
| 598 | `` | 空行，用于提升可读性。 |
| 599 | `  const labels = currentData.map(r =&gt; String(r[xField]).substring(0, 10));` | 定义变量或常量，保存页面状态。 |
| 600 | `` | 空行，用于提升可读性。 |
| 601 | `  const dataCols = tableColumns.filter(c =&gt; c !== xField);` | 定义变量或常量，保存页面状态。 |
| 602 | `  // 天蓝色系图表配色` | JavaScript注释，用于分区和说明。 |
| 603 | `  const skyColors = [` | 定义变量或常量，保存页面状态。 |
| 604 | `    &#x27;#4FA8D7&#x27;, &#x27;#7EC4E8&#x27;, &#x27;#3A8AB8&#x27;, &#x27;#A8D4ED&#x27;,` | JavaScript业务逻辑或DOM操作。 |
| 605 | `    &#x27;#6AAED6&#x27;, &#x27;#2E7DAF&#x27;, &#x27;#9AC8E3&#x27;, &#x27;#1F6A9E&#x27;` | JavaScript业务逻辑或DOM操作。 |
| 606 | `  ];` | JavaScript业务逻辑或DOM操作。 |
| 607 | `  const datasets = dataCols.map((col, i) =&gt; {` | 定义变量或常量，保存页面状态。 |
| 608 | `    const color = skyColors[i % skyColors.length];` | 定义变量或常量，保存页面状态。 |
| 609 | `    if (chartType === &#x27;scatter&#x27;) {` | 条件分支，控制逻辑流程。 |
| 610 | `      return {` | 函数返回值。 |
| 611 | `        label: col,` | JavaScript业务逻辑或DOM操作。 |
| 612 | `        data: currentData.map(r =&gt; ({` | JavaScript业务逻辑或DOM操作。 |
| 613 | `          x: r[xField],` | JavaScript业务逻辑或DOM操作。 |
| 614 | `          y: r[col] !== null &amp;&amp; r[col] !== undefined ? parseFloat(r[col]) : 0` | JavaScript业务逻辑或DOM操作。 |
| 615 | `        })),` | JavaScript业务逻辑或DOM操作。 |
| 616 | `        borderColor: color,` | JavaScript业务逻辑或DOM操作。 |
| 617 | `        backgroundColor: color + &#x27;cc&#x27;,` | JavaScript业务逻辑或DOM操作。 |
| 618 | `      };` | JavaScript业务逻辑或DOM操作。 |
| 619 | `    }` | JavaScript业务逻辑或DOM操作。 |
| 620 | `    return {` | 函数返回值。 |
| 621 | `      label: col,` | JavaScript业务逻辑或DOM操作。 |
| 622 | `      data: currentData.map(r =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 623 | `        const val = r[col];` | 定义变量或常量，保存页面状态。 |
| 624 | `        return val !== null &amp;&amp; val !== undefined ? parseFloat(val) : 0;` | 函数返回值。 |
| 625 | `      }),` | JavaScript业务逻辑或DOM操作。 |
| 626 | `      borderColor: color,` | JavaScript业务逻辑或DOM操作。 |
| 627 | `      backgroundColor: chartType === &#x27;line&#x27; ? &#x27;transparent&#x27; : color + &#x27;aa&#x27;,` | JavaScript业务逻辑或DOM操作。 |
| 628 | `      borderWidth: 2,` | JavaScript业务逻辑或DOM操作。 |
| 629 | `      tension: 0.3,` | JavaScript业务逻辑或DOM操作。 |
| 630 | `      pointRadius: chartType === &#x27;line&#x27; ? 3 : 0,` | JavaScript业务逻辑或DOM操作。 |
| 631 | `      pointHoverRadius: 5,` | JavaScript业务逻辑或DOM操作。 |
| 632 | `    };` | JavaScript业务逻辑或DOM操作。 |
| 633 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 634 | `  ` | 空行，用于提升可读性。 |
| 635 | `  const ctx = document.getElementById(&#x27;mainChart&#x27;).getContext(&#x27;2d&#x27;);` | 定义变量或常量，保存页面状态。 |
| 636 | `  currentChart = new Chart(ctx, {` | 创建Chart.js图表实例。 |
| 637 | `    type: chartType,` | JavaScript业务逻辑或DOM操作。 |
| 638 | `    data: { labels, datasets },` | JavaScript业务逻辑或DOM操作。 |
| 639 | `    options: {` | JavaScript业务逻辑或DOM操作。 |
| 640 | `      responsive: true,` | JavaScript业务逻辑或DOM操作。 |
| 641 | `      maintainAspectRatio: true,` | JavaScript业务逻辑或DOM操作。 |
| 642 | `      aspectRatio: chartType === &#x27;pie&#x27; \|\| chartType === &#x27;heatmap&#x27; ? 1.5 : 2.5,` | JavaScript业务逻辑或DOM操作。 |
| 643 | `      plugins: {` | JavaScript业务逻辑或DOM操作。 |
| 644 | `        legend: { labels: { color: &#x27;#888888&#x27;, font: { size: 12 } } },` | JavaScript业务逻辑或DOM操作。 |
| 645 | `        tooltip: {` | JavaScript业务逻辑或DOM操作。 |
| 646 | `          callbacks: {` | JavaScript业务逻辑或DOM操作。 |
| 647 | `            label: ctx =&gt; `${ctx.dataset.label}: ${fmtNum(ctx.raw)}`` | JavaScript业务逻辑或DOM操作。 |
| 648 | `          }` | JavaScript业务逻辑或DOM操作。 |
| 649 | `        }` | JavaScript业务逻辑或DOM操作。 |
| 650 | `      },` | JavaScript业务逻辑或DOM操作。 |
| 651 | `      scales: chartType === &#x27;pie&#x27; \|\| chartType === &#x27;heatmap&#x27; \|\| chartType === &#x27;radar&#x27; ? {} : chartType === &#x27;scatter&#x27; ? {` | JavaScript业务逻辑或DOM操作。 |
| 652 | `        x: { type: &#x27;linear&#x27;, ticks: { color: &#x27;#888888&#x27; }, grid: { color: &#x27;#353538&#x27; } },` | JavaScript业务逻辑或DOM操作。 |
| 653 | `        y: { ticks: { color: &#x27;#888888&#x27;, callback: v =&gt; fmtNum(v) }, grid: { color: &#x27;#353538&#x27; } }` | JavaScript业务逻辑或DOM操作。 |
| 654 | `      } : {` | JavaScript业务逻辑或DOM操作。 |
| 655 | `        x: { ticks: { color: &#x27;#888888&#x27;, maxRotation: 45 }, grid: { color: &#x27;#353538&#x27; } },` | JavaScript业务逻辑或DOM操作。 |
| 656 | `        y: { ticks: { color: &#x27;#888888&#x27;, callback: v =&gt; fmtNum(v) }, grid: { color: &#x27;#353538&#x27; } }` | JavaScript业务逻辑或DOM操作。 |
| 657 | `      }` | JavaScript业务逻辑或DOM操作。 |
| 658 | `    }` | JavaScript业务逻辑或DOM操作。 |
| 659 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 660 | `}` | JavaScript业务逻辑或DOM操作。 |
| 661 | `` | 空行，用于提升可读性。 |
| 662 | `function updateStatCards(data, yFields) {` | 定义函数，封装交互或渲染逻辑。 |
| 663 | `  document.getElementById(&#x27;statCards&#x27;).style.display = &#x27;grid&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 664 | `` | 空行，用于提升可读性。 |
| 665 | `  let html = &#x27;&#x27;;` | 定义变量或常量，保存页面状态。 |
| 666 | `  yFields.slice(0, 4).forEach(field =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 667 | `    const values = data.map(r =&gt; parseFloat(r[field]) \|\| 0).filter(v =&gt; !isNaN(v));` | 定义变量或常量，保存页面状态。 |
| 668 | `    const sum = values.reduce((a, b) =&gt; a + b, 0);` | 定义变量或常量，保存页面状态。 |
| 669 | `    const avg = values.length ? sum / values.length : 0;` | 定义变量或常量，保存页面状态。 |
| 670 | `    const max = values.length ? Math.max(...values) : 0;` | 定义变量或常量，保存页面状态。 |
| 671 | `    const min = values.length ? Math.min(...values) : 0;` | 定义变量或常量，保存页面状态。 |
| 672 | `    const sumClass = sum &gt;= 0 ? &#x27;pos&#x27; : &#x27;neg&#x27;;` | 定义变量或常量，保存页面状态。 |
| 673 | `    html += `&lt;div class=&quot;stat-card&quot;&gt;&lt;div class=&quot;sc-label&quot;&gt;${field} 合计&lt;/div&gt;&lt;div class=&quot;sc-value ${sumClass}&quot;&gt;${fmtNum(sum)}&lt;/div&gt;&lt;/div&gt;`;` | JavaScript业务逻辑或DOM操作。 |
| 674 | `    html += `&lt;div class=&quot;stat-card&quot;&gt;&lt;div class=&quot;sc-label&quot;&gt;${field} 均值&lt;/div&gt;&lt;div class=&quot;sc-value neu&quot;&gt;${fmtNum(avg)}&lt;/div&gt;&lt;/div&gt;`;` | JavaScript业务逻辑或DOM操作。 |
| 675 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 676 | `  html += `&lt;div class=&quot;stat-card&quot;&gt;&lt;div class=&quot;sc-label&quot;&gt;记录数&lt;/div&gt;&lt;div class=&quot;sc-value neu&quot;&gt;${data.length.toLocaleString()}&lt;/div&gt;&lt;/div&gt;`;` | JavaScript业务逻辑或DOM操作。 |
| 677 | `` | 空行，用于提升可读性。 |
| 678 | `  document.getElementById(&#x27;statCards&#x27;).innerHTML = html;` | JavaScript业务逻辑或DOM操作。 |
| 679 | `}` | JavaScript业务逻辑或DOM操作。 |
| 680 | `` | 空行，用于提升可读性。 |
| 681 | `let tableSortCol = null;` | 定义变量或常量，保存页面状态。 |
| 682 | `let tableSortDir = &#x27;asc&#x27;;` | 定义变量或常量，保存页面状态。 |
| 683 | `let tableFilters = {};` | 定义变量或常量，保存页面状态。 |
| 684 | `` | 空行，用于提升可读性。 |
| 685 | `async function showTable() {` | 定义异步函数，用于请求后端数据。 |
| 686 | `  const tableSel = document.getElementById(&#x27;tableSelect&#x27;);` | 定义变量或常量，保存页面状态。 |
| 687 | `  const table = tableSel.options[tableSel.selectedIndex]?.value \|\| currentTable;` | 定义变量或常量，保存页面状态。 |
| 688 | `  if (!table) { showError(&#x27;请先选择数据表&#x27;); return; }` | 条件分支，控制逻辑流程。 |
| 689 | `  if (currentData.length === 0) { await renderChart(); }` | 条件分支，控制逻辑流程。 |
| 690 | `  if (currentData.length === 0) return;` | 条件分支，控制逻辑流程。 |
| 691 | `` | 空行，用于提升可读性。 |
| 692 | `  document.getElementById(&#x27;tableContainer&#x27;).style.display = &#x27;block&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 693 | `` | 空行，用于提升可读性。 |
| 694 | `  const dateCols = [&#x27;date&#x27;, &#x27;日期&#x27;, &#x27;Date&#x27;, &#x27;DATE&#x27;];` | 定义变量或常量，保存页面状态。 |
| 695 | `  const orderedCols = [...tableColumns].sort((a, b) =&gt; {` | 定义变量或常量，保存页面状态。 |
| 696 | `    if (dateCols.includes(a) &amp;&amp; !dateCols.includes(b)) return -1;` | 条件分支，控制逻辑流程。 |
| 697 | `    if (!dateCols.includes(a) &amp;&amp; dateCols.includes(b)) return 1;` | 条件分支，控制逻辑流程。 |
| 698 | `    return 0;` | 函数返回值。 |
| 699 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 700 | `` | 空行，用于提升可读性。 |
| 701 | `  const filterOptions = {};` | 定义变量或常量，保存页面状态。 |
| 702 | `  orderedCols.forEach(col =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 703 | `    const vals = [...new Set(currentData.map(r =&gt; r[col] !== null &amp;&amp; r[col] !== undefined ? String(r[col]) : &#x27;&#x27;))];` | 定义变量或常量，保存页面状态。 |
| 704 | `    vals.sort();` | JavaScript业务逻辑或DOM操作。 |
| 705 | `    filterOptions[col] = vals;` | JavaScript业务逻辑或DOM操作。 |
| 706 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 707 | `` | 空行，用于提升可读性。 |
| 708 | `  orderedCols.forEach(col =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 709 | `    if (!(col in tableFilters)) tableFilters[col] = &#x27;&#x27;;` | 条件分支，控制逻辑流程。 |
| 710 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 711 | `` | 空行，用于提升可读性。 |
| 712 | `  let filteredData = currentData.filter(row =&gt; {` | 定义变量或常量，保存页面状态。 |
| 713 | `    return orderedCols.every(col =&gt; {` | 函数返回值。 |
| 714 | `      const filterVal = tableFilters[col];` | 定义变量或常量，保存页面状态。 |
| 715 | `      if (!filterVal) return true;` | 条件分支，控制逻辑流程。 |
| 716 | `      return String(row[col]) === filterVal;` | 函数返回值。 |
| 717 | `    });` | JavaScript业务逻辑或DOM操作。 |
| 718 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 719 | `` | 空行，用于提升可读性。 |
| 720 | `  if (tableSortCol &amp;&amp; orderedCols.includes(tableSortCol)) {` | 条件分支，控制逻辑流程。 |
| 721 | `    filteredData.sort((a, b) =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 722 | `      let va = a[tableSortCol], vb = b[tableSortCol];` | 定义变量或常量，保存页面状态。 |
| 723 | `      const isNum = typeof va === &#x27;number&#x27; &amp;&amp; typeof vb === &#x27;number&#x27;;` | 定义变量或常量，保存页面状态。 |
| 724 | `      if (isNum) {` | 条件分支，控制逻辑流程。 |
| 725 | `        return tableSortDir === &#x27;asc&#x27; ? va - vb : vb - va;` | 函数返回值。 |
| 726 | `      }` | JavaScript业务逻辑或DOM操作。 |
| 727 | `      va = String(va \|\| &#x27;&#x27;), vb = String(vb \|\| &#x27;&#x27;);` | JavaScript业务逻辑或DOM操作。 |
| 728 | `      return tableSortDir === &#x27;asc&#x27; ? va.localeCompare(vb) : vb.localeCompare(va);` | 函数返回值。 |
| 729 | `    });` | JavaScript业务逻辑或DOM操作。 |
| 730 | `  }` | JavaScript业务逻辑或DOM操作。 |
| 731 | `` | 空行，用于提升可读性。 |
| 732 | `  const thead = document.getElementById(&#x27;tableHead&#x27;);` | 定义变量或常量，保存页面状态。 |
| 733 | `  thead.innerHTML = &#x27;&lt;tr&gt;&#x27; + orderedCols.map(col =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 734 | `    const sortIcon = tableSortCol === col ? (tableSortDir === &#x27;asc&#x27; ? &#x27; ▲&#x27; : &#x27; ▼&#x27;) : &#x27;&#x27;;` | 定义变量或常量，保存页面状态。 |
| 735 | `    return `&lt;th onclick=&quot;toggleSort(&#x27;${col}&#x27;)&quot; style=&quot;cursor:pointer; user-select:none;&quot;&gt;${col}${sortIcon}&lt;/th&gt;`;` | 函数返回值。 |
| 736 | `  }).join(&#x27;&#x27;) + &#x27;&lt;/tr&gt;&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 737 | `` | 空行，用于提升可读性。 |
| 738 | `  const filterRow = document.createElement(&#x27;tr&#x27;);` | 定义变量或常量，保存页面状态。 |
| 739 | `  filterRow.style.background = &#x27;#2A2A2E&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 740 | `  orderedCols.forEach(col =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 741 | `    const sel = document.createElement(&#x27;select&#x27;);` | 定义变量或常量，保存页面状态。 |
| 742 | `    sel.style.width = &#x27;100%&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 743 | `    sel.style.fontSize = &#x27;11px&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 744 | `    sel.onchange = () =&gt; { tableFilters[col] = sel.value; showTable(); };` | JavaScript业务逻辑或DOM操作。 |
| 745 | `    sel.innerHTML = &#x27;&lt;option value=&quot;&quot;&gt;--全部--&lt;/option&gt;&#x27; +` | JavaScript业务逻辑或DOM操作。 |
| 746 | `      filterOptions[col].map(v =&gt; `&lt;option value=&quot;${v.replace(/&quot;/g, &#x27;&amp;quot;&#x27;)}&quot; ${tableFilters[col] === v ? &#x27;selected&#x27; : &#x27;&#x27;}&gt;${v.substring(0, 20)}&lt;/option&gt;`).join(&#x27;&#x27;);` | JavaScript业务逻辑或DOM操作。 |
| 747 | `    const td = document.createElement(&#x27;td&#x27;);` | 定义变量或常量，保存页面状态。 |
| 748 | `    td.style.padding = &#x27;2px&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 749 | `    td.appendChild(sel);` | JavaScript业务逻辑或DOM操作。 |
| 750 | `    filterRow.appendChild(td);` | JavaScript业务逻辑或DOM操作。 |
| 751 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 752 | `  thead.appendChild(filterRow);` | JavaScript业务逻辑或DOM操作。 |
| 753 | `` | 空行，用于提升可读性。 |
| 754 | `  const tbody = document.getElementById(&#x27;tableBody&#x27;);` | 定义变量或常量，保存页面状态。 |
| 755 | `  tbody.innerHTML = &#x27;&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 756 | `  filteredData.forEach(row =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 757 | `    const tr = document.createElement(&#x27;tr&#x27;);` | 定义变量或常量，保存页面状态。 |
| 758 | `    tr.innerHTML = orderedCols.map(c =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 759 | `      let v = row[c];` | 定义变量或常量，保存页面状态。 |
| 760 | `      const isStr = typeof v === &#x27;string&#x27;;` | 定义变量或常量，保存页面状态。 |
| 761 | `      if (!isStr &amp;&amp; v !== null &amp;&amp; v !== undefined) v = parseFloat(v);` | 条件分支，控制逻辑流程。 |
| 762 | `      const cls = typeof v === &#x27;number&#x27; ? (v &gt;= 0 ? &#x27;pos&#x27; : &#x27;neg&#x27;) : &#x27;&#x27;;` | 定义变量或常量，保存页面状态。 |
| 763 | `      const fmt = typeof v === &#x27;number&#x27; ? fmtNum(v) : String(v).substring(0, 30);` | 定义变量或常量，保存页面状态。 |
| 764 | `      return `&lt;td class=&quot;${cls}&quot;&gt;${fmt}&lt;/td&gt;`;` | 函数返回值。 |
| 765 | `    }).join(&#x27;&#x27;);` | JavaScript业务逻辑或DOM操作。 |
| 766 | `    tbody.appendChild(tr);` | JavaScript业务逻辑或DOM操作。 |
| 767 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 768 | `}` | JavaScript业务逻辑或DOM操作。 |
| 769 | `` | 空行，用于提升可读性。 |
| 770 | `function toggleSort(col) {` | 定义函数，封装交互或渲染逻辑。 |
| 771 | `  if (tableSortCol === col) {` | 条件分支，控制逻辑流程。 |
| 772 | `    tableSortDir = tableSortDir === &#x27;asc&#x27; ? &#x27;desc&#x27; : &#x27;asc&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 773 | `  } else {` | JavaScript业务逻辑或DOM操作。 |
| 774 | `    tableSortCol = col;` | JavaScript业务逻辑或DOM操作。 |
| 775 | `    tableSortDir = &#x27;asc&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 776 | `  }` | JavaScript业务逻辑或DOM操作。 |
| 777 | `  showTable();` | JavaScript业务逻辑或DOM操作。 |
| 778 | `}` | JavaScript业务逻辑或DOM操作。 |
| 779 | `` | 空行，用于提升可读性。 |
| 780 | `function exportCSV() {` | 定义函数，封装交互或渲染逻辑。 |
| 781 | `  if (!currentData.length) return;` | 条件分支，控制逻辑流程。 |
| 782 | `  const headers = tableColumns.join(&#x27;,&#x27;);` | 定义变量或常量，保存页面状态。 |
| 783 | `  const rows = currentData.map(row =&gt; tableColumns.map(c =&gt; {` | 定义变量或常量，保存页面状态。 |
| 784 | `    const v = row[c];` | 定义变量或常量，保存页面状态。 |
| 785 | `    return typeof v === &#x27;number&#x27; ? v : `&quot;${v}&quot;`;` | 函数返回值。 |
| 786 | `  }).join(&#x27;,&#x27;));` | JavaScript业务逻辑或DOM操作。 |
| 787 | `  const csv = [headers, ...rows].join(&#x27;\n&#x27;);` | 定义变量或常量，保存页面状态。 |
| 788 | `  const blob = new Blob([csv], { type: &#x27;text/csv&#x27; });` | 定义变量或常量，保存页面状态。 |
| 789 | `  const url = URL.createObjectURL(blob);` | 定义变量或常量，保存页面状态。 |
| 790 | `  const a = document.createElement(&#x27;a&#x27;);` | 定义变量或常量，保存页面状态。 |
| 791 | `  a.href = url; a.download = `export_${currentTable}_${Date.now()}.csv`; a.click();` | JavaScript业务逻辑或DOM操作。 |
| 792 | `  URL.revokeObjectURL(url);` | JavaScript业务逻辑或DOM操作。 |
| 793 | `}` | JavaScript业务逻辑或DOM操作。 |
| 794 | `` | 空行，用于提升可读性。 |
| 795 | `// ============================================================` | JavaScript注释，用于分区和说明。 |
| 796 | `// 快捷预设` | JavaScript注释，用于分区和说明。 |
| 797 | `// ============================================================` | JavaScript注释，用于分区和说明。 |
| 798 | `` | 空行，用于提升可读性。 |
| 799 | `async function applyPreset(preset) {` | 定义异步函数，用于请求后端数据。 |
| 800 | `  document.getElementById(&#x27;dbSelect&#x27;).value = &#x27;analysis&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 801 | `  await onDbChange();` | JavaScript业务逻辑或DOM操作。 |
| 802 | `  document.getElementById(&#x27;tableSelect&#x27;).value = &#x27;k12_token_spread_size_daily_v2&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 803 | `  await onTableChange();` | JavaScript业务逻辑或DOM操作。 |
| 804 | `` | 空行，用于提升可读性。 |
| 805 | `  if (preset === &#x27;daily_pnl&#x27;) {` | 条件分支，控制逻辑流程。 |
| 806 | `    document.querySelectorAll(&#x27;#yFieldGroup input&#x27;).forEach(cb =&gt; cb.checked = cb.value === &#x27;alpha&#x27;);` | JavaScript业务逻辑或DOM操作。 |
| 807 | `    setChartType(&#x27;line&#x27;, document.querySelector(&#x27;.chart-type-btn[onclick=&quot;setChartType(\&#x27;line\&#x27;, this)&quot;]&#x27;));` | JavaScript业务逻辑或DOM操作。 |
| 808 | `  } else if (preset === &#x27;heatmap&#x27;) {` | JavaScript业务逻辑或DOM操作。 |
| 809 | `    document.getElementById(&#x27;noData&#x27;).style.display = &#x27;none&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 810 | `    const dateFrom = document.getElementById(&#x27;dateFrom&#x27;).value;` | 定义变量或常量，保存页面状态。 |
| 811 | `    const dateTo = document.getElementById(&#x27;dateTo&#x27;).value;` | 定义变量或常量，保存页面状态。 |
| 812 | `    try {` | JavaScript业务逻辑或DOM操作。 |
| 813 | `      const resp = await fetch(&#x27;/api/heatmap&#x27;, {` | 定义变量或常量，保存页面状态。 |
| 814 | `        method: &#x27;POST&#x27;, headers: {&#x27;Content-Type&#x27;: &#x27;application/json&#x27;},` | JavaScript业务逻辑或DOM操作。 |
| 815 | `        body: JSON.stringify({ table: currentTable \|\| &#x27;k12_token_spread_size_daily_v2&#x27;, db: currentDb, metric: &#x27;alpha&#x27;, date_from: dateFrom, date_to: dateTo })` | JavaScript业务逻辑或DOM操作。 |
| 816 | `      });` | JavaScript业务逻辑或DOM操作。 |
| 817 | `      const data = await resp.json();` | 定义变量或常量，保存页面状态。 |
| 818 | `      renderTrueHeatmap(data);` | JavaScript业务逻辑或DOM操作。 |
| 819 | `      document.getElementById(&#x27;chartContainer&#x27;).style.display = &#x27;block&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 820 | `      document.getElementById(&#x27;chartTitle&#x27;).textContent = &#x27;Alpha 热力图（价差区间 × 规模区间）&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 821 | `      document.getElementById(&#x27;tableContainer&#x27;).style.display = &#x27;none&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 822 | `    } catch(e) { showError(e.message); }` | JavaScript业务逻辑或DOM操作。 |
| 823 | `    return;` | JavaScript业务逻辑或DOM操作。 |
| 824 | `  } else if (preset === &#x27;spread_top&#x27;) {` | JavaScript业务逻辑或DOM操作。 |
| 825 | `    document.querySelectorAll(&#x27;#yFieldGroup input&#x27;).forEach(cb =&gt; cb.checked = [&#x27;alpha&#x27;,&#x27;theoretical_profit&#x27;,&#x27;bundle_fee&#x27;].includes(cb.value));` | JavaScript业务逻辑或DOM操作。 |
| 826 | `    setChartType(&#x27;bar&#x27;, document.querySelector(&#x27;.chart-type-btn[onclick=&quot;setChartType(\&#x27;bar\&#x27;, this)&quot;]&#x27;));` | JavaScript业务逻辑或DOM操作。 |
| 827 | `  } else if (preset === &#x27;size_top&#x27;) {` | JavaScript业务逻辑或DOM操作。 |
| 828 | `    document.querySelectorAll(&#x27;#yFieldGroup input&#x27;).forEach(cb =&gt; cb.checked = [&#x27;alpha&#x27;,&#x27;theoretical_profit&#x27;,&#x27;bundle_fee&#x27;].includes(cb.value));` | JavaScript业务逻辑或DOM操作。 |
| 829 | `    setChartType(&#x27;bar&#x27;, document.querySelector(&#x27;.chart-type-btn[onclick=&quot;setChartType(\&#x27;bar\&#x27;, this)&quot;]&#x27;));` | JavaScript业务逻辑或DOM操作。 |
| 830 | `  }` | JavaScript业务逻辑或DOM操作。 |
| 831 | `` | 空行，用于提升可读性。 |
| 832 | `  renderChart();` | JavaScript业务逻辑或DOM操作。 |
| 833 | `}` | JavaScript业务逻辑或DOM操作。 |
| 834 | `` | 空行，用于提升可读性。 |
| 835 | `function renderHeatmap(data) {` | 定义函数，封装交互或渲染逻辑。 |
| 836 | `  if (currentChart) currentChart.destroy();` | 条件分支，控制逻辑流程。 |
| 837 | `  ` | 空行，用于提升可读性。 |
| 838 | `  // 提取 spread_range 和 size_range 的唯一值` | JavaScript注释，用于分区和说明。 |
| 839 | `  const spreads = [...new Set(data.map(r =&gt; r.spread_range))].sort();` | 定义变量或常量，保存页面状态。 |
| 840 | `  const sizes = [...new Set(data.map(r =&gt; r.size_range))].sort();` | 定义变量或常量，保存页面状态。 |
| 841 | `  ` | 空行，用于提升可读性。 |
| 842 | `  const ctx = document.getElementById(&#x27;mainChart&#x27;).getContext(&#x27;2d&#x27;);` | 定义变量或常量，保存页面状态。 |
| 843 | `  ` | 空行，用于提升可读性。 |
| 844 | `  // 简单用柱状图模拟热力图（每组堆叠柱）` | JavaScript注释，用于分区和说明。 |
| 845 | `  currentChart = new Chart(ctx, {` | 创建Chart.js图表实例。 |
| 846 | `    type: &#x27;bar&#x27;,` | JavaScript业务逻辑或DOM操作。 |
| 847 | `    data: {` | JavaScript业务逻辑或DOM操作。 |
| 848 | `      labels: spreads,` | JavaScript业务逻辑或DOM操作。 |
| 849 | `      datasets: sizes.map((size, i) =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 850 | `        const skyPalette = [&#x27;#4FA8D7&#x27;,&#x27;#7EC4E8&#x27;,&#x27;#3A8AB8&#x27;,&#x27;#6AAED6&#x27;,&#x27;#2E7DAF&#x27;,&#x27;#9AC8E3&#x27;,&#x27;#A8D4ED&#x27;,&#x27;#1F6A9E&#x27;];` | 定义变量或常量，保存页面状态。 |
| 851 | `        return {` | 函数返回值。 |
| 852 | `          label: size,` | JavaScript业务逻辑或DOM操作。 |
| 853 | `          data: spreads.map(sp =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 854 | `            const row = data.find(r =&gt; r.spread_range === sp &amp;&amp; r.size_range === size);` | 定义变量或常量，保存页面状态。 |
| 855 | `            return row ? row.value : 0;` | 函数返回值。 |
| 856 | `          }),` | JavaScript业务逻辑或DOM操作。 |
| 857 | `          backgroundColor: skyPalette[i % skyPalette.length] + &#x27;99&#x27;,` | JavaScript业务逻辑或DOM操作。 |
| 858 | `        };` | JavaScript业务逻辑或DOM操作。 |
| 859 | `      })` | JavaScript业务逻辑或DOM操作。 |
| 860 | `    },` | JavaScript业务逻辑或DOM操作。 |
| 861 | `    options: {` | JavaScript业务逻辑或DOM操作。 |
| 862 | `      responsive: true,` | JavaScript业务逻辑或DOM操作。 |
| 863 | `      maintainAspectRatio: true,` | JavaScript业务逻辑或DOM操作。 |
| 864 | `      aspectRatio: 1.5,` | JavaScript业务逻辑或DOM操作。 |
| 865 | `      plugins: {` | JavaScript业务逻辑或DOM操作。 |
| 866 | `        legend: { labels: { color: &#x27;#888888&#x27; } },` | JavaScript业务逻辑或DOM操作。 |
| 867 | `        tooltip: { callbacks: { label: ctx =&gt; `${ctx.dataset.label}: ${fmtNum(ctx.raw)}` } }` | JavaScript业务逻辑或DOM操作。 |
| 868 | `      },` | JavaScript业务逻辑或DOM操作。 |
| 869 | `      scales: {` | JavaScript业务逻辑或DOM操作。 |
| 870 | `        x: { ticks: { color: &#x27;#888888&#x27; }, grid: { color: &#x27;#353538&#x27; } },` | JavaScript业务逻辑或DOM操作。 |
| 871 | `        y: { ticks: { color: &#x27;#888888&#x27;, callback: v =&gt; fmtNum(v) }, grid: { color: &#x27;#353538&#x27; } }` | JavaScript业务逻辑或DOM操作。 |
| 872 | `      }` | JavaScript业务逻辑或DOM操作。 |
| 873 | `    }` | JavaScript业务逻辑或DOM操作。 |
| 874 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 875 | `}` | JavaScript业务逻辑或DOM操作。 |
| 876 | `` | 空行，用于提升可读性。 |
| 877 | `// ============================================================` | JavaScript注释，用于分区和说明。 |
| 878 | `// 工具函数` | JavaScript注释，用于分区和说明。 |
| 879 | `// ============================================================` | JavaScript注释，用于分区和说明。 |
| 880 | `` | 空行，用于提升可读性。 |
| 881 | `function fmtNum(v) {` | 定义函数，封装交互或渲染逻辑。 |
| 882 | `  if (v === null \|\| v === undefined \|\| isNaN(v)) return &#x27;0&#x27;;` | 条件分支，控制逻辑流程。 |
| 883 | `  if (typeof v === &#x27;string&#x27;) return v;` | 条件分支，控制逻辑流程。 |
| 884 | `  v = parseFloat(v);` | JavaScript业务逻辑或DOM操作。 |
| 885 | `  if (Math.abs(v) &gt;= 1e6) return (v / 1e6).toFixed(1) + &#x27;m&#x27;;` | 条件分支，控制逻辑流程。 |
| 886 | `  if (Math.abs(v) &gt;= 1e3) return (v / 1e3).toFixed(1) + &#x27;k&#x27;;` | 条件分支，控制逻辑流程。 |
| 887 | `  return v.toFixed(2);` | 函数返回值。 |
| 888 | `}` | JavaScript业务逻辑或DOM操作。 |
| 889 | `` | 空行，用于提升可读性。 |
| 890 | `function showError(msg) {` | 定义函数，封装交互或渲染逻辑。 |
| 891 | `  document.getElementById(&#x27;errorBox&#x27;).innerHTML = `&lt;div class=&quot;error-msg&quot;&gt;${msg}&lt;/div&gt;`;` | JavaScript业务逻辑或DOM操作。 |
| 892 | `}` | JavaScript业务逻辑或DOM操作。 |
| 893 | `` | 空行，用于提升可读性。 |
| 894 | `// ============================================================` | JavaScript注释，用于分区和说明。 |
| 895 | `// 热力图渲染增强（spread × size 交叉矩阵）` | JavaScript注释，用于分区和说明。 |
| 896 | `// ============================================================` | JavaScript注释，用于分区和说明。 |
| 897 | `` | 空行，用于提升可读性。 |
| 898 | `function renderTrueHeatmap(data) {` | 定义函数，封装交互或渲染逻辑。 |
| 899 | `  if (currentChart) currentChart.destroy();` | 条件分支，控制逻辑流程。 |
| 900 | `  if (!data \|\| data.length === 0) { showError(&#x27;无热力图数据&#x27;); return; }` | 条件分支，控制逻辑流程。 |
| 901 | `` | 空行，用于提升可读性。 |
| 902 | `  const spreads = [...new Set(data.map(r =&gt; r.spread_range))].sort();` | 定义变量或常量，保存页面状态。 |
| 903 | `  const sizes = [...new Set(data.map(r =&gt; r.size_range))].sort();` | 定义变量或常量，保存页面状态。 |
| 904 | `` | 空行，用于提升可读性。 |
| 905 | `  // 构建矩阵` | JavaScript注释，用于分区和说明。 |
| 906 | `  const matrix = {};` | 定义变量或常量，保存页面状态。 |
| 907 | `  data.forEach(r =&gt; {` | JavaScript业务逻辑或DOM操作。 |
| 908 | `    if (!matrix[r.spread_range]) matrix[r.spread_range] = {};` | 条件分支，控制逻辑流程。 |
| 909 | `    matrix[r.spread_range][r.size_range] = r.value;` | JavaScript业务逻辑或DOM操作。 |
| 910 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 911 | `` | 空行，用于提升可读性。 |
| 912 | `  const ctx = document.getElementById(&#x27;mainChart&#x27;).getContext(&#x27;2d&#x27;);` | 定义变量或常量，保存页面状态。 |
| 913 | `  const skyPalette = [&#x27;#4FA8D7&#x27;,&#x27;#7EC4E8&#x27;,&#x27;#3A8AB8&#x27;,&#x27;#6AAED6&#x27;,&#x27;#2E7DAF&#x27;,&#x27;#9AC8E3&#x27;,&#x27;#A8D4ED&#x27;,&#x27;#1F6A9E&#x27;];` | 定义变量或常量，保存页面状态。 |
| 914 | `` | 空行，用于提升可读性。 |
| 915 | `  currentChart = new Chart(ctx, {` | 创建Chart.js图表实例。 |
| 916 | `    type: &#x27;bar&#x27;,` | JavaScript业务逻辑或DOM操作。 |
| 917 | `    data: {` | JavaScript业务逻辑或DOM操作。 |
| 918 | `      labels: spreads,` | JavaScript业务逻辑或DOM操作。 |
| 919 | `      datasets: sizes.map((size, i) =&gt; ({` | JavaScript业务逻辑或DOM操作。 |
| 920 | `        label: size,` | JavaScript业务逻辑或DOM操作。 |
| 921 | `        data: spreads.map(sp =&gt; matrix[sp]?.[size] \|\| 0),` | JavaScript业务逻辑或DOM操作。 |
| 922 | `        backgroundColor: skyPalette[i % skyPalette.length] + &#x27;99&#x27;,` | JavaScript业务逻辑或DOM操作。 |
| 923 | `        borderColor: skyPalette[i % skyPalette.length],` | JavaScript业务逻辑或DOM操作。 |
| 924 | `        borderWidth: 1,` | JavaScript业务逻辑或DOM操作。 |
| 925 | `      }))` | JavaScript业务逻辑或DOM操作。 |
| 926 | `    },` | JavaScript业务逻辑或DOM操作。 |
| 927 | `    options: {` | JavaScript业务逻辑或DOM操作。 |
| 928 | `      responsive: true,` | JavaScript业务逻辑或DOM操作。 |
| 929 | `      maintainAspectRatio: true,` | JavaScript业务逻辑或DOM操作。 |
| 930 | `      aspectRatio: 1.8,` | JavaScript业务逻辑或DOM操作。 |
| 931 | `      plugins: {` | JavaScript业务逻辑或DOM操作。 |
| 932 | `        legend: { position: &#x27;bottom&#x27;, labels: { color: &#x27;#888888&#x27;, font: { size: 11 } } },` | JavaScript业务逻辑或DOM操作。 |
| 933 | `        tooltip: {` | JavaScript业务逻辑或DOM操作。 |
| 934 | `          callbacks: {` | JavaScript业务逻辑或DOM操作。 |
| 935 | `            label: ctx =&gt; `${ctx.dataset.label}: ${fmtNum(ctx.raw)}`` | JavaScript业务逻辑或DOM操作。 |
| 936 | `          }` | JavaScript业务逻辑或DOM操作。 |
| 937 | `        }` | JavaScript业务逻辑或DOM操作。 |
| 938 | `      },` | JavaScript业务逻辑或DOM操作。 |
| 939 | `      scales: {` | JavaScript业务逻辑或DOM操作。 |
| 940 | `        x: { ticks: { color: &#x27;#888888&#x27;, maxRotation: 45, font: { size: 10 } }, grid: { color: &#x27;#353538&#x27; } },` | JavaScript业务逻辑或DOM操作。 |
| 941 | `        y: { ticks: { color: &#x27;#888888&#x27;, callback: v =&gt; fmtNum(v) }, grid: { color: &#x27;#353538&#x27; } }` | JavaScript业务逻辑或DOM操作。 |
| 942 | `      }` | JavaScript业务逻辑或DOM操作。 |
| 943 | `    }` | JavaScript业务逻辑或DOM操作。 |
| 944 | `  });` | JavaScript业务逻辑或DOM操作。 |
| 945 | `` | 空行，用于提升可读性。 |
| 946 | `  document.getElementById(&#x27;chartContainer&#x27;).style.display = &#x27;block&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 947 | `  document.getElementById(&#x27;noData&#x27;).style.display = &#x27;none&#x27;;` | JavaScript业务逻辑或DOM操作。 |
| 948 | `}` | JavaScript业务逻辑或DOM操作。 |
| 949 | `&lt;/script&gt;` | 脚本块结束。 |
| 950 | `&lt;/body&gt;` | 页面主体结束。 |
| 951 | `&lt;/html&gt;` | 页面结构或文本内容。 |
