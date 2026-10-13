# -*- coding: utf-8 -*-
import os
import sys
import json
import urllib.request
import urllib.parse
from PIL import Image
import concurrent.futures

sys.stdout.reconfigure(encoding='utf-8')
USER_AGENT = 'EzzeMapHeritage/1.0 (https://github.com/ImranHasan13421/EzzeMap; contact: imranhasan13421@gmail.com)'

def search_wiki(q, lang='en'):
    clean = q.replace(' ', '_')
    url = f"https://{lang}.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(clean)}&prop=pageimages&format=json&pithumbsize=1600"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=5) as r:
            d = json.loads(r.read())
            pages = d.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                if pid != '-1' and 'thumbnail' in pdata:
                    return pdata['thumbnail']['source']
    except Exception:
        pass
    return None

def search_wiki_generator(q, lang='en'):
    url = f"https://{lang}.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrlimit=1&prop=pageimages&format=json&pithumbsize=1600"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=5) as r:
            d = json.loads(r.read())
            pages = d.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                if pid != '-1' and 'thumbnail' in pdata:
                    return pdata['thumbnail']['source']
    except Exception:
        pass
    return None

def search_commons(q):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrlimit=1&gsrnamespace=6&prop=imageinfo&iiprop=url&iiurlwidth=1600&format=json"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=5) as r:
            d = json.loads(r.read())
            pages = d.get('query', {}).get('pages', {})
            for pid, pdata in pages.items():
                if pid != '-1' and 'imageinfo' in pdata and len(pdata['imageinfo']) > 0:
                    info = pdata['imageinfo'][0]
                    return info.get('thumburl') or info.get('url')
    except Exception:
        pass
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
        with urllib.request.urlopen(req, timeout=12) as resp, open(temp_file, 'wb') as f:
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

    url, source = find_best_image_url(queries)
    if url:
        success = download_and_crop(url, out_path)
        if success:
            return (slug, key, "DOWNLOADED", source, out_path)
    
    # Fallback to general district photographic search if specific failed
    fallback_queries = [f"{slug} Bangladesh", f"{slug} district", "Bangladesh landscape"]
    url2, source2 = find_best_image_url(fallback_queries)
    if url2:
        success2 = download_and_crop(url2, out_path)
        if success2:
            return (slug, key, "FALLBACK_PHOTO", source2, out_path)

    return (slug, key, "FAILED", None, out_path)

def main():
    with open('scripts/search_map_14.json', 'r', encoding='utf-8') as f:
        search_map = json.load(f)

    tasks = []
    for slug, items in search_map.items():
        for key, queries in items.items():
            tasks.append((slug, key, queries))

    print(f"Total images to fetch: {len(tasks)} (14 districts x 16 images each)")
    print("Launching multi-threaded download with 8 workers...")

    results = []
    downloaded = 0
    fallback_photo = 0
    failed = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
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
            if total_done % 10 == 0 or total_done == len(tasks):
                print(f"Progress: [{total_done}/{len(tasks)}] (Exact Photos: {downloaded}, District Photos: {fallback_photo}, Failed: {failed})")

    print("\n=======================================================")
    print(f"SUMMARY FOR 14 DISTRICTS:")
    print(f"Exact Landmark Photographs: {downloaded}")
    print(f"District Landscape Photographs: {fallback_photo}")
    print(f"Failed: {failed}")

if __name__ == '__main__':
    main()
