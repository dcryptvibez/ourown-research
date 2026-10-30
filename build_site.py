#!/usr/bin/env python3
"""Render the markdown deliverables into a static site under docs/ for GitHub Pages."""
import html
import re
import pathlib

import markdown

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "docs"

PAGES = [
    ("README.md", "Research Plan"),
    ("01-executive-research-summary.md", "1. Executive Summary"),
    ("02-business-and-market-research-report.md", "2. Business & Market Report"),
    ("03-market-sizing-model.md", "3. Market Sizing (TAM/SAM/SOM)"),
    ("04-competitor-intelligence-database.md", "4. Competitor Database"),
    ("05-supplier-research-pack.md", "5. Supplier Research Pack"),
    ("06-unit-economics-workbook-spec.md", "6. Unit Economics Workbook"),
    ("07-swot-tows.md", "7. SWOT & TOWS"),
    ("08-technical-operational-readiness.md", "8. Tech & Ops Readiness"),
    ("09-regulatory-compliance-memo.md", "9. Regulatory & Compliance"),
    ("10-ourown-whitepaper-draft.md", "10. Whitepaper Draft"),
    ("11-30-day-validation-plan.md", "11. 30-Day Validation Plan"),
    ("12-assumptions-evidence-gap-register.md", "12. Assumptions & Gaps Register"),
    ("13-decision-framework.md", "13. Decision Framework"),
]

CSS = """
:root{--bg:#f7f6f3;--panel:#fff;--ink:#1c1b19;--muted:#6b675f;--accent:#0b6b4f;--line:#e4e1da;--code:#f0efea}
*{box-sizing:border-box}
body{margin:0;font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;color:var(--ink);background:var(--bg)}
.layout{display:flex;min-height:100vh}
nav{width:290px;flex:0 0 290px;background:#12211c;color:#dfe7e3;padding:22px 18px;position:sticky;top:0;height:100vh;overflow-y:auto}
nav .brand{font-size:19px;font-weight:700;color:#fff;letter-spacing:.2px}
nav .sub{font-size:12px;color:#8fb3a6;margin:4px 0 18px}
nav a{display:block;color:#c9d8d2;text-decoration:none;padding:7px 10px;border-radius:7px;font-size:14px;margin-bottom:2px}
nav a:hover{background:#1d332b;color:#fff}
nav a.active{background:var(--accent);color:#fff}
main{flex:1;padding:38px 46px 80px;max-width:1000px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:30px 36px;box-shadow:0 1px 3px rgba(0,0,0,.04)}
h1{font-size:30px;margin:0 0 6px;line-height:1.25}
h2{font-size:22px;margin:34px 0 10px;padding-top:18px;border-top:1px solid var(--line)}
h3{font-size:17px;margin:24px 0 8px}
h4{font-size:15px;margin:18px 0 6px;color:var(--muted)}
p,li{font-size:15.5px}
a{color:var(--accent)}
blockquote{margin:14px 0;padding:10px 16px;border-left:4px solid var(--accent);background:#eef4f1;color:#33443d;border-radius:0 8px 8px 0}
table{border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;display:block;overflow-x:auto}
th,td{border:1px solid var(--line);padding:8px 11px;text-align:left;vertical-align:top}
th{background:#eef1ee;font-weight:600;white-space:nowrap}
tr:nth-child(even) td{background:#fafaf8}
code{background:var(--code);padding:2px 5px;border-radius:4px;font-size:13.5px;font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
pre{background:#12211c;color:#e7efe9;padding:16px;border-radius:10px;overflow-x:auto}
pre code{background:none;color:inherit;padding:0}
hr{border:0;border-top:1px solid var(--line);margin:28px 0}
.pager{display:flex;justify-content:space-between;gap:12px;margin-top:30px}
.pager a{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:10px 16px;text-decoration:none;font-size:14px}
.pager a:hover{border-color:var(--accent)}
.crumb{color:var(--muted);font-size:13px;margin-bottom:14px}
@media(max-width:860px){.layout{flex-direction:column}nav{width:100%;flex:none;height:auto;position:static}main{padding:22px 16px 60px}.card{padding:20px 16px}}
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — OurOwn Market Research</title>
<style>{css}</style>
</head>
<body>
<div class="layout">
<nav>
  <div class="brand">OurOwn Market Research</div>
  <div class="sub">Kano grocery e-commerce · evidence-based validation · Oct 2026</div>
  {navlinks}
</nav>
<main>
  <div class="crumb">OurOwn research package · {label}</div>
  <div class="card">
    {body}
    <div class="pager">{prev}{next}</div>
  </div>
</main>
</div>
</body>
</html>
"""


def slug(fname: str) -> str:
    return "index.html" if fname == "README.md" else fname.replace(".md", ".html")


def build() -> None:
    OUT.mkdir(exist_ok=True)
    md = markdown.Markdown(extensions=["tables", "toc", "fenced_code"])
    navlinks = "\n  ".join(
        f'<a href="{slug(f)}">{html.escape(label)}</a>' for f, label in PAGES
    )
    for i, (fname, label) in enumerate(PAGES):
        src = ROOT / fname
        text = src.read_text(encoding="utf-8")
        md.reset()
        body = md.convert(text)
        active_nav = "\n  ".join(
            f'<a class="{"active" if f == fname else ""}" href="{slug(f)}">{html.escape(lab)}</a>'
            for f, lab in PAGES
        )
        prev = (
            f'<a href="{slug(PAGES[i-1][0])}">← {html.escape(PAGES[i-1][1])}</a>'
            if i > 0 else '<a href="index.html">← Research Plan</a>'
        )
        nxt = (
            f'<a href="{slug(PAGES[i+1][0])}">{html.escape(PAGES[i+1][1])} →</a>'
            if i + 1 < len(PAGES) else '<a href="index.html">Back to start →</a>'
        )
        out = TEMPLATE.format(
            title=html.escape(label),
            css=CSS,
            navlinks=active_nav,
            label=html.escape(label),
            body=body,
            prev=prev,
            next=nxt,
        )
        (OUT / slug(fname)).write_text(out, encoding="utf-8")
        print("built", slug(fname))


if __name__ == "__main__":
    build()
