# -*- coding: utf-8 -*-
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/all_17_extracted_raw.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

cleaned_all = {}

for slug, dist in raw.items():
    name = dist['name']
    places = dist['places']
    
    # We can parse place name and location from full_query or page text
    cleaned_places = []
    for p in places:
        q = p['full_query']
        # Typically "Place Name, Location, District" or "Place Name, Location"
        parts = [pt.strip() for pt in q.split(',') if pt.strip()]
        if len(parts) >= 2:
            p_name = parts[0]
            p_loc = ', '.join(parts[1:])
        else:
            p_name = q
            p_loc = f"{name} district"

        cleaned_places.append({
            'index': p['index'],
            'type': p['type'],
            'nameEn': p_name,
            'locationEn': p_loc,
            'mapUrl': p['uri'],
            'full_query': q
        })
    
    cleaned_all[slug] = {
        'name': name,
        'slug': slug,
        'places': cleaned_places
    }

with open('scripts/all_17_cleaned.json', 'w', encoding='utf-8') as f:
    json.dump(cleaned_all, f, ensure_ascii=False, indent=2)

print(f"Cleaned {len(cleaned_all)} districts.")
for slug, d in cleaned_all.items():
    print(f"\n=== {d['name']} ({slug}) ===")
    print("  HIST:")
    for p in d['places'][:5]:
        print(f"    [{p['index']}] {p['nameEn']} | Loc: {p['locationEn']}")
    print("  TOUR:")
    for p in d['places'][5:]:
        print(f"    [{p['index']}] {p['nameEn']} | Loc: {p['locationEn']}")
