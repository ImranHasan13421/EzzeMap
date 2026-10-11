import os
from PIL import Image, ImageDraw, ImageFont

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

# Path to the generated Lalbagh Fort image
artifact_hero_jpg = r"C:\Users\imran\.gemini\antigravity-ide\brain\569be0d8-2861-4da9-94bf-4a82eb3dc98a\dhaka_lalbagh_fort_1791737843907.jpg"

dhaka_dir = os.path.join("images", "districts", "dhaka")
ensure_dir(dhaka_dir)

# 1. Convert Lalbagh Fort to hero.webp (1920x1080 optimized webp)
if os.path.exists(artifact_hero_jpg):
    with Image.open(artifact_hero_jpg) as img:
        img = img.resize((1920, 1080), Image.Resampling.LANCZOS)
        hero_path = os.path.join(dhaka_dir, "hero.webp")
        img.save(hero_path, "WEBP", quality=85)
        print(f"Saved {hero_path}")
else:
    print(f"Artifact {artifact_hero_jpg} not found, generating programmatically")

# Helper to generate styled artistic gradient banner
def create_artistic_webp(output_path, title, subtitle, tag, color_start, color_end, width=1280, height=720):
    img = Image.new("RGB", (width, height), color=color_start)
    draw = ImageDraw.Draw(img)

    # Gradient fill
    r1, g1, b1 = color_start
    r2, g2, b2 = color_end
    for y in range(height):
        ratio = y / height
        r = int(r1 * (1 - ratio) + r2 * ratio)
        g = int(g1 * (1 - ratio) + g2 * ratio)
        b = int(b1 * (1 - ratio) + b2 * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))

    # Geometric ambient accents
    # Outer circle
    draw.ellipse([width - 300, -100, width + 200, 400], outline=(255, 255, 255, 30), width=3)
    draw.ellipse([width - 250, -50, width + 150, 350], outline=(16, 185, 129, 60), width=2)
    # Bottom left glow
    draw.ellipse([-100, height - 300, 300, height + 100], outline=(244, 42, 65, 40), width=2)

    # Accent badge box
    draw.rounded_rectangle([60, height - 180, 240, height - 140], radius=8, fill=(16, 185, 129))
    draw.text((75, height - 170), tag, fill=(255, 255, 255))

    # Main text title
    draw.text((60, height - 125), title, fill=(255, 255, 255))
    draw.text((60, height - 85), subtitle, fill=(203, 213, 225))

    # Top right watermark
    draw.text((width - 220, 40), "LOCAL HOST • BD 64", fill=(148, 163, 184))

    img.save(output_path, "WEBP", quality=82)
    print(f"Generated {output_path}")

# Palette definitions
PALETTES = [
    ((6, 95, 70), (4, 47, 34)),      # Deep Emerald to Forest
    ((15, 23, 42), (8, 47, 73)),     # Slate Navy to Ocean
    ((127, 29, 29), (69, 10, 10)),   # Crimson Red to Maroon
    ((19, 78, 74), (4, 47, 46)),     # Deep Teal to Cypress
    ((49, 46, 129), (17, 24, 39)),   # Indigo to Obsidian
]

# Generate Dhaka Carousel (5 items)
carousel_items = [
    ("Lalbagh Fort & Mughal Terraces", "17th-century Mughal fort complex and Bibi Pari mausoleum", "HERITAGE"),
    ("Ahsan Manzil (Pink Palace)", "Nawab residential palace overlooking the Buriganga river", "PALACE"),
    ("National Parliament House", "Louis Kahn's monumental brutalist modernist landmark", "ARCHITECTURE"),
    ("Hatirjheel Waterfront Promenade", "Illuminated urban lake, pedestrian bridges, and water taxis", "RECREATION"),
    ("Dhakeshwari National Temple", "Centuries of cultural heritage in historic Old Dhaka", "SACRED")
]

for i, (title, sub, tag) in enumerate(carousel_items):
    c_path = os.path.join(dhaka_dir, f"carousel-{i+1}.webp")
    p1, p2 = PALETTES[i % len(PALETTES)]
    create_artistic_webp(c_path, title, sub, tag, p1, p2, width=1280, height=800)

# Generate Dhaka Historical Places (5 items)
hist_items = [
    ("Lalbagh Fort Complex", "Mausoleum of Pari Bibi, Hammamkhana and 3-domed Mosque", "MUGHAL FORT"),
    ("Ahsan Manzil Royal Palace", "Grand Pink Palace and 23 museum gallery archives", "PALATIAL"),
    ("Tara Masjid (Star Mosque)", "Chinitikri porcelain star mosaic craftsmanship in Armanitola", "CHINITIKRI"),
    ("Chhota Katra & Bara Katra", "17th-century fortified commercial caravanserais in Chawkbazar", "CARAVANSERAI"),
    ("Dhakeshwari Temple", "National Hindu temple sanctuary dating to the 12th-century Sena era", "HISTORIC TEMPLE")
]

for i, (title, sub, tag) in enumerate(hist_items):
    h_path = os.path.join(dhaka_dir, f"hist-{i+1}.webp")
    p1, p2 = PALETTES[(i + 1) % len(PALETTES)]
    create_artistic_webp(h_path, title, sub, tag, p1, p2, width=960, height=540)

# Generate Dhaka Tourist Attractions (5 items)
tour_items = [
    ("National Parliament House", "Monumental brutalist masterpiece by architect Louis Kahn", "MONUMENT"),
    ("Hatirjheel Lakeside Corridor", "Scenic pedestrian promenades and evening musical fountain", "WATERFRONT"),
    ("Bangladesh National Museum", "Four expansive floors of archaeology, art, and liberation archives", "MUSEUM"),
    ("Dhanmondi Lake & Rabindra Sarobar", "Serene aquatic parkway, jogging tracks, and open-air theater", "PARKWAY"),
    ("Ramna Park & Suhrawardy Udyan", "Centenary banyan trees and historical national monuments", "BOTANICAL")
]

for i, (title, sub, tag) in enumerate(tour_items):
    t_path = os.path.join(dhaka_dir, f"tour-{i+1}.webp")
    p1, p2 = PALETTES[(i + 2) % len(PALETTES)]
    create_artistic_webp(t_path, title, sub, tag, p1, p2, width=960, height=540)

# Also generate default/fallback images for any missing district links
fallback_dir = os.path.join("images", "default")
ensure_dir(fallback_dir)
create_artistic_webp(os.path.join(fallback_dir, "hero.webp"), "Explore Bangladesh", "Discover authentic heritage across 64 districts", "LOCAL HOST", (4, 47, 34), (6, 95, 70), 1920, 1080)
create_artistic_webp(os.path.join(fallback_dir, "card.webp"), "District Archive", "Historical and scenic preservation records", "ARCHIVE", (15, 23, 42), (8, 47, 73), 960, 540)

# If hero.webp was not created from artifact, create artistic one
hero_path = os.path.join(dhaka_dir, "hero.webp")
if not os.path.exists(hero_path):
    create_artistic_webp(hero_path, "Dhaka (ঢাকা)", "Historic Mughal Metropolis & Modern Capital of Bangladesh", "CAPITAL", (4, 47, 34), (6, 95, 70), 1920, 1080)

print("All WebP images generated successfully!")
