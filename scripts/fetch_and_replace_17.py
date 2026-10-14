# -*- coding: utf-8 -*-
import os
import sys
import time
import json
import urllib.request
import urllib.parse
from PIL import Image
import concurrent.futures

sys.stdout.reconfigure(encoding='utf-8')

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'

def get_json(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=8) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception:
        return None

def search_wiki(q, lang='en'):
    clean = q.replace(' ', '_')
    url = f"https://{lang}.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(clean)}&prop=pageimages&format=json&pithumbsize=1600"
    d = get_json(url)
    if d:
        pages = d.get('query', {}).get('pages', {})
        for pid, pdata in pages.items():
            if pid != '-1' and 'thumbnail' in pdata:
                return pdata['thumbnail']['source']
    return None

def search_wiki_generator(q, lang='en'):
    url = f"https://{lang}.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrlimit=1&prop=pageimages&format=json&pithumbsize=1600"
    d = get_json(url)
    if d:
        pages = d.get('query', {}).get('pages', {})
        for pid, pdata in pages.items():
            if pid != '-1' and 'thumbnail' in pdata:
                return pdata['thumbnail']['source']
    return None

def search_commons(q):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrlimit=1&gsrnamespace=6&prop=imageinfo&iiprop=url&iiurlwidth=1600&format=json"
    d = get_json(url)
    if d:
        pages = d.get('query', {}).get('pages', {})
        for pid, pdata in pages.items():
            if pid != '-1' and 'imageinfo' in pdata and len(pdata['imageinfo']) > 0:
                info = pdata['imageinfo'][0]
                return info.get('thumburl') or info.get('url')
    return None

def find_best_image_url(queries):
    for q in queries:
        # 1. Direct EN wiki
        url = search_wiki(q, 'en')
        if url: return (url, f"en_wiki: {q}")
        # 2. Direct BN wiki
        url = search_wiki(q, 'bn')
        if url: return (url, f"bn_wiki: {q}")
        # 3. Commons generator
        url = search_commons(q)
        if url: return (url, f"commons: {q}")
        # 4. Search generator EN wiki
        url = search_wiki_generator(q, 'en')
        if url: return (url, f"en_gen: {q}")
        # 5. Search generator BN wiki
        url = search_wiki_generator(q, 'bn')
        if url: return (url, f"bn_gen: {q}")
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

def process_item(item):
    slug, key, queries = item
    out_dir = os.path.join('images', 'districts', slug)
    os.makedirs(out_dir, exist_ok=True)
    filename = f"{key}.webp"
    out_path = os.path.join(out_dir, filename)

    if os.path.exists(out_path) and os.path.getsize(out_path) > 5000:
        return (slug, key, "EXISTING", "cached", out_path)

    url, source = find_best_image_url(queries)
    if url:
        success = download_and_crop(url, out_path)
        if success:
            return (slug, key, "DOWNLOADED", source, out_path)
    
    # Secondary district & landscape fallback search
    fallback_queries = [
        f"{slug} District",
        f"{slug} Bangladesh",
        f"{slug} town",
        "Landscape of northern Bangladesh",
        "Rivers of Bangladesh"
    ]
    url2, source2 = find_best_image_url(fallback_queries)
    if url2:
        success2 = download_and_crop(url2, out_path)
        if success2:
            return (slug, key, "FALLBACK_PHOTO", source2, out_path)

    return (slug, key, "FAILED", None, out_path)

def main():
    with open('scripts/search_map_17.json', 'r', encoding='utf-8') as f:
        search_map = json.load(f)

    tasks = []
    for slug, items in search_map.items():
        for key, queries in items.items():
            out_path = os.path.join('images', 'districts', slug, f"{key}.webp")
            if not os.path.exists(out_path) or os.path.getsize(out_path) < 5000:
                tasks.append((slug, key, queries))

    print(f"Remaining images to download: {len(tasks)}", flush=True)
    if not tasks:
        print("All 272 images are already present and verified!", flush=True)
        return

    results = []
    downloaded = 0
    fallback_photo = 0
    failed = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(process_item, t): t for t in tasks}
        for future in concurrent.futures.as_completed(futures):
            res = future.result()
            results.append(res)
            slug, key, status, source, out_path = res
            if status == "DOWNLOADED":
                downloaded += 1
            elif status == "FALLBACK_PHOTO":
                fallback_photo += 1
            else:
                failed += 1

            total_done = len(results)
            if total_done % 5 == 0 or total_done == len(tasks):
                print(f"Progress: [{total_done}/{len(tasks)}] (Exact: {downloaded}, District: {fallback_photo}, Failed: {failed})", flush=True)

    print("\n=======================================================", flush=True)
    print(f"COMPLETED BATCH:")
    print(f"Exact Landmark Photographs: {downloaded}", flush=True)
    print(f"District Landscape Photographs: {fallback_photo}", flush=True)
    print(f"Failed: {failed}", flush=True)

if __name__ == '__main__':
    main()
