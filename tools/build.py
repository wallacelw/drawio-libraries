#!/usr/bin/env python3
"""Rebuild the color/*.xml draw.io libraries from the src/ source tree.

Usage:
  python3 tools/build.py          # write all libraries
  python3 tools/build.py --check  # diff generated vs on-disk, exit nonzero on drift
"""
import base64
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLOR = ROOT / "color"
SRC = ROOT / "src"
LIBRARIES = SRC / "libraries.json"
MANIFEST = SRC / "manifest.json"
GROUPS_MANIFEST = SRC / "groups" / "manifest.json"


def escape_html(text: str) -> str:
    """Apply the same one-level HTML escaping draw.io uses (& first)."""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def build_icons(out_name: str, category: str, manifest: dict) -> str:
    entries = manifest["categories"][category]
    lines = []
    for entry in entries:
        b64 = base64.b64encode((SRC / "icons" / category / entry["file"]).read_bytes())
        data = "data:image/svg+xml;base64," + b64.decode("ascii")
        obj = {
            "data": data,
            "w": entry["w"],
            "h": entry["h"],
            "title": escape_html(entry["title"]),
            "aspect": entry["aspect"],
        }
        lines.append(json.dumps(obj, separators=(",", ":"), ensure_ascii=False))
    return "<mxlibrary>[\n" + ",\n".join(lines) + "\n]</mxlibrary>\n"


def build_groups() -> str:
    manifest = sorted(
        json.loads(GROUPS_MANIFEST.read_text(encoding="utf-8")),
        key=lambda g: g["order"],
    )
    arr = []
    for g in manifest:
        xmltext = (SRC / "groups" / g["filename"]).read_text(encoding="utf-8")
        arr.append(
            {
                "xml": escape_html(xmltext),
                "w": g["w"],
                "h": g["h"],
                "aspect": "fixed",
                "title": g["title"],
            }
        )
    return "<mxlibrary>" + json.dumps(arr, indent=2, ensure_ascii=False) + "</mxlibrary>"


def generate(libs: dict, manifest: dict) -> dict:
    outputs = {}
    for out_name, spec in libs.items():
        if spec["type"] == "icons":
            outputs[COLOR / out_name] = build_icons(out_name, spec["category"], manifest)
        elif spec["type"] == "groups":
            outputs[COLOR / out_name] = build_groups()
        else:
            sys.exit(f"unknown library type: {spec['type']}")
    return outputs


def main():
    check = "--check" in sys.argv[1:]
    libs = json.loads(LIBRARIES.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    outputs = generate(libs, manifest)

    drift = []
    for path, content in outputs.items():
        if check:
            existing = path.read_bytes() if path.exists() else b""
            if existing != content.encode("utf-8"):
                drift.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content.encode("utf-8"))

    if check:
        if drift:
            print("DRIFT detected in:")
            for name in drift:
                print("  " + name)
            sys.exit(1)
        print(f"OK: {len(outputs)} libraries match on-disk bytes.")
    else:
        print(f"Wrote {len(outputs)} libraries to {COLOR}/")


if __name__ == "__main__":
    main()
