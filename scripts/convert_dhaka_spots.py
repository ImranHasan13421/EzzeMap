import os
from PIL import Image

BRAIN_DIR = r"C:\Users\imran\.gemini\antigravity-ide\brain\569be0d8-2861-4da9-94bf-4a82eb3dc98a"
TARGET_DIR = r"f:\EzzeMap\images\districts\dhaka"
DEFAULT_DIR = r"f:\EzzeMap\images\default"

os.makedirs(TARGET_DIR, exist_ok=True)
os.makedirs(DEFAULT_DIR, exist_ok=True)

MAPPINGS = {
    "hero.webp": (os.path.join(BRAIN_DIR, "dhaka_lalbagh_fort_1791737843907.jpg"), (1600, 900)),
    "carousel-1.webp": (os.path.join(BRAIN_DIR, "dhaka_lalbagh_fort_1791737843907.jpg"), (1200, 750)),
    "carousel-2.webp": (os.path.join(BRAIN_DIR, "ahsan_manzil_dhaka_1791739603444.jpg"), (1200, 750)),
    "carousel-3.webp": (os.path.join(BRAIN_DIR, "parliament_house_dhaka_1791739696508.jpg"), (1200, 750)),
    "carousel-4.webp": (os.path.join(BRAIN_DIR, "hatirjheel_lake_dhaka_1791739720771.jpg"), (1200, 750)),
    "carousel-5.webp": (os.path.join(BRAIN_DIR, "dhakeshwari_temple_dhaka_1791739671234.jpg"), (1200, 750)),
    
    # Top-5 Historical
    "hist-1.webp": (os.path.join(BRAIN_DIR, "dhaka_lalbagh_fort_1791737843907.jpg"), (1200, 675)),
    "hist-2.webp": (os.path.join(BRAIN_DIR, "ahsan_manzil_dhaka_1791739603444.jpg"), (1200, 675)),
    "hist-3.webp": (os.path.join(BRAIN_DIR, "tara_masjid_dhaka_1791739624650.jpg"), (1200, 675)),
    "hist-4.webp": (os.path.join(BRAIN_DIR, "chhota_katra_dhaka_1791739646376.jpg"), (1200, 675)),
    "hist-5.webp": (os.path.join(BRAIN_DIR, "dhakeshwari_temple_dhaka_1791739671234.jpg"), (1200, 675)),
    
    # Top-5 Tourist
    "tour-1.webp": (os.path.join(BRAIN_DIR, "parliament_house_dhaka_1791739696508.jpg"), (1200, 675)),
    "tour-2.webp": (os.path.join(BRAIN_DIR, "hatirjheel_lake_dhaka_1791739720771.jpg"), (1200, 675)),
    "tour-3.webp": (os.path.join(BRAIN_DIR, "national_museum_dhaka_1791739749171.jpg"), (1200, 675)),
    "tour-4.webp": (os.path.join(BRAIN_DIR, "dhanmondi_lake_dhaka_1791739776536.jpg"), (1200, 675)),
    "tour-5.webp": (os.path.join(BRAIN_DIR, "ramna_park_dhaka_1791739806248.jpg"), (1200, 675)),
}

for filename, (src_path, size) in MAPPINGS.items():
    if os.path.exists(src_path):
        img = Image.open(src_path).convert("RGB")
        img = img.resize(size, Image.Resampling.LANCZOS)
        out_path = os.path.join(TARGET_DIR, filename)
        img.save(out_path, "WEBP", quality=86, method=6)
        print(f"Saved: {out_path} ({os.path.getsize(out_path)} bytes)")
    else:
        print(f"Missing source: {src_path}")

# Also update default fallback images with high quality
default_hero = os.path.join(DEFAULT_DIR, "hero.webp")
default_card = os.path.join(DEFAULT_DIR, "card.webp")
Image.open(os.path.join(BRAIN_DIR, "dhaka_lalbagh_fort_1791737843907.jpg")).resize((1600, 900), Image.Resampling.LANCZOS).save(default_hero, "WEBP", quality=85)
Image.open(os.path.join(BRAIN_DIR, "hatirjheel_lake_dhaka_1791739720771.jpg")).resize((1200, 675), Image.Resampling.LANCZOS).save(default_card, "WEBP", quality=85)
print("Updated default fallback images")
