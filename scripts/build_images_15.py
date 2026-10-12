# -*- coding: utf-8 -*-
import os
import sys
import json
import urllib.request
import urllib.parse
from PIL import Image, ImageDraw, ImageFont
import importlib

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('scripts'))
sys.path.insert(0, os.path.abspath('scripts/data_districts'))

USER_AGENT = 'EzzeMapHeritage/1.0 (https://github.com/ImranHasan13421/EzzeMap; contact: imranhasan13421@gmail.com)'

TARGET_SLUGS = [
    "munshiganj", "gazipur", "narsingdi", "manikganj", "shariatpur",
    "madaripur", "tangail", "brahmanbaria", "rajbari", "chandpur",
    "mymensingh", "kishoreganj", "sirajganj", "faridpur", "jamalpur"
]

CUSTOM_SEARCH_KEYS = {
    # Munshiganj
    "Idrakpur Fort": ["Idrakpur Fort", "Munshiganj Fort"],
    "Baba Adam Mosque": ["Baba Adam's Mosque", "Baba Adam Mosque"],
    "Sonarang Twin Temples": ["Sonarang Twin Temples", "Sonarang"],
    "Bikrampur Buddhist Bihar and Museum of Antiquities": ["Bikrampur Vihara", "Raghurampur", "Bikrampur"],
    "Shyamsiddhi Math": ["Shyamsiddhi Math", "Sreenagar Upazila"],
    "Mawa Ferry Ghat and Padma Riverfront": ["Mawa, Bangladesh", "Padma River", "Padma Bridge"],
    "Padma Bridge Viewpoint, Mawa side": ["Padma Bridge", "Mawa"],
    "Meghna Riverbank, Gazaria": ["Meghna River", "Gazaria Upazila"],
    "Rampal Dighi": ["Rampal, Munshiganj", "Bikrampur"],
    "Bhagyakul Zamindar Bari area": ["Bhagyakul", "Sreenagar Upazila"],

    # Gazipur
    "Bhawal Rajbari": ["Bhawal Rajbari", "Joydebpur", "Bhawal estate"],
    "Baliadi Zamindar Bari": ["Baliadi Zamindar Bari", "Kaliakair Upazila"],
    "St. Nicholas Church": ["St. Nicholas Church, Nagari", "Nagari, Gazipur"],
    "Bhawal Estate heritage sites": ["Bhawal estate", "Joydebpur"],
    "Nagari historic Catholic settlement": ["Nagari, Gazipur", "Kaliganj Upazila, Gazipur"],
    "Bangabandhu Sheikh Mujib Safari Park": ["Bangabandhu Sheikh Mujib Safari Park", "Safari park"],
    "Bhawal National Park": ["Bhawal National Park", "Gazipur"],
    "Nuhash Polli": ["Nuhash Polli", "Humayun Ahmed"],
    "Bangladesh Agricultural Research Institute gardens and grounds": ["Bangladesh Agricultural Research Institute", "Joydebpur"],
    "Turag Waterfront": ["Turag River", "Gazipur"],

    # Narsingdi
    "Wari-Bateshwar Archaeological Site": ["Wari-Bateshwar", "Wari-Bateshwar ruins"],
    "Sonaimuri Tek": ["Sonaimuri Tek", "Shibpur Upazila"],
    "Ashrafpur Mosque": ["Ashrafpur", "Shibpur Upazila, Narsingdi"],
    "Parulia Shahi Mosque": ["Parulia Mosque", "Palash Upazila"],
    "Historic Shibpur landscape": ["Shibpur Upazila", "Narsingdi"],
    "Dream Holiday Park": ["Dream Holiday Park", "Narsingdi"],
    "Meghna Riverfront, Raipura": ["Meghna River", "Raipura Upazila"],
    "Balapur Zamindar Bari": ["Balapur Zamindar Bari", "Madhabdi"],
    "Belabo Countryside": ["Belabo Upazila", "Narsingdi"],
    "Shekherchar Baburhat Textile Market": ["Baburhat", "Madhabdi", "Narsingdi"],

    # Manikganj
    "Baliati Palace": ["Baliati Palace", "Baliati Prasadh"],
    "Teota Zamindar Bari": ["Teota Zamindar Bari", "Teota"],
    "Dhankora Zamindar Bari": ["Dhankora", "Saturia Upazila"],
    "Machain Mosque": ["Harirampur Upazila", "Manikganj"],
    "Betila Palace / Zamindar Bari": ["Betila", "Manikganj"],
    "Aricha Ghat": ["Aricha Ghat", "Jamuna River"],
    "Padma Riverbank, Harirampur": ["Padma River", "Harirampur Upazila"],
    "Kaliganga Riverfront, Manikganj Sadar": ["Kaliganga River", "Manikganj"],
    "Noboganga and surrounding countryside": ["Singair Upazila", "Manikganj"],
    "Manikganj Sweetmeat Quarter": ["Manikganj", "Patali Gur"],

    # Shariatpur
    "Fatehjangpur Fort": ["Fatehjangpur", "Naria Upazila"],
    "Dhanuka Manasa Bari / historic temples": ["Dhanuka", "Shariatpur"],
    "Rudrakar Math": ["Rudrakar Math", "Shariatpur"],
    "Burirhat historic mosque": ["Bhedarganj Upazila", "Shariatpur"],
    "Kurashi zamindar-era heritage": ["Shariatpur District"],
    "Padma Riverbank, Naria": ["Naria Upazila", "Padma River"],
    "Jazira Padma Bridge approach and char areas": ["Padma Bridge", "Jazira Upazila"],
    "Shakhipur riverine countryside": ["Shakhipur", "Bhedarganj Upazila"],
    "Damudya countryside and canal landscapes": ["Damudya Upazila", "Shariatpur"],
    "Shariatpur town park and central dighi": ["Shariatpur town", "Shariatpur"],

    # Madaripur
    "Jhaudi Giri Mosque": ["Jhaudi", "Madaripur"],
    "Aoliapur Neelkuthi": ["Aoliapur", "Madaripur"],
    "Senapati Dighi": ["Senapati Dighi", "Kalkini Upazila"],
    "Charmuguria Port historic quarter": ["Charmuguria", "Madaripur"],
    "Ganesh Pagal Ashram": ["Ganesh Pagal", "Kadambari"],
    "Madaripur Shakuni Lake": ["Shakuni Lake", "Madaripur"],
    "Arial Khan Riverfront, Madaripur Sadar": ["Arial Khan River", "Madaripur"],
    "Shibchar riverine landscape": ["Shibchar Upazila", "Madaripur"],
    "Rajoir wetland and rural countryside": ["Rajoir Upazila", "Madaripur"],
    "Kalkini canal and river scenes": ["Kalkini Upazila", "Madaripur"],

    # Tangail
    "Atia Mosque": ["Atia Mosque", "Delduar Upazila"],
    "Mohera Zamindar Bari": ["Mohera Zamindar Bari", "Mirzapur Upazila, Tangail"],
    "Dhanbari Nawab Palace": ["Dhanbari Nawab Palace", "Dhanbari Upazila"],
    "Pakulla Zamindar Bari": ["Pakulla", "Mirzapur Upazila"],
    "Hemnagar Zamindar Bari": ["Hemnagar Zamindar Bari", "Gopalpur Upazila"],
    "Madhupur National Park": ["Madhupur National Park", "Madhupur tract"],
    "Jamuna Riverbank, Bhuapur": ["Jamuna River", "Bhuapur Upazila"],
    "201 Dome Mosque": ["201 Dome Mosque", "Gopalpur, Tangail"],
    "Tangail Porabari Chomchom Lane": ["Chomchom", "Porabari", "Tangail"],
    "Karatia Zamindar Bari and Canal": ["Karatia Zamindar Bari", "Karatia, Tangail"],

    # Brahmanbaria
    "Arifail Mosque": ["Arifail Mosque", "Sarail Upazila"],
    "Hatirpul": ["Hatirpul", "Sarail Upazila"],
    "Kharampur Mazar Sharif": ["Kharampur Mazar Sharif", "Akhaura Upazila"],
    "Kalbhairab Temple": ["Kalbhairab Temple, Brahmanbaria", "Medda, Brahmanbaria"],
    "Ustad Alauddin Khan Memorial": ["Alauddin Khan", "Brahmanbaria"],
    "Titas Riverfront": ["Titas River", "Brahmanbaria"],
    "Akhaura Land Port and border viewpoint": ["Akhaura", "Agartala border"],
    "Sarail Greyhound area and rural villages": ["Sarail hound", "Sarail Upazila"],
    "Kasba border landscape and Shahid Memorial": ["Kasba Upazila", "Brahmanbaria"],
    "Brahmanbaria town confectionery lane": ["Chhanamukhi", "Brahmanbaria"],

    # Rajbari
    "Mir Mosharraf Hossain Memorial": ["Mir Mosharraf Hossain", "Padamdi"],
    "Kalyan Dighi": ["Baliakandi Upazila", "Rajbari"],
    "Chandana River heritage settlements": ["Chandana River", "Pangsha Upazila"],
    "Samadhinagar Math": ["Rajbari District"],
    "Historic Goalando railway junction heritage": ["Goalondo Ghat", "Eastern Bengal Railway"],
    "Daulatdia Ghat and Padma Riverfront": ["Daulatdia", "Goalando Upazila"],
    "Godar Bazar Padma River Viewpoint": ["Padma River", "Rajbari"],
    "Gorai Riverbank": ["Gorai River", "Pangsha Upazila"],
    "Baliakandi rural countryside": ["Baliakandi Upazila", "Rajbari"],
    "Rajbari Town Park and Lal Pahar area": ["Rajbari town", "Rajbari"],

    # Chandpur
    "Rupsha Zamindar Bari": ["Rupsha Zamindar Bari", "Faridganj Upazila"],
    "Sachar Jagannath Dham": ["Sachar, Chandpur", "Kachua Upazila, Chandpur"],
    "Bakila Shahi Mosque": ["Haziganj Upazila", "Chandpur"],
    "Haziganj Historical Boro Masjid": ["Hajiganj Boro Masjid", "Haziganj"],
    "Meherswar Kali Temple": ["Shahrasti Upazila", "Chandpur"],
    "Chandpur Mohona (Mollahed Tri-River Estuary)": ["Chandpur, Bangladesh", "Meghna River"],
    "Boro Station Launch Terminal and Riverfront": ["Chandpur launch terminal", "Chandpur Sadar"],
    "Meghna-Dhonagoda Irrigation Project and Embankment": ["Meghna-Dhonagoda", "Matlab Uttar"],
    "Chandpur Hilsa Fish Market": ["Ilish", "Chandpur, Bangladesh"],
    "Mini Cox's Bazar / Char Riverfront": ["Rajrajeshwar", "Chandpur"],

    # Mymensingh
    "Shashi Lodge (Rajbari)": ["Shashi Lodge", "Mymensingh"],
    "Muktagacha Zamindar Bari": ["Muktagacha Rajbari", "Muktagacha"],
    "Alexander Castle": ["Alexander Castle, Mymensingh", "Mymensingh"],
    "Gouripur Lodge": ["Gouripur, Mymensingh", "Mymensingh"],
    "Bangladesh Agricultural University historic campus landmarks": ["Bangladesh Agricultural University", "Mymensingh"],
    "Brahmaputra Riverfront": ["Brahmaputra River", "Mymensingh"],
    "Birisiri and China Clay Hills": ["Birisiri", "Durgapur, Netrokona"],
    "Zainul Abedin Sangrahashala": ["Zainul Abedin Museum", "Mymensingh"],
    "Mymensingh Museum": ["Mymensingh Museum"],
    "Shilpacharya Zainul Abedin Park / riverfront promenade": ["Mymensingh town", "Zainul Abedin"],

    # Kishoreganj
    "Egarosindur historic settlement": ["Egarosindur", "Pakundia Upazila"],
    "Shah Mahmud Mosque": ["Shah Mahmud Mosque", "Egarosindur"],
    "Sadi Mosque": ["Sadi Mosque", "Egarosindur"],
    "Jangalbari Fort / Isa Khan's residence remains": ["Jangalbari Fort", "Karimganj Upazila"],
    "Pagla Mosque": ["Pagla Mosque", "Kishoreganj"],
    "Nikli Haor": ["Nikli Haor", "Nikli Upazila"],
    "Mithamain–Austagram road and haor views": ["All-weather road, Kishoreganj", "Mithamain Upazila"],
    "Austagram Haor landscape": ["Austagram Upazila", "Qutub Shahi Mosque"],
    "Bhairab Bridge and Meghna river views": ["Bhairab Bridge", "Bhairab Upazila"],
    "Chandrabati Temple": ["Chandrabati", "Kishoreganj"],

    # Sirajganj
    "Hatikumrul Navaratna Temple": ["Hatikumrul Navaratna Temple", "Ullapara Upazila"],
    "Shahjadpur Rabindra Kachharibari": ["Rabindra Kachharibari", "Shahjadpur Upazila"],
    "Nolaka / local zamindar-era heritage buildings": ["Sirajganj District", "Sirajganj"],
    "Makhdum Shah's Shrine": ["Makhdum Shah Daulah", "Shahjadpur"],
    "Historic Sirajganj river-port and trading quarter": ["Sirajganj", "Jamuna River"],
    "Bangabandhu Jamuna Bridge viewpoint": ["Jamuna Bridge", "Bangabandhu Bridge"],
    "Jamuna Riverbank and char landscape": ["Jamuna River", "Sirajganj"],
    "Jamuna Eco Park / riverfront leisure area": ["Jamuna Bridge", "Sirajganj"],
    "Enayetpur riverside area": ["Enayetpur", "Chauhali Upazila"],
    "Sirajganj town markets and local food streets": ["Sirajganj town", "Sirajganj"],

    # Faridpur
    "Mathurapur Deul": ["Mathurapur Deul", "Madhukhali Upazila"],
    "Shatair Mosque": ["Shatair Mosque", "Boalmari Upazila"],
    "Faridpur Rajbari / old estate buildings": ["Faridpur, Bangladesh", "Faridpur"],
    "Basudev Temple heritage site": ["Faridpur District", "Faridpur"],
    "Historic Ambikapur settlement": ["Jasimuddin", "Ambikapur, Faridpur"],
    "Padma Riverbank, Char Bhadrasan": ["Char Bhadrasan Upazila", "Padma River"],
    "Kanaipur rural countryside": ["Kanaipur", "Faridpur Sadar"],
    "Madhukhali countryside and river landscape": ["Madhukhali Upazila", "Faridpur"],
    "Faridpur town public spaces and markets": ["Faridpur, Bangladesh", "Faridpur town"],
    "Arial Khan Riverbank": ["Arial Khan River", "Faridpur"],

    # Jamalpur
    "Hazrat Shah Jamal Shrine": ["Jamalpur, Bangladesh", "Shah Jamal"],
    "Hazrat Shah Kamal Shrine": ["Jamalpur District"],
    "Malancha Mosque / historic mosque area": ["Jamalpur District"],
    "Doyamoyee Temple": ["Doyamoyee Temple", "Jamalpur"],
    "Historic Jamalpur town centre": ["Jamalpur, Bangladesh"],
    "Jamuna Riverbank": ["Jamuna River", "Sarishabari"],
    "Jamalpur town park and public spaces": ["Jamalpur, Bangladesh"],
    "Sarishabari river and countryside": ["Sarishabari Upazila", "Jamalpur"],
    "Dewanganj riverine landscape": ["Dewanganj Upazila", "Jamalpur"],
    "Jamalpur local handloom and craft markets": ["Nakshi kantha", "Jamalpur"]
}

