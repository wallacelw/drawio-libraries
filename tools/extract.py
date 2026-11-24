#!/usr/bin/env python3
"""Extract icons and groups from the draw.io XML libraries into a source tree.

Reads color/*.xml (as described by src/libraries.json) and writes:
  src/icons/<Category>/<Title>.svg   decoded SVG bytes, one file per icon
  src/manifest.json                  ordered per-category icon metadata
  src/groups/<Title>.xml             unescaped mxGraphModel XML blobs
  src/groups/manifest.json           ordered group metadata
"""
import base64
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLOR = ROOT / "color"
SRC = ROOT / "src"
LIBRARIES = SRC / "libraries.json"

# Deliberate title typo corrections (original -> corrected).
TITLE_FIXES = {
    "Cloud Application Egine (CAE)": "Cloud Application Engine (CAE)",
    "Log Tank Servce (LTS)": "Log Tank Service (LTS)",
    "Data Encryption Worshop (DEW)": "Data Encryption Workshop (DEW)",
    "FGPA Accelerated Cloud Server (FACS)": "FPGA Accelerated Cloud Server (FACS)",
}

_UNSAFE = set('/\\:*?"<>|')


def sanitize(title: str) -> str:
    """Turn a title into a filesystem-safe filename stem, keeping spaces/parens."""
    out = []
    for ch in title:
        if ch in _UNSAFE or ord(ch) < 32:
            out.append("-")
        else:
            out.append(ch)
    return "".join(out).strip() or "untitled"


def unescape_html(text: str) -> str:
    """Decode one level of HTML/XML escaping (&amp; last so &amp;lt; -> &lt;)."""
    return (
        text.replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", '"')
        .replace("&amp;", "&")
    )


def load_library(path: Path):
    raw = path.read_text(encoding="utf-8")
    start = raw.index("[")
    end = raw.rindex("]")
    return json.loads(raw[start : end + 1])


def extract_icons(out_name: str, category: str):
    entries = load_library(COLOR / out_name)
    outdir = SRC / "icons" / category
    outdir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for entry in entries:
        title = unescape_html(entry["title"])
        title = TITLE_FIXES.get(title, title)
        filename = sanitize(title) + ".svg"
        b64 = entry["data"].split(",", 1)[1]
        (outdir / filename).write_bytes(base64.b64decode(b64))
        manifest.append(
            {
                "title": title,
                "file": filename,
                "w": entry["w"],
                "h": entry["h"],
                "aspect": entry["aspect"],
            }
        )
    return manifest


def extract_groups(out_name: str):
    entries = load_library(COLOR / out_name)
    outdir = SRC / "groups"
    outdir.mkdir(parents=True, exist_ok=True)
    manifest = []
    for order, entry in enumerate(entries, start=1):
        title = unescape_html(entry["title"])
        filename = sanitize(title) + ".xml"
        xmltext = unescape_html(entry["xml"])
        (outdir / filename).write_text(xmltext, encoding="utf-8")
        manifest.append(
            {
                "title": title,
                "filename": filename,
                "w": entry["w"],
                "h": entry["h"],
                "order": order,
            }
        )
    return manifest


def main():
    libs = json.loads(LIBRARIES.read_text(encoding="utf-8"))
    manifest = {"title_fixes": TITLE_FIXES, "categories": {}}
    groups_manifest = []

    for out_name, spec in libs.items():
        if spec["type"] == "icons":
            manifest["categories"][spec["category"]] = extract_icons(
                out_name, spec["category"]
            )
        elif spec["type"] == "groups":
            groups_manifest = extract_groups(out_name)
        else:
            sys.exit(f"unknown library type: {spec['type']}")

    (SRC / "manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (SRC / "groups" / "manifest.json").write_text(
        json.dumps(groups_manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Extracted {sum(len(v) for v in manifest['categories'].values())} icons "
          f"in {len(manifest['categories'])} categories and {len(groups_manifest)} groups.")


if __name__ == "__main__":
    main()
