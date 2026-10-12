# -*- coding: utf-8 -*-
import os
import sys
import importlib
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('scripts'))

from build_all_images import (
    search_wikimedia_image,
    download_and_crop,
    generate_artistic_fallback,
    CUSTOM_SEARCH_KEYS
)

SLUGS = [
    'narayanganj', 'feni', 'cumilla', 'bhola',
    'barishal', 'chattogram', 'sylhet', 'noakhali',
    'rajshahi', 'coxs_bazar', 'kurigram', 'dinajpur'
]

def process_district(slug):
    mod = importlib.import_module(f'scripts.data_districts.{slug}')
    d = mod.DISTRICT_DATA
    dist_slug = d['slug']
    en_name = d['en']
    bn_name = d['bn']

    target_dir = os.path.join('images', 'districts', dist_slug)
    os.makedirs(target_dir, exist_ok=True)
    print(f"\n==================== Processing {en_name} ({dist_slug}) ====================")

    # 1. Historical Places
    hist_images = []
    for h in d['hist']:
        hid = h['id']
        name_en = h['nameEn']
        cat_en = h['categoryEn']
        out_path = os.path.join(target_dir, f"hist-{hid}.webp")
        keys = CUSTOM_SEARCH_KEYS.get(name_en, [name_en, f"{name_en} {en_name}"])
        print(f"  Hist #{hid}: {name_en} -> searching...")
        img_url = search_wikimedia_image(keys)
        success = False
        if img_url:
            print(f"    Found URL: {img_url[:70]}...")
            success = download_and_crop(img_url, out_path, (1200, 675))
        
        if not success:
            print(f"    Generating fallback for {name_en}")
            generate_artistic_fallback(out_path, name_en, f"Historic landmark in {en_name}", cat_en, palette_idx=hid, target_size=(1200, 675))

        hist_images.append(out_path)

    # 2. Tourist Attractions
    tour_images = []
    for t in d['tour']:
        tid = t['id']
        name_en = t['nameEn']
        cat_en = t['categoryEn']
        out_path = os.path.join(target_dir, f"tour-{tid}.webp")
        keys = CUSTOM_SEARCH_KEYS.get(name_en, [name_en, f"{name_en} {en_name}"])
        print(f"  Tour #{tid}: {name_en} -> searching...")
        img_url = search_wikimedia_image(keys)
        success = False
        if img_url:
            print(f"    Found URL: {img_url[:70]}...")
            success = download_and_crop(img_url, out_path, (1200, 675))

        if not success:
            print(f"    Generating fallback for {name_en}")
            generate_artistic_fallback(out_path, name_en, f"Tourist highlight in {en_name}", cat_en, palette_idx=tid+2, target_size=(1200, 675))

        tour_images.append(out_path)

    # 3. Carousel (1..5)
    # Selected highlights: hist-1, hist-2, tour-1, tour-2, tour-3
    carousel_sources = [
        hist_images[0], # spot 1
        hist_images[1] if len(hist_images) > 1 else hist_images[0],
        tour_images[0], # spot 3
        tour_images[1] if len(tour_images) > 1 else tour_images[0],
        tour_images[2] if len(tour_images) > 2 else hist_images[2]
    ]

    for idx, src_p in enumerate(carousel_sources):
        c_path = os.path.join(target_dir, f"carousel-{idx+1}.webp")
        with Image.open(src_p) as img:
            # Resize / crop to (1200, 750)
            img = img.resize((1200, 750), Image.Resampling.LANCZOS)
            img.save(c_path, 'WEBP', quality=85, method=6)
        print(f"  Saved Carousel-{idx+1}: {c_path}")

    # 4. Hero image (1600, 900)
    hero_path = os.path.join(target_dir, "hero.webp")
    # Base hero on hist-1 (prime historic symbol) or tour-1
    prime_source = hist_images[0]
    with Image.open(prime_source) as img:
        img = img.resize((1600, 900), Image.Resampling.LANCZOS)
        img.save(hero_path, 'WEBP', quality=85, method=6)
    print(f"  Saved Hero: {hero_path}")

if __name__ == '__main__':
    for s in SLUGS:
        process_district(s)
    print("\nAll 12 districts images generated and saved successfully!")
