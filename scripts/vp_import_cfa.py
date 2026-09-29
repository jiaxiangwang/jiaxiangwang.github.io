#!/usr/bin/env python3
"""把 /Users/jiaxiang/Documents/code/cfa/pz_question_bank 导入 VitePress 的 docs/cfa/ 目录。

结构：docs/cfa/{来源目录}/{book-slug}.md
  - 来源目录保留中文名（真题 / 品职出题 ...），与原 README 心智模型一致
  - book-slug = 大类名转 slug（英文字母数字小写 + 中文保留），避免 "26年 " 等空格/特殊字符
  - 每个文件加 frontmatter（title / 来源 / book / 题数）
  - **题目排版升级**：源文件是带 `**题干**` / `**选项**` / `**[图片内容-OCR]**` 标签的纯 markdown，
    导入时转换为结构化 HTML 块（题号徽章 / OCR 数据块转表格 / 选项组 / Case 小题卡片），
    配合 theme/styles/question.css 渲染
  - docs/cfa/index.md = 来源×大类矩阵总览（含各文件题数）
  - 每个来源目录生成 index.md（该来源下的大类清单）

跳过派生目录 Other+原版书（与 Other / 原版书内容重复）。
用法：python3 scripts/vp_import_cfa.py
"""
import os
import re
import shutil

BANK = "/Users/jiaxiang/Documents/code/cfa/pz_question_bank"
DOCS_CFA = "/Users/jiaxiang/Documents/code/blog/docs/cfa"

# (目录名, 来源代码, 展示名) —— 顺序即侧边栏顺序：按复习价值排序
SOURCES = [
    ("Other", "OTH", "Other"),
    ("品职出题", "PZ", "品职出题"),
    ("原版书", "ORIG", "原版书"),
    ("Handbook", "HB", "Handbook"),
    ("Mock", "MOCK", "Mock"),
    ("真题", "REAL", "真题"),
    ("经典题", "CLASS", "经典题"),
]

# 大类展示顺序（按 CFA III 知识体系）
BOOK_ORDER = [
    "26年 Core-Derivatives and Risk Management- Derivatives",
    "Core-Asset Allocation-AA",
    "Core-Asset Allocation-CME",
    "Core-Portfolio Construction-个人IPS",
    "Core-Portfolio Construction-机构IPS",
    "Core-Portfolio Construction-Equity",
    "Core-Portfolio Construction-Fixed Income",
    "Core-Portfolio Construction-Alternative",
    "Core-Portfolio Construction-Trading",
    "Core-Performance Measurement-GIPS",
    "Core-Performance Measurement-Performance Evaluation",
    "Pathway-Portfolio Management-Fixed Income",
    "Pathway-Portfolio Management-Trading",
    "Pathway-Portfolio Management-机构IPS",
    "Pathway-Private Wealth",
]

BOOK_LABELS = {
    "26年 Core-Derivatives and Risk Management- Derivatives": "衍生品与风险管理（26年大纲）",
    "Core-Asset Allocation-AA": "资产配置 · AA",
    "Core-Asset Allocation-CME": "资本市场预期 · CME",
    "Core-Portfolio Construction-个人IPS": "组合构建 · 个人 IPS",
    "Core-Portfolio Construction-机构IPS": "组合构建 · 机构 IPS",
    "Core-Portfolio Construction-Equity": "组合构建 · 股票",
    "Core-Portfolio Construction-Fixed Income": "组合构建 · 固定收益",
    "Core-Portfolio Construction-Alternative": "组合构建 · 另类投资",
    "Core-Portfolio Construction-Trading": "组合构建 · 交易",
    "Core-Performance Measurement-GIPS": "绩效度量 · GIPS",
    "Core-Performance Measurement-Performance Evaluation": "绩效度量 · 绩效评估",
    "Pathway-Portfolio Management-Fixed Income": "Pathway · 组合管理-固定收益",
    "Pathway-Portfolio Management-Trading": "Pathway · 组合管理-交易",
    "Pathway-Portfolio Management-机构IPS": "Pathway · 组合管理-机构IPS",
    "Pathway-Private Wealth": "Pathway · 私人财富管理",
}

TYPE_LABELS = {
    "选择题": "单选",
    "单选题": "单选",
    "问答题": "问答",
    "选择题组": "单选",
    "问答题组": "问答",
    "综合题组": "综合",
}

# 源文件中已 OCR 为文字的表格行：`> a | b | c`
OCR_ROW = re.compile(r"^> (.*) \| (.*)$")


def slugify(book: str, suffix: str) -> str:
    """大类名 -> 文件 slug。保留中文，英文小写，空格/特殊字符转连字符。"""
    s = book.strip()
    s = re.sub(r"\s*-\s*", "-", s)
    s = s.replace("26年 ", "26-")
    s = re.sub(r"[^0-9a-zA-Z\u4e00-\u9fff-]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-").lower()
    return f"{s}_{suffix}"


