# -*- coding: utf-8 -*-
import os
import sys
import time
import json
import urllib.request
import urllib.parse
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')

USER_AGENT = 'EzzeMapHeritage/2.4 (https://github.com/ImranHasan13421/EzzeMap; contact: imranhasan13421@gmail.com)'

def get_rest_image(title, lang='en'):
    clean = title.replace(' ', '_')
    url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{urllib.parse.quote(clean)}"
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            d = json.loads(r.read().decode('utf-8'))
            return d.get('originalimage', {}).get('source') or d.get('thumbnail', {}).get('source')
    except Exception:
        pass
    return None

def get_media_list_image(title, lang='en'):
    clean = title.replace(' ', '_')
    url = f"https://{lang}.wikipedia.org/api/rest_v1/page/media-list/{urllib.parse.quote(clean)}"
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            d = json.loads(r.read().decode('utf-8'))
            items = d.get('items', [])
            for it in items:
                if it.get('type') == 'image':
                    title_img = it.get('title', '')
                    if not any(x in title_img.lower() for x in ['flag', 'map', 'icon', 'symbol', 'locator', 'coat_of_arms']):
                        srcset = it.get('srcset', [])
                        if srcset:
                            return 'https:' + srcset[-1]['src']
    except Exception:
        pass
    return None

def find_image(queries, district_slug):
    for q in queries:
        img = get_rest_image(q, 'en')
        if img: return (img, f"en_summary: {q}")
        img = get_rest_image(q, 'bn')
        if img: return (img, f"bn_summary: {q}")
        img = get_media_list_image(q, 'en')
        if img: return (img, f"en_media: {q}")
        img = get_media_list_image(q, 'bn')
        if img: return (img, f"bn_media: {q}")

    # Fallback to district queries
    district_queries = [
        (f"{district_slug.title()} District", 'en'),
        (f"{district_slug.title()}", 'en'),
        (f"{district_slug.title()} Upazila", 'en'),
        ("Chittagong Hill Tracts", 'en') if district_slug in ['rangamati', 'bandarban', 'khagrachhari'] else ("Northern Bangladesh", 'en')
    ]
    for dq, l in district_queries:
        img = get_rest_image(dq, l)
        if img: return (img, f"dist_summary: {dq}")
        img = get_media_list_image(dq, l)
        if img: return (img, f"dist_media: {dq}")

    return (None, None)

def download_and_crop(url, out_path, target_size=(1200, 675)):
    temp_file = out_path + ".temp"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=15) as resp, open(temp_file, 'wb') as f:
            f.write(resp.read())

        with Image.open(temp_file) as img:
            img = img.convert('RGB')
            target_w, target_h = target_size
            target_aspect = target_w / target_h
            img_aspect = img.width / img.height

            if img_aspect > target_aspect:
                new_w = int(img.height * target_aspect)
                offset_x = (img.width - new_w) // 2
                img = img.crop((offset_x, 0, offset_x + new_w, img.height))
            else:
                new_h = int(img.width / target_aspect)
                offset_y = (img.height - new_h) // 2
                img = img.crop((0, offset_y, img.width, offset_y + new_h))

            img = img.resize(target_size, Image.Resampling.LANCZOS)
            img.save(out_path, 'WEBP', quality=88, method=6)

        if os.path.exists(temp_file):
            os.remove(temp_file)
        return True
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        return False

def main():
    with open('scripts/search_map_17.json', 'r', encoding='utf-8') as f:
        search_map = json.load(f)

    pending = []
    for slug, items in search_map.items():
        for key, queries in items.items():
            out_path = os.path.join('images', 'districts', slug, f"{key}.webp")
            if not os.path.exists(out_path) or os.path.getsize(out_path) < 5000:
                pending.append((slug, key, queries, out_path))

    print(f"Total images needing download: {len(pending)}", flush=True)

    success_count = 0
    fail_count = 0

    for idx, (slug, key, queries, out_path) in enumerate(pending):
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        img_url, source = find_image(queries, slug)
        if img_url:
            ok = download_and_crop(img_url, out_path)
            if ok:
                success_count += 1
                print(f"[{idx+1}/{len(pending)}] OK: {slug}/{key} ({source}) -> {os.path.getsize(out_path)} bytes", flush=True)
            else:
                fail_count += 1
                print(f"[{idx+1}/{len(pending)}] Crop Error: {slug}/{key}", flush=True)
        else:
            fail_count += 1
            print(f"[{idx+1}/{len(pending)}] No URL found: {slug}/{key}", flush=True)

        # slight delay to be respectful
        time.sleep(0.15)

    print("\n==========================================", flush=True)
    print(f"Finished! Success: {success_count}, Failed: {fail_count}", flush=True)

if __name__ == '__main__':
    main()
