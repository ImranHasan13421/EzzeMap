import json

with open('scripts/parsed_all_items.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('scripts/all_items_dump.txt', 'w', encoding='utf-8') as out:
    for d in data:
        out.write(f"\n==================== {d['district']} ({d['slug']}) ====================\n")
        for it in d['items']:
            out.write(f"#{it['num']} [{it['category_type']}]: {it['raw_lines']}\n")
            out.write(f"   MAP: {it['link']}\n")

print("Dumped in UTF-8 to scripts/all_items_dump.txt")
