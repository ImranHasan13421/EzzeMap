# -*- coding: utf-8 -*-
import os
import sys
import json
import importlib.util

sys.stdout.reconfigure(encoding='utf-8')

# Load curated_all_47.json
with open('scripts/curated_all_47.json', encoding='utf-8') as f:
    master_64 = json.load(f)

print(f"Loaded {len(master_64)} districts from curated_all_47.json")

# 17 new districts
districts_17 = [
    'magura', 'narail', 'naogaon', 'satkhira', 'khagrachhari',
    'joypurhat', 'sunamganj', 'gaibandha', 'rangpur', 'rangamati',
    'chapainawabganj', 'bandarban', 'barguna', 'lalmonirhat',
    'nilphamari', 'thakurgaon', 'panchagarh'
]

for slug in districts_17:
    py_path = f"scripts/data_districts_17/{slug}.py"
    spec = importlib.util.spec_from_file_location(slug, py_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    data = getattr(module, 'data', getattr(module, 'DISTRICT_DATA', None))
    if not data:
        raise ValueError(f"Could not find data dict in {slug}")
    master_64[slug] = data
    print(f"Merged {slug}: {len(data['hist'])} hist, {len(data['tour'])} tour, {len(data['carousel'])} carousel")

print(f"Total curated districts in master_64 (excluding dhaka): {len(master_64)}")

with open('scripts/curated_all_64.json', 'w', encoding='utf-8') as f:
    json.dump(master_64, f, ensure_ascii=False, indent=2)

print("Saved scripts/curated_all_64.json successfully!")
