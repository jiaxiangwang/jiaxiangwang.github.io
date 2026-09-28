#!/usr/bin/env python3
"""One-off: extract VuePress 1.x built HTML back to Markdown for VitePress."""
import os
import re
import shutil
from bs4 import BeautifulSoup, NavigableString, Tag
from markdownify import MarkdownConverter

SRC = "/Users/jiaxiang/Documents/code/blog"
OUT = os.path.join(SRC, "docs")
SKIP_FILES = {"index.html", "404.html"}

CODE_BLOCKS = {}  # placeholder -> markdown fenced block
_container_converters = {}


class ContentConverter(MarkdownConverter):
    """markdownify with small tweaks for VuePress SSR output."""

    def convert_a(self, el, text, parent_tags=None):
        # Drop VuePress header anchors (#) and empty links
        cls = el.get("class") or []
        if "header-anchor" in cls:
            return ""
        return super().convert_a(el, text, parent_tags)

    def convert_p(self, el, text, parent_tags=None):
        cls = el.get("class") or []
        if "custom-block-title" in cls:
            return ""  # handled by container wrapper
        return super().convert_p(el, text, parent_tags)

    def convert_div(self, el, text, parent_tags=None):
        cls = el.get("class") or []
        for kind in ("tip", "warning", "danger", "details", "info"):
            if kind in cls and "custom-block" in cls:
                title_el = el.select_one("p.custom-block-title")
                title = title_el.get_text(strip=True) if title_el else kind
                inner = el
                if title_el is not None:
                    inner_html = "".join(
                        str(c) if not isinstance(c, NavigableString) else str(c)
                        for c in el.contents
                        if not (isinstance(c, Tag) and c is title_el)
                    )
                    inner = BeautifulSoup(inner_html, "lxml")
                body = self.process_tag(inner, parent_tags=parent_tags).strip()
                fence = ":::" if kind != "details" else "::: details"
                return f"\n{fence} {title}\n{body}\n{fence}\n"
        return text  # unwrap other divs

    def convert_img(self, el, text, parent_tags=None):
        src = el.get("src", "")
        alt = el.get("alt", "")
        return f"![{alt}]({src})"


def md(el):
    return ContentConverter(heading_style="ATX", bullets="-").convert_soup(el)


def extract_code_blocks(content: Tag):
    """Replace VuePress code block divs with placeholders; return mapping."""
    blocks = {}
    for i, div in enumerate(content.select("div[class*=language-]")):
        classes = div.get("class") or []
        lang = next((c.split("language-")[1] for c in classes if c.startswith("language-")), "")
        code = div.find("code")
        text = code.get_text() if code else div.get_text()
        key = f"@@CODEBLOCK{i}@@"
        blocks[key] = f"\n```{lang}\n{text.rstrip()}\n```\n"
        div.replace_with(NavigableString(key))
    return blocks


def clean(content: Tag):
    for sel in [".header-anchor", ".line-numbers-wrapper", "script", "style"]:
        for el in content.select(sel):
            el.decompose()


def rewrite_links(soup: Tag, valid_paths):
    """Rewrite internal .html links to VitePress-friendly paths."""
    for a in soup.select("a[href]"):
        href = a.get("href", "")
        if not href.startswith("/"):
            continue
        href = re.sub(r"\.html($|#.*)$", r"\1", href)
        href = re.sub(r"/index($|#.*|$)", "/\\1", href)
        if href.rstrip("#") and not href.rstrip("#").split("#")[0].rstrip("/") + "/" or True:
            pass
        a["href"] = href


NAME_FIXUPS = {
    "css": "CSS", "dart": "Dart", "graphql": "GraphQL", "javascript": "JavaScript",
    "typescript": "TypeScript", "vue": "Vue", "react": "React", "rxjs": "RxJS",
    "flutter": "Flutter", "webassembly": "WebAssembly", "webcomponents": "Web Components",
    "micro-frontends": "Micro Frontends", "http": "HTTP", "nginx": "Nginx",
    "mongodb": "MongoDB", "nodejs": "Node.js", "node": "Node.js", "gin": "Gin",
    "spring": "Spring", "express": "Express", "flask": "Flask", "koa": "Koa",
    "go": "Go", "java": "Java", "python": "Python", "javascript-in-html": "JavaScript in HTML",
    "language-basics": "Language Basics", "what-is-javascript": "What is JavaScript",
    "deep": "深度学习", "array": "Array",
}


def prettify(name: str) -> str:
    low = name.lower()
    if low in NAME_FIXUPS:
        return NAME_FIXUPS[low]
    return " ".join(w.capitalize() for w in re.split(r"[-_]", name) if w)


def page_title(soup, content, path):
    h1 = content.find("h1") if content else None
    if h1:
        t = h1.get_text(strip=True)
        if t and t.lower() != "test":
            return t
    t = soup.title.get_text() if soup.title else ""
    t = re.sub(r"\s*\|\s*Jasper的个人笔记\s*$", "", t)
    if t and t not in ("Jasper的个人笔记", "test"):
        return t
    base = os.path.splitext(os.path.basename(path))[0]
    if base == "index":
        return prettify(os.path.basename(os.path.dirname(path)))
    return prettify(base)


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    html_files = []
    for root, dirs, files in os.walk(SRC):
        dirs[:] = [d for d in dirs if d not in (".git", ".workbuddy", "node_modules", "docs", "assets")]
        for f in files:
            if f.endswith(".html"):
                rel = os.path.relpath(os.path.join(root, f), SRC)
                if rel not in SKIP_FILES:
                    html_files.append(rel)
    html_files.sort()
    print(f"{len(html_files)} content pages")

    valid = set()
    for rel in html_files:
        p = rel[:-5] if rel.endswith(".html") else rel  # .html -> ''
        p = "/index" if p == "index" else p
        valid.add(p)

    pages = []
    for rel in html_files:
        src_path = os.path.join(SRC, rel)
        out_rel = rel[:-5] + ".md"
        soup = BeautifulSoup(open(src_path, errors="ignore").read(), "lxml")
        content = soup.select_one(".theme-default-content")
        if content is None:
            print(f"!! no content: {rel}")
            continue

        blocks = extract_code_blocks(content)
        clean(content)
        title = page_title(soup, content, rel)
        rewrite_links(content, valid)

        body = md(content)
        for k, v in blocks.items():
            body = body.replace(k, v)
        body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"

        front = f"---\ntitle: {title}\n---\n\n" if title else ""
        os.makedirs(os.path.dirname(os.path.join(OUT, out_rel)), exist_ok=True)
        with open(os.path.join(OUT, out_rel), "w") as fp:
            fp.write(front + body)
        pages.append((out_rel, title))

    for p, t in pages:
        print(f"  {p}  [{t}]")


if __name__ == "__main__":
    main()