def search_wikimedia_image(query_list):
    for q in query_list:
        clean = q.replace(' ', '_')
        # 1. Direct pageimage query
        url = f"https://en.wikipedia.org/w/api.php?action=query&titles={urllib.parse.quote(clean)}&prop=pageimages&format=json&pithumbsize=1600"
        try:
            req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
            with urllib.request.urlopen(req, timeout=4) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                pages = data.get('query', {}).get('pages', {})
                for pid, pdata in pages.items():
                    if pid != '-1' and 'thumbnail' in pdata:
                        return pdata['thumbnail']['source']
        except Exception:
            pass

        # 2. Generator search query
        url2 = f"https://en.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrlimit=1&prop=pageimages&format=json&pithumbsize=1600"
        try:
            req2 = urllib.request.Request(url2, headers={'User-Agent': USER_AGENT})
            with urllib.request.urlopen(req2, timeout=4) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                pages = data.get('query', {}).get('pages', {})
                for pid, pdata in pages.items():
                    if pid != '-1' and 'thumbnail' in pdata:
                        return pdata['thumbnail']['source']
        except Exception:
            pass

        # 3. Commons image search
        url3 = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrlimit=1&gsrnamespace=6&prop=imageinfo&iiprop=url&iiurlwidth=1600&format=json"
        try:
            req3 = urllib.request.Request(url3, headers={'User-Agent': USER_AGENT})
            with urllib.request.urlopen(req3, timeout=4) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                pages = data.get('query', {}).get('pages', {})
                for pid, pdata in pages.items():
                    if pid != '-1' and 'imageinfo' in pdata and len(pdata['imageinfo']) > 0:
                        info = pdata['imageinfo'][0]
                        return info.get('thumburl') or info.get('url')
        except Exception:
            pass
            
    return None

