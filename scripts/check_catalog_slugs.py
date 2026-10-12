import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('data/main-info/catalog.js', 'r', encoding='utf-8') as f:
    cat_text = f.read()

districts = [
    'Munshiganj', 'Gazipur', 'Narsingdi', 'Manikganj', 'Shariatpur',
    'Madaripur', 'Tangail', 'Brahmanbaria', 'Rajbari', 'Chandpur',
    'Mymensingh', 'Kishoreganj', 'Sirajganj', 'Faridpur', 'Jamalpur'
]

matches = re.findall(r'\{\s*"slug":\s*"([^"]+)",\s*"en":\s*"([^"]+)",\s*"bn":\s*"([^"]+)"', cat_text)
cat_map = {en.lower(): (slug, bn) for slug, en, bn in matches}

print(f"Total entries in catalog: {len(matches)}")
found_all = True
for d in districts:
    match = cat_map.get(d.lower())
    if match:
        print(f"{d:15s} -> slug: {match[0]:15s} bn: {match[1]}")
    else:
        # Check partial or variations
        found = False
        for k, v in cat_map.items():
            if d.lower() in k or k in d.lower():
                print(f"{d:15s} -> (approx) {k}: slug={v[0]} bn={v[1]}")
                found = True
                break
        if not found:
            print(f"{d:15s} -> NOT FOUND IN CATALOG!")
            found_all = False

if found_all:
    print("\nALL 15 DISTRICTS FOUND IN CATALOG!")