def count_questions(text: str) -> int:
    return len(re.findall(r"^## No\.", text, re.M))


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def ocr_lines_to_html(block_lines):
    """把连续的 `> a | b | c` OCR 行转成 <table>。非 `|` 分隔的行转普通段落。"""
    table_rows, para_rows, out = [], [], []
    for ln in block_lines:
        m = OCR_ROW.match(ln)
        if m and "|" in ln[2:]:
            # 按裸 | 切分（OCR 行内不会出现转义管道）
            cells = [c.strip() for c in ln[2:].split(" | ")]
            table_rows.append(cells)
        else:
            para_rows.append(ln)
    if table_rows:
        body = "".join(
            "<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in table_rows
        )
        out.append(f'<div class="q-exhibit"><table><tbody>{body}</tbody></table></div>')
    for p in para_rows:
        out.append(f"<p>{esc(p[2:])}</p>")
    return out


def md_inline(s: str) -> str:
    """极简行内 markdown：粗体/斜体/行内代码。其余字符转义由调用方处理。"""
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s


def render_stem(stem_lines):
    """题干块：普通行转段落，OCR 块转表格/段落。"""
    out, ocr = [], []

    def flush():
        nonlocal ocr
        if ocr:
            out.extend(ocr_lines_to_html(ocr))
            ocr = []

    for ln in stem_lines:
        if ln.startswith("> "):
            ocr.append(ln)
        else:
            flush()
            s = ln.strip()
            # 跳过 OCR 标记行（表格自带视觉呈现，无需"图片内容"字样）
            if s and s != "**[图片内容-OCR]**":
                out.append(f"<p>{md_inline(ln)}</p>")
    flush()
    return out


def render_options(opts):
    """选项列表 -> 分组 HTML。首 token 是 A./B./C. 时提取为字母徽章。"""
    if not opts:
        return []
    items = []
    for o in opts:
        m = re.match(r"^([A-Z])[.\s、)]\s*(.*)$", o.strip())
        key = m.group(1) if m else "·"
        rest = m.group(2) if m else o.strip()
        items.append(f'<li data-k="{key}">{md_inline(rest)}</li>')
    return [f'<div class="q-options"><ul>{"".join(items)}</ul></div>']


def render_question(q):
    """单题（## No.xxx）或 Case 小题（### 第N小题）-> HTML 块列表。"""
    t = q["type"]
    m = re.match(r"Case题·(\d+)小题$", t)
    if m:
        label = f"Case · {m.group(1)} 小题"
    else:
        label = TYPE_LABELS.get(t, t)
    badge = f'<span class="q-badge q-badge-{ "grp" if q["is_sub"] else "main" }">{label}</span>'
    no = f'<span class="q-no">No.{q["no"]}</span>' if q["no"] else ""

    html = [f'<div class="q-card{" q-sub" if q["is_sub"] else ""}">']
    html.append(f'<div class="q-head">{no}{badge}</div>')

    if q.get("material"):
        html.append('<div class="q-material">')
        html.extend(render_stem(q["material"]))
        html.append("</div>")

    if q.get("stem"):
        html.append('<div class="q-stem">')
        html.extend(render_stem(q["stem"]))
        html.append("</div>")

    html.extend(render_options(q.get("options")))
    html.append("</div>")
    return html


def parse_and_render(text):
    """把源 markdown 正文解析为题目对象列表并渲染为 HTML。"""
    lines = text.split("\n")
    questions = []          # [{no,type,material,stem,options,is_sub}]
    cur = None              # 当前主题（Case 题组的容器）
    sub = None              # 当前小题
    mode = None             # 'material' | 'stem' | 'options'

    def new_target(kind, header):
        nonlocal cur, sub, mode
        if kind == "main":
            cur = {"no": header["no"], "type": header["type"], "material": [], "stem": [], "options": [], "is_sub": False}
            questions.append(cur)
            sub = None
            mode = "material" if header["type"] in TYPE_LABELS and "组" in header["type"] else "stem"
        else:  # sub
            sub = {"no": "", "type": header["type"], "material": [], "stem": [], "options": [], "is_sub": True}
            if cur is not None:
                cur.setdefault("subs", []).append(sub)
            else:  # 容错：无主题头的小题（不应出现）
                questions.append(sub)
            mode = "stem"
        return cur if kind == "main" else sub

    target = None
    i = 0
    while i < len(lines):
        ln = lines[i]

        m = re.match(r"^## No\.(\d+)（(.+?)）\s*$", ln)
        if m:
            target = new_target("main", {"no": m.group(1), "type": m.group(2)})
            i += 1
            continue

        m = re.match(r"^### 第(\d+)小题（(.+?)）\s*$", ln)
        if m:
            target = new_target("sub", {"no": m.group(1), "type": m.group(2)})
            i += 1
            continue

        if ln.strip() == "**题干材料**":
            mode = "material"
            i += 1
            continue
        if ln.strip() == "**题干**":
            mode = "stem"
            i += 1
            continue
        if ln.strip() == "**选项**":
            mode = "options"
            i += 1
            continue

        if target is not None:
            if mode == "options":
                m = re.match(r"^- (.+)$", ln)
                if m:
                    target["options"].append(m.group(1))
                    i += 1
                    continue
                if ln.strip() == "":
                    i += 1
                    continue
                # 选项区出现的非列表行（罕见）归入题干
                target["stem"].append(ln)
                i += 1
                continue
            # material / stem：OCR 引用行与普通行
            target[mode].append(ln)
        i += 1

    html = []
    for q in questions:
        html.extend(render_question(q))
        for s in q.pop("subs", []):
            html.extend(render_question(s))
    return "\n".join(html)


