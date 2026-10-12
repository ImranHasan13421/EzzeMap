# -*- coding: utf-8 -*-
import os
import sys
import json
import importlib

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('scripts'))

SLUGS = [
    'narayanganj', 'feni', 'cumilla', 'bhola',
    'barishal', 'chattogram', 'sylhet', 'noakhali',
    'rajshahi', 'coxs_bazar', 'kurigram', 'dinajpur'
]

curated_dict = {}

for s in SLUGS:
    mod = importlib.import_module(f'scripts.data_districts.{s}')
    d = mod.DISTRICT_DATA
    curated_dict[d['slug']] = d

with open('scripts/curated_all_12.json', 'w', encoding='utf-8') as f:
    json.dump(curated_dict, f, ensure_ascii=False, indent=2)

print("Exported scripts/curated_all_12.json successfully with", len(curated_dict), "districts.")
