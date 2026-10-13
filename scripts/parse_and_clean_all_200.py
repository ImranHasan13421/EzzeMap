import json
import urllib.parse
import re

with open('scripts/all_200_raw.json', 'r', encoding='utf-8') as f:
    raw = json.load(f)

extracted_data = {}

for slug, d in raw.items():
    dname = d['name']
    p1_text = d['p1_text']
    p2_text = d['p2_text']
    combined_text = p1_text + "\n" + p2_text
    
    hist_spots = []
    for i, url in enumerate(d['hist_links']):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query).get('query', [''])[0]
        # split by comma: first part is usually name, rest is location
        parts = [p.strip() for p in q.split(',') if p.strip()]
        if len(parts) >= 2:
            name = parts[0]
            loc = ', '.join(parts[1:])
        else:
            name = q
            loc = dname
        hist_spots.append({
            'index': i + 1,
            'name': name,
            'location': loc,
            'query': q,
            'mapUrl': url
        })
        
    tour_spots = []
    for i, url in enumerate(d['tour_links']):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(url).query).get('query', [''])[0]
        parts = [p.strip() for p in q.split(',') if p.strip()]
        if len(parts) >= 2:
            name = parts[0]
            loc = ', '.join(parts[1:])
        else:
            name = q
            loc = dname
        tour_spots.append({
            'index': i + 1,
            'name': name,
            'location': loc,
            'query': q,
            'mapUrl': url
        })
        
    extracted_data[slug] = {
        'name': dname,
        'slug': slug,
        'hist_spots': hist_spots,
        'tour_spots': tour_spots
    }

with open('scripts/all_200_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(extracted_data, f, ensure_ascii=False, indent=2)

print(f"Successfully extracted {len(extracted_data)} districts into scripts/all_200_extracted.json")
