# -*- coding: utf-8 -*-
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/curated_all_47.json', 'r', encoding='utf-8') as f:
    catalog = json.load(f)

slugs = [
    'sherpur', 'jashore', 'jhalokathi', 'moulvibazar',
    'bagerhat', 'bogura', 'natore', 'pirojpur',
    'kushtia', 'jhenaidah', 'khulna', 'chuadanga',
    'meherpur', 'patuakhali'
]

dump = {}
for s in slugs:
    d = catalog[s]
    dump[s] = {
        'en': d['en'],
        'bn': d['bn'],
        'hist': [{'id': h['id'], 'nameEn': h['nameEn'], 'nameBn': h['nameBn'], 'locEn': h['locationEn']} for h in d['hist']],
        'tour': [{'id': t['id'], 'nameEn': t['nameEn'], 'nameBn': t['nameBn'], 'locEn': t['locationEn']} for t in d['tour']],
        'carousel': [{'id': c['id'], 'titleEn': c['titleEn'], 'titleBn': c['titleBn']} for c in d['carousel']]
    }

with open('scripts/spots_14_districts.json', 'w', encoding='utf-8') as f:
    json.dump(dump, f, ensure_ascii=False, indent=2)

print(f"Dumped spots for {len(dump)} districts.")
