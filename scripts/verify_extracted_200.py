import json

with open('scripts/all_200_extracted.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

lines = []
lines.append(f"Total districts: {len(data)}")
for slug, d in data.items():
    lines.append(f"\n[{slug.upper()}] {d['name']}")
    lines.append("  Historical:")
    for h in d['hist_spots']:
        lines.append(f"    {h['index']}. {h['name']} | Loc: {h['location']} | Link: {h['mapUrl']}")
    lines.append("  Tourist:")
    for t in d['tour_spots']:
        lines.append(f"    {t['index']}. {t['name']} | Loc: {t['location']} | Link: {t['mapUrl']}")

with open('scripts/extracted_summary.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("Successfully written to scripts/extracted_summary.txt")
