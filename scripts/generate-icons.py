#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
OWNER = "ZzQiao7"
REPO = "goodgood"
BRANCH = "main"

COUNTRY_PREFIXES = ("flag-",)

# All non-country icons share one alphabetical list, including new/custom icons.
def group_for(stem):
    return "99 国家图标" if stem.lower().startswith(COUNTRY_PREFIXES) else "01 非国家图标"

pngs = [p for p in ROOT.rglob("*.png") if ".git" not in p.parts]
pngs.sort(key=lambda p: (
    group_for(p.stem),
    p.stem.lower(),
    p.relative_to(ROOT).as_posix().lower(),
))

icons = []
for path in pngs:
    rel = path.relative_to(ROOT).as_posix()
    version = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
    icons.append({
        "name": path.stem,
        "category": group_for(path.stem),
        "url": f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/{quote(rel, safe='/')}?v={version}",
    })

data = {
    "name": "goodgood",
    "description": "Custom policy group icons for Surge",
    "icons": icons,
}

content = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
(ROOT / "zzzz-surge-icon.json").write_text(content, encoding="utf-8")
print(f"Generated Surge icon set with {len(icons)} icons.")
