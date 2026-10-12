import json
import re

with open('scripts/extracted_raw.json', 'r', encoding='utf-8') as f:
    raw_data = json.load(f)

parsed_districts = []

for dist_obj in raw_data:
    dist_name = dist_obj['district']
    slug = dist_obj['slug']
    lines = [l.strip() for l in dist_obj['raw_text'].split('\n') if l.strip()]
    links = dist_obj['links']
    
    # We want to identify items 1..10
    # An item starts with a line containing solely the number 1..10 (or item number)
    # and ends at 'Open Google Maps'
    items = []
    
    # Find indices of each number 1 to 10
    # Note that in the page, the numbers 1,2,3,4,5 appear after 'Historical ...' and 6,7,8,9,10 appear after 'Tourist attractions'
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^([1-9]|10)$', line)
        if m:
            num = int(m.group(1))
            # Find next 'Open Google Maps'
            j = i + 1
            while j < len(lines) and lines[j] != 'Open Google Maps':
                j += 1
            if j < len(lines) and lines[j] == 'Open Google Maps':
                item_lines = lines[i+1:j]
                # In item_lines, the last line is the location!
                # Wait, could location wrap across lines? Let's check!
                # For example:
                # Bandar, near the Shitalakshya \n River
                # Let's inspect item_lines
                items.append({
                    'num': num,
                    'raw_lines': item_lines,
                    'link': links[num - 1] if (num - 1) < len(links) else ''
                })
                i = j
        i += 1
        
    parsed_districts.append({
        'district': dist_name,
        'slug': slug,
        'items': items
    })

print(f"Total districts parsed: {len(parsed_districts)}")
for d in parsed_districts:
    print(f"{d['district']} ({d['slug']}): {len(d['items'])} items")
    if len(d['items']) != 10:
        print(f"  WARNING: {d['district']} has {len(d['items'])} items instead of 10")

with open('scripts/parsed_debug.json', 'w', encoding='utf-8') as f:
    json.dump(parsed_districts, f, ensure_ascii=False, indent=2)
