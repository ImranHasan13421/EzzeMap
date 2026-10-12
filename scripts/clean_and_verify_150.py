import json, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/all_150_extracted.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for d in data:
    for it in d['items']:
        # Fix Faridpur tourist 1
        if d['slug'] == 'faridpur' and it['id'] == 1 and it['category'] == 'tourist':
            it['name'] = "Padma Riverbank, Char Bhadrasan"
            it['description'] = "The Padma river and its chars create a wide, changing landscape around Char Bhadrasan. Visitors can enjoy views of boats, sandbars and rural river life. Seasonal water levels strongly affect the scenery and access. Some areas require boat transport and local guidance. Avoid unstable banks and follow current safety advice."
            it['location'] = "Char Bhadrasan riverbank and char areas, Faridpur, Faridpur, Bangladesh"

with open('scripts/all_150_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Saved cleaned data. Now listing all:")
for d in data:
    print(f"\n=== {d['district']} ({d['slug']}) ===")
    for it in d['items']:
        cat = it['category'][:4].upper()
        print(f"  [{cat}-{it['id']}] {it['name']}")
        print(f"         Location: {it['location']}")
        print(f"         Map:      {it['map_link'][:60]}...")
