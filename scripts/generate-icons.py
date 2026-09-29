#!/usr/bin/env python3
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
OWNER = "ZzQiao7"
REPO = "goodgood"
BRANCH = "main"

COUNTRY_PREFIXES = ("flag-",)

# App / service / browser icons. Everything else stays in the middle as General.
APP_NAMES = {
    "amap", "apple-weather", "apple", "baidu-netdisk", "bilibili", "bluesky",
    "chatgpt", "chrome-canary", "chrome", "chromium", "discord", "edge",
    "element", "emby", "firefox-developer", "firefox-nightly", "firefox",
    "github", "gitlab", "inaturalist", "instagram", "internet-explorer", "jd",
    "jellyfin", "linkedin", "mastodon", "meitu", "microsoft", "musicbrainz",
    "netease-cloud-music", "netscape-navigator", "openfoodfact", "openstreetmap",
    "opera", "paypal", "peertube", "pinduoduo", "pinterest", "pixelfed",
    "qq-music", "quark", "safari", "soul", "spotify", "taobao", "telegram",
    "tiktok", "twitter", "wechat", "wikidata", "windows", "winrar", "xianyu",
    "xiaoheihe", "xiaohongshu", "youtube",
}

def group_for(stem):
    key = stem.lower()
    if key.startswith(COUNTRY_PREFIXES):
        return "99 Country"
    if key in APP_NAMES:
        return "01 App"
    return "02 General"

pngs = [p for p in ROOT.rglob("*.png") if ".git" not in p.parts]
pngs.sort(key=lambda p: (
    {"01 App": 0, "02 General": 1, "99 Country": 2}[group_for(p.stem)],
    p.stem.lower(),
    p.relative_to(ROOT).as_posix().lower(),
))

icons = []
for path in pngs:
    rel = path.relative_to(ROOT).as_posix()
    icons.append({
        "name": path.stem,
        "category": group_for(path.stem),
        "url": f"https://raw.githubusercontent.com/{OWNER}/{REPO}/{BRANCH}/{quote(rel, safe='/')}",
    })

data = {
    "name": "goodgood",
    "description": "Custom policy group icons for Surge",
    "icons": icons,
}

(ROOT / "surge-icon.json").write_text(
    json.dumps(data, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)
print(f"Generated surge-icon.json with {len(icons)} icons.")
