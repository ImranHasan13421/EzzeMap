import json
import re

with open('scripts/extracted_raw.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

all_parsed = []

for dist in raw_data:
    district_name = dist['district']
    slug = dist['slug']
    links = dist['links']
    lines = [l.strip() for l in dist['raw_text'].split('\n') if l.strip()]
    
    # Locate all items 1..10
    # Let's track positions of line == '1'..'10'
    items = []
    
    # We find number markers
    # 1..5 belong to Historical, 6..10 belong to Tourist
    num_indices = []
    for idx, l in enumerate(lines):
        if re.match(r'^(?:[1-9]|10)$', l):
            num = int(l)
            num_indices.append((num, idx))
            
    # Verify we got 1..10
    found_nums = [n for n, _ in num_indices]
    
    for i, (num, start_idx) in enumerate(num_indices):
        # find end_idx which is the next 'Open Google Maps' after start_idx
        end_idx = None
        for j in range(start_idx + 1, len(lines)):
            if lines[j] == 'Open Google Maps':
                end_idx = j
                break
                
        content_lines = lines[start_idx + 1 : end_idx] if end_idx else []
        
        # Link
        link = links[num - 1] if num - 1 < len(links) else ""
        
        category_type = "historical" if num <= 5 else "tourist"
        
        items.append({
            'num': num,
            'category_type': category_type,
            'raw_lines': content_lines,
            'link': link
        })
        
    all_parsed.append({
        'district': district_name,
        'slug': slug,
        'items': items
    })

with open('scripts/parsed_all_items.json', 'w', encoding='utf-8') as f:
    json.dump(all_parsed, f, ensure_ascii=False, indent=2)

print("Saved scripts/parsed_all_items.json")
