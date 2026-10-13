# -*- coding: utf-8 -*-
import os
import sys
import json
import importlib.util

sys.stdout.reconfigure(encoding='utf-8')

def load_module_from_file(filepath):
    mod_name = os.path.splitext(os.path.basename(filepath))[0]
    spec = importlib.util.spec_from_file_location(mod_name, filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.DISTRICT_DATA

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    curated27_path = os.path.join(root, 'scripts', 'curated_all_27.json')
    with open(curated27_path, 'r', encoding='utf-8') as f:
        master_data = json.load(f)
    print(f"Loaded existing curated districts: {len(master_data)}")

    districts_dir = os.path.join(root, 'scripts', 'data_districts_20')
    py_files = sorted([f for f in os.listdir(districts_dir) if f.endswith('.py')])
    print(f"Found {len(py_files)} district modules to merge.")

    added_or_updated = 0
    for f in py_files:
        fp = os.path.join(districts_dir, f)
        data = load_module_from_file(fp)
        slug = data['slug']
        
        # Validation checks
        assert len(data['carousel']) == 5, f"{slug}: carousel must have 5 items"
        assert len(data['hist']) == 5, f"{slug}: hist must have 5 items"
        assert len(data['tour']) == 5, f"{slug}: tour must have 5 items"
        assert data.get('tagline_en') and data.get('tagline_bn'), f"{slug}: taglines required"
        
        for idx, h in enumerate(data['hist']):
            assert h.get('nameEn') and h.get('nameBn'), f"{slug} hist {idx+1} missing names"
            assert h.get('descEn') and h.get('descBn'), f"{slug} hist {idx+1} missing descriptions"
            assert h.get('locationEn') and h.get('locationBn'), f"{slug} hist {idx+1} missing locations"
            assert h.get('mapUrl') and h['mapUrl'].startswith('http'), f"{slug} hist {idx+1} invalid mapUrl: {h.get('mapUrl')}"
            
        for idx, t in enumerate(data['tour']):
            assert t.get('nameEn') and t.get('nameBn'), f"{slug} tour {idx+1} missing names"
            assert t.get('descEn') and t.get('descBn'), f"{slug} tour {idx+1} missing descriptions"
            assert t.get('locationEn') and t.get('locationBn'), f"{slug} tour {idx+1} missing locations"
            assert t.get('mapUrl') and t['mapUrl'].startswith('http'), f"{slug} tour {idx+1} invalid mapUrl: {t.get('mapUrl')}"

        master_data[slug] = data
        added_or_updated += 1
        print(f"  [OK] Validated & merged: {slug} ({data['en']} / {data['bn']})")

    out_path = os.path.join(root, 'scripts', 'curated_all_47.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)

    print(f"\nSuccessfully wrote {out_path}!")
    print(f"Total curated districts in master dataset: {len(master_data)}")

if __name__ == '__main__':
    main()
