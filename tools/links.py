#!/usr/bin/env python3
"""Generate one-click install links for the README.

Each link opens app.diagrams.net with a library loaded straight from the
jsDelivr CDN (pinned to a release tag). Multiple libraries are joined with
`;U` in the `clibs` URL parameter, which draw.io splits and loads in order.

Usage:
  python3 tools/links.py                          # huaweicloud-latam @ latest tag
  python3 tools/links.py --repo user/repo --tag v4.0
  python3 tools/links.py --format markdown         # README table
  python3 tools/links.py --format json             # machine-readable
"""
import argparse
import json
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIBRARIES = ROOT / "src" / "libraries.json"

APP = "https://app.diagrams.net/?splash=0&libs=0&clibs="


def latest_tag() -> str:
    import subprocess

    try:
        return subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            capture_output=True,
            text=True,
            check=True,
            cwd=ROOT,
        ).stdout.strip() or "main"
    except subprocess.CalledProcessError:
        return "main"


def build(repo: str, tag: str) -> dict:
    libs = json.loads(LIBRARIES.read_text(encoding="utf-8"))
    entries = []
    for out_name in sorted(libs):
        display = out_name.removeprefix("HWC ").removesuffix(".xml").strip()
        cdn = f"https://cdn.jsdelivr.net/gh/{repo}@{tag}/color/{out_name}"
        entries.append(
            {
                "file": out_name,
                "name": display,
                "cdn": cdn,
                "oneclick": APP + "U" + urllib.parse.quote(cdn, safe=""),
            }
        )
    # The all-in-one library: every shape in a single file. Not part of the
    # install-all join, which loads the per-category libraries instead.
    aio_cdn = f"https://cdn.jsdelivr.net/gh/{repo}@{tag}/all-in-one/HWC%20All-in-One%20(color).xml"
    all_in_one = {
        "file": "HWC All-in-One (color).xml",
        "name": "All-in-One (color)",
        "cdn": aio_cdn,
        "oneclick": APP + "U" + urllib.parse.quote(aio_cdn, safe=""),
    }
    install_all = APP + ";".join("U" + urllib.parse.quote(e["cdn"], safe="") for e in entries)
    return {"repo": repo, "tag": tag, "libraries": entries, "all_in_one": all_in_one, "install_all": install_all}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="huaweicloud-latam/drawio-libraries")
    ap.add_argument("--tag", default=None)
    ap.add_argument("--format", choices=["markdown", "json", "plain"], default="plain")
    args = ap.parse_args()

    tag = args.tag or latest_tag()
    data = build(args.repo, tag)

    if args.format == "json":
        json.dump(data, sys.stdout, indent=2)
        print()
        return

    if args.format == "markdown":
        print("| Library | One-click install |")
        print("|---|---|")
        for e in data["libraries"]:
            print(f"| {e['name']} | [Add to draw.io]({e['oneclick']}) |")
        aio = data["all_in_one"]
        print(f"| {aio['name']} | [Add to draw.io]({aio['oneclick']}) |")
        print()
        print(f"[**Install all libraries at once**]({data['install_all']})")
        return

    for e in data["libraries"]:
        print(f"{e['name']}\n  CDN:     {e['cdn']}\n  OneClick: {e['oneclick']}")
    print(f"\nInstall all:\n  {data['install_all']}")


if __name__ == "__main__":
    main()