def main():
    # 清空重建 docs/cfa
    if os.path.exists(DOCS_CFA):
        shutil.rmtree(DOCS_CFA)
    os.makedirs(DOCS_CFA)

    matrix, source_totals, all_books = {}, {}, set()

    for dname, code, label in SOURCES:
        src_dir = os.path.join(BANK, dname)
        out_dir = os.path.join(DOCS_CFA, dname)
        os.makedirs(out_dir)
        source_totals[code] = 0

        for f in sorted(os.listdir(src_dir)):
            if not f.endswith(".md"):
                continue
            m = re.search(r"_[A-Z]+\.md$", f)
            book = f[: m.start()] if m else f[:-3]
            all_books.add(book)
            text = open(os.path.join(src_dir, f), encoding="utf-8").read()
            n = count_questions(text)
            source_totals[code] += n

            slug = slugify(book, code)
            body = text.split("\n", 1)[1].lstrip("\n") if text.startswith("# ") else text
            body = re.sub(r"^> .*导出：.*\n+", "", body)
            rendered = parse_and_render(body)

            front = (
                "---\n"
                f'title: "{BOOK_LABELS.get(book, book)}（{label}）"\n'
                f"source: {code}\n"
                f'book: "{book}"\n'
                f"questions: {n}\n"
                "---\n\n"
            )
            with open(os.path.join(out_dir, slug + ".md"), "w", encoding="utf-8") as fp:
                fp.write(front + rendered + "\n")

            matrix.setdefault(book, {})[code] = {"slug": slug, "count": n}
        print(f"{dname} ({code}): {source_totals[code]} questions")

    # ---- 各来源 index.md ----
    for dname, code, label in SOURCES:
        books = sorted(
            (b for b in all_books if code in matrix.get(b, {})),
            key=lambda b: BOOK_ORDER.index(b) if b in BOOK_ORDER else 99,
        )
        lines = [
            "---",
            f'title: "CFA 题库 · {label}"',
            "---",
            "",
            f"# CFA 题库 · {label}",
            "",
            f"> 共 **{source_totals[code]}** 题，按大类分文件。",
            "",
        ]
        for b in books:
            info = matrix[b][code]
            lines.append(f"- [{BOOK_LABELS.get(b, b)}](/cfa/{dname}/{info['slug']})（{info['count']} 题）")
        lines.append("")
        open(os.path.join(DOCS_CFA, dname, "index.md"), "w", encoding="utf-8").write("\n".join(lines))

    # ---- 总览矩阵 docs/cfa/index.md ----
    ordered_books = [b for b in BOOK_ORDER if b in all_books] + sorted(
        b for b in all_books if b not in BOOK_ORDER
    )
    codes = [c for _, c, _ in SOURCES]
    total = sum(source_totals.values())
    dir_of = {c_: d for d, c_, _ in SOURCES}

    lines = [
        "---",
        'title: "CFA 题库"',
        "outline: deep",
        "---",
        "",
        "# CFA Level III 题库",
        "",
        f"> 来源：品职 PZ Academy 导出（2026-09-13）｜共 **{total}** 题、**{len(all_books)}** 个大类。Case 题组 = 题干材料 + 逐个小题。",
        "> 按来源浏览：",
    ]
    for dname, code, label in SOURCES:
        lines.append(f"> [{label}](/cfa/{dname}/)（{source_totals[code]} 题）｜")
    lines.append("")
    lines.append("## 来源 × 大类矩阵")
    lines.append("")
    header = "| 大类 | " + " | ".join(c for c in codes) + " |"
    sep = "| --- |" + " --- |" * len(codes)
    lines += [header, sep]
    for b in ordered_books:
        row = [BOOK_LABELS.get(b, b)]
        for c in codes:
            cell = matrix.get(b, {}).get(c)
            row.append(f"[{cell['count']}](/cfa/{dir_of[c]}/{cell['slug']})" if cell else "—")
        lines.append("| " + " | ".join(row) + " |")
    row = ["**合计**"] + [f"**{source_totals[c]}**" for c in codes]
    lines.append("| " + " | ".join(row) + " |")
    lines.append("")

    open(os.path.join(DOCS_CFA, "index.md"), "w", encoding="utf-8").write("\n".join(lines))
    print(f"\nTotal: {total} questions, {len(all_books)} books -> {DOCS_CFA}")


if __name__ == "__main__":
    main()
