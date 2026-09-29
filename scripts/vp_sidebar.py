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

# cfa 分区：来源目录的自定义顺序（与 vp_import_cfa.py 的 SOURCES 一致；当前仅保留 Other）
CFA_SOURCE_ORDER = ["Other"]


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


def groups_for(key):
    d = os.path.join(DOCS, key)
    if not os.path.isdir(d):
        return []
    names = os.listdir(d)
    if key == "cfa":
        names = [n for n in CFA_SOURCE_ORDER if n in names] + sorted(
            n for n in names if n not in CFA_SOURCE_ORDER and os.path.isdir(os.path.join(d, n))
        )
    else:
        names = sorted(n for n in names if os.path.isdir(os.path.join(d, n)))
    groups = []
    for name in names:
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
