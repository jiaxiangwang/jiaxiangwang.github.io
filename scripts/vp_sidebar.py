#!/usr/bin/env python3
"""Generate docs/.vitepress/sidebar.ts from the docs directory tree + frontmatter titles."""
import os
import re
import json

DOCS = "/Users/jiaxiang/Documents/code/blog/docs"
SECTIONS = [
    ("cfa", "CFA 2027"),
    ("front-end", "前端"),
    ("back-end", "后端"),
    ("machine-learning", "机器学习"),
    ("other", "其他"),
]

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


def read_sidebar_title(md_path):
    text = open(md_path).read(2048)
    match = re.search(r'^sidebarTitle:\s*"(.+)"$', text, re.M)
    return match.group(1) if match else read_title(md_path)


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


def topic_sidebars(group, entry, content_map):
    root = os.path.join(DOCS, "cfa", entry["id"])
    base = "/cfa/" + entry["id"]
    review, questions = [], []
    for module in content_map["modules"]:
        name = module["directory"]
        pages = [{"text": "Overview", "link": f"{base}/review/{name}/"}]
        pages.extend({"text": read_sidebar_title(os.path.join(DOCS, step["review"].lstrip("/") + ".md")),
                      "link": step["review"]} for step in module["steps"])
        pages.append({"text": "Module Review", "link": f"{base}/review/{name}/review"})
        review.append({"text": module["name"], "collapsed": True, "items": pages})
        questions.append({
            "text": module["name"],
            "link": f'{base}/questions/#module-{module["directory"]}',
            "collapsed": True,
            "items": [
                {
                    "text": read_sidebar_title(os.path.join(DOCS, step["review"].lstrip("/") + ".md")),
                    "link": f'{base}/questions/#concept-{step["concept"]}',
                }
                for step in module["steps"] if step["questions"]
            ],
        })
    title = group["name"] + " → " + entry["name"]
    sources = [{"text": "Sources & Coverage", "link": base + "/sources"}]
    if os.path.exists(os.path.join(root, "skip-review.md")):
        sources.append({"text": "跳过记录复核", "link": base + "/skip-review"})
    utilities = {"text": "来源与核验", "collapsed": True, "items": sources}
    overview = {"text": title, "link": base + "/", "items": [
        {"text": "Learning Map", "link": base + "/"},
        {"text": "Learning Modules", "collapsed": False, "items": [
            {"text": module["name"], "link": f'{base}/review/{module["directory"]}/'}
            for module in content_map["modules"]
        ]},
        {"text": "Topic Review", "link": base + "/topic-review"},
        {"text": "Question Bank →", "link": base + "/questions/"},
    ]}
    course = {"text": title, "link": base + "/", "items": [
        {"text": "Learning Map", "link": base + "/"},
        {"text": "Question Bank →", "link": base + "/questions/"},
        {"text": "Topic Review", "link": base + "/topic-review"},
    ]}
    bank = {"text": title, "link": base + "/questions/", "items": [
        {"text": "Practice by Concept", "link": base + "/questions/"},
        {"text": "Review Course →", "link": base + "/"},
        {"text": "Topic Review", "link": base + "/topic-review"},
    ]}
    return {
        base + "/": [overview, utilities],
        base + "/review/": [course, *review, utilities],
        base + "/questions/": [bank, *questions, utilities],
    }


def cfa_sidebars():
    with open(os.path.join(DOCS, "cfa", "catalog.json")) as source:
        catalog = json.load(source)
    center = {"text": "CFA 2027 · 学习中心", "link": "/cfa/", "items": [
        {"text": "Review Course", "link": "/cfa/review/"},
        {"text": "Question Bank", "link": "/cfa/questions/"},
    ]}
    hubs = {mode: [center] for mode in ["all", "review", "questions"]}
    routes = {}
    for group in catalog["groups"]:
        published = []
        for entry in group["entries"]:
            path = os.path.join(DOCS, "cfa", entry["id"], "content-map.json")
            if not os.path.exists(path):
                continue
            with open(path) as source:
                content_map = json.load(source)
            published.append(entry)
            routes.update(topic_sidebars(group, entry, content_map))
        for mode in hubs:
            hubs[mode].append({"text": group["name"], "link": "/cfa/#" + group["id"], "items": [
                {"text": entry["name"], "link": "/cfa/" + entry["id"] + ("/questions/" if mode == "questions" else "/")}
                for entry in published
            ]})
    routes.update({"/cfa/": hubs["all"], "/cfa/review/": hubs["review"], "/cfa/questions/": hubs["questions"]})
    return routes


def groups_for(key):
    d = os.path.join(DOCS, key)
    if not os.path.isdir(d):
        return []
    names = os.listdir(d)
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
        if key == "cfa":
            for route, groups in cfa_sidebars().items():
                lines.append(f"  '{route}': {fmt(groups, 1)},")
                print(f"{route}: {len(groups)} groups")
            continue
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