def download_and_crop(url, out_path, target_size=(1200, 675)):
    temp_file = out_path + ".temp"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        with urllib.request.urlopen(req, timeout=10) as response, open(temp_file, 'wb') as out_file:
            out_file.write(response.read())

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
            img.save(out_path, 'WEBP', quality=85, method=6)

        if os.path.exists(temp_file):
            os.remove(temp_file)
        return True
    except Exception as e:
        if os.path.exists(temp_file):
            os.remove(temp_file)
        return False

PALETTES = [
    ((6, 95, 70), (4, 47, 34)),      # Deep Emerald to Forest
    ((15, 23, 42), (8, 47, 73)),     # Slate Navy to Ocean
    ((127, 29, 29), (69, 10, 10)),   # Crimson Red to Maroon
    ((19, 78, 74), (4, 47, 46)),     # Deep Teal to Cypress
    ((120, 53, 15), (67, 20, 7)),    # Rich Ochre to Dark Amber
    ((49, 46, 129), (30, 27, 75)),   # Royal Indigo to Night Sky
    ((88, 28, 135), (59, 7, 100)),   # Imperial Violet to Mulberry
    ((30, 41, 59), (15, 23, 42)),    # Midnight Slate
    ((20, 83, 45), (5, 46, 22)),     # Forest Moss
    ((136, 19, 55), (76, 5, 25))     # Rosewood Crimson
]

