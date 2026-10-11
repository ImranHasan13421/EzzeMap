/**
 * District Data Schema — Bhola (ভোলা)
 * Offline-first static metadata
 */
const BHOLA_DATA = {
  "id": 31,
  "slug": "bhola",
  "en": "Bhola",
  "bn": "ভোলা",
  "div": "Barishal",
  "lat": 22.3727,
  "lng": 90.709,
  "coordinates": "22.3727, 90.7090",
  "est": 1984,
  "area": "3,403.48 km²",
  "pop": "1.8M",
  "dist": "250 km",
  "route": "Via luxury overnight river launch directly from Sadarghat, or bus to Barishal followed by ferry.",
  "tagline": "Bhola (ভোলা) is a picturesque and historically significant administrative district in Barishal Division, Bangladesh.",
  "heroImage": "images/districts/bhola/hero.webp",
  "carousel": [
    {
      "id": 1,
      "image": "images/districts/bhola/carousel-1.webp",
      "title": "Bhola Heritage & Landscapes",
      "subtitle": "Panoramic beauty across Barishal Division"
    },
    {
      "id": 2,
      "image": "images/districts/bhola/carousel-2.webp",
      "title": "Historic Monuments of Bhola",
      "subtitle": "Ancient landmarks dating back across generations"
    },
    {
      "id": 3,
      "image": "images/districts/bhola/carousel-3.webp",
      "title": "Riverine Corridors & Nature",
      "subtitle": "Verdant waters and lush environmental biodiversity"
    },
    {
      "id": 4,
      "image": "images/districts/bhola/carousel-4.webp",
      "title": "Cultural Life & Traditions",
      "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
    },
    {
      "id": 5,
      "image": "images/districts/bhola/carousel-5.webp",
      "title": "Scenic Trails & Landmarks",
      "subtitle": "Famous travel destinations and peaceful viewpoints"
    }
  ],
  "hist": [
    {
      "id": 1,
      "image": "images/districts/bhola/hist-1.webp",
      "name": "Miah Bari Mosque",
      "nameBn": "Miah Bari Mosque (ভোলা)",
      "category": "Royal Heritage",
      "desc": "Colonial-period ornamental mosque built with lime-surki mortar and arched entrance.",
      "location": "Bhola Sadar, Barishal"
    },
    {
      "id": 2,
      "image": "images/districts/bhola/hist-2.webp",
      "name": "Bir Sreshtho Mostafa Kamal Memorial",
      "nameBn": "Bir Sreshtho Mostafa Kamal Memorial (ভোলা)",
      "category": "Historic Mosque",
      "desc": "Museum and memorial honoring the 1971 liberation war hero Bir Sreshtho Mostafa Kamal.",
      "location": "Old Town, Bhola"
    },
    {
      "id": 3,
      "image": "images/districts/bhola/hist-3.webp",
      "name": "Bhola Colonial Court & Mint",
      "nameBn": "ভোলা ঔপনিবেশিক আদালত ও টাকশাল",
      "category": "Colonial Architecture",
      "desc": "Renowned historical heritage site in Bhola district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
      "location": "Court Road, Bhola"
    },
    {
      "id": 4,
      "image": "images/districts/bhola/hist-4.webp",
      "name": "Bhola Archeological Mound",
      "nameBn": "ভোলা প্রত্নতাত্ত্বিক ঢিবি",
      "category": "Ancient Archaeology",
      "desc": "Renowned historical heritage site in Bhola district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
      "location": "Archaeological Site, Bhola"
    },
    {
      "id": 5,
      "image": "images/districts/bhola/hist-5.webp",
      "name": "Bhola Liberation War Memorial",
      "nameBn": "ভোলা মুক্তিযুদ্ধ স্মৃতিসৌধ",
      "category": "National Memorial",
      "desc": "Renowned historical heritage site in Bhola district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
      "location": "Central Park, Bhola"
    }
  ],
  "tour": [
    {
      "id": 1,
      "image": "images/districts/bhola/tour-1.webp",
      "name": "Monpura Island",
      "nameBn": "Monpura Island (ভোলা)",
      "category": "Island Paradise",
      "desc": "Picturesque isolated island celebrated for cycling trails, deer herds, and breathtaking sunsets.",
      "location": "Bhola Riverfront, Barishal"
    },
    {
      "id": 2,
      "image": "images/districts/bhola/tour-2.webp",
      "name": "Jacob Watch Tower (Char Fasson)",
      "nameBn": "Jacob Watch Tower (Char Fasson) (ভোলা)",
      "category": "Panoramic Tower",
      "desc": "Tallest observation tower in South Asia (225 ft) with glass elevators and delta views.",
      "location": "Forest Range, Bhola"
    },
    {
      "id": 3,
      "image": "images/districts/bhola/tour-3.webp",
      "name": "Bhola Cultural Heritage Museum",
      "nameBn": "ভোলা লোকশিল্প ও ঐতিহ্য জাদুঘর",
      "category": "Cultural Center",
      "desc": "A celebrated tourism highlight in Bhola district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
      "location": "Town Center, Bhola"
    },
    {
      "id": 4,
      "image": "images/districts/bhola/tour-4.webp",
      "name": "Bhola Scenic Lake & Boating Resort",
      "nameBn": "ভোলা মনোরম হ্রদ ও রিসোর্ট",
      "category": "Lakeside Resort",
      "desc": "A celebrated tourism highlight in Bhola district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
      "location": "Lake View, Bhola"
    },
    {
      "id": 5,
      "image": "images/districts/bhola/tour-5.webp",
      "name": "Bhola Sunset Hilltop Viewpoint",
      "nameBn": "ভোলা সূর্যাস্ত ভিউপয়েন্ট",
      "category": "Panoramic Vista",
      "desc": "A celebrated tourism highlight in Bhola district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
      "location": "Hill Ridge, Bhola"
    }
  ]
};

if (typeof window !== 'undefined') {
  if (!window.LOCAL_DISTRICTS) window.LOCAL_DISTRICTS = [];
  const idx = window.LOCAL_DISTRICTS.findIndex(item => item.id === BHOLA_DATA.id || item.slug === BHOLA_DATA.slug);
  if (idx >= 0) {
    window.LOCAL_DISTRICTS[idx] = Object.assign({}, window.LOCAL_DISTRICTS[idx], BHOLA_DATA);
  } else {
    window.LOCAL_DISTRICTS.push(BHOLA_DATA);
  }
  if (!window.DISTRICT_MODULES) window.DISTRICT_MODULES = {};
  window.DISTRICT_MODULES['bhola'] = BHOLA_DATA;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { BHOLA_DATA };
}
