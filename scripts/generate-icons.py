#!/usr/bin/env python3
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
OWNER = "ZzQiao7"
REPO = "surge-icons"
BRANCH = "main"

pngs = sorted(
    (p for p in ROOT.rglob("*.png") if ".git" not in p.parts),
    key=lambda p: p.relative_to(ROOT).as_posix().lower(),
)

icons = []
for path in pngs:
    rel = path.relative_to(ROOT).as_posix()
    icons.append({
        "name": path.stem,
        "category": "ZzQiao7",
        "url": f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/{quote(rel, safe='/')}",
    })

data = {
    "name": "ZzQiao7 Surge Icons",
    "description": "Custom policy group icons for Surge",
    "icons": icons,
}

(ROOT / "surge-icon.json").write_text(
    json.dumps(data, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)
print(f"Generated surge-icon.json with {len(icons)} icons.")