def generate_artistic_fallback(out_path, title, subtitle, district_name, target_size=(1200, 675), palette_idx=0):
    w, h = target_size
    col_top, col_bot = PALETTES[palette_idx % len(PALETTES)]

    # 1. Base gradient
    base = Image.new('RGB', (w, h), col_top)
    draw = ImageDraw.Draw(base)

    for y in range(h):
        r = int(col_top[0] + (col_bot[0] - col_top[0]) * (y / h))
        g = int(col_top[1] + (col_bot[1] - col_top[1]) * (y / h))
        b = int(col_top[2] + (col_bot[2] - col_top[2]) * (y / h))
        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # 2. Atmospheric lighting circles
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    
    accent_r = int((col_top[0] + 80) % 255)
    accent_g = int((col_top[1] + 100) % 255)
    accent_b = int((col_top[2] + 90) % 255)

    ov_draw.ellipse([(-w // 4, -h // 4), (w // 2, h // 2)], fill=(accent_r, accent_g, accent_b, 45))
    ov_draw.ellipse([(w // 2, h // 3), (w + w // 3, h + h // 3)], fill=(255, 255, 255, 20))
    ov_draw.ellipse([(w // 4, h // 4), (3 * w // 4, 3 * h // 4)], outline=(255, 255, 255, 18), width=3)
    ov_draw.ellipse([(w // 4 - 40, h // 4 - 40), (3 * w // 4 + 40, 3 * h // 4 + 40)], outline=(255, 255, 255, 10), width=1)

    # Darker vignette bar at the bottom for text legibility
    for y in range(int(h * 0.45), h):
        alpha = int(220 * ((y - h * 0.45) / (h * 0.55)))
        ov_draw.line([(0, y), (w, y)], fill=(0, 0, 0, alpha))

    base = Image.alpha_composite(base.convert('RGBA'), overlay).convert('RGB')
    final_draw = ImageDraw.Draw(base)

    # 3. Typography
    try:
        font_dist = ImageFont.truetype("arialbd.ttf", 24)
        font_title = ImageFont.truetype("arialbd.ttf", 46)
        font_sub = ImageFont.truetype("arial.ttf", 26)
    except Exception:
        font_dist = font_title = font_sub = ImageFont.load_default()

    margin_x = 70
    bot_y = h - 85

    # Subtitle
    final_draw.text((margin_x, bot_y), subtitle[:75], fill=(226, 232, 240), font=font_sub)
    # Title
    title_y = bot_y - 65
    final_draw.text((margin_x, title_y), title[:50], fill=(255, 255, 255), font=font_title)
    
    # District badge tag
    badge_y = title_y - 45
    badge_text = f"EZZE MAP  •  {district_name.upper()} HERITAGE"
    badge_w = len(badge_text) * 11 + 20
    final_draw.rectangle([margin_x, badge_y - 4, margin_x + badge_w, badge_y + 24], fill=(255, 255, 255, 30), outline=(255, 255, 255, 120))
    final_draw.text((margin_x + 10, badge_y), badge_text, fill=(248, 250, 252), font=font_dist)

    base.save(out_path, 'WEBP', quality=85, method=6)
    return True

def process_all_15():
    with open('scripts/curated_all_27.json', 'r', encoding='utf-8') as f:
        catalog = json.load(f)

    total_images = 0
    total_downloaded = 0
    total_generated = 0

    for slug in TARGET_SLUGS:
        d = catalog.get(slug)
        if not d:
            print(f"Skipping {slug}, not found in catalog")
            continue

        dist_name = d['en']
        out_dir = os.path.join('images', 'districts', slug)
        os.makedirs(out_dir, exist_ok=True)
        print(f"\nProcessing {dist_name} ({slug})...")

        # 1. Hero Image (1600x900)
        hero_path = os.path.join(out_dir, "hero.webp")
        total_images += 1
        hero_queries = [f"{dist_name} District", dist_name, f"{dist_name} Bangladesh"]
        thumb = search_wikimedia_image(hero_queries)
        if thumb and download_and_crop(thumb, hero_path, target_size=(1600, 900)):
            print("  ✓ hero.webp (Wikimedia)")
            total_downloaded += 1
        else:
            generate_artistic_fallback(hero_path, d['hero_title_en'], d['hero_sub_en'], dist_name, target_size=(1600, 900), palette_idx=0)
            print("  ★ hero.webp (Artistic High-Res)")
            total_generated += 1

        # 2. Carousel Images 1..5 (1200x750)
        for idx, car in enumerate(d.get('carousel', [])):
            c_num = idx + 1
            c_path = os.path.join(out_dir, f"carousel-{c_num}.webp")
            total_images += 1
            c_title = car['titleEn']
            c_sub = car['subtitleEn']
            queries = CUSTOM_SEARCH_KEYS.get(c_title, [c_title, f"{c_title} {dist_name}", f"{dist_name}"])
            thumb = search_wikimedia_image(queries)
            if thumb and download_and_crop(thumb, c_path, target_size=(1200, 750)):
                print(f"  ✓ carousel-{c_num}.webp (Wikimedia)")
                total_downloaded += 1
            else:
                generate_artistic_fallback(c_path, c_title, c_sub, dist_name, target_size=(1200, 750), palette_idx=c_num)
                print(f"  ★ carousel-{c_num}.webp (Artistic High-Res)")
                total_generated += 1

        # 3. Historical spots 1..5 (1200x675)
        for idx, h in enumerate(d.get('hist', [])):
            h_num = idx + 1
            h_path = os.path.join(out_dir, f"hist-{h_num}.webp")
            total_images += 1
            h_name = h['nameEn']
            h_cat = h['categoryEn']
            queries = CUSTOM_SEARCH_KEYS.get(h_name, [h_name, f"{h_name} {dist_name}", f"{dist_name}"])
            thumb = search_wikimedia_image(queries)
            if thumb and download_and_crop(thumb, h_path, target_size=(1200, 675)):
                print(f"  ✓ hist-{h_num}.webp: {h_name} (Wikimedia)")
                total_downloaded += 1
            else:
                generate_artistic_fallback(h_path, h_name, f"{h_cat} • {h['locationEn']}", dist_name, target_size=(1200, 675), palette_idx=h_num + 2)
                print(f"  ★ hist-{h_num}.webp: {h_name} (Artistic High-Res)")
                total_generated += 1

        # 4. Tourist spots 1..5 (1200x675)
        for idx, t in enumerate(d.get('tour', [])):
            t_num = idx + 1
            t_path = os.path.join(out_dir, f"tour-{t_num}.webp")
            total_images += 1
            t_name = t['nameEn']
            t_cat = t['categoryEn']
            queries = CUSTOM_SEARCH_KEYS.get(t_name, [t_name, f"{t_name} {dist_name}", f"{dist_name}"])
            thumb = search_wikimedia_image(queries)
            if thumb and download_and_crop(thumb, t_path, target_size=(1200, 675)):
                print(f"  ✓ tour-{t_num}.webp: {t_name} (Wikimedia)")
                total_downloaded += 1
            else:
                generate_artistic_fallback(t_path, t_name, f"{t_cat} • {t['locationEn']}", dist_name, target_size=(1200, 675), palette_idx=t_num + 5)
                print(f"  ★ tour-{t_num}.webp: {t_name} (Artistic High-Res)")
                total_generated += 1

    print(f"\n==========================================")
    print(f"Total processed images: {total_images}")
    print(f"Wikimedia photos: {total_downloaded}")
    print(f"Artistic High-Res banners: {total_generated}")
    print(f"All 15 districts now have complete image suites in images/districts/<slug>/")

if __name__ == '__main__':
    process_all_15()
