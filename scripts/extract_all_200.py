import json
import urllib.parse
import re

with open('scripts/new_20_pdf_dump.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

# District list and page mapping:
# Page 1: cover, Page 2: index
# Each district takes 2 pages starting from page 3 (index 2)
district_names = [
    "Lakshmipur", "Gopalganj", "Habiganj", "Pabna", "Netrokona",
    "Noakhali", "Sherpur", "Jashore", "Jhalokathi", "Moulvibazar",
    "Bagerhat", "Bogura", "Natore", "Pirojpur", "Kushtia",
    "Jhenaidah", "Khulna", "Chuadanga", "Meherpur", "Patuakhali"
]

slug_map = {
    "Lakshmipur": "lakshmipur",
    "Gopalganj": "gopalganj",
    "Habiganj": "habiganj",
    "Pabna": "pabna",
    "Netrokona": "netrokona",
    "Noakhali": "noakhali",
    "Sherpur": "sherpur",
    "Jashore": "jashore",
    "Jhalokathi": "jhalokathi",
    "Moulvibazar": "moulvibazar",
    "Bagerhat": "bagerhat",
    "Bogura": "bogura",
    "Natore": "natore",
    "Pirojpur": "pirojpur",
    "Kushtia": "kushtia",
    "Jhenaidah": "jhenaidah",
    "Khulna": "khulna",
    "Chuadanga": "chuadanga",
    "Meherpur": "meherpur",
    "Patuakhali": "patuakhali"
}

districts_extracted = {}

for i, dname in enumerate(district_names):
    p1_idx = 2 + i * 2
    p2_idx = 3 + i * 2
    p1 = pages[p1_idx]
    p2 = pages[p2_idx]
    
    links = [l['uri'] for l in p1['links']] + [l['uri'] for l in p2['links']]
    print(f"District {i+1}: {dname} (Pages {p1['page']}, {p2['page']}) -> {len(links)} links")
    
    if len(links) != 10:
        print(f"  WARNING: Expected 10 links, got {len(links)}!")
    
    hist_links = links[:5]
    tour_links = links[5:]
    
    districts_extracted[slug_map[dname]] = {
        'name': dname,
        'slug': slug_map[dname],
        'pages': [p1['page'], p2['page']],
        'hist_links': hist_links,
        'tour_links': tour_links,
        'p1_text': p1['text'],
        'p2_text': p2['text']
    }

with open('scripts/all_200_raw.json', 'w', encoding='utf-8') as f:
    json.dump(districts_extracted, f, ensure_ascii=False, indent=2)

print("\nAll 20 districts successfully checked.")
