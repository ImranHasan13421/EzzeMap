# -*- coding: utf-8 -*-
import os, sys, importlib, json

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('scripts/data_districts'))

MODULES = [
    # 12 previously curated
    "narayanganj", "feni", "cumilla", "bhola", "barishal", "chattogram",
    "sylhet", "noakhali", "rajshahi", "coxs_bazar", "kurigram", "dinajpur",
    # 15 newly curated
    "munshiganj", "gazipur", "narsingdi", "manikganj", "shariatpur",
    "madaripur", "tangail", "brahmanbaria", "rajbari", "chandpur",
    "mymensingh", "kishoreganj", "sirajganj", "faridpur", "jamalpur"
]

all_curated = {}
error_count = 0

for mod_name in MODULES:
    try:
        mod = importlib.import_module(mod_name)
        data = getattr(mod, 'DISTRICT_DATA')
        slug = data['slug']
        en = data['en']
        hist = data['hist']
        tour = data['tour']
        carousel = data['carousel']
        
        # Verify counts
        assert len(hist) == 5, f"{mod_name} hist count is {len(hist)}"
        assert len(tour) == 5, f"{mod_name} tour count is {len(tour)}"
        assert len(carousel) == 5, f"{mod_name} carousel count is {len(carousel)}"
        
        # Verify required keys in each spot
        for it in hist + tour:
            for k in ['id', 'nameEn', 'nameBn', 'categoryEn', 'categoryBn', 'descEn', 'descBn', 'locationEn', 'locationBn', 'mapUrl']:
                assert k in it and it[k], f"Missing {k} in {mod_name} spot {it.get('nameEn')}"
                
        all_curated[slug] = data
        print(f"OK: {en:15s} (slug: {slug:15s}) | 5 hist + 5 tour + 5 carousel")
    except Exception as e:
        print(f"ERROR in {mod_name}: {e}")
        error_count += 1

print(f"\nTotal verified districts: {len(all_curated)} / {len(MODULES)}")
if error_count == 0:
    # Save to curated_all_27.json
    with open('scripts/curated_all_27.json', 'w', encoding='utf-8') as f:
        json.dump(all_curated, f, ensure_ascii=False, indent=2)
    print("Saved scripts/curated_all_27.json successfully!")
else:
    sys.exit(1)
