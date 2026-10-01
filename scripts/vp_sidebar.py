#!/usr/bin/env python3
"""Generate docs/.vitepress/sidebar.ts from the docs directory tree + frontmatter titles."""
import os
import re

DOCS = "/Users/jiaxiang/Documents/code/blog/docs"
SECTIONS = [
    ("cfa", "CFA 题库"),
    ("front-end", "前端"),
    ("back-end", "后端"),
    ("machine-learning", "机器学习"),
    ("other", "其他"),
]

# cfa 分区：Review/Practice Topic 与已存在的来源题库共存。
CFA_SOURCE_ORDER = ["asset-allocation", "Other"]


def read_title(md_path):
    text = open(md_path).read(2048)
    m = re.search(r"^title:\s*(.+)$", text, re.M)
    if m:
        t = m.group(1).strip()
        if len(t) >= 2 and t[0] == t[-1] and t[0] in "\"'":
            t = t[1:-1]
        return t
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else os.path.basename(md_path)


def items_for(dir_path):
    items = []
    for root, dirs, files in os.walk(dir_path):
        dirs.sort()
        for f in sorted(files):
            if not f.endswith(".md") or f == "index.md":
                continue
            full = os.path.join(root, f)
            rel = os.path.relpath(full, DOCS)
            link = "/" + rel[:-3]
            items.append({"text": read_title(full), "link": link})
    return items


def asset_allocation_group():
    root = os.path.join(DOCS, "cfa", "asset-allocation")
    base = "/cfa/asset-allocation"
    review = []
    review_root = os.path.join(root, "review")
    for name in sorted(os.listdir(review_root)):
        directory = os.path.join(review_root, name)
        if not os.path.isdir(directory):
            continue
        pages = [{"text": "Overview", "link": f"{base}/review/{name}/"}]
        for filename in sorted(os.listdir(directory)):
            if filename.startswith("step-") and filename.endswith(".md"):
                pages.append({"text": read_title(os.path.join(directory, filename)),
                              "link": f"{base}/review/{name}/{filename[:-3]}"})
        pages.append({"text": "Module Review", "link": f"{base}/review/{name}/review"})
        title = read_title(os.path.join(directory, "index.md")).replace(" — Overview", "")
        review.append({"text": title, "collapsed": True, "items": pages})
    questions = items_for(os.path.join(root, "questions"))
    return {"text": "CORE → Asset Allocation", "link": base + "/", "items": [
        {"text": "Learning Map", "link": base + "/"},
        {"text": "Review Course", "collapsed": False, "items": review},
        {"text": "Topic Review", "link": base + "/topic-review"},
        {"text": "Question Bank", "link": base + "/questions/", "collapsed": True, "items": questions},
        {"text": "Sources & Coverage", "link": base + "/sources"},
    ]}


def groups_for(key):
    d = os.path.join(DOCS, key)
    if not os.path.isdir(d):
        return []
    names = os.listdir(d)
    if key == "cfa":
        names = [n for n in CFA_SOURCE_ORDER if n in names]
    else:
        names = sorted(n for n in names if os.path.isdir(os.path.join(d, n)))
    groups = []
    for name in names:
        if key == "cfa" and name == "asset-allocation":
            groups.append(asset_allocation_group())
            continue
        sd = os.path.join(d, name)
        if not os.path.isdir(sd):
            continue
        index_md = os.path.join(sd, "index.md")
        if os.path.exists(index_md):
            groups.append({
                "text": read_title(index_md),
                "link": f"/{key}/{name}/",
                "collapsed": False,
                "items": items_for(sd),
            })
        else:
            groups.append({
                "text": name,
                "collapsed": False,
                "items": items_for(sd),
            })
    return groups


def fmt(obj, indent=0):
    pad = "  " * indent
    if isinstance(obj, bool):
        return "true" if obj else "false"
    if isinstance(obj, dict):
        parts = [f"{pad}  {k}: {fmt(v, indent + 1)}" for k, v in obj.items()]
        return "{\n" + ",\n".join(parts) + f"\n{pad}}}"
    if isinstance(obj, list):
        if not obj:
            return "[]"
        parts = [f"{pad}  {fmt(v, indent + 1)}" for v in obj]
        return "[\n" + ",\n".join(parts) + f"\n{pad}]"
    return '"' + str(obj).replace('"', '\\"') + '"'


def main():
    lines = []
    for key, label in SECTIONS:
        groups = groups_for(key)
        # cfa：每个大类（来源目录）独立侧边栏 key；/cfa/ 总览页保留聚合侧边栏
        if key == "cfa" and groups:
            for g in groups:
                k = g["link"]  # 形如 /cfa/Other/
                lines.append(f"  '{k}': {fmt([g], 1)},")
                print(f"{k}: 1 group, {len(g['items'])} pages")
        lines.append(f"  '/{key}/': {fmt(groups, 1)},")
        total = sum(len(g["items"]) for g in groups)
        print(f"{key} ({label}): {len(groups)} groups, {total} pages")
    out = "// AUTO-GENERATED — do not edit by hand.\n"
    out += "import type { DefaultTheme } from 'vitepress'\n\n"
    out += "export const sidebar: Record<string, DefaultTheme.SidebarItem[]> = {\n"
    out += "\n".join(lines) + "\n}\n"
    with open(os.path.join(DOCS, ".vitepress", "sidebar.ts"), "w") as fp:
        fp.write(out)
    print("sidebar.ts written")


if __name__ == "__main__":
    main()
