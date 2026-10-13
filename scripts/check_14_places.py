# -*- coding: utf-8 -*-
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/curated_all_47.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

slugs = [
    'sherpur', 'jashore', 'jhalokathi', 'moulvibazar',
    'bagerhat', 'bogura', 'natore', 'pirojpur',
    'kushtia', 'jhenaidah', 'khulna', 'chuadanga',
    'meherpur', 'patuakhali'
]

for s in slugs:
    dist = d[s]
    print(f"\n=== {dist['en']} ({s}) ===")
    print("HISTORICAL:")
    for h in dist['hist']:
        print(f"  [{h['id']}] {h['nameEn']} (BN: {h['nameBn']}) - Loc: {h['locationEn']}")
    print("TOURIST:")
    for t in dist['tour']:
        print(f"  [{t['id']}] {t['nameEn']} (BN: {t['nameBn']}) - Loc: {t['locationEn']}")
