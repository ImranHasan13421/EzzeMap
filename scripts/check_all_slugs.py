# -*- coding: utf-8 -*-
import json
import re

with open('scripts/curated_all_64.json', encoding='utf-8') as f:
    master = json.load(f)

with open('district-data.js', encoding='utf-8') as f:
    content = f.read()

dd_slugs = re.findall(r'"slug":\s*"([^"]+)"', content)
print(f"Total districts in district-data.js: {len(dd_slugs)}")

missing_in_dd = [s for s in master.keys() if s not in dd_slugs and s != 'coxs-bazar']
if 'coxs-bazar' in master and 'cox-s-bazar' in dd_slugs:
    print("Note: coxs-bazar maps to cox-s-bazar in district-data.js")

print(f"Missing in district-data.js: {missing_in_dd}")
missing_in_master = [s for s in dd_slugs if s not in master and s != 'dhaka' and s != 'cox-s-bazar']
print(f"Missing in master_64: {missing_in_master}")
