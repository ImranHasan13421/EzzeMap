import json, sys, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/all_150_extracted.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

issues = []
for d in data:
    for it in d['items']:
        name = it['name']
        desc = it['description']
        loc = it['location']
        unq = it['query_full']
        
        # Check for weird characters
        if '■' in name or '■' in desc or '■' in loc:
            issues.append((d['district'], it['id'], it['category'], 'Black square symbol', name, desc[:50], loc))
        if name.endswith(','):
            issues.append((d['district'], it['id'], it['category'], 'Trailing comma in name', name, desc[:50], loc))
        if len(name.split()) > 10:
            issues.append((d['district'], it['id'], it['category'], 'Name unusually long', name, desc[:50], loc))
        if len(desc.split()) < 10:
            issues.append((d['district'], it['id'], it['category'], 'Desc unusually short', name, desc, loc))

print(f"Total potential issues found: {len(issues)}")
for iss in issues:
    print("Issue:", iss)
