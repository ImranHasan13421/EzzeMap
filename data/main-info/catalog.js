/**
 * Master Offline-First Catalog for all 64 Districts of Bangladesh
 * Pure local memory buffers — Zero external API dependencies
 */
const LOCAL_DISTRICTS = [
  {
    "id": 1,
    "slug": "dhaka",
    "en": "Dhaka",
    "bn": "ঢাকা",
    "div": "Dhaka",
    "lat": 23.7869,
    "lng": 90.2508,
    "coordinates": "23.7869, 90.2508",
    "est": 1772,
    "area": "1,463.60 km²",
    "pop": "14.7M",
    "dist": "0 km",
    "route": "Central confluence of national transportation. Seamlessly connected to all 8 divisions via prime national expressways (N1, N2, N3, N5), Padma Bridge corridor, high-frequency railway networks from Kamalapur, inland passenger launches at Sadarghat terminal, and direct aviation routes via Hazrat Shahjalal International Airport.",
    "tagline": "The historic Mughal metropolis of Jahangirnagar and the dynamic capital of Bangladesh, harmonizing four centuries of riverine trade and grand heritage.",
    "heroImage": "images/districts/dhaka/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/dhaka/carousel-1.webp",
        "title": "Lalbagh Fort & Mughal Gardens",
        "subtitle": "17th-century bastion of Subahdar Shaista Khan and Prince Azam Shah"
      },
      {
        "id": 2,
        "image": "images/districts/dhaka/carousel-2.webp",
        "title": "Ahsan Manzil on Buriganga",
        "subtitle": "The iconic Pink Palace and ancestral seat of the Nawabs of Dhaka"
      },
      {
        "id": 3,
        "image": "images/districts/dhaka/carousel-3.webp",
        "title": "National Parliament House",
        "subtitle": "Louis Kahn's monumental brutalist architectural marvel in Sher-e-Bangla Nagar"
      },
      {
        "id": 4,
        "image": "images/districts/dhaka/carousel-4.webp",
        "title": "Hatirjheel Waterfront Promenade",
        "subtitle": "Illuminated express bridges and vibrant lakeside transit corridors"
      },
      {
        "id": 5,
        "image": "images/districts/dhaka/carousel-5.webp",
        "title": "Dhakeshwari Heritage & Old Dhaka",
        "subtitle": "Centuries of cultural harmony, historic temples, and bustling spice markets"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/dhaka/hist-1.webp",
        "name": "Lalbagh Fort",
        "nameBn": "লালবাগ কেল্লা",
        "category": "Mughal Architecture",
        "desc": "Commissioned in 1678 by Mughal Prince Muhammad Azam and expanded by Viceroy Shaista Khan, Lalbagh Fort (Fort Aurangabad) stands as the quintessential Mughal monument of Bengal. The complex houses the octagonal mausoleum of Bibi Pari adorned with Rajasthani marble and Persian tiles, an elegant three-domed mosque, and a subterranean Hammamkhana bathhouse set against terraced lawns.",
        "location": "Lalbagh, Old Dhaka, Bangladesh"
      },
      {
        "id": 2,
        "image": "images/districts/dhaka/hist-2.webp",
        "name": "Ahsan Manzil",
        "nameBn": "আহসান মঞ্জিল",
        "category": "Indo-Saracenic Palace",
        "desc": "Perched gracefully along the northern bank of the Buriganga River in Kumartoli, Ahsan Manzil served as the official residential palace and seat of the Nawabs of Dhaka. Reconstructed after the 1888 tornado with an imposing grand dome, triple-arched portals, and neoclassical verandas, the vibrant pink palace now houses 23 museum galleries exhibiting royal artifacts, court costumes, and colonial archives.",
        "location": "Kumartoli, Sadarghat, Old Dhaka"
      },
      {
        "id": 3,
        "image": "images/districts/dhaka/hist-3.webp",
        "name": "Tara Masjid (Star Mosque)",
        "nameBn": "তারা মসজিদ",
        "category": "Chinitikri Mosaic",
        "desc": "Erected in the early 18th century by Mirza Golam Pir in Armanitola, Tara Masjid is renowned for its magnificent chinitikri mosaic craftsmanship utilizing broken pieces of fine Japanese and English porcelain. Redesigned with five domes and two towering minarets, the white marble exterior is adorned with hundreds of glistening blue star motifs and floral porcelain inlays that shimmer in the sunlight.",
        "location": "Armanitola, Old Dhaka, Bangladesh"
      },
      {
        "id": 4,
        "image": "images/districts/dhaka/hist-4.webp",
        "name": "Chhota Katra & Bara Katra",
        "nameBn": "ছোট কাটরা ও বড় কাটরা",
        "category": "Mughal Caravanserai",
        "desc": "Built respectively in 1644 by Prince Shah Shuja's chief architect and in 1663 by Subahdar Shaista Khan, Bara Katra and Chhota Katra were grand fortified caravanserais constructed to host international merchants, diplomats, and travelers arriving along the Buriganga river trade routes. Their massive vaulted archways and octagonal defensive bastions represent early commercial civil engineering in Mughal Bengal.",
        "location": "Chawkbazar, Old Dhaka, Bangladesh"
      },
      {
        "id": 5,
        "image": "images/districts/dhaka/hist-5.webp",
        "name": "Dhakeshwari National Temple",
        "nameBn": "ঢাকেশ্বরী জাতীয় মন্দির",
        "category": "Sacred Heritage",
        "desc": "Regarded as the spiritual namesake of Dhaka city, the Dhakeshwari National Temple traces its historical foundation to the 12th-century Ballal Sen era of the Sena dynasty. Rebuilt with four spires in traditional Bengali chala architecture, the sacred sanctuary serves as the national epicenter for Hindu devotional heritage and major cultural festivals such as Durga Puja.",
        "location": "Dhakeshwari Road, Lalbagh, Dhaka"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/dhaka/tour-1.webp",
        "name": "National Parliament House",
        "nameBn": "জাতীয় সংসদ ভবন",
        "category": "Architectural Marvel",
        "desc": "Designed by legendary modernist architect Louis I. Kahn and completed in 1982, the Jatiya Sangsad Bhaban is globally celebrated as a monumental triumph of twentieth-century architecture. Fabricated with monolithic raw concrete, marble inlays, and geometric light cutouts, the building appears to float serenely over an artificial crescent lake in Sher-e-Bangla Nagar.",
        "location": "Sher-e-Bangla Nagar, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/dhaka/tour-2.webp",
        "name": "Hatirjheel Waterfront Promenade",
        "nameBn": "হাতিরঝিল",
        "category": "Urban Recreation",
        "desc": "Spanning over 300 acres across central Dhaka, Hatirjheel transformed an urban wetland into a world-class recreational lakeside corridor. Illuminated by sweeping cable-stayed viaducts and musical water fountains, the lake features scenic pedestrian promenades, amphitheaters, open-air cafes, and clean electric water taxis connecting Rampura, Gulshan, and Karwan Bazar.",
        "location": "Tejgaon / Gulshan Link, Dhaka"
      },
      {
        "id": 3,
        "image": "images/districts/dhaka/tour-3.webp",
        "name": "Bangladesh National Museum",
        "nameBn": "বাংলাদেশ জাতীয় জাদুঘর",
        "category": "Cultural Exposition",
        "desc": "Established in Shahbagh across four expansive floors and 46 curated galleries, the National Museum houses comprehensive collections spanning Bengal's rich natural history, ancient Maurya and Gupta coins, Buddhist terracotta sculptures, folk musical instruments, and rare wartime archives from the 1971 Bangladesh Liberation War.",
        "location": "Shahbagh, Central Dhaka"
      },
      {
        "id": 4,
        "image": "images/districts/dhaka/tour-4.webp",
        "name": "Dhanmondi Lake & Rabindra Sarobar",
        "nameBn": "ধানমন্ডি লেক ও রবীন্দ্র সরোবর",
        "category": "Lakeside Amphitheater",
        "desc": "A sprawling aquatic haven meandering through residential Dhanmondi, this lake features miles of tree-shaded fitness tracks, wooden footbridges, and paddle-boating waters. The southern bank at Rabindra Sarobar hosts a celebrated open-air amphitheater that vibrates with evening acoustic concerts, poetry recitals, and traditional Bengali street food stalls.",
        "location": "Road 8A, Dhanmondi, Dhaka"
      },
      {
        "id": 5,
        "image": "images/districts/dhaka/tour-5.webp",
        "name": "Ramna Park & Suhrawardy Udyan",
        "nameBn": "রমনা পার্ক ও সোহরাওয়ার্দী উদ্যান",
        "category": "Historic Botanical Garden",
        "desc": "Established during the Mughal era and landscaped as a formal 68-acre botanical park in 1949, Ramna Park is famed for centenary banyan trees and its serene central lake. It serves as the cultural epicenter for Bengali New Year (Pohela Boishakh) celebrations at the Ramna Batamul, alongside the adjacent Independence Monument at Suhrawardy Udyan.",
        "location": "Moulana Bhasani Road, Shahbagh, Dhaka"
      }
    ]
  },
  {
    "id": 2,
    "slug": "faridpur",
    "en": "Faridpur",
    "bn": "ফরিদপুর",
    "div": "Dhaka",
    "lat": 23.4789,
    "lng": 89.8388,
    "coordinates": "23.4789, 89.8388",
    "est": 1815,
    "area": "2,072.72 km²",
    "pop": "1.9M",
    "dist": "138 km",
    "route": "Via Dhaka-Mawa Expressway and Padma Bridge (approx. 2.5 hours by car/bus).",
    "tagline": "Faridpur (ফরিদপুর) is a picturesque and historically significant administrative district in Dhaka Division, Bangladesh.",
    "heroImage": "images/districts/faridpur/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/faridpur/carousel-1.webp",
        "title": "Faridpur Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Dhaka Division"
      },
      {
        "id": 2,
        "image": "images/districts/faridpur/carousel-2.webp",
        "title": "Historic Monuments of Faridpur",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/faridpur/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/faridpur/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/faridpur/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/faridpur/hist-1.webp",
        "name": "Bhatpara Nilkuthi",
        "nameBn": "Bhatpara Nilkuthi (ফরিদপুর)",
        "category": "Royal Heritage",
        "desc": "Bhatpara Nilkuthi is one of the most prominent historical monuments in Faridpur district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Faridpur Sadar, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/faridpur/hist-2.webp",
        "name": "Kanaipur Zamindar Bari",
        "nameBn": "Kanaipur Zamindar Bari (ফরিদপুর)",
        "category": "Historic Mosque",
        "desc": "Kanaipur Zamindar Bari is one of the most prominent historical monuments in Faridpur district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Faridpur"
      },
      {
        "id": 3,
        "image": "images/districts/faridpur/hist-3.webp",
        "name": "Faridpur Colonial Court & Mint",
        "nameBn": "ফরিদপুর ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Faridpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Faridpur"
      },
      {
        "id": 4,
        "image": "images/districts/faridpur/hist-4.webp",
        "name": "Faridpur Archeological Mound",
        "nameBn": "ফরিদপুর প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Faridpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Faridpur"
      },
      {
        "id": 5,
        "image": "images/districts/faridpur/hist-5.webp",
        "name": "Faridpur Liberation War Memorial",
        "nameBn": "ফরিদপুর মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Faridpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Faridpur"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/faridpur/tour-1.webp",
        "name": "Padma River Embankment",
        "nameBn": "Padma River Embankment (ফরিদপুর)",
        "category": "Scenic Riverside",
        "desc": "Padma River Embankment stands as an iconic tourist highlight in Faridpur district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Faridpur Riverfront, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/faridpur/tour-2.webp",
        "name": "Palli Kabi Jasimuddin Homestead",
        "nameBn": "Palli Kabi Jasimuddin Homestead (ফরিদপুর)",
        "category": "Cultural Heritage",
        "desc": "Palli Kabi Jasimuddin Homestead stands as an iconic tourist highlight in Faridpur district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Faridpur"
      },
      {
        "id": 3,
        "image": "images/districts/faridpur/tour-3.webp",
        "name": "Faridpur Cultural Heritage Museum",
        "nameBn": "ফরিদপুর লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Faridpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Faridpur"
      },
      {
        "id": 4,
        "image": "images/districts/faridpur/tour-4.webp",
        "name": "Faridpur Scenic Lake & Boating Resort",
        "nameBn": "ফরিদপুর মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Faridpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Faridpur"
      },
      {
        "id": 5,
        "image": "images/districts/faridpur/tour-5.webp",
        "name": "Faridpur Sunset Hilltop Viewpoint",
        "nameBn": "ফরিদপুর সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Faridpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Faridpur"
      }
    ]
  },
  {
    "id": 3,
    "slug": "gazipur",
    "en": "Gazipur",
    "bn": "গাজীপুর",
    "div": "Dhaka",
    "lat": 24.0984,
    "lng": 90.4449,
    "coordinates": "24.0984, 90.4449",
    "est": 1984,
    "area": "1,741.53 km²",
    "pop": "3.8M",
    "dist": "35 km",
    "route": "Via Dhaka-Mymensingh Highway N3 or commuter trains from Kamalapur (approx. 1 hour).",
    "tagline": "Gazipur (গাজীপুর) is a picturesque and historically significant administrative district in Dhaka Division, Bangladesh.",
    "heroImage": "images/districts/gazipur/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/gazipur/carousel-1.webp",
        "title": "Gazipur Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Dhaka Division"
      },
      {
        "id": 2,
        "image": "images/districts/gazipur/carousel-2.webp",
        "title": "Historic Monuments of Gazipur",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/gazipur/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/gazipur/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/gazipur/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/gazipur/hist-1.webp",
        "name": "Bhawal Rajbari",
        "nameBn": "Bhawal Rajbari (গাজীপুর)",
        "category": "Royal Heritage",
        "desc": "Grand 19th-century royal palace of the Bhawal kings, famous for the Bhawal Sanyasi case.",
        "location": "Gazipur Sadar, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/gazipur/hist-2.webp",
        "name": "Tongi Mir Jumla Bridge",
        "nameBn": "Tongi Mir Jumla Bridge (গাজীপুর)",
        "category": "Historic Mosque",
        "desc": "Tongi Mir Jumla Bridge is one of the most prominent historical monuments in Gazipur district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Gazipur"
      },
      {
        "id": 3,
        "image": "images/districts/gazipur/hist-3.webp",
        "name": "Gazipur Colonial Court & Mint",
        "nameBn": "গাজীপুর ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Gazipur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Gazipur"
      },
      {
        "id": 4,
        "image": "images/districts/gazipur/hist-4.webp",
        "name": "Gazipur Archeological Mound",
        "nameBn": "গাজীপুর প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Gazipur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Gazipur"
      },
      {
        "id": 5,
        "image": "images/districts/gazipur/hist-5.webp",
        "name": "Gazipur Liberation War Memorial",
        "nameBn": "গাজীপুর মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Gazipur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Gazipur"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/gazipur/tour-1.webp",
        "name": "Bhawal National Park",
        "nameBn": "Bhawal National Park (গাজীপুর)",
        "category": "Eco-Tourism",
        "desc": "Sprawling protected Sal forest reserve popular for picnics, cycling, and nature trails.",
        "location": "Gazipur Riverfront, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/gazipur/tour-2.webp",
        "name": "Bangabandhu Safari Park",
        "nameBn": "Bangabandhu Safari Park (গাজীপুর)",
        "category": "Wildlife Sanctuary",
        "desc": "Bangabandhu Safari Park stands as an iconic tourist highlight in Gazipur district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Gazipur"
      },
      {
        "id": 3,
        "image": "images/districts/gazipur/tour-3.webp",
        "name": "Gazipur Cultural Heritage Museum",
        "nameBn": "গাজীপুর লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Gazipur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Gazipur"
      },
      {
        "id": 4,
        "image": "images/districts/gazipur/tour-4.webp",
        "name": "Gazipur Scenic Lake & Boating Resort",
        "nameBn": "গাজীপুর মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Gazipur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Gazipur"
      },
      {
        "id": 5,
        "image": "images/districts/gazipur/tour-5.webp",
        "name": "Gazipur Sunset Hilltop Viewpoint",
        "nameBn": "গাজীপুর সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Gazipur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Gazipur"
      }
    ]
  },
  {
    "id": 4,
    "slug": "gopalganj",
    "en": "Gopalganj",
    "bn": "গোপালগঞ্জ",
    "div": "Dhaka",
    "lat": 23.1055,
    "lng": 89.8995,
    "coordinates": "23.1055, 89.8995",
    "est": 1984,
    "area": "1,489.92 km²",
    "pop": "1.2M",
    "dist": "160 km",
    "route": "Via Padma Bridge and Dhaka-Khulna Highway N805 (approx. 2.5 to 3 hours).",
    "tagline": "Gopalganj (গোপালগঞ্জ) is a picturesque and historically significant administrative district in Dhaka Division, Bangladesh.",
    "heroImage": "images/districts/gopalganj/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/gopalganj/carousel-1.webp",
        "title": "Gopalganj Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Dhaka Division"
      },
      {
        "id": 2,
        "image": "images/districts/gopalganj/carousel-2.webp",
        "title": "Historic Monuments of Gopalganj",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/gopalganj/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/gopalganj/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/gopalganj/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/gopalganj/hist-1.webp",
        "name": "Tungipara National Mausoleum",
        "nameBn": "Tungipara National Mausoleum (গোপালগঞ্জ)",
        "category": "Royal Heritage",
        "desc": "Tungipara National Mausoleum is one of the most prominent historical monuments in Gopalganj district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Gopalganj Sadar, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/gopalganj/hist-2.webp",
        "name": "Ulpur Zamindar Bari",
        "nameBn": "Ulpur Zamindar Bari (গোপালগঞ্জ)",
        "category": "Historic Mosque",
        "desc": "Ulpur Zamindar Bari is one of the most prominent historical monuments in Gopalganj district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Gopalganj"
      },
      {
        "id": 3,
        "image": "images/districts/gopalganj/hist-3.webp",
        "name": "Gopalganj Colonial Court & Mint",
        "nameBn": "গোপালগঞ্জ ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Gopalganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Gopalganj"
      },
      {
        "id": 4,
        "image": "images/districts/gopalganj/hist-4.webp",
        "name": "Gopalganj Archeological Mound",
        "nameBn": "গোপালগঞ্জ প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Gopalganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Gopalganj"
      },
      {
        "id": 5,
        "image": "images/districts/gopalganj/hist-5.webp",
        "name": "Gopalganj Liberation War Memorial",
        "nameBn": "গোপালগঞ্জ মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Gopalganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Gopalganj"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/gopalganj/tour-1.webp",
        "name": "Madhupati Wetland",
        "nameBn": "Madhupati Wetland (গোপালগঞ্জ)",
        "category": "Birdwatching",
        "desc": "Madhupati Wetland stands as an iconic tourist highlight in Gopalganj district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Gopalganj Riverfront, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/gopalganj/tour-2.webp",
        "name": "Barnal Baor",
        "nameBn": "Barnal Baor (গোপালগঞ্জ)",
        "category": "Lakeside Eco-Spot",
        "desc": "Barnal Baor stands as an iconic tourist highlight in Gopalganj district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Gopalganj"
      },
      {
        "id": 3,
        "image": "images/districts/gopalganj/tour-3.webp",
        "name": "Gopalganj Cultural Heritage Museum",
        "nameBn": "গোপালগঞ্জ লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Gopalganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Gopalganj"
      },
      {
        "id": 4,
        "image": "images/districts/gopalganj/tour-4.webp",
        "name": "Gopalganj Scenic Lake & Boating Resort",
        "nameBn": "গোপালগঞ্জ মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Gopalganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Gopalganj"
      },
      {
        "id": 5,
        "image": "images/districts/gopalganj/tour-5.webp",
        "name": "Gopalganj Sunset Hilltop Viewpoint",
        "nameBn": "গোপালগঞ্জ সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Gopalganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Gopalganj"
      }
    ]
  },
  {
    "id": 5,
    "slug": "kishoreganj",
    "en": "Kishoreganj",
    "bn": "কিশোরগঞ্জ",
    "div": "Dhaka",
    "lat": 24.3762,
    "lng": 90.9423,
    "coordinates": "24.3762, 90.9423",
    "est": 1984,
    "area": "2,688.86 km²",
    "pop": "3.1M",
    "dist": "135 km",
    "route": "Via Dhaka-Sylhet Highway N2 or Kishoreganj Express train from Kamalapur (3-4 hrs).",
    "tagline": "Kishoreganj (কিশোরগঞ্জ) is a picturesque and historically significant administrative district in Dhaka Division, Bangladesh.",
    "heroImage": "images/districts/kishoreganj/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/kishoreganj/carousel-1.webp",
        "title": "Kishoreganj Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Dhaka Division"
      },
      {
        "id": 2,
        "image": "images/districts/kishoreganj/carousel-2.webp",
        "title": "Historic Monuments of Kishoreganj",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/kishoreganj/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/kishoreganj/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/kishoreganj/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/kishoreganj/hist-1.webp",
        "name": "Shah Mahmud Mosque (Egarasindhur)",
        "nameBn": "Shah Mahmud Mosque (Egarasindhur) (কিশোরগঞ্জ)",
        "category": "Royal Heritage",
        "desc": "Shah Mahmud Mosque (Egarasindhur) is one of the most prominent historical monuments in Kishoreganj district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Kishoreganj Sadar, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/kishoreganj/hist-2.webp",
        "name": "Jangalbari Fort",
        "nameBn": "Jangalbari Fort (কিশোরগঞ্জ)",
        "category": "Historic Mosque",
        "desc": "Historic headquarters of Isa Khan, legendary leader of the Baro-Bhuiyans of Bengal.",
        "location": "Old Town, Kishoreganj"
      },
      {
        "id": 3,
        "image": "images/districts/kishoreganj/hist-3.webp",
        "name": "Kishoreganj Colonial Court & Mint",
        "nameBn": "কিশোরগঞ্জ ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Kishoreganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Kishoreganj"
      },
      {
        "id": 4,
        "image": "images/districts/kishoreganj/hist-4.webp",
        "name": "Kishoreganj Archeological Mound",
        "nameBn": "কিশোরগঞ্জ প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Kishoreganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Kishoreganj"
      },
      {
        "id": 5,
        "image": "images/districts/kishoreganj/hist-5.webp",
        "name": "Kishoreganj Liberation War Memorial",
        "nameBn": "কিশোরগঞ্জ মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Kishoreganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Kishoreganj"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/kishoreganj/tour-1.webp",
        "name": "Nikli & Mithamoin Haor",
        "nameBn": "Nikli & Mithamoin Haor (কিশোরগঞ্জ)",
        "category": "Wetland Wonder",
        "desc": "Spectacular aquatic expanses with all-weather roads surrounded by endless water in monsoon.",
        "location": "Kishoreganj Riverfront, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/kishoreganj/tour-2.webp",
        "name": "Chandrabati Shiva Temple",
        "nameBn": "Chandrabati Shiva Temple (কিশোরগঞ্জ)",
        "category": "Archaeology",
        "desc": "Chandrabati Shiva Temple stands as an iconic tourist highlight in Kishoreganj district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Kishoreganj"
      },
      {
        "id": 3,
        "image": "images/districts/kishoreganj/tour-3.webp",
        "name": "Kishoreganj Cultural Heritage Museum",
        "nameBn": "কিশোরগঞ্জ লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Kishoreganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Kishoreganj"
      },
      {
        "id": 4,
        "image": "images/districts/kishoreganj/tour-4.webp",
        "name": "Kishoreganj Scenic Lake & Boating Resort",
        "nameBn": "কিশোরগঞ্জ মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Kishoreganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Kishoreganj"
      },
      {
        "id": 5,
        "image": "images/districts/kishoreganj/tour-5.webp",
        "name": "Kishoreganj Sunset Hilltop Viewpoint",
        "nameBn": "কিশোরগঞ্জ সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Kishoreganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Kishoreganj"
      }
    ]
  },
  {
    "id": 6,
    "slug": "madaripur",
    "en": "Madaripur",
    "bn": "মাদারীপুর",
    "div": "Dhaka",
    "lat": 23.2182,
    "lng": 90.1651,
    "coordinates": "23.2182, 90.1651",
    "est": 1984,
    "area": "1,144.96 km²",
    "pop": "1.3M",
    "dist": "90 km",
    "route": "Directly accessible via Dhaka-Mawa Expressway across Padma Bridge (1.5 - 2 hours).",
    "tagline": "Madaripur (মাদারীপুর) is a picturesque and historically significant administrative district in Dhaka Division, Bangladesh.",
    "heroImage": "images/districts/madaripur/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/madaripur/carousel-1.webp",
        "title": "Madaripur Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Dhaka Division"
      },
      {
        "id": 2,
        "image": "images/districts/madaripur/carousel-2.webp",
        "title": "Historic Monuments of Madaripur",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/madaripur/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/madaripur/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/madaripur/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/madaripur/hist-1.webp",
        "name": "Raja Ram Temple",
        "nameBn": "Raja Ram Temple (মাদারীপুর)",
        "category": "Royal Heritage",
        "desc": "Raja Ram Temple is one of the most prominent historical monuments in Madaripur district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Madaripur Sadar, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/madaripur/hist-2.webp",
        "name": "Mithapur Zamindar Bari",
        "nameBn": "Mithapur Zamindar Bari (মাদারীপুর)",
        "category": "Historic Mosque",
        "desc": "Heritage mansion reflecting early 20th-century aristocratic Bengali architecture.",
        "location": "Old Town, Madaripur"
      },
      {
        "id": 3,
        "image": "images/districts/madaripur/hist-3.webp",
        "name": "Madaripur Colonial Court & Mint",
        "nameBn": "মাদারীপুর ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Madaripur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Madaripur"
      },
      {
        "id": 4,
        "image": "images/districts/madaripur/hist-4.webp",
        "name": "Madaripur Archeological Mound",
        "nameBn": "মাদারীপুর প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Madaripur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Madaripur"
      },
      {
        "id": 5,
        "image": "images/districts/madaripur/hist-5.webp",
        "name": "Madaripur Liberation War Memorial",
        "nameBn": "মাদারীপুর মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Madaripur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Madaripur"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/madaripur/tour-1.webp",
        "name": "Shakuni Lake & Eco Walkway",
        "nameBn": "Shakuni Lake & Eco Walkway (মাদারীপুর)",
        "category": "Urban Lakefront",
        "desc": "Shakuni Lake & Eco Walkway stands as an iconic tourist highlight in Madaripur district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Madaripur Riverfront, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/madaripur/tour-2.webp",
        "name": "Arial Khan Riverside",
        "nameBn": "Arial Khan Riverside (মাদারীপুর)",
        "category": "Scenic Waters",
        "desc": "Picturesque riverbanks celebrated for evening breezes and fresh hilsa delicacies.",
        "location": "Forest Range, Madaripur"
      },
      {
        "id": 3,
        "image": "images/districts/madaripur/tour-3.webp",
        "name": "Madaripur Cultural Heritage Museum",
        "nameBn": "মাদারীপুর লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Madaripur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Madaripur"
      },
      {
        "id": 4,
        "image": "images/districts/madaripur/tour-4.webp",
        "name": "Madaripur Scenic Lake & Boating Resort",
        "nameBn": "মাদারীপুর মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Madaripur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Madaripur"
      },
      {
        "id": 5,
        "image": "images/districts/madaripur/tour-5.webp",
        "name": "Madaripur Sunset Hilltop Viewpoint",
        "nameBn": "মাদারীপুর সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Madaripur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Madaripur"
      }
    ]
  },
  {
    "id": 7,
    "slug": "manikganj",
    "en": "Manikganj",
    "bn": "মানিকগঞ্জ",
    "div": "Dhaka",
    "lat": 23.844,
    "lng": 89.9496,
    "coordinates": "23.8440, 89.9496",
    "est": 1984,
    "area": "1,379.00 km²",
    "pop": "1.4M",
    "dist": "65 km",
    "route": "Via Dhaka-Aricha Highway N5 (approx. 1.5 hours by direct bus or car).",
    "tagline": "Manikganj (মানিকগঞ্জ) is a picturesque and historically significant administrative district in Dhaka Division, Bangladesh.",
    "heroImage": "images/districts/manikganj/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/manikganj/carousel-1.webp",
        "title": "Manikganj Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Dhaka Division"
      },
      {
        "id": 2,
        "image": "images/districts/manikganj/carousel-2.webp",
        "title": "Historic Monuments of Manikganj",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/manikganj/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/manikganj/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/manikganj/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/manikganj/hist-1.webp",
        "name": "Baliati Palace",
        "nameBn": "Baliati Palace (মানিকগঞ্জ)",
        "category": "Royal Heritage",
        "desc": "Spectacular 19th-century neoclassical palace complex with 200 rooms and monumental columns.",
        "location": "Manikganj Sadar, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/manikganj/hist-2.webp",
        "name": "Teota Zamindar Palace",
        "nameBn": "Teota Zamindar Palace (মানিকগঞ্জ)",
        "category": "Historic Mosque",
        "desc": "Overlooks the Jamuna river, associated with national poet Kazi Nazrul Islam’s youth.",
        "location": "Old Town, Manikganj"
      },
      {
        "id": 3,
        "image": "images/districts/manikganj/hist-3.webp",
        "name": "Manikganj Colonial Court & Mint",
        "nameBn": "মানিকগঞ্জ ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Manikganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Manikganj"
      },
      {
        "id": 4,
        "image": "images/districts/manikganj/hist-4.webp",
        "name": "Manikganj Archeological Mound",
        "nameBn": "মানিকগঞ্জ প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Manikganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Manikganj"
      },
      {
        "id": 5,
        "image": "images/districts/manikganj/hist-5.webp",
        "name": "Manikganj Liberation War Memorial",
        "nameBn": "মানিকগঞ্জ মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Manikganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Manikganj"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/manikganj/tour-1.webp",
        "name": "Aricha Ghat",
        "nameBn": "Aricha Ghat (মানিকগঞ্জ)",
        "category": "River Confluence",
        "desc": "Aricha Ghat stands as an iconic tourist highlight in Manikganj district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Manikganj Riverfront, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/manikganj/tour-2.webp",
        "name": "Dhaleshwari Waterfront",
        "nameBn": "Dhaleshwari Waterfront (মানিকগঞ্জ)",
        "category": "Rural Serenity",
        "desc": "Serene riverside plains ideal for boat trips and tasting Manikganj’s famous Gur (molasses).",
        "location": "Forest Range, Manikganj"
      },
      {
        "id": 3,
        "image": "images/districts/manikganj/tour-3.webp",
        "name": "Manikganj Cultural Heritage Museum",
        "nameBn": "মানিকগঞ্জ লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Manikganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Manikganj"
      },
      {
        "id": 4,
        "image": "images/districts/manikganj/tour-4.webp",
        "name": "Manikganj Scenic Lake & Boating Resort",
        "nameBn": "মানিকগঞ্জ মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Manikganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Manikganj"
      },
      {
        "id": 5,
        "image": "images/districts/manikganj/tour-5.webp",
        "name": "Manikganj Sunset Hilltop Viewpoint",
        "nameBn": "মানিকগঞ্জ সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Manikganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Manikganj"
      }
    ]
  },
  {
    "id": 8,
    "slug": "munshiganj",
    "en": "Munshiganj",
    "bn": "মুন্সীগঞ্জ",
    "div": "Dhaka",
    "lat": 23.5258,
    "lng": 90.4173,
    "coordinates": "23.5258, 90.4173",
    "est": 1984,
    "area": "954.96 km²",
    "pop": "1.5M",
    "dist": "30 km",
    "route": "Via Dhaka-Mawa Expressway N8 or Muktarpur Bridge (approx. 45 - 60 minutes).",
    "tagline": "Munshiganj (মুন্সীগঞ্জ) is a picturesque and historically significant administrative district in Dhaka Division, Bangladesh.",
    "heroImage": "images/districts/munshiganj/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/munshiganj/carousel-1.webp",
        "title": "Munshiganj Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Dhaka Division"
      },
      {
        "id": 2,
        "image": "images/districts/munshiganj/carousel-2.webp",
        "title": "Historic Monuments of Munshiganj",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/munshiganj/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/munshiganj/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/munshiganj/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/munshiganj/hist-1.webp",
        "name": "Idrakpur Fort",
        "nameBn": "Idrakpur Fort (মুন্সীগঞ্জ)",
        "category": "Royal Heritage",
        "desc": "Historic 1660 river fortress built by Subahdar Mir Jumla to defend against pirates.",
        "location": "Munshiganj Sadar, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/munshiganj/hist-2.webp",
        "name": "Baba Adam Mosque",
        "nameBn": "Baba Adam Mosque (মুন্সীগঞ্জ)",
        "category": "Historic Mosque",
        "desc": "Pre-Mughal 1483 Sultanate mosque celebrated for six domes and intricate terracotta.",
        "location": "Old Town, Munshiganj"
      },
      {
        "id": 3,
        "image": "images/districts/munshiganj/hist-3.webp",
        "name": "Munshiganj Colonial Court & Mint",
        "nameBn": "মুন্সীগঞ্জ ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Munshiganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Munshiganj"
      },
      {
        "id": 4,
        "image": "images/districts/munshiganj/hist-4.webp",
        "name": "Munshiganj Archeological Mound",
        "nameBn": "মুন্সীগঞ্জ প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Munshiganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Munshiganj"
      },
      {
        "id": 5,
        "image": "images/districts/munshiganj/hist-5.webp",
        "name": "Munshiganj Liberation War Memorial",
        "nameBn": "মুন্সীগঞ্জ মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Munshiganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Munshiganj"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/munshiganj/tour-1.webp",
        "name": "Padma Bridge North Bank",
        "nameBn": "Padma Bridge North Bank (মুন্সীগঞ্জ)",
        "category": "Modern Landmark",
        "desc": "Padma Bridge North Bank stands as an iconic tourist highlight in Munshiganj district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Munshiganj Riverfront, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/munshiganj/tour-2.webp",
        "name": "Mawa Ferry Fish Market",
        "nameBn": "Mawa Ferry Fish Market (মুন্সীগঞ্জ)",
        "category": "Food & River Life",
        "desc": "Renowned culinary destination for freshly fried Padma Hilsa served with steaming rice.",
        "location": "Forest Range, Munshiganj"
      },
      {
        "id": 3,
        "image": "images/districts/munshiganj/tour-3.webp",
        "name": "Munshiganj Cultural Heritage Museum",
        "nameBn": "মুন্সীগঞ্জ লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Munshiganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Munshiganj"
      },
      {
        "id": 4,
        "image": "images/districts/munshiganj/tour-4.webp",
        "name": "Munshiganj Scenic Lake & Boating Resort",
        "nameBn": "মুন্সীগঞ্জ মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Munshiganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Munshiganj"
      },
      {
        "id": 5,
        "image": "images/districts/munshiganj/tour-5.webp",
        "name": "Munshiganj Sunset Hilltop Viewpoint",
        "nameBn": "মুন্সীগঞ্জ সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Munshiganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Munshiganj"
      }
    ]
  },
  {
    "id": 9,
    "slug": "narayanganj",
    "en": "Narayanganj",
    "bn": "নারায়ণগঞ্জ",
    "div": "Dhaka",
    "lat": 23.7232,
    "lng": 90.5781,
    "coordinates": "23.7232, 90.5781",
    "est": 1984,
    "area": "759.57 km²",
    "pop": "3.9M",
    "dist": "20 km",
    "route": "Via Dhaka-Chittagong Highway N1 or Dhaka-Narayanganj commuter train (30 minutes).",
    "tagline": "Narayanganj (নারায়ণগঞ্জ) is a picturesque and historically significant administrative district in Dhaka Division, Bangladesh.",
    "heroImage": "images/districts/narayanganj/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/narayanganj/carousel-1.webp",
        "title": "Narayanganj Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Dhaka Division"
      },
      {
        "id": 2,
        "image": "images/districts/narayanganj/carousel-2.webp",
        "title": "Historic Monuments of Narayanganj",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/narayanganj/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/narayanganj/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/narayanganj/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/narayanganj/hist-1.webp",
        "name": "Sonargaon Panam City",
        "nameBn": "Sonargaon Panam City (নারায়ণগঞ্জ)",
        "category": "Royal Heritage",
        "desc": "Preserved 19th-century street of neoclassical merchant mansions in ancient capital of Bengal.",
        "location": "Narayanganj Sadar, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/narayanganj/hist-2.webp",
        "name": "Hajiganj & Sonakanda Forts",
        "nameBn": "Hajiganj & Sonakanda Forts (নারায়ণগঞ্জ)",
        "category": "Historic Mosque",
        "desc": "Hajiganj & Sonakanda Forts is one of the most prominent historical monuments in Narayanganj district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Narayanganj"
      },
      {
        "id": 3,
        "image": "images/districts/narayanganj/hist-3.webp",
        "name": "Narayanganj Colonial Court & Mint",
        "nameBn": "নারায়ণগঞ্জ ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Narayanganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Narayanganj"
      },
      {
        "id": 4,
        "image": "images/districts/narayanganj/hist-4.webp",
        "name": "Narayanganj Archeological Mound",
        "nameBn": "নারায়ণগঞ্জ প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Narayanganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Narayanganj"
      },
      {
        "id": 5,
        "image": "images/districts/narayanganj/hist-5.webp",
        "name": "Narayanganj Liberation War Memorial",
        "nameBn": "নারায়ণগঞ্জ মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Narayanganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Narayanganj"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/narayanganj/tour-1.webp",
        "name": "Folk Art & Craft Museum",
        "nameBn": "Folk Art & Craft Museum (নারায়ণগঞ্জ)",
        "category": "Cultural Center",
        "desc": "Folk Art & Craft Museum stands as an iconic tourist highlight in Narayanganj district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Narayanganj Riverfront, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/narayanganj/tour-2.webp",
        "name": "Murapara Rajbari",
        "nameBn": "Murapara Rajbari (নারায়ণগঞ্জ)",
        "category": "Royal Architecture",
        "desc": "Murapara Rajbari stands as an iconic tourist highlight in Narayanganj district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Narayanganj"
      },
      {
        "id": 3,
        "image": "images/districts/narayanganj/tour-3.webp",
        "name": "Narayanganj Cultural Heritage Museum",
        "nameBn": "নারায়ণগঞ্জ লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Narayanganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Narayanganj"
      },
      {
        "id": 4,
        "image": "images/districts/narayanganj/tour-4.webp",
        "name": "Narayanganj Scenic Lake & Boating Resort",
        "nameBn": "নারায়ণগঞ্জ মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Narayanganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Narayanganj"
      },
      {
        "id": 5,
        "image": "images/districts/narayanganj/tour-5.webp",
        "name": "Narayanganj Sunset Hilltop Viewpoint",
        "nameBn": "নারায়ণগঞ্জ সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Narayanganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Narayanganj"
      }
    ]
  },
  {
    "id": 10,
    "slug": "narsingdi",
    "en": "Narsingdi",
    "bn": "নরসিংদী",
    "div": "Dhaka",
    "lat": 24.0024,
    "lng": 90.7732,
    "coordinates": "24.0024, 90.7732",
    "est": 1984,
    "area": "1,140.76 km²",
    "pop": "2.5M",
    "dist": "50 km",
    "route": "Via Dhaka-Sylhet Highway N2 or intercity trains heading to Kishoreganj/Sylhet (1-1.5 hrs).",
    "tagline": "Narsingdi (নরসিংদী) is a picturesque and historically significant administrative district in Dhaka Division, Bangladesh.",
    "heroImage": "images/districts/narsingdi/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/narsingdi/carousel-1.webp",
        "title": "Narsingdi Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Dhaka Division"
      },
      {
        "id": 2,
        "image": "images/districts/narsingdi/carousel-2.webp",
        "title": "Historic Monuments of Narsingdi",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/narsingdi/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/narsingdi/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/narsingdi/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/narsingdi/hist-1.webp",
        "name": "Wari-Bateshwar Ancient City",
        "nameBn": "Wari-Bateshwar Ancient City (নরসিংদী)",
        "category": "Royal Heritage",
        "desc": "2500-year-old archaeological site proving ancient urban civilization along the Old Brahmaputra.",
        "location": "Narsingdi Sadar, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/narsingdi/hist-2.webp",
        "name": "Parulia Shahi Mosque",
        "nameBn": "Parulia Shahi Mosque (নরসিংদী)",
        "category": "Historic Mosque",
        "desc": "1714 historic three-domed mosque constructed during the reign of Murshid Quli Khan.",
        "location": "Old Town, Narsingdi"
      },
      {
        "id": 3,
        "image": "images/districts/narsingdi/hist-3.webp",
        "name": "Narsingdi Colonial Court & Mint",
        "nameBn": "নরসিংদী ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Narsingdi district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Narsingdi"
      },
      {
        "id": 4,
        "image": "images/districts/narsingdi/hist-4.webp",
        "name": "Narsingdi Archeological Mound",
        "nameBn": "নরসিংদী প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Narsingdi district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Narsingdi"
      },
      {
        "id": 5,
        "image": "images/districts/narsingdi/hist-5.webp",
        "name": "Narsingdi Liberation War Memorial",
        "nameBn": "নরসিংদী মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Narsingdi district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Narsingdi"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/narsingdi/tour-1.webp",
        "name": "Dream Holiday Park",
        "nameBn": "Dream Holiday Park (নরসিংদী)",
        "category": "Amusement Resort",
        "desc": "Large modern family leisure park featuring water slides, wave pool, and safari rides.",
        "location": "Narsingdi Riverfront, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/narsingdi/tour-2.webp",
        "name": "Shitalakshya River Cruise",
        "nameBn": "Shitalakshya River Cruise (নরসিংদী)",
        "category": "Waterway",
        "desc": "Shitalakshya River Cruise stands as an iconic tourist highlight in Narsingdi district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Narsingdi"
      },
      {
        "id": 3,
        "image": "images/districts/narsingdi/tour-3.webp",
        "name": "Narsingdi Cultural Heritage Museum",
        "nameBn": "নরসিংদী লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Narsingdi district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Narsingdi"
      },
      {
        "id": 4,
        "image": "images/districts/narsingdi/tour-4.webp",
        "name": "Narsingdi Scenic Lake & Boating Resort",
        "nameBn": "নরসিংদী মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Narsingdi district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Narsingdi"
      },
      {
        "id": 5,
        "image": "images/districts/narsingdi/tour-5.webp",
        "name": "Narsingdi Sunset Hilltop Viewpoint",
        "nameBn": "নরসিংদী সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Narsingdi district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Narsingdi"
      }
    ]
  },
  {
    "id": 11,
    "slug": "rajbari",
    "en": "Rajbari",
    "bn": "রাজবাড়ী",
    "div": "Dhaka",
    "lat": 23.7276,
    "lng": 89.5615,
    "coordinates": "23.7276, 89.5615",
    "est": 1984,
    "area": "1,118.80 km²",
    "pop": "1.1M",
    "dist": "115 km",
    "route": "Via Padma Bridge or Paturia-Daulatdia ferry crossing (approx. 2.5 hours).",
    "tagline": "Rajbari (রাজবাড়ী) is a picturesque and historically significant administrative district in Dhaka Division, Bangladesh.",
    "heroImage": "images/districts/rajbari/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/rajbari/carousel-1.webp",
        "title": "Rajbari Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Dhaka Division"
      },
      {
        "id": 2,
        "image": "images/districts/rajbari/carousel-2.webp",
        "title": "Historic Monuments of Rajbari",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/rajbari/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/rajbari/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/rajbari/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/rajbari/hist-1.webp",
        "name": "Kalyan Dighi & Temple",
        "nameBn": "Kalyan Dighi & Temple (রাজবাড়ী)",
        "category": "Royal Heritage",
        "desc": "Kalyan Dighi & Temple is one of the most prominent historical monuments in Rajbari district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Rajbari Sadar, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/rajbari/hist-2.webp",
        "name": "Nawapara Shahi Mosque",
        "nameBn": "Nawapara Shahi Mosque (রাজবাড়ী)",
        "category": "Historic Mosque",
        "desc": "Nawapara Shahi Mosque is one of the most prominent historical monuments in Rajbari district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Rajbari"
      },
      {
        "id": 3,
        "image": "images/districts/rajbari/hist-3.webp",
        "name": "Rajbari Colonial Court & Mint",
        "nameBn": "রাজবাড়ী ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Rajbari district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Rajbari"
      },
      {
        "id": 4,
        "image": "images/districts/rajbari/hist-4.webp",
        "name": "Rajbari Archeological Mound",
        "nameBn": "রাজবাড়ী প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Rajbari district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Rajbari"
      },
      {
        "id": 5,
        "image": "images/districts/rajbari/hist-5.webp",
        "name": "Rajbari Liberation War Memorial",
        "nameBn": "রাজবাড়ী মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Rajbari district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Rajbari"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/rajbari/tour-1.webp",
        "name": "Goalanda River Junction",
        "nameBn": "Goalanda River Junction (রাজবাড়ী)",
        "category": "Culinary & River",
        "desc": "Legendary railway and steamer confluence, celebrated for historical river culture.",
        "location": "Rajbari Riverfront, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/rajbari/tour-2.webp",
        "name": "Padma Sandbars (Char)",
        "nameBn": "Padma Sandbars (Char) (রাজবাড়ী)",
        "category": "Nature & Camping",
        "desc": "Expansive winter sandbanks ideal for camping, evening strolls, and watching fishing fleets.",
        "location": "Forest Range, Rajbari"
      },
      {
        "id": 3,
        "image": "images/districts/rajbari/tour-3.webp",
        "name": "Rajbari Cultural Heritage Museum",
        "nameBn": "রাজবাড়ী লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Rajbari district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Rajbari"
      },
      {
        "id": 4,
        "image": "images/districts/rajbari/tour-4.webp",
        "name": "Rajbari Scenic Lake & Boating Resort",
        "nameBn": "রাজবাড়ী মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Rajbari district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Rajbari"
      },
      {
        "id": 5,
        "image": "images/districts/rajbari/tour-5.webp",
        "name": "Rajbari Sunset Hilltop Viewpoint",
        "nameBn": "রাজবাড়ী সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Rajbari district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Rajbari"
      }
    ]
  },
  {
    "id": 12,
    "slug": "shariatpur",
    "en": "Shariatpur",
    "bn": "শরীয়তপুর",
    "div": "Dhaka",
    "lat": 23.2477,
    "lng": 90.4074,
    "coordinates": "23.2477, 90.4074",
    "est": 1984,
    "area": "1,181.53 km²",
    "pop": "1.2M",
    "dist": "80 km",
    "route": "Via Dhaka-Mawa Expressway crossing directly into Jajira over Padma Bridge (1.5 - 2 hrs).",
    "tagline": "Shariatpur (শরীয়তপুর) is a picturesque and historically significant administrative district in Dhaka Division, Bangladesh.",
    "heroImage": "images/districts/shariatpur/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/shariatpur/carousel-1.webp",
        "title": "Shariatpur Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Dhaka Division"
      },
      {
        "id": 2,
        "image": "images/districts/shariatpur/carousel-2.webp",
        "title": "Historic Monuments of Shariatpur",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/shariatpur/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/shariatpur/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/shariatpur/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/shariatpur/hist-1.webp",
        "name": "Fatehjangpur Fort",
        "nameBn": "Fatehjangpur Fort (শরীয়তপুর)",
        "category": "Royal Heritage",
        "desc": "Fatehjangpur Fort is one of the most prominent historical monuments in Shariatpur district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Shariatpur Sadar, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/shariatpur/hist-2.webp",
        "name": "Ramsiddhi Mosque",
        "nameBn": "Ramsiddhi Mosque (শরীয়তপুর)",
        "category": "Historic Mosque",
        "desc": "Ramsiddhi Mosque is one of the most prominent historical monuments in Shariatpur district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Shariatpur"
      },
      {
        "id": 3,
        "image": "images/districts/shariatpur/hist-3.webp",
        "name": "Shariatpur Colonial Court & Mint",
        "nameBn": "শরীয়তপুর ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Shariatpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Shariatpur"
      },
      {
        "id": 4,
        "image": "images/districts/shariatpur/hist-4.webp",
        "name": "Shariatpur Archeological Mound",
        "nameBn": "শরীয়তপুর প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Shariatpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Shariatpur"
      },
      {
        "id": 5,
        "image": "images/districts/shariatpur/hist-5.webp",
        "name": "Shariatpur Liberation War Memorial",
        "nameBn": "শরীয়তপুর মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Shariatpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Shariatpur"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/shariatpur/tour-1.webp",
        "name": "Padma South Bridge Plaza",
        "nameBn": "Padma South Bridge Plaza (শরীয়তপুর)",
        "category": "Engineering Sight",
        "desc": "Padma South Bridge Plaza stands as an iconic tourist highlight in Shariatpur district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Shariatpur Riverfront, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/shariatpur/tour-2.webp",
        "name": "Naria Waterfront",
        "nameBn": "Naria Waterfront (শরীয়তপুর)",
        "category": "Delta River Life",
        "desc": "Naria Waterfront stands as an iconic tourist highlight in Shariatpur district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Shariatpur"
      },
      {
        "id": 3,
        "image": "images/districts/shariatpur/tour-3.webp",
        "name": "Shariatpur Cultural Heritage Museum",
        "nameBn": "শরীয়তপুর লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Shariatpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Shariatpur"
      },
      {
        "id": 4,
        "image": "images/districts/shariatpur/tour-4.webp",
        "name": "Shariatpur Scenic Lake & Boating Resort",
        "nameBn": "শরীয়তপুর মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Shariatpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Shariatpur"
      },
      {
        "id": 5,
        "image": "images/districts/shariatpur/tour-5.webp",
        "name": "Shariatpur Sunset Hilltop Viewpoint",
        "nameBn": "শরীয়তপুর সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Shariatpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Shariatpur"
      }
    ]
  },
  {
    "id": 13,
    "slug": "tangail",
    "en": "Tangail",
    "bn": "টাঙ্গাইল",
    "div": "Dhaka",
    "lat": 24.3563,
    "lng": 89.9986,
    "coordinates": "24.3563, 89.9986",
    "est": 1969,
    "area": "3,414.39 km²",
    "pop": "3.8M",
    "dist": "95 km",
    "route": "Via Dhaka-Tangail 4-lane Highway N4 or Jamuna Bridge train routes (approx. 2 hours).",
    "tagline": "Tangail (টাঙ্গাইল) is a picturesque and historically significant administrative district in Dhaka Division, Bangladesh.",
    "heroImage": "images/districts/tangail/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/tangail/carousel-1.webp",
        "title": "Tangail Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Dhaka Division"
      },
      {
        "id": 2,
        "image": "images/districts/tangail/carousel-2.webp",
        "title": "Historic Monuments of Tangail",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/tangail/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/tangail/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/tangail/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/tangail/hist-1.webp",
        "name": "Atiya Mosque",
        "nameBn": "Atiya Mosque (টাঙ্গাইল)",
        "category": "Royal Heritage",
        "desc": "1609 iconic Sultanate-Mughal mosque immortalized on the historic 10-Taka currency note.",
        "location": "Tangail Sadar, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/tangail/hist-2.webp",
        "name": "Mohera Zamindar Bari",
        "nameBn": "Mohera Zamindar Bari (টাঙ্গাইল)",
        "category": "Historic Mosque",
        "desc": "Exquisitely conserved European neoclassical estate with lush flower gardens and lodge.",
        "location": "Old Town, Tangail"
      },
      {
        "id": 3,
        "image": "images/districts/tangail/hist-3.webp",
        "name": "Tangail Colonial Court & Mint",
        "nameBn": "টাঙ্গাইল ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Tangail district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Tangail"
      },
      {
        "id": 4,
        "image": "images/districts/tangail/hist-4.webp",
        "name": "Tangail Archeological Mound",
        "nameBn": "টাঙ্গাইল প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Tangail district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Tangail"
      },
      {
        "id": 5,
        "image": "images/districts/tangail/hist-5.webp",
        "name": "Tangail Liberation War Memorial",
        "nameBn": "টাঙ্গাইল মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Tangail district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Tangail"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/tangail/tour-1.webp",
        "name": "Madhupur National Park",
        "nameBn": "Madhupur National Park (টাঙ্গাইল)",
        "category": "Eco Forest & Pineapples",
        "desc": "Dense deciduous sal forest known for indigenous Garo culture and sweetest pineapples.",
        "location": "Tangail Riverfront, Dhaka"
      },
      {
        "id": 2,
        "image": "images/districts/tangail/tour-2.webp",
        "name": "Tangail Saree & Sweet Haven",
        "nameBn": "Tangail Saree & Sweet Haven (টাঙ্গাইল)",
        "category": "Craft & Gastronomy",
        "desc": "Tangail Saree & Sweet Haven stands as an iconic tourist highlight in Tangail district. Nestled in natural surroundings under Dhaka Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Tangail"
      },
      {
        "id": 3,
        "image": "images/districts/tangail/tour-3.webp",
        "name": "Tangail Cultural Heritage Museum",
        "nameBn": "টাঙ্গাইল লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Tangail district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Tangail"
      },
      {
        "id": 4,
        "image": "images/districts/tangail/tour-4.webp",
        "name": "Tangail Scenic Lake & Boating Resort",
        "nameBn": "টাঙ্গাইল মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Tangail district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Tangail"
      },
      {
        "id": 5,
        "image": "images/districts/tangail/tour-5.webp",
        "name": "Tangail Sunset Hilltop Viewpoint",
        "nameBn": "টাঙ্গাইল সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Tangail district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Tangail"
      }
    ]
  },
  {
    "id": 14,
    "slug": "bandarban",
    "en": "Bandarban",
    "bn": "বান্দরবান",
    "div": "Chattogram",
    "lat": 21.8071,
    "lng": 92.3638,
    "coordinates": "21.8071, 92.3638",
    "est": 1981,
    "area": "4,479.03 km²",
    "pop": "0.45M",
    "dist": "320 km",
    "route": "Direct AC/Non-AC overnight highway buses (8-9 hrs), or fly to Chattogram and drive 2.5 hrs.",
    "tagline": "Bandarban (বান্দরবান) is a picturesque and historically significant administrative district in Chattogram Division, Bangladesh.",
    "heroImage": "images/districts/bandarban/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/bandarban/carousel-1.webp",
        "title": "Bandarban Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Chattogram Division"
      },
      {
        "id": 2,
        "image": "images/districts/bandarban/carousel-2.webp",
        "title": "Historic Monuments of Bandarban",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/bandarban/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/bandarban/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/bandarban/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/bandarban/hist-1.webp",
        "name": "Bohmong King Palace",
        "nameBn": "Bohmong King Palace (বান্দরবান)",
        "category": "Royal Heritage",
        "desc": "Seat of the hereditary Bohmong Circle Royal Chief holding historic annual Raj Punnah.",
        "location": "Bandarban Sadar, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/bandarban/hist-2.webp",
        "name": "Buddha Dhatu Jadi (Golden Temple)",
        "nameBn": "Buddha Dhatu Jadi (Golden Temple) (বান্দরবান)",
        "category": "Historic Mosque",
        "desc": "Buddha Dhatu Jadi (Golden Temple) is one of the most prominent historical monuments in Bandarban district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Bandarban"
      },
      {
        "id": 3,
        "image": "images/districts/bandarban/hist-3.webp",
        "name": "Bandarban Colonial Court & Mint",
        "nameBn": "বান্দরবান ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Bandarban district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Bandarban"
      },
      {
        "id": 4,
        "image": "images/districts/bandarban/hist-4.webp",
        "name": "Bandarban Archeological Mound",
        "nameBn": "বান্দরবান প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Bandarban district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Bandarban"
      },
      {
        "id": 5,
        "image": "images/districts/bandarban/hist-5.webp",
        "name": "Bandarban Liberation War Memorial",
        "nameBn": "বান্দরবান মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Bandarban district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Bandarban"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/bandarban/tour-1.webp",
        "name": "Nilgiri & Thanchi",
        "nameBn": "Nilgiri & Thanchi (বান্দরবান)",
        "category": "High Altitude Peaks",
        "desc": "Nilgiri & Thanchi stands as an iconic tourist highlight in Bandarban district. Nestled in natural surroundings under Chattogram Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Bandarban Riverfront, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/bandarban/tour-2.webp",
        "name": "Boga Lake & Keokradong",
        "nameBn": "Boga Lake & Keokradong (বান্দরবান)",
        "category": "Trekking Summit",
        "desc": "Mystical freshwater volcanic crater lake and the country’s premier trekking peaks.",
        "location": "Forest Range, Bandarban"
      },
      {
        "id": 3,
        "image": "images/districts/bandarban/tour-3.webp",
        "name": "Bandarban Cultural Heritage Museum",
        "nameBn": "বান্দরবান লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Bandarban district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Bandarban"
      },
      {
        "id": 4,
        "image": "images/districts/bandarban/tour-4.webp",
        "name": "Bandarban Scenic Lake & Boating Resort",
        "nameBn": "বান্দরবান মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Bandarban district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Bandarban"
      },
      {
        "id": 5,
        "image": "images/districts/bandarban/tour-5.webp",
        "name": "Bandarban Sunset Hilltop Viewpoint",
        "nameBn": "বান্দরবান সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Bandarban district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Bandarban"
      }
    ]
  },
  {
    "id": 15,
    "slug": "brahmanbaria",
    "en": "Brahmanbaria",
    "bn": "ব্রাহ্মণবাড়িয়া",
    "div": "Chattogram",
    "lat": 23.953,
    "lng": 91.0835,
    "coordinates": "23.9530, 91.0835",
    "est": 1984,
    "area": "1,927.11 km²",
    "pop": "3.0M",
    "dist": "110 km",
    "route": "Via Dhaka-Sylhet Highway N2 or Upakul/Kalni Express trains from Dhaka (2 - 2.5 hrs).",
    "tagline": "Brahmanbaria (ব্রাহ্মণবাড়িয়া) is a picturesque and historically significant administrative district in Chattogram Division, Bangladesh.",
    "heroImage": "images/districts/brahmanbaria/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/brahmanbaria/carousel-1.webp",
        "title": "Brahmanbaria Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Chattogram Division"
      },
      {
        "id": 2,
        "image": "images/districts/brahmanbaria/carousel-2.webp",
        "title": "Historic Monuments of Brahmanbaria",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/brahmanbaria/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/brahmanbaria/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/brahmanbaria/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/brahmanbaria/hist-1.webp",
        "name": "Arifil Mosque",
        "nameBn": "Arifil Mosque (ব্রাহ্মণবাড়িয়া)",
        "category": "Royal Heritage",
        "desc": "Arifil Mosque is one of the most prominent historical monuments in Brahmanbaria district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Brahmanbaria Sadar, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/brahmanbaria/hist-2.webp",
        "name": "Ulchapara Mosque & Kalidaha Pond",
        "nameBn": "Ulchapara Mosque & Kalidaha Pond (ব্রাহ্মণবাড়িয়া)",
        "category": "Historic Mosque",
        "desc": "Ulchapara Mosque & Kalidaha Pond is one of the most prominent historical monuments in Brahmanbaria district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Brahmanbaria"
      },
      {
        "id": 3,
        "image": "images/districts/brahmanbaria/hist-3.webp",
        "name": "Brahmanbaria Colonial Court & Mint",
        "nameBn": "ব্রাহ্মণবাড়িয়া ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Brahmanbaria district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Brahmanbaria"
      },
      {
        "id": 4,
        "image": "images/districts/brahmanbaria/hist-4.webp",
        "name": "Brahmanbaria Archeological Mound",
        "nameBn": "ব্রাহ্মণবাড়িয়া প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Brahmanbaria district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Brahmanbaria"
      },
      {
        "id": 5,
        "image": "images/districts/brahmanbaria/hist-5.webp",
        "name": "Brahmanbaria Liberation War Memorial",
        "nameBn": "ব্রাহ্মণবাড়িয়া মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Brahmanbaria district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Brahmanbaria"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/brahmanbaria/tour-1.webp",
        "name": "Titas River Waterfront",
        "nameBn": "Titas River Waterfront (ব্রাহ্মণবাড়িয়া)",
        "category": "Cultural River",
        "desc": "Titas River Waterfront stands as an iconic tourist highlight in Brahmanbaria district. Nestled in natural surroundings under Chattogram Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Brahmanbaria Riverfront, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/brahmanbaria/tour-2.webp",
        "name": "Sarail Hound Heritage & Chanamukhi",
        "nameBn": "Sarail Hound Heritage & Chanamukhi (ব্রাহ্মণবাড়িয়া)",
        "category": "Heritage & Sweets",
        "desc": "Birthplace of the famed Sarail hunting hounds and mouthwatering Chanamukhi sweets.",
        "location": "Forest Range, Brahmanbaria"
      },
      {
        "id": 3,
        "image": "images/districts/brahmanbaria/tour-3.webp",
        "name": "Brahmanbaria Cultural Heritage Museum",
        "nameBn": "ব্রাহ্মণবাড়িয়া লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Brahmanbaria district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Brahmanbaria"
      },
      {
        "id": 4,
        "image": "images/districts/brahmanbaria/tour-4.webp",
        "name": "Brahmanbaria Scenic Lake & Boating Resort",
        "nameBn": "ব্রাহ্মণবাড়িয়া মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Brahmanbaria district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Brahmanbaria"
      },
      {
        "id": 5,
        "image": "images/districts/brahmanbaria/tour-5.webp",
        "name": "Brahmanbaria Sunset Hilltop Viewpoint",
        "nameBn": "ব্রাহ্মণবাড়িয়া সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Brahmanbaria district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Brahmanbaria"
      }
    ]
  },
  {
    "id": 16,
    "slug": "chandpur",
    "en": "Chandpur",
    "bn": "চাঁদপুর",
    "div": "Chattogram",
    "lat": 23.2797,
    "lng": 90.7779,
    "coordinates": "23.2797, 90.7779",
    "est": 1984,
    "area": "1,704.06 km²",
    "pop": "2.5M",
    "dist": "115 km",
    "route": "Scenic luxury river launch from Dhaka Sadarghat (3 hours) or Dhaka-Chittagong Highway N1.",
    "tagline": "Chandpur (চাঁদপুর) is a picturesque and historically significant administrative district in Chattogram Division, Bangladesh.",
    "heroImage": "images/districts/chandpur/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/chandpur/carousel-1.webp",
        "title": "Chandpur Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Chattogram Division"
      },
      {
        "id": 2,
        "image": "images/districts/chandpur/carousel-2.webp",
        "title": "Historic Monuments of Chandpur",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/chandpur/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/chandpur/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/chandpur/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/chandpur/hist-1.webp",
        "name": "Rupsha Zamindar Bari",
        "nameBn": "Rupsha Zamindar Bari (চাঁদপুর)",
        "category": "Royal Heritage",
        "desc": "Rupsha Zamindar Bari is one of the most prominent historical monuments in Chandpur district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Chandpur Sadar, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/chandpur/hist-2.webp",
        "name": "Haji Begum Mosque",
        "nameBn": "Haji Begum Mosque (চাঁদপুর)",
        "category": "Historic Mosque",
        "desc": "Haji Begum Mosque is one of the most prominent historical monuments in Chandpur district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Chandpur"
      },
      {
        "id": 3,
        "image": "images/districts/chandpur/hist-3.webp",
        "name": "Chandpur Colonial Court & Mint",
        "nameBn": "চাঁদপুর ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Chandpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Chandpur"
      },
      {
        "id": 4,
        "image": "images/districts/chandpur/hist-4.webp",
        "name": "Chandpur Archeological Mound",
        "nameBn": "চাঁদপুর প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Chandpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Chandpur"
      },
      {
        "id": 5,
        "image": "images/districts/chandpur/hist-5.webp",
        "name": "Chandpur Liberation War Memorial",
        "nameBn": "চাঁদপুর মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Chandpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Chandpur"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/chandpur/tour-1.webp",
        "name": "Chandpur Mohona (Triveni Sangam)",
        "nameBn": "Chandpur Mohona (Triveni Sangam) (চাঁদপুর)",
        "category": "River Confluence",
        "desc": "Chandpur Mohona (Triveni Sangam) stands as an iconic tourist highlight in Chandpur district. Nestled in natural surroundings under Chattogram Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Chandpur Riverfront, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/chandpur/tour-2.webp",
        "name": "Hilsa Fish Hub",
        "nameBn": "Hilsa Fish Hub (চাঁদপুর)",
        "category": "Culinary Capital",
        "desc": "Hilsa Fish Hub stands as an iconic tourist highlight in Chandpur district. Nestled in natural surroundings under Chattogram Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Chandpur"
      },
      {
        "id": 3,
        "image": "images/districts/chandpur/tour-3.webp",
        "name": "Chandpur Cultural Heritage Museum",
        "nameBn": "চাঁদপুর লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Chandpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Chandpur"
      },
      {
        "id": 4,
        "image": "images/districts/chandpur/tour-4.webp",
        "name": "Chandpur Scenic Lake & Boating Resort",
        "nameBn": "চাঁদপুর মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Chandpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Chandpur"
      },
      {
        "id": 5,
        "image": "images/districts/chandpur/tour-5.webp",
        "name": "Chandpur Sunset Hilltop Viewpoint",
        "nameBn": "চাঁদপুর সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Chandpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Chandpur"
      }
    ]
  },
  {
    "id": 17,
    "slug": "chattogram",
    "en": "Chattogram",
    "bn": "চট্টগ্রাম",
    "div": "Chattogram",
    "lat": 22.4367,
    "lng": 91.8653,
    "coordinates": "22.4367, 91.8653",
    "est": 1666,
    "area": "5,282.98 km²",
    "pop": "9.2M",
    "dist": "240 km",
    "route": "Dhaka-Chattogram Highway N1 (4.5 hrs), Suborno/Sonar Bangla Express train (4.5 hrs), or 40-min flight.",
    "tagline": "Chattogram (চট্টগ্রাম) is a picturesque and historically significant administrative district in Chattogram Division, Bangladesh.",
    "heroImage": "images/districts/chattogram/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/chattogram/carousel-1.webp",
        "title": "Chattogram Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Chattogram Division"
      },
      {
        "id": 2,
        "image": "images/districts/chattogram/carousel-2.webp",
        "title": "Historic Monuments of Chattogram",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/chattogram/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/chattogram/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/chattogram/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/chattogram/hist-1.webp",
        "name": "Anderkilla Shahi Jame Mosque",
        "nameBn": "Anderkilla Shahi Jame Mosque (চট্টগ্রাম)",
        "category": "Royal Heritage",
        "desc": "Historic 1667 hill-top mosque constructed by Shaista Khan following the conquest.",
        "location": "Chattogram Sadar, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/chattogram/hist-2.webp",
        "name": "Commonwealth War Cemetery",
        "nameBn": "Commonwealth War Cemetery (চট্টগ্রাম)",
        "category": "Historic Mosque",
        "desc": "Commonwealth War Cemetery is one of the most prominent historical monuments in Chattogram district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Chattogram"
      },
      {
        "id": 3,
        "image": "images/districts/chattogram/hist-3.webp",
        "name": "Chattogram Colonial Court & Mint",
        "nameBn": "চট্টগ্রাম ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Chattogram district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Chattogram"
      },
      {
        "id": 4,
        "image": "images/districts/chattogram/hist-4.webp",
        "name": "Chattogram Archeological Mound",
        "nameBn": "চট্টগ্রাম প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Chattogram district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Chattogram"
      },
      {
        "id": 5,
        "image": "images/districts/chattogram/hist-5.webp",
        "name": "Chattogram Liberation War Memorial",
        "nameBn": "চট্টগ্রাম মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Chattogram district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Chattogram"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/chattogram/tour-1.webp",
        "name": "Patenga Sea Beach & Naval Point",
        "nameBn": "Patenga Sea Beach & Naval Point (চট্টগ্রাম)",
        "category": "Ocean Coast",
        "desc": "Patenga Sea Beach & Naval Point stands as an iconic tourist highlight in Chattogram district. Nestled in natural surroundings under Chattogram Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Chattogram Riverfront, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/chattogram/tour-2.webp",
        "name": "Foy’s Lake & Amusement World",
        "nameBn": "Foy’s Lake & Amusement World (চট্টগ্রাম)",
        "category": "Eco Leisure",
        "desc": "Foy’s Lake & Amusement World stands as an iconic tourist highlight in Chattogram district. Nestled in natural surroundings under Chattogram Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Chattogram"
      },
      {
        "id": 3,
        "image": "images/districts/chattogram/tour-3.webp",
        "name": "Chattogram Cultural Heritage Museum",
        "nameBn": "চট্টগ্রাম লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Chattogram district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Chattogram"
      },
      {
        "id": 4,
        "image": "images/districts/chattogram/tour-4.webp",
        "name": "Chattogram Scenic Lake & Boating Resort",
        "nameBn": "চট্টগ্রাম মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Chattogram district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Chattogram"
      },
      {
        "id": 5,
        "image": "images/districts/chattogram/tour-5.webp",
        "name": "Chattogram Sunset Hilltop Viewpoint",
        "nameBn": "চট্টগ্রাম সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Chattogram district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Chattogram"
      }
    ]
  },
  {
    "id": 18,
    "slug": "cumilla",
    "en": "Cumilla",
    "bn": "কুমিল্লা",
    "div": "Chattogram",
    "lat": 23.4369,
    "lng": 91.034,
    "coordinates": "23.4369, 91.0340",
    "est": 1790,
    "area": "3,087.33 km²",
    "pop": "5.9M",
    "dist": "100 km",
    "route": "Via Dhaka-Chittagong Highway N1 (approx. 2 hours) or Dhaka-Chattogram railway link.",
    "tagline": "Cumilla (কুমিল্লা) is a picturesque and historically significant administrative district in Chattogram Division, Bangladesh.",
    "heroImage": "images/districts/cumilla/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/cumilla/carousel-1.webp",
        "title": "Cumilla Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Chattogram Division"
      },
      {
        "id": 2,
        "image": "images/districts/cumilla/carousel-2.webp",
        "title": "Historic Monuments of Cumilla",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/cumilla/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/cumilla/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/cumilla/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/cumilla/hist-1.webp",
        "name": "Shalban Vihara & Mainamati",
        "nameBn": "Shalban Vihara & Mainamati (কুমিল্লা)",
        "category": "Royal Heritage",
        "desc": "World-famous 8th-century Buddhist monastic ruins with terracotta art and archaeological museum.",
        "location": "Cumilla Sadar, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/cumilla/hist-2.webp",
        "name": "Shah Suja Mosque",
        "nameBn": "Shah Suja Mosque (কুমিল্লা)",
        "category": "Historic Mosque",
        "desc": "Shah Suja Mosque is one of the most prominent historical monuments in Cumilla district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Cumilla"
      },
      {
        "id": 3,
        "image": "images/districts/cumilla/hist-3.webp",
        "name": "Cumilla Colonial Court & Mint",
        "nameBn": "কুমিল্লা ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Cumilla district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Cumilla"
      },
      {
        "id": 4,
        "image": "images/districts/cumilla/hist-4.webp",
        "name": "Cumilla Archeological Mound",
        "nameBn": "কুমিল্লা প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Cumilla district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Cumilla"
      },
      {
        "id": 5,
        "image": "images/districts/cumilla/hist-5.webp",
        "name": "Cumilla Liberation War Memorial",
        "nameBn": "কুমিল্লা মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Cumilla district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Cumilla"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/cumilla/tour-1.webp",
        "name": "Dharmasagar Dighi",
        "nameBn": "Dharmasagar Dighi (কুমিল্লা)",
        "category": "Historic Reservoir",
        "desc": "Dharmasagar Dighi stands as an iconic tourist highlight in Cumilla district. Nestled in natural surroundings under Chattogram Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Cumilla Riverfront, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/cumilla/tour-2.webp",
        "name": "Matri Bhander & Lalmai Hills",
        "nameBn": "Matri Bhander & Lalmai Hills (কুমিল্লা)",
        "category": "Sweets & Geology",
        "desc": "Original home of world-famous authentic Comilla Rasmalai alongside ancient red hills.",
        "location": "Forest Range, Cumilla"
      },
      {
        "id": 3,
        "image": "images/districts/cumilla/tour-3.webp",
        "name": "Cumilla Cultural Heritage Museum",
        "nameBn": "কুমিল্লা লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Cumilla district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Cumilla"
      },
      {
        "id": 4,
        "image": "images/districts/cumilla/tour-4.webp",
        "name": "Cumilla Scenic Lake & Boating Resort",
        "nameBn": "কুমিল্লা মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Cumilla district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Cumilla"
      },
      {
        "id": 5,
        "image": "images/districts/cumilla/tour-5.webp",
        "name": "Cumilla Sunset Hilltop Viewpoint",
        "nameBn": "কুমিল্লা সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Cumilla district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Cumilla"
      }
    ]
  },
  {
    "id": 19,
    "slug": "coxs-bazar",
    "en": "Cox's Bazar",
    "bn": "কক্সবাজার",
    "div": "Chattogram",
    "lat": 21.4726,
    "lng": 92.071,
    "coordinates": "21.4726, 92.0710",
    "est": 1984,
    "area": "2,491.86 km²",
    "pop": "2.8M",
    "dist": "395 km",
    "route": "Direct train via Cox's Bazar Express (8 hrs), overnight highway buses, or 50-minute commercial flight.",
    "tagline": "Cox's Bazar (কক্সবাজার) is a picturesque and historically significant administrative district in Chattogram Division, Bangladesh.",
    "heroImage": "images/districts/coxs-bazar/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/coxs-bazar/carousel-1.webp",
        "title": "Cox's Bazar Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Chattogram Division"
      },
      {
        "id": 2,
        "image": "images/districts/coxs-bazar/carousel-2.webp",
        "title": "Historic Monuments of Cox's Bazar",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/coxs-bazar/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/coxs-bazar/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/coxs-bazar/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/coxs-bazar/hist-1.webp",
        "name": "Aggamedha Khyang",
        "nameBn": "Aggamedha Khyang (কক্সবাজার)",
        "category": "Royal Heritage",
        "desc": "Aggamedha Khyang is one of the most prominent historical monuments in Cox's Bazar district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Cox's Bazar Sadar, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/coxs-bazar/hist-2.webp",
        "name": "Ramu 100-Foot Reclining Buddha",
        "nameBn": "Ramu 100-Foot Reclining Buddha (কক্সবাজার)",
        "category": "Historic Mosque",
        "desc": "Colossal bronze-painted reclining Buddha statue in the peaceful Vimukti monastery.",
        "location": "Old Town, Cox's Bazar"
      },
      {
        "id": 3,
        "image": "images/districts/coxs-bazar/hist-3.webp",
        "name": "Cox's Bazar Colonial Court & Mint",
        "nameBn": "কক্সবাজার ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Cox's Bazar district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Cox's Bazar"
      },
      {
        "id": 4,
        "image": "images/districts/coxs-bazar/hist-4.webp",
        "name": "Cox's Bazar Archeological Mound",
        "nameBn": "কক্সবাজার প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Cox's Bazar district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Cox's Bazar"
      },
      {
        "id": 5,
        "image": "images/districts/coxs-bazar/hist-5.webp",
        "name": "Cox's Bazar Liberation War Memorial",
        "nameBn": "কক্সবাজার মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Cox's Bazar district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Cox's Bazar"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/coxs-bazar/tour-1.webp",
        "name": "World's Longest Natural Sea Beach",
        "nameBn": "World's Longest Natural Sea Beach (কক্সবাজার)",
        "category": "120 km Ocean Beach",
        "desc": "World's Longest Natural Sea Beach stands as an iconic tourist highlight in Cox's Bazar district. Nestled in natural surroundings under Chattogram Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Cox's Bazar Riverfront, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/coxs-bazar/tour-2.webp",
        "name": "Marine Drive & Himchari",
        "nameBn": "Marine Drive & Himchari (কক্সবাজার)",
        "category": "Scenic Coastal Drive",
        "desc": "Spectacular ocean road flanked by lush green tropical hills on one side and breaking surf.",
        "location": "Forest Range, Cox's Bazar"
      },
      {
        "id": 3,
        "image": "images/districts/coxs-bazar/tour-3.webp",
        "name": "Cox's Bazar Cultural Heritage Museum",
        "nameBn": "কক্সবাজার লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Cox's Bazar district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Cox's Bazar"
      },
      {
        "id": 4,
        "image": "images/districts/coxs-bazar/tour-4.webp",
        "name": "Cox's Bazar Scenic Lake & Boating Resort",
        "nameBn": "কক্সবাজার মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Cox's Bazar district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Cox's Bazar"
      },
      {
        "id": 5,
        "image": "images/districts/coxs-bazar/tour-5.webp",
        "name": "Cox's Bazar Sunset Hilltop Viewpoint",
        "nameBn": "কক্সবাজার সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Cox's Bazar district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Cox's Bazar"
      }
    ]
  },
  {
    "id": 20,
    "slug": "feni",
    "en": "Feni",
    "bn": "ফেনী",
    "div": "Chattogram",
    "lat": 23.0032,
    "lng": 91.4127,
    "coordinates": "23.0032, 91.4127",
    "est": 1984,
    "area": "928.34 km²",
    "pop": "1.5M",
    "dist": "150 km",
    "route": "Via Dhaka-Chittagong Highway N1 (approx. 2.5 - 3 hours by express bus or intercity train).",
    "tagline": "Feni (ফেনী) is a picturesque and historically significant administrative district in Chattogram Division, Bangladesh.",
    "heroImage": "images/districts/feni/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/feni/carousel-1.webp",
        "title": "Feni Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Chattogram Division"
      },
      {
        "id": 2,
        "image": "images/districts/feni/carousel-2.webp",
        "title": "Historic Monuments of Feni",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/feni/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/feni/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/feni/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/feni/hist-1.webp",
        "name": "Bijoy Singh Dighi",
        "nameBn": "Bijoy Singh Dighi (ফেনী)",
        "category": "Royal Heritage",
        "desc": "Massive historic water tank dating back to the Sena dynasty surrounded by grand shade trees.",
        "location": "Feni Sadar, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/feni/hist-2.webp",
        "name": "Shamsher Gazi Fort",
        "nameBn": "Shamsher Gazi Fort (ফেনী)",
        "category": "Historic Mosque",
        "desc": "Remnants of the 18th-century rebel ruler Shamsher Gazi who fought colonial expansion.",
        "location": "Old Town, Feni"
      },
      {
        "id": 3,
        "image": "images/districts/feni/hist-3.webp",
        "name": "Feni Colonial Court & Mint",
        "nameBn": "ফেনী ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Feni district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Feni"
      },
      {
        "id": 4,
        "image": "images/districts/feni/hist-4.webp",
        "name": "Feni Archeological Mound",
        "nameBn": "ফেনী প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Feni district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Feni"
      },
      {
        "id": 5,
        "image": "images/districts/feni/hist-5.webp",
        "name": "Feni Liberation War Memorial",
        "nameBn": "ফেনী মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Feni district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Feni"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/feni/tour-1.webp",
        "name": "Muhuri Irrigation Project & Dam",
        "nameBn": "Muhuri Irrigation Project & Dam (ফেনী)",
        "category": "Eco-Tourism",
        "desc": "Second-largest water control project in Bangladesh with mangrove trees and winter waterbirds.",
        "location": "Feni Riverfront, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/feni/tour-2.webp",
        "name": "Chandgazi Mosque",
        "nameBn": "Chandgazi Mosque (ফেনী)",
        "category": "Mughal Architecture",
        "desc": "Chandgazi Mosque stands as an iconic tourist highlight in Feni district. Nestled in natural surroundings under Chattogram Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Feni"
      },
      {
        "id": 3,
        "image": "images/districts/feni/tour-3.webp",
        "name": "Feni Cultural Heritage Museum",
        "nameBn": "ফেনী লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Feni district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Feni"
      },
      {
        "id": 4,
        "image": "images/districts/feni/tour-4.webp",
        "name": "Feni Scenic Lake & Boating Resort",
        "nameBn": "ফেনী মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Feni district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Feni"
      },
      {
        "id": 5,
        "image": "images/districts/feni/tour-5.webp",
        "name": "Feni Sunset Hilltop Viewpoint",
        "nameBn": "ফেনী সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Feni district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Feni"
      }
    ]
  },
  {
    "id": 21,
    "slug": "khagrachhari",
    "en": "Khagrachhari",
    "bn": "খাগড়াছড়ি",
    "div": "Chattogram",
    "lat": 23.1642,
    "lng": 91.9521,
    "coordinates": "23.1642, 91.9521",
    "est": 1983,
    "area": "2,699.55 km²",
    "pop": "0.65M",
    "dist": "270 km",
    "route": "Direct AC/Non-AC buses from Dhaka via Feni-Mirsharai hill route (approx. 7 hours).",
    "tagline": "Khagrachhari (খাগড়াছড়ি) is a picturesque and historically significant administrative district in Chattogram Division, Bangladesh.",
    "heroImage": "images/districts/khagrachhari/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/khagrachhari/carousel-1.webp",
        "title": "Khagrachhari Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Chattogram Division"
      },
      {
        "id": 2,
        "image": "images/districts/khagrachhari/carousel-2.webp",
        "title": "Historic Monuments of Khagrachhari",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/khagrachhari/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/khagrachhari/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/khagrachhari/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/khagrachhari/hist-1.webp",
        "name": "Alutila Mysterious Cave",
        "nameBn": "Alutila Mysterious Cave (খাগড়াছড়ি)",
        "category": "Royal Heritage",
        "desc": "Dark, thrilling subterranean limestone tunnel running through ancient mountain stone.",
        "location": "Khagrachhari Sadar, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/khagrachhari/hist-2.webp",
        "name": "Manikchhari Mong Rajbari",
        "nameBn": "Manikchhari Mong Rajbari (খাগড়াছড়ি)",
        "category": "Historic Mosque",
        "desc": "Manikchhari Mong Rajbari is one of the most prominent historical monuments in Khagrachhari district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Khagrachhari"
      },
      {
        "id": 3,
        "image": "images/districts/khagrachhari/hist-3.webp",
        "name": "Khagrachhari Colonial Court & Mint",
        "nameBn": "খাগড়াছড়ি ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Khagrachhari district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Khagrachhari"
      },
      {
        "id": 4,
        "image": "images/districts/khagrachhari/hist-4.webp",
        "name": "Khagrachhari Archeological Mound",
        "nameBn": "খাগড়াছড়ি প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Khagrachhari district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Khagrachhari"
      },
      {
        "id": 5,
        "image": "images/districts/khagrachhari/hist-5.webp",
        "name": "Khagrachhari Liberation War Memorial",
        "nameBn": "খাগড়াছড়ি মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Khagrachhari district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Khagrachhari"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/khagrachhari/tour-1.webp",
        "name": "Sajek Valley & Ruilui Para",
        "nameBn": "Sajek Valley & Ruilui Para (খাগড়াছড়ি)",
        "category": "Valley in Clouds",
        "desc": "The celebrated \"Queen of Hills\" at 1,800 ft with floating clouds and wooden cottages.",
        "location": "Khagrachhari Riverfront, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/khagrachhari/tour-2.webp",
        "name": "Risang Waterfall",
        "nameBn": "Risang Waterfall (খাগড়াছড়ি)",
        "category": "Natural Cascades",
        "desc": "Risang Waterfall stands as an iconic tourist highlight in Khagrachhari district. Nestled in natural surroundings under Chattogram Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Khagrachhari"
      },
      {
        "id": 3,
        "image": "images/districts/khagrachhari/tour-3.webp",
        "name": "Khagrachhari Cultural Heritage Museum",
        "nameBn": "খাগড়াছড়ি লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Khagrachhari district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Khagrachhari"
      },
      {
        "id": 4,
        "image": "images/districts/khagrachhari/tour-4.webp",
        "name": "Khagrachhari Scenic Lake & Boating Resort",
        "nameBn": "খাগড়াছড়ি মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Khagrachhari district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Khagrachhari"
      },
      {
        "id": 5,
        "image": "images/districts/khagrachhari/tour-5.webp",
        "name": "Khagrachhari Sunset Hilltop Viewpoint",
        "nameBn": "খাগড়াছড়ি সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Khagrachhari district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Khagrachhari"
      }
    ]
  },
  {
    "id": 22,
    "slug": "lakshmipur",
    "en": "Lakshmipur",
    "bn": "লক্ষ্মীপুর",
    "div": "Chattogram",
    "lat": 22.9005,
    "lng": 90.8557,
    "coordinates": "22.9005, 90.8557",
    "est": 1984,
    "area": "1,455.96 km²",
    "pop": "1.8M",
    "dist": "155 km",
    "route": "Via Padma Bridge expressway through Chandpur, or Dhaka-Chittagong highway branch (3.5 hrs).",
    "tagline": "Lakshmipur (লক্ষ্মীপুর) is a picturesque and historically significant administrative district in Chattogram Division, Bangladesh.",
    "heroImage": "images/districts/lakshmipur/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/lakshmipur/carousel-1.webp",
        "title": "Lakshmipur Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Chattogram Division"
      },
      {
        "id": 2,
        "image": "images/districts/lakshmipur/carousel-2.webp",
        "title": "Historic Monuments of Lakshmipur",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/lakshmipur/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/lakshmipur/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/lakshmipur/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/lakshmipur/hist-1.webp",
        "name": "Dalal Bazar Zamindar Bari",
        "nameBn": "Dalal Bazar Zamindar Bari (লক্ষ্মীপুর)",
        "category": "Royal Heritage",
        "desc": "Dalal Bazar Zamindar Bari is one of the most prominent historical monuments in Lakshmipur district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Lakshmipur Sadar, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/lakshmipur/hist-2.webp",
        "name": "Khoa Sagor Dighi",
        "nameBn": "Khoa Sagor Dighi (লক্ষ্মীপুর)",
        "category": "Historic Mosque",
        "desc": "Immense historic water reservoir named after the morning mist that covers the surface.",
        "location": "Old Town, Lakshmipur"
      },
      {
        "id": 3,
        "image": "images/districts/lakshmipur/hist-3.webp",
        "name": "Lakshmipur Colonial Court & Mint",
        "nameBn": "লক্ষ্মীপুর ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Lakshmipur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Lakshmipur"
      },
      {
        "id": 4,
        "image": "images/districts/lakshmipur/hist-4.webp",
        "name": "Lakshmipur Archeological Mound",
        "nameBn": "লক্ষ্মীপুর প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Lakshmipur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Lakshmipur"
      },
      {
        "id": 5,
        "image": "images/districts/lakshmipur/hist-5.webp",
        "name": "Lakshmipur Liberation War Memorial",
        "nameBn": "লক্ষ্মীপুর মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Lakshmipur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Lakshmipur"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/lakshmipur/tour-1.webp",
        "name": "Meghna River Estuary",
        "nameBn": "Meghna River Estuary (লক্ষ্মীপুর)",
        "category": "Coastal Waters",
        "desc": "Meghna River Estuary stands as an iconic tourist highlight in Lakshmipur district. Nestled in natural surroundings under Chattogram Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Lakshmipur Riverfront, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/lakshmipur/tour-2.webp",
        "name": "Ramgati Coastal Fishing Ports",
        "nameBn": "Ramgati Coastal Fishing Ports (লক্ষ্মীপুর)",
        "category": "Maritime Culture",
        "desc": "Ramgati Coastal Fishing Ports stands as an iconic tourist highlight in Lakshmipur district. Nestled in natural surroundings under Chattogram Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Lakshmipur"
      },
      {
        "id": 3,
        "image": "images/districts/lakshmipur/tour-3.webp",
        "name": "Lakshmipur Cultural Heritage Museum",
        "nameBn": "লক্ষ্মীপুর লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Lakshmipur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Lakshmipur"
      },
      {
        "id": 4,
        "image": "images/districts/lakshmipur/tour-4.webp",
        "name": "Lakshmipur Scenic Lake & Boating Resort",
        "nameBn": "লক্ষ্মীপুর মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Lakshmipur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Lakshmipur"
      },
      {
        "id": 5,
        "image": "images/districts/lakshmipur/tour-5.webp",
        "name": "Lakshmipur Sunset Hilltop Viewpoint",
        "nameBn": "লক্ষ্মীপুর সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Lakshmipur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Lakshmipur"
      }
    ]
  },
  {
    "id": 23,
    "slug": "noakhali",
    "en": "Noakhali",
    "bn": "নোয়াখালী",
    "div": "Chattogram",
    "lat": 22.811,
    "lng": 91.1241,
    "coordinates": "22.8110, 91.1241",
    "est": 1821,
    "area": "4,202.70 km²",
    "pop": "3.2M",
    "dist": "165 km",
    "route": "Via Dhaka-Chittagong Highway branching at Comilla (approx. 3.5 - 4 hours by bus/train).",
    "tagline": "Noakhali (নোয়াখালী) is a picturesque and historically significant administrative district in Chattogram Division, Bangladesh.",
    "heroImage": "images/districts/noakhali/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/noakhali/carousel-1.webp",
        "title": "Noakhali Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Chattogram Division"
      },
      {
        "id": 2,
        "image": "images/districts/noakhali/carousel-2.webp",
        "title": "Historic Monuments of Noakhali",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/noakhali/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/noakhali/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/noakhali/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/noakhali/hist-1.webp",
        "name": "Gandhi Ashram Trust (Jayag)",
        "nameBn": "Gandhi Ashram Trust (Jayag) (নোয়াখালী)",
        "category": "Royal Heritage",
        "desc": "Historic sanctuary founded following Mahatma Gandhi's 1946 peace mission in Noakhali.",
        "location": "Noakhali Sadar, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/noakhali/hist-2.webp",
        "name": "Bajra Shahi Mosque",
        "nameBn": "Bajra Shahi Mosque (নোয়াখালী)",
        "category": "Historic Mosque",
        "desc": "Majestic 1741 Mughal mosque inspired by Delhi's historic grand congregational mosque.",
        "location": "Old Town, Noakhali"
      },
      {
        "id": 3,
        "image": "images/districts/noakhali/hist-3.webp",
        "name": "Noakhali Colonial Court & Mint",
        "nameBn": "নোয়াখালী ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Noakhali district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Noakhali"
      },
      {
        "id": 4,
        "image": "images/districts/noakhali/hist-4.webp",
        "name": "Noakhali Archeological Mound",
        "nameBn": "নোয়াখালী প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Noakhali district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Noakhali"
      },
      {
        "id": 5,
        "image": "images/districts/noakhali/hist-5.webp",
        "name": "Noakhali Liberation War Memorial",
        "nameBn": "নোয়াখালী মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Noakhali district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Noakhali"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/noakhali/tour-1.webp",
        "name": "Nijhum Dwip (Silent Island)",
        "nameBn": "Nijhum Dwip (Silent Island) (নোয়াখালী)",
        "category": "National Marine Park",
        "desc": "Serene offshore island famous for thousands of wild spotted deer and migratory birdlife.",
        "location": "Noakhali Riverfront, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/noakhali/tour-2.webp",
        "name": "Swarnadwip & Coastal Polders",
        "nameBn": "Swarnadwip & Coastal Polders (নোয়াখালী)",
        "category": "Delta Frontier",
        "desc": "Swarnadwip & Coastal Polders stands as an iconic tourist highlight in Noakhali district. Nestled in natural surroundings under Chattogram Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Noakhali"
      },
      {
        "id": 3,
        "image": "images/districts/noakhali/tour-3.webp",
        "name": "Noakhali Cultural Heritage Museum",
        "nameBn": "নোয়াখালী লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Noakhali district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Noakhali"
      },
      {
        "id": 4,
        "image": "images/districts/noakhali/tour-4.webp",
        "name": "Noakhali Scenic Lake & Boating Resort",
        "nameBn": "নোয়াখালী মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Noakhali district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Noakhali"
      },
      {
        "id": 5,
        "image": "images/districts/noakhali/tour-5.webp",
        "name": "Noakhali Sunset Hilltop Viewpoint",
        "nameBn": "নোয়াখালী সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Noakhali district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Noakhali"
      }
    ]
  },
  {
    "id": 24,
    "slug": "rangamati",
    "en": "Rangamati",
    "bn": "রাঙ্গামাটি",
    "div": "Chattogram",
    "lat": 22.83,
    "lng": 92.2795,
    "coordinates": "22.8300, 92.2795",
    "est": 1983,
    "area": "6,116.13 km²",
    "pop": "0.62M",
    "dist": "305 km",
    "route": "Direct highway buses from Dhaka (8 hrs), or fly to Chattogram and drive 2 hours.",
    "tagline": "Rangamati (রাঙ্গামাটি) is a picturesque and historically significant administrative district in Chattogram Division, Bangladesh.",
    "heroImage": "images/districts/rangamati/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/rangamati/carousel-1.webp",
        "title": "Rangamati Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Chattogram Division"
      },
      {
        "id": 2,
        "image": "images/districts/rangamati/carousel-2.webp",
        "title": "Historic Monuments of Rangamati",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/rangamati/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/rangamati/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/rangamati/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/rangamati/hist-1.webp",
        "name": "Chakma Royal Palace",
        "nameBn": "Chakma Royal Palace (রাঙ্গামাটি)",
        "category": "Royal Heritage",
        "desc": "Historical seat of the Chakma Raja, relocated following the creation of Kaptai Lake.",
        "location": "Rangamati Sadar, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/rangamati/hist-2.webp",
        "name": "Rajban Vihara",
        "nameBn": "Rajban Vihara (রাঙ্গামাটি)",
        "category": "Historic Mosque",
        "desc": "Rajban Vihara is one of the most prominent historical monuments in Rangamati district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Rangamati"
      },
      {
        "id": 3,
        "image": "images/districts/rangamati/hist-3.webp",
        "name": "Rangamati Colonial Court & Mint",
        "nameBn": "রাঙ্গামাটি ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Rangamati district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Rangamati"
      },
      {
        "id": 4,
        "image": "images/districts/rangamati/hist-4.webp",
        "name": "Rangamati Archeological Mound",
        "nameBn": "রাঙ্গামাটি প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Rangamati district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Rangamati"
      },
      {
        "id": 5,
        "image": "images/districts/rangamati/hist-5.webp",
        "name": "Rangamati Liberation War Memorial",
        "nameBn": "রাঙ্গামাটি মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Rangamati district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Rangamati"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/rangamati/tour-1.webp",
        "name": "Kaptai Lake & Hanging Bridge",
        "nameBn": "Kaptai Lake & Hanging Bridge (রাঙ্গামাটি)",
        "category": "Lake Paradise",
        "desc": "Largest artificial lake in South Asia with iconic hanging bridge and island restaurants.",
        "location": "Rangamati Riverfront, Chattogram"
      },
      {
        "id": 2,
        "image": "images/districts/rangamati/tour-2.webp",
        "name": "Shuvolong Waterfalls",
        "nameBn": "Shuvolong Waterfalls (রাঙ্গামাটি)",
        "category": "Boat Adventure",
        "desc": "Scenic gorge waterfall reached via peaceful motorized wooden boat rides across the lake.",
        "location": "Forest Range, Rangamati"
      },
      {
        "id": 3,
        "image": "images/districts/rangamati/tour-3.webp",
        "name": "Rangamati Cultural Heritage Museum",
        "nameBn": "রাঙ্গামাটি লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Rangamati district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Rangamati"
      },
      {
        "id": 4,
        "image": "images/districts/rangamati/tour-4.webp",
        "name": "Rangamati Scenic Lake & Boating Resort",
        "nameBn": "রাঙ্গামাটি মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Rangamati district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Rangamati"
      },
      {
        "id": 5,
        "image": "images/districts/rangamati/tour-5.webp",
        "name": "Rangamati Sunset Hilltop Viewpoint",
        "nameBn": "রাঙ্গামাটি সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Rangamati district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Rangamati"
      }
    ]
  },
  {
    "id": 25,
    "slug": "habiganj",
    "en": "Habiganj",
    "bn": "হবিগঞ্জ",
    "div": "Sylhet",
    "lat": 24.3681,
    "lng": 91.4303,
    "coordinates": "24.3681, 91.4303",
    "est": 1984,
    "area": "2,636.58 km²",
    "pop": "2.1M",
    "dist": "160 km",
    "route": "Via Dhaka-Sylhet Highway N2 or Upaban/Parabat Express intercity trains (approx. 3 hours).",
    "tagline": "Habiganj (হবিগঞ্জ) is a picturesque and historically significant administrative district in Sylhet Division, Bangladesh.",
    "heroImage": "images/districts/habiganj/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/habiganj/carousel-1.webp",
        "title": "Habiganj Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Sylhet Division"
      },
      {
        "id": 2,
        "image": "images/districts/habiganj/carousel-2.webp",
        "title": "Historic Monuments of Habiganj",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/habiganj/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/habiganj/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/habiganj/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/habiganj/hist-1.webp",
        "name": "Bithangal Akhra",
        "nameBn": "Bithangal Akhra (হবিগঞ্জ)",
        "category": "Royal Heritage",
        "desc": "17th-century Vaishnavite monastery housing antique carved wooden chariots and relics.",
        "location": "Habiganj Sadar, Sylhet"
      },
      {
        "id": 2,
        "image": "images/districts/habiganj/hist-2.webp",
        "name": "Uchail Shankerpasha Mosque",
        "nameBn": "Uchail Shankerpasha Mosque (হবিগঞ্জ)",
        "category": "Historic Mosque",
        "desc": "Early 16th-century Sultanate red-brick mosque with ornate terracotta flower motifs.",
        "location": "Old Town, Habiganj"
      },
      {
        "id": 3,
        "image": "images/districts/habiganj/hist-3.webp",
        "name": "Habiganj Colonial Court & Mint",
        "nameBn": "হবিগঞ্জ ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Habiganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Habiganj"
      },
      {
        "id": 4,
        "image": "images/districts/habiganj/hist-4.webp",
        "name": "Habiganj Archeological Mound",
        "nameBn": "হবিগঞ্জ প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Habiganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Habiganj"
      },
      {
        "id": 5,
        "image": "images/districts/habiganj/hist-5.webp",
        "name": "Habiganj Liberation War Memorial",
        "nameBn": "হবিগঞ্জ মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Habiganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Habiganj"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/habiganj/tour-1.webp",
        "name": "Satchari National Park",
        "nameBn": "Satchari National Park (হবিগঞ্জ)",
        "category": "Rainforest Haven",
        "desc": "Dense evergreen forest sanctuary home to rare hoolock gibbons and exotic canopy birds.",
        "location": "Habiganj Riverfront, Sylhet"
      },
      {
        "id": 2,
        "image": "images/districts/habiganj/tour-2.webp",
        "name": "Rolling Tea Gardens of Bahubal",
        "nameBn": "Rolling Tea Gardens of Bahubal (হবিগঞ্জ)",
        "category": "Tea Estates",
        "desc": "Verdant rolling hills carpeted with emerald green tea bushes as far as the eye can see.",
        "location": "Forest Range, Habiganj"
      },
      {
        "id": 3,
        "image": "images/districts/habiganj/tour-3.webp",
        "name": "Habiganj Cultural Heritage Museum",
        "nameBn": "হবিগঞ্জ লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Habiganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Habiganj"
      },
      {
        "id": 4,
        "image": "images/districts/habiganj/tour-4.webp",
        "name": "Habiganj Scenic Lake & Boating Resort",
        "nameBn": "হবিগঞ্জ মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Habiganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Habiganj"
      },
      {
        "id": 5,
        "image": "images/districts/habiganj/tour-5.webp",
        "name": "Habiganj Sunset Hilltop Viewpoint",
        "nameBn": "হবিগঞ্জ সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Habiganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Habiganj"
      }
    ]
  },
  {
    "id": 26,
    "slug": "moulvibazar",
    "en": "Moulvibazar",
    "bn": "মৌলভীবাজার",
    "div": "Sylhet",
    "lat": 24.4804,
    "lng": 91.9154,
    "coordinates": "24.4804, 91.9154",
    "est": 1984,
    "area": "2,799.38 km²",
    "pop": "2.2M",
    "dist": "200 km",
    "route": "Via Dhaka-Sylhet Highway N2 or intercity trains stopping at Sreemangal station (3.5 - 4 hrs).",
    "tagline": "Moulvibazar (মৌলভীবাজার) is a picturesque and historically significant administrative district in Sylhet Division, Bangladesh.",
    "heroImage": "images/districts/moulvibazar/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/moulvibazar/carousel-1.webp",
        "title": "Moulvibazar Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Sylhet Division"
      },
      {
        "id": 2,
        "image": "images/districts/moulvibazar/carousel-2.webp",
        "title": "Historic Monuments of Moulvibazar",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/moulvibazar/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/moulvibazar/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/moulvibazar/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/moulvibazar/hist-1.webp",
        "name": "Prithimpassa Nawab Estate",
        "nameBn": "Prithimpassa Nawab Estate (মৌলভীবাজার)",
        "category": "Royal Heritage",
        "desc": "Stately aristocratic estate established in 1792 with historical armory collections.",
        "location": "Moulvibazar Sadar, Sylhet"
      },
      {
        "id": 2,
        "image": "images/districts/moulvibazar/hist-2.webp",
        "name": "Khoja Mosque",
        "nameBn": "Khoja Mosque (মৌলভীবাজার)",
        "category": "Historic Mosque",
        "desc": "Ancient stone-and-brick prayer structure associated with early regional Sufi preachers.",
        "location": "Old Town, Moulvibazar"
      },
      {
        "id": 3,
        "image": "images/districts/moulvibazar/hist-3.webp",
        "name": "Moulvibazar Colonial Court & Mint",
        "nameBn": "মৌলভীবাজার ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Moulvibazar district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Moulvibazar"
      },
      {
        "id": 4,
        "image": "images/districts/moulvibazar/hist-4.webp",
        "name": "Moulvibazar Archeological Mound",
        "nameBn": "মৌলভীবাজার প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Moulvibazar district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Moulvibazar"
      },
      {
        "id": 5,
        "image": "images/districts/moulvibazar/hist-5.webp",
        "name": "Moulvibazar Liberation War Memorial",
        "nameBn": "মৌলভীবাজার মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Moulvibazar district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Moulvibazar"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/moulvibazar/tour-1.webp",
        "name": "Sreemangal Tea Country",
        "nameBn": "Sreemangal Tea Country (মৌলভীবাজার)",
        "category": "Tea Capital",
        "desc": "World capital of fine black and green tea gardens, pineapple hills, and Nilkantha 7-layer tea.",
        "location": "Moulvibazar Riverfront, Sylhet"
      },
      {
        "id": 2,
        "image": "images/districts/moulvibazar/tour-2.webp",
        "name": "Lawachara Rain Forest & Madhabkunda",
        "nameBn": "Lawachara Rain Forest & Madhabkunda (মৌলভীবাজার)",
        "category": "Rainforest & Falls",
        "desc": "Biodiverse rainforest home to rare primates paired with the highest natural waterfall in BD.",
        "location": "Forest Range, Moulvibazar"
      },
      {
        "id": 3,
        "image": "images/districts/moulvibazar/tour-3.webp",
        "name": "Moulvibazar Cultural Heritage Museum",
        "nameBn": "মৌলভীবাজার লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Moulvibazar district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Moulvibazar"
      },
      {
        "id": 4,
        "image": "images/districts/moulvibazar/tour-4.webp",
        "name": "Moulvibazar Scenic Lake & Boating Resort",
        "nameBn": "মৌলভীবাজার মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Moulvibazar district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Moulvibazar"
      },
      {
        "id": 5,
        "image": "images/districts/moulvibazar/tour-5.webp",
        "name": "Moulvibazar Sunset Hilltop Viewpoint",
        "nameBn": "মৌলভীবাজার সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Moulvibazar district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Moulvibazar"
      }
    ]
  },
  {
    "id": 27,
    "slug": "sunamganj",
    "en": "Sunamganj",
    "bn": "সুনামগঞ্জ",
    "div": "Sylhet",
    "lat": 24.9386,
    "lng": 91.346,
    "coordinates": "24.9386, 91.3460",
    "est": 1984,
    "area": "3,747.18 km²",
    "pop": "2.6M",
    "dist": "280 km",
    "route": "Via Dhaka-Sylhet Highway branching to Sunamganj or direct express buses (5.5 - 6 hours).",
    "tagline": "Sunamganj (সুনামগঞ্জ) is a picturesque and historically significant administrative district in Sylhet Division, Bangladesh.",
    "heroImage": "images/districts/sunamganj/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/sunamganj/carousel-1.webp",
        "title": "Sunamganj Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Sylhet Division"
      },
      {
        "id": 2,
        "image": "images/districts/sunamganj/carousel-2.webp",
        "title": "Historic Monuments of Sunamganj",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/sunamganj/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/sunamganj/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/sunamganj/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/sunamganj/hist-1.webp",
        "name": "Hason Raja Museum & Palace",
        "nameBn": "Hason Raja Museum & Palace (সুনামগঞ্জ)",
        "category": "Royal Heritage",
        "desc": "Ancestral memorial estate of the mystic folk philosopher, songwriter, and poet Hason Raja.",
        "location": "Sunamganj Sadar, Sylhet"
      },
      {
        "id": 2,
        "image": "images/districts/sunamganj/hist-2.webp",
        "name": "Pagla Jame Mosque",
        "nameBn": "Pagla Jame Mosque (সুনামগঞ্জ)",
        "category": "Historic Mosque",
        "desc": "Modern and neo-traditional Islamic monument adorned with intricate colored marble work.",
        "location": "Old Town, Sunamganj"
      },
      {
        "id": 3,
        "image": "images/districts/sunamganj/hist-3.webp",
        "name": "Sunamganj Colonial Court & Mint",
        "nameBn": "সুনামগঞ্জ ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Sunamganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Sunamganj"
      },
      {
        "id": 4,
        "image": "images/districts/sunamganj/hist-4.webp",
        "name": "Sunamganj Archeological Mound",
        "nameBn": "সুনামগঞ্জ প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Sunamganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Sunamganj"
      },
      {
        "id": 5,
        "image": "images/districts/sunamganj/hist-5.webp",
        "name": "Sunamganj Liberation War Memorial",
        "nameBn": "সুনামগঞ্জ মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Sunamganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Sunamganj"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/sunamganj/tour-1.webp",
        "name": "Tanguar Haor Ramsar Site",
        "nameBn": "Tanguar Haor Ramsar Site (সুনামগঞ্জ)",
        "category": "Wetland Paradise",
        "desc": "World heritage freshwater wetland sanctuary traversed by traditional luxury houseboats.",
        "location": "Sunamganj Riverfront, Sylhet"
      },
      {
        "id": 2,
        "image": "images/districts/sunamganj/tour-2.webp",
        "name": "Shimul Bagan & Jadukata River",
        "nameBn": "Shimul Bagan & Jadukata River (সুনামগঞ্জ)",
        "category": "Spring Wonderland",
        "desc": "Enchanting silk-cotton forest bursting with crimson flowers along transparent mountain waters.",
        "location": "Forest Range, Sunamganj"
      },
      {
        "id": 3,
        "image": "images/districts/sunamganj/tour-3.webp",
        "name": "Sunamganj Cultural Heritage Museum",
        "nameBn": "সুনামগঞ্জ লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Sunamganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Sunamganj"
      },
      {
        "id": 4,
        "image": "images/districts/sunamganj/tour-4.webp",
        "name": "Sunamganj Scenic Lake & Boating Resort",
        "nameBn": "সুনামগঞ্জ মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Sunamganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Sunamganj"
      },
      {
        "id": 5,
        "image": "images/districts/sunamganj/tour-5.webp",
        "name": "Sunamganj Sunset Hilltop Viewpoint",
        "nameBn": "সুনামগঞ্জ সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Sunamganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Sunamganj"
      }
    ]
  },
  {
    "id": 28,
    "slug": "sylhet",
    "en": "Sylhet",
    "bn": "সিলেট",
    "div": "Sylhet",
    "lat": 24.9192,
    "lng": 91.9873,
    "coordinates": "24.9192, 91.9873",
    "est": 1772,
    "area": "3,490.40 km²",
    "pop": "3.9M",
    "dist": "240 km",
    "route": "Via Dhaka-Sylhet Highway N2 (5 hrs), Parabat/Kalni Express train (5 hrs), or 35-min flight.",
    "tagline": "Sylhet (সিলেট) is a picturesque and historically significant administrative district in Sylhet Division, Bangladesh.",
    "heroImage": "images/districts/sylhet/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/sylhet/carousel-1.webp",
        "title": "Sylhet Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Sylhet Division"
      },
      {
        "id": 2,
        "image": "images/districts/sylhet/carousel-2.webp",
        "title": "Historic Monuments of Sylhet",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/sylhet/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/sylhet/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/sylhet/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/sylhet/hist-1.webp",
        "name": "Dargah of Hazrat Shah Jalal (R.)",
        "nameBn": "Dargah of Hazrat Shah Jalal (R.) (সিলেট)",
        "category": "Royal Heritage",
        "desc": "Famed 14th-century Sufi pilgrimage shrine complex featuring holy springs and koi fish pond.",
        "location": "Sylhet Sadar, Sylhet"
      },
      {
        "id": 2,
        "image": "images/districts/sylhet/hist-2.webp",
        "name": "Keane Bridge & Ali Amjad Clock",
        "nameBn": "Keane Bridge & Ali Amjad Clock (সিলেট)",
        "category": "Historic Mosque",
        "desc": "Keane Bridge & Ali Amjad Clock is one of the most prominent historical monuments in Sylhet district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Sylhet"
      },
      {
        "id": 3,
        "image": "images/districts/sylhet/hist-3.webp",
        "name": "Sylhet Colonial Court & Mint",
        "nameBn": "সিলেট ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Sylhet district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Sylhet"
      },
      {
        "id": 4,
        "image": "images/districts/sylhet/hist-4.webp",
        "name": "Sylhet Archeological Mound",
        "nameBn": "সিলেট প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Sylhet district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Sylhet"
      },
      {
        "id": 5,
        "image": "images/districts/sylhet/hist-5.webp",
        "name": "Sylhet Liberation War Memorial",
        "nameBn": "সিলেট মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Sylhet district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Sylhet"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/sylhet/tour-1.webp",
        "name": "Ratargul Freshwater Swamp Forest",
        "nameBn": "Ratargul Freshwater Swamp Forest (সিলেট)",
        "category": "Flooded Forest",
        "desc": "One of the world’s rare freshwater swamp forests explored via quiet wooden canoes.",
        "location": "Sylhet Riverfront, Sylhet"
      },
      {
        "id": 2,
        "image": "images/districts/sylhet/tour-2.webp",
        "name": "Jaflong & Bisnakandi",
        "nameBn": "Jaflong & Bisnakandi (সিলেট)",
        "category": "Rocky Rivers & Cliffs",
        "desc": "Pristine mountain streams rolling over gravel beds directly beneath the Meghalaya mountains.",
        "location": "Forest Range, Sylhet"
      },
      {
        "id": 3,
        "image": "images/districts/sylhet/tour-3.webp",
        "name": "Sylhet Cultural Heritage Museum",
        "nameBn": "সিলেট লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Sylhet district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Sylhet"
      },
      {
        "id": 4,
        "image": "images/districts/sylhet/tour-4.webp",
        "name": "Sylhet Scenic Lake & Boating Resort",
        "nameBn": "সিলেট মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Sylhet district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Sylhet"
      },
      {
        "id": 5,
        "image": "images/districts/sylhet/tour-5.webp",
        "name": "Sylhet Sunset Hilltop Viewpoint",
        "nameBn": "সিলেট সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Sylhet district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Sylhet"
      }
    ]
  },
  {
    "id": 29,
    "slug": "barguna",
    "en": "Barguna",
    "bn": "বরগুনা",
    "div": "Barishal",
    "lat": 22.1412,
    "lng": 90.1207,
    "coordinates": "22.1412, 90.1207",
    "est": 1984,
    "area": "1,831.31 km²",
    "pop": "0.9M",
    "dist": "320 km",
    "route": "Via Padma Bridge expressway through Barishal (6-7 hrs) or luxury overnight launch from Sadarghat.",
    "tagline": "Barguna (বরগুনা) is a picturesque and historically significant administrative district in Barishal Division, Bangladesh.",
    "heroImage": "images/districts/barguna/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/barguna/carousel-1.webp",
        "title": "Barguna Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Barishal Division"
      },
      {
        "id": 2,
        "image": "images/districts/barguna/carousel-2.webp",
        "title": "Historic Monuments of Barguna",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/barguna/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/barguna/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/barguna/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/barguna/hist-1.webp",
        "name": "Bibi Chini Shahi Mosque",
        "nameBn": "Bibi Chini Shahi Mosque (বরগুনা)",
        "category": "Royal Heritage",
        "desc": "Bibi Chini Shahi Mosque is one of the most prominent historical monuments in Barguna district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Barguna Sadar, Barishal"
      },
      {
        "id": 2,
        "image": "images/districts/barguna/hist-2.webp",
        "name": "Kankradon Historical Zamindar Estate",
        "nameBn": "Kankradon Historical Zamindar Estate (বরগুনা)",
        "category": "Historic Mosque",
        "desc": "Kankradon Historical Zamindar Estate is one of the most prominent historical monuments in Barguna district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Barguna"
      },
      {
        "id": 3,
        "image": "images/districts/barguna/hist-3.webp",
        "name": "Barguna Colonial Court & Mint",
        "nameBn": "বরগুনা ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Barguna district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Barguna"
      },
      {
        "id": 4,
        "image": "images/districts/barguna/hist-4.webp",
        "name": "Barguna Archeological Mound",
        "nameBn": "বরগুনা প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Barguna district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Barguna"
      },
      {
        "id": 5,
        "image": "images/districts/barguna/hist-5.webp",
        "name": "Barguna Liberation War Memorial",
        "nameBn": "বরগুনা মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Barguna district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Barguna"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/barguna/tour-1.webp",
        "name": "Shuvo Sandhya Sea Beach",
        "nameBn": "Shuvo Sandhya Sea Beach (বরগুনা)",
        "category": "Coastal Beach",
        "desc": "Pristine 4 km untouched sandy beach where the Payra River embraces the Bay of Bengal.",
        "location": "Barguna Riverfront, Barishal"
      },
      {
        "id": 2,
        "image": "images/districts/barguna/tour-2.webp",
        "name": "Tengragiri Wildlife Sanctuary",
        "nameBn": "Tengragiri Wildlife Sanctuary (বরগুনা)",
        "category": "Mangrove Forest",
        "desc": "Second-largest coastal mangrove forest in Bangladesh with deer trails and wooden walkways.",
        "location": "Forest Range, Barguna"
      },
      {
        "id": 3,
        "image": "images/districts/barguna/tour-3.webp",
        "name": "Barguna Cultural Heritage Museum",
        "nameBn": "বরগুনা লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Barguna district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Barguna"
      },
      {
        "id": 4,
        "image": "images/districts/barguna/tour-4.webp",
        "name": "Barguna Scenic Lake & Boating Resort",
        "nameBn": "বরগুনা মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Barguna district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Barguna"
      },
      {
        "id": 5,
        "image": "images/districts/barguna/tour-5.webp",
        "name": "Barguna Sunset Hilltop Viewpoint",
        "nameBn": "বরগুনা সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Barguna district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Barguna"
      }
    ]
  },
  {
    "id": 30,
    "slug": "barishal",
    "en": "Barishal",
    "bn": "বরিশাল",
    "div": "Barishal",
    "lat": 22.8017,
    "lng": 90.3074,
    "coordinates": "22.8017, 90.3074",
    "est": 1797,
    "area": "2,784.52 km²",
    "pop": "2.4M",
    "dist": "185 km",
    "route": "Via Padma Bridge & Dhaka-Barishal Highway N8 (approx. 3.5 - 4 hrs) or overnight luxury launch.",
    "tagline": "Barishal (বরিশাল) is a picturesque and historically significant administrative district in Barishal Division, Bangladesh.",
    "heroImage": "images/districts/barishal/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/barishal/carousel-1.webp",
        "title": "Barishal Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Barishal Division"
      },
      {
        "id": 2,
        "image": "images/districts/barishal/carousel-2.webp",
        "title": "Historic Monuments of Barishal",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/barishal/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/barishal/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/barishal/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/barishal/hist-1.webp",
        "name": "Oxford Mission Epiphany Church",
        "nameBn": "Oxford Mission Epiphany Church (বরিশাল)",
        "category": "Royal Heritage",
        "desc": "Magnificent 1903 red-brick Greek-style cathedral, one of the grandest churches in Asia.",
        "location": "Barishal Sadar, Barishal"
      },
      {
        "id": 2,
        "image": "images/districts/barishal/hist-2.webp",
        "name": "Durga Sagar Dighi",
        "nameBn": "Durga Sagar Dighi (বরিশাল)",
        "category": "Historic Mosque",
        "desc": "Vast 1780 freshwater lake excavated by Rani Durgabati with a wildlife-rich center island.",
        "location": "Old Town, Barishal"
      },
      {
        "id": 3,
        "image": "images/districts/barishal/hist-3.webp",
        "name": "Barishal Colonial Court & Mint",
        "nameBn": "বরিশাল ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Barishal district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Barishal"
      },
      {
        "id": 4,
        "image": "images/districts/barishal/hist-4.webp",
        "name": "Barishal Archeological Mound",
        "nameBn": "বরিশাল প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Barishal district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Barishal"
      },
      {
        "id": 5,
        "image": "images/districts/barishal/hist-5.webp",
        "name": "Barishal Liberation War Memorial",
        "nameBn": "বরিশাল মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Barishal district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Barishal"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/barishal/tour-1.webp",
        "name": "Bhimruli Floating Guava Market",
        "nameBn": "Bhimruli Floating Guava Market (বরিশাল)",
        "category": "Waterway Heritage",
        "desc": "Picturesque floating fruit market where boatmen trade in wooden canoes through canal networks.",
        "location": "Barishal Riverfront, Barishal"
      },
      {
        "id": 2,
        "image": "images/districts/barishal/tour-2.webp",
        "name": "Bells Park (Bangabandhu Udyan)",
        "nameBn": "Bells Park (Bangabandhu Udyan) (বরিশাল)",
        "category": "Riverside Promenade",
        "desc": "Bells Park (Bangabandhu Udyan) stands as an iconic tourist highlight in Barishal district. Nestled in natural surroundings under Barishal Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Barishal"
      },
      {
        "id": 3,
        "image": "images/districts/barishal/tour-3.webp",
        "name": "Barishal Cultural Heritage Museum",
        "nameBn": "বরিশাল লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Barishal district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Barishal"
      },
      {
        "id": 4,
        "image": "images/districts/barishal/tour-4.webp",
        "name": "Barishal Scenic Lake & Boating Resort",
        "nameBn": "বরিশাল মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Barishal district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Barishal"
      },
      {
        "id": 5,
        "image": "images/districts/barishal/tour-5.webp",
        "name": "Barishal Sunset Hilltop Viewpoint",
        "nameBn": "বরিশাল সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Barishal district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Barishal"
      }
    ]
  },
  {
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
  },
  {
    "id": 32,
    "slug": "jhalokathi",
    "en": "Jhalokathi",
    "bn": "ঝালকাঠি",
    "div": "Barishal",
    "lat": 22.5728,
    "lng": 90.1839,
    "coordinates": "22.5728, 90.1839",
    "est": 1984,
    "area": "749.33 km²",
    "pop": "0.7M",
    "dist": "195 km",
    "route": "Via Padma Bridge and Barishal highway (approx. 4 hours) or river route from Dhaka.",
    "tagline": "Jhalokathi (ঝালকাঠি) is a picturesque and historically significant administrative district in Barishal Division, Bangladesh.",
    "heroImage": "images/districts/jhalokathi/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/jhalokathi/carousel-1.webp",
        "title": "Jhalokathi Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Barishal Division"
      },
      {
        "id": 2,
        "image": "images/districts/jhalokathi/carousel-2.webp",
        "title": "Historic Monuments of Jhalokathi",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/jhalokathi/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/jhalokathi/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/jhalokathi/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/jhalokathi/hist-1.webp",
        "name": "Sujabad Mughal Fort",
        "nameBn": "Sujabad Mughal Fort (ঝালকাঠি)",
        "category": "Royal Heritage",
        "desc": "Historic 17th-century river fortress built to protect Barishal region from pirate attacks.",
        "location": "Jhalokathi Sadar, Barishal"
      },
      {
        "id": 2,
        "image": "images/districts/jhalokathi/hist-2.webp",
        "name": "Kirtipasha Zamindar Bari",
        "nameBn": "Kirtipasha Zamindar Bari (ঝালকাঠি)",
        "category": "Historic Mosque",
        "desc": "Historical ruins of a grand feudal palace surrounded by water moats and old banyan trees.",
        "location": "Old Town, Jhalokathi"
      },
      {
        "id": 3,
        "image": "images/districts/jhalokathi/hist-3.webp",
        "name": "Jhalokathi Colonial Court & Mint",
        "nameBn": "ঝালকাঠি ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Jhalokathi district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Jhalokathi"
      },
      {
        "id": 4,
        "image": "images/districts/jhalokathi/hist-4.webp",
        "name": "Jhalokathi Archeological Mound",
        "nameBn": "ঝালকাঠি প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Jhalokathi district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Jhalokathi"
      },
      {
        "id": 5,
        "image": "images/districts/jhalokathi/hist-5.webp",
        "name": "Jhalokathi Liberation War Memorial",
        "nameBn": "ঝালকাঠি মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Jhalokathi district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Jhalokathi"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/jhalokathi/tour-1.webp",
        "name": "Bhimruli Canal & Guava Orchards",
        "nameBn": "Bhimruli Canal & Guava Orchards (ঝালকাঠি)",
        "category": "Canal Tourism",
        "desc": "Vast network of lush canal waterways called the \"Venice of Bengal\", famed for floating guava trade.",
        "location": "Jhalokathi Riverfront, Barishal"
      },
      {
        "id": 2,
        "image": "images/districts/jhalokathi/tour-2.webp",
        "name": "Gaba Shahi Mosque",
        "nameBn": "Gaba Shahi Mosque (ঝালকাঠি)",
        "category": "Historic Monument",
        "desc": "Ancient three-domed prayer house showcasing traditional lime and brick construction.",
        "location": "Forest Range, Jhalokathi"
      },
      {
        "id": 3,
        "image": "images/districts/jhalokathi/tour-3.webp",
        "name": "Jhalokathi Cultural Heritage Museum",
        "nameBn": "ঝালকাঠি লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Jhalokathi district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Jhalokathi"
      },
      {
        "id": 4,
        "image": "images/districts/jhalokathi/tour-4.webp",
        "name": "Jhalokathi Scenic Lake & Boating Resort",
        "nameBn": "ঝালকাঠি মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Jhalokathi district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Jhalokathi"
      },
      {
        "id": 5,
        "image": "images/districts/jhalokathi/tour-5.webp",
        "name": "Jhalokathi Sunset Hilltop Viewpoint",
        "nameBn": "ঝালকাঠি সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Jhalokathi district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Jhalokathi"
      }
    ]
  },
  {
    "id": 33,
    "slug": "patuakhali",
    "en": "Patuakhali",
    "bn": "পটুয়াখালী",
    "div": "Barishal",
    "lat": 22.3139,
    "lng": 90.4084,
    "coordinates": "22.3139, 90.4084",
    "est": 1969,
    "area": "3,221.31 km²",
    "pop": "1.6M",
    "dist": "260 km",
    "route": "Directly via Padma Bridge and Payra Bridge expressway (approx. 5 hrs) or overnight launch.",
    "tagline": "Patuakhali (পটুয়াখালী) is a picturesque and historically significant administrative district in Barishal Division, Bangladesh.",
    "heroImage": "images/districts/patuakhali/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/patuakhali/carousel-1.webp",
        "title": "Patuakhali Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Barishal Division"
      },
      {
        "id": 2,
        "image": "images/districts/patuakhali/carousel-2.webp",
        "title": "Historic Monuments of Patuakhali",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/patuakhali/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/patuakhali/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/patuakhali/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/patuakhali/hist-1.webp",
        "name": "Kuakata Ancient Buddhist Wells",
        "nameBn": "Kuakata Ancient Buddhist Wells (পটুয়াখালী)",
        "category": "Royal Heritage",
        "desc": "Centuries-old wooden wells dug by Rakhine settlers to obtain sweet water near the sea.",
        "location": "Patuakhali Sadar, Barishal"
      },
      {
        "id": 2,
        "image": "images/districts/patuakhali/hist-2.webp",
        "name": "Shreerampur Shahi Mosque",
        "nameBn": "Shreerampur Shahi Mosque (পটুয়াখালী)",
        "category": "Historic Mosque",
        "desc": "Shreerampur Shahi Mosque is one of the most prominent historical monuments in Patuakhali district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Patuakhali"
      },
      {
        "id": 3,
        "image": "images/districts/patuakhali/hist-3.webp",
        "name": "Patuakhali Colonial Court & Mint",
        "nameBn": "পটুয়াখালী ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Patuakhali district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Patuakhali"
      },
      {
        "id": 4,
        "image": "images/districts/patuakhali/hist-4.webp",
        "name": "Patuakhali Archeological Mound",
        "nameBn": "পটুয়াখালী প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Patuakhali district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Patuakhali"
      },
      {
        "id": 5,
        "image": "images/districts/patuakhali/hist-5.webp",
        "name": "Patuakhali Liberation War Memorial",
        "nameBn": "পটুয়াখালী মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Patuakhali district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Patuakhali"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/patuakhali/tour-1.webp",
        "name": "Kuakata \"Daughter of the Sea\" Beach",
        "nameBn": "Kuakata \"Daughter of the Sea\" Beach (পটুয়াখালী)",
        "category": "Sunrise & Sunset Coast",
        "desc": "Rare 18 km continuous beach where visitors can witness both sunrise and sunset over the ocean.",
        "location": "Patuakhali Riverfront, Barishal"
      },
      {
        "id": 2,
        "image": "images/districts/patuakhali/tour-2.webp",
        "name": "Fatrar Char & Mangrove Forest",
        "nameBn": "Fatrar Char & Mangrove Forest (পটুয়াখালী)",
        "category": "Eco Wilderness",
        "desc": "Dense coastal mangrove island extension of the Sundarbans accessible by trawler boats.",
        "location": "Forest Range, Patuakhali"
      },
      {
        "id": 3,
        "image": "images/districts/patuakhali/tour-3.webp",
        "name": "Patuakhali Cultural Heritage Museum",
        "nameBn": "পটুয়াখালী লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Patuakhali district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Patuakhali"
      },
      {
        "id": 4,
        "image": "images/districts/patuakhali/tour-4.webp",
        "name": "Patuakhali Scenic Lake & Boating Resort",
        "nameBn": "পটুয়াখালী মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Patuakhali district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Patuakhali"
      },
      {
        "id": 5,
        "image": "images/districts/patuakhali/tour-5.webp",
        "name": "Patuakhali Sunset Hilltop Viewpoint",
        "nameBn": "পটুয়াখালী সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Patuakhali district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Patuakhali"
      }
    ]
  },
  {
    "id": 34,
    "slug": "pirojpur",
    "en": "Pirojpur",
    "bn": "পিরোজপুর",
    "div": "Barishal",
    "lat": 22.5338,
    "lng": 89.9932,
    "coordinates": "22.5338, 89.9932",
    "est": 1984,
    "area": "1,307.61 km²",
    "pop": "1.2M",
    "dist": "210 km",
    "route": "Via Padma Bridge and Bekutia (8th Bangladesh-China Friendship) Bridge (approx. 4.5 hrs).",
    "tagline": "Pirojpur (পিরোজপুর) is a picturesque and historically significant administrative district in Barishal Division, Bangladesh.",
    "heroImage": "images/districts/pirojpur/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/pirojpur/carousel-1.webp",
        "title": "Pirojpur Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Barishal Division"
      },
      {
        "id": 2,
        "image": "images/districts/pirojpur/carousel-2.webp",
        "title": "Historic Monuments of Pirojpur",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/pirojpur/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/pirojpur/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/pirojpur/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/pirojpur/hist-1.webp",
        "name": "Rayerkathi Zamindar Palace & Temple",
        "nameBn": "Rayerkathi Zamindar Palace & Temple (পিরোজপুর)",
        "category": "Royal Heritage",
        "desc": "Centuries-old royal estate founded in 1658 with surviving temples and historical ponds.",
        "location": "Pirojpur Sadar, Barishal"
      },
      {
        "id": 2,
        "image": "images/districts/pirojpur/hist-2.webp",
        "name": "Majlishpur Ancient Mosque",
        "nameBn": "Majlishpur Ancient Mosque (পিরোজপুর)",
        "category": "Historic Mosque",
        "desc": "Majlishpur Ancient Mosque is one of the most prominent historical monuments in Pirojpur district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Pirojpur"
      },
      {
        "id": 3,
        "image": "images/districts/pirojpur/hist-3.webp",
        "name": "Pirojpur Colonial Court & Mint",
        "nameBn": "পিরোজপুর ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Pirojpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Pirojpur"
      },
      {
        "id": 4,
        "image": "images/districts/pirojpur/hist-4.webp",
        "name": "Pirojpur Archeological Mound",
        "nameBn": "পিরোজপুর প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Pirojpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Pirojpur"
      },
      {
        "id": 5,
        "image": "images/districts/pirojpur/hist-5.webp",
        "name": "Pirojpur Liberation War Memorial",
        "nameBn": "পিরোজপুর মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Pirojpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Pirojpur"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/pirojpur/tour-1.webp",
        "name": "Bekutia Bridge & Sandhya River",
        "nameBn": "Bekutia Bridge & Sandhya River (পিরোজপুর)",
        "category": "Modern Engineering",
        "desc": "Bekutia Bridge & Sandhya River stands as an iconic tourist highlight in Pirojpur district. Nestled in natural surroundings under Barishal Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Pirojpur Riverfront, Barishal"
      },
      {
        "id": 2,
        "image": "images/districts/pirojpur/tour-2.webp",
        "name": "Kuriana Floating Fruit Orchards",
        "nameBn": "Kuriana Floating Fruit Orchards (পিরোজপুর)",
        "category": "Horticultural Waterways",
        "desc": "Lush water canals where local farmers harvest and trade hog plums, guavas, and betel nuts.",
        "location": "Forest Range, Pirojpur"
      },
      {
        "id": 3,
        "image": "images/districts/pirojpur/tour-3.webp",
        "name": "Pirojpur Cultural Heritage Museum",
        "nameBn": "পিরোজপুর লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Pirojpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Pirojpur"
      },
      {
        "id": 4,
        "image": "images/districts/pirojpur/tour-4.webp",
        "name": "Pirojpur Scenic Lake & Boating Resort",
        "nameBn": "পিরোজপুর মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Pirojpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Pirojpur"
      },
      {
        "id": 5,
        "image": "images/districts/pirojpur/tour-5.webp",
        "name": "Pirojpur Sunset Hilltop Viewpoint",
        "nameBn": "পিরোজপুর সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Pirojpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Pirojpur"
      }
    ]
  },
  {
    "id": 35,
    "slug": "bagerhat",
    "en": "Bagerhat",
    "bn": "বাগেরহাট",
    "div": "Khulna",
    "lat": 22.522,
    "lng": 89.7599,
    "coordinates": "22.5220, 89.7599",
    "est": 1984,
    "area": "3,959.11 km²",
    "pop": "1.5M",
    "dist": "200 km",
    "route": "Via Padma Bridge and Dhaka-Khulna Highway N8 (approx. 3.5 - 4 hours by bus/car).",
    "tagline": "Bagerhat (বাগেরহাট) is a picturesque and historically significant administrative district in Khulna Division, Bangladesh.",
    "heroImage": "images/districts/bagerhat/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/bagerhat/carousel-1.webp",
        "title": "Bagerhat Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Khulna Division"
      },
      {
        "id": 2,
        "image": "images/districts/bagerhat/carousel-2.webp",
        "title": "Historic Monuments of Bagerhat",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/bagerhat/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/bagerhat/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/bagerhat/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/bagerhat/hist-1.webp",
        "name": "Sixty Dome Mosque (Shat Gombuj)",
        "nameBn": "Sixty Dome Mosque (Shat Gombuj) (বাগেরহাট)",
        "category": "Royal Heritage",
        "desc": "UNESCO World Heritage Site: 15th-century masterpiece with 77 domes built by Khan Jahan Ali.",
        "location": "Bagerhat Sadar, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/bagerhat/hist-2.webp",
        "name": "Mausoleum of Khan Jahan Ali",
        "nameBn": "Mausoleum of Khan Jahan Ali (বাগেরহাট)",
        "category": "Historic Mosque",
        "desc": "Sacred shrine complex featuring the famous Thakur Dighi lake inhabited by holy marsh crocodiles.",
        "location": "Old Town, Bagerhat"
      },
      {
        "id": 3,
        "image": "images/districts/bagerhat/hist-3.webp",
        "name": "Bagerhat Colonial Court & Mint",
        "nameBn": "বাগেরহাট ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Bagerhat district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Bagerhat"
      },
      {
        "id": 4,
        "image": "images/districts/bagerhat/hist-4.webp",
        "name": "Bagerhat Archeological Mound",
        "nameBn": "বাগেরহাট প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Bagerhat district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Bagerhat"
      },
      {
        "id": 5,
        "image": "images/districts/bagerhat/hist-5.webp",
        "name": "Bagerhat Liberation War Memorial",
        "nameBn": "বাগেরহাট মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Bagerhat district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Bagerhat"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/bagerhat/tour-1.webp",
        "name": "Sundarbans East Eco-Sanctuary",
        "nameBn": "Sundarbans East Eco-Sanctuary (বাগেরহাট)",
        "category": "UNESCO Mangrove Forest",
        "desc": "Gateway to the world’s largest mangrove forest, home to Bengal tigers and spotted deer.",
        "location": "Bagerhat Riverfront, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/bagerhat/tour-2.webp",
        "name": "Chunakhola Mosque",
        "nameBn": "Chunakhola Mosque (বাগেরহাট)",
        "category": "Archaeology",
        "desc": "Chunakhola Mosque stands as an iconic tourist highlight in Bagerhat district. Nestled in natural surroundings under Khulna Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Bagerhat"
      },
      {
        "id": 3,
        "image": "images/districts/bagerhat/tour-3.webp",
        "name": "Bagerhat Cultural Heritage Museum",
        "nameBn": "বাগেরহাট লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Bagerhat district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Bagerhat"
      },
      {
        "id": 4,
        "image": "images/districts/bagerhat/tour-4.webp",
        "name": "Bagerhat Scenic Lake & Boating Resort",
        "nameBn": "বাগেরহাট মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Bagerhat district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Bagerhat"
      },
      {
        "id": 5,
        "image": "images/districts/bagerhat/tour-5.webp",
        "name": "Bagerhat Sunset Hilltop Viewpoint",
        "nameBn": "বাগেরহাট সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Bagerhat district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Bagerhat"
      }
    ]
  },
  {
    "id": 36,
    "slug": "chuadanga",
    "en": "Chuadanga",
    "bn": "চুয়াডাঙ্গা",
    "div": "Khulna",
    "lat": 23.6083,
    "lng": 88.848,
    "coordinates": "23.6083, 88.8480",
    "est": 1984,
    "area": "1,170.87 km²",
    "pop": "1.2M",
    "dist": "230 km",
    "route": "Via Padma Bridge and Jhenaidah-Chuadanga highway or Chitra Express train (approx. 5 hrs).",
    "tagline": "Chuadanga (চুয়াডাঙ্গা) is a picturesque and historically significant administrative district in Khulna Division, Bangladesh.",
    "heroImage": "images/districts/chuadanga/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/chuadanga/carousel-1.webp",
        "title": "Chuadanga Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Khulna Division"
      },
      {
        "id": 2,
        "image": "images/districts/chuadanga/carousel-2.webp",
        "title": "Historic Monuments of Chuadanga",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/chuadanga/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/chuadanga/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/chuadanga/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/chuadanga/hist-1.webp",
        "name": "Gholdari Shahi Mosque",
        "nameBn": "Gholdari Shahi Mosque (চুয়াডাঙ্গা)",
        "category": "Royal Heritage",
        "desc": "Ancient 1006 CE mosque believed to be one of the earliest Muslim religious monuments in Bengal.",
        "location": "Chuadanga Sadar, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/chuadanga/hist-2.webp",
        "name": "Carew & Co. Historic Distillery",
        "nameBn": "Carew & Co. Historic Distillery (চুয়াডাঙ্গা)",
        "category": "Historic Mosque",
        "desc": "Founded in 1897 during British colonial rule, the historic distillery and sugar mill.",
        "location": "Old Town, Chuadanga"
      },
      {
        "id": 3,
        "image": "images/districts/chuadanga/hist-3.webp",
        "name": "Chuadanga Colonial Court & Mint",
        "nameBn": "চুয়াডাঙ্গা ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Chuadanga district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Chuadanga"
      },
      {
        "id": 4,
        "image": "images/districts/chuadanga/hist-4.webp",
        "name": "Chuadanga Archeological Mound",
        "nameBn": "চুয়াডাঙ্গা প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Chuadanga district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Chuadanga"
      },
      {
        "id": 5,
        "image": "images/districts/chuadanga/hist-5.webp",
        "name": "Chuadanga Liberation War Memorial",
        "nameBn": "চুয়াডাঙ্গা মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Chuadanga district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Chuadanga"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/chuadanga/tour-1.webp",
        "name": "Karpasdanga Christian Church & Memorial",
        "nameBn": "Karpasdanga Christian Church & Memorial (চুয়াডাঙ্গা)",
        "category": "Literary Heritage",
        "desc": "Historic 19th-century church where Rabindranath Tagore stayed during his estate visits.",
        "location": "Chuadanga Riverfront, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/chuadanga/tour-2.webp",
        "name": "Mathabhanga River Bank",
        "nameBn": "Mathabhanga River Bank (চুয়াডাঙ্গা)",
        "category": "Riverside Peace",
        "desc": "Mathabhanga River Bank stands as an iconic tourist highlight in Chuadanga district. Nestled in natural surroundings under Khulna Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Chuadanga"
      },
      {
        "id": 3,
        "image": "images/districts/chuadanga/tour-3.webp",
        "name": "Chuadanga Cultural Heritage Museum",
        "nameBn": "চুয়াডাঙ্গা লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Chuadanga district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Chuadanga"
      },
      {
        "id": 4,
        "image": "images/districts/chuadanga/tour-4.webp",
        "name": "Chuadanga Scenic Lake & Boating Resort",
        "nameBn": "চুয়াডাঙ্গা মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Chuadanga district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Chuadanga"
      },
      {
        "id": 5,
        "image": "images/districts/chuadanga/tour-5.webp",
        "name": "Chuadanga Sunset Hilltop Viewpoint",
        "nameBn": "চুয়াডাঙ্গা সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Chuadanga district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Chuadanga"
      }
    ]
  },
  {
    "id": 37,
    "slug": "jashore",
    "en": "Jashore",
    "bn": "যশোর",
    "div": "Khulna",
    "lat": 23.0898,
    "lng": 89.1747,
    "coordinates": "23.0898, 89.1747",
    "est": 1781,
    "area": "2,566.98 km²",
    "pop": "2.8M",
    "dist": "190 km",
    "route": "Via Padma Bridge expressway (approx. 3.5 hrs), Benapole Express train, or 35-min flight.",
    "tagline": "Jashore (যশোর) is a picturesque and historically significant administrative district in Khulna Division, Bangladesh.",
    "heroImage": "images/districts/jashore/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/jashore/carousel-1.webp",
        "title": "Jashore Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Khulna Division"
      },
      {
        "id": 2,
        "image": "images/districts/jashore/carousel-2.webp",
        "title": "Historic Monuments of Jashore",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/jashore/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/jashore/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/jashore/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/jashore/hist-1.webp",
        "name": "Mirzanagar Hammamkhana",
        "nameBn": "Mirzanagar Hammamkhana (যশোর)",
        "category": "Royal Heritage",
        "desc": "Mirzanagar Hammamkhana is one of the most prominent historical monuments in Jashore district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Jashore Sadar, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/jashore/hist-2.webp",
        "name": "Chanchra Rajbari & Shiva Temple",
        "nameBn": "Chanchra Rajbari & Shiva Temple (যশোর)",
        "category": "Historic Mosque",
        "desc": "Chanchra Rajbari & Shiva Temple is one of the most prominent historical monuments in Jashore district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Jashore"
      },
      {
        "id": 3,
        "image": "images/districts/jashore/hist-3.webp",
        "name": "Jashore Colonial Court & Mint",
        "nameBn": "যশোর ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Jashore district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Jashore"
      },
      {
        "id": 4,
        "image": "images/districts/jashore/hist-4.webp",
        "name": "Jashore Archeological Mound",
        "nameBn": "যশোর প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Jashore district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Jashore"
      },
      {
        "id": 5,
        "image": "images/districts/jashore/hist-5.webp",
        "name": "Jashore Liberation War Memorial",
        "nameBn": "যশোর মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Jashore district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Jashore"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/jashore/tour-1.webp",
        "name": "Gadkhali Flower Capital",
        "nameBn": "Gadkhali Flower Capital (যশোর)",
        "category": "Floral Tourism",
        "desc": "Vibrant commercial flower-growing hub producing carpets of roses, gerberas, and tuberoses.",
        "location": "Jashore Riverfront, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/jashore/tour-2.webp",
        "name": "Sagardari (Michael Madhusudan Memorial)",
        "nameBn": "Sagardari (Michael Madhusudan Memorial) (যশোর)",
        "category": "Literary Memorial",
        "desc": "Picturesque birthplace and memorial museum of legendary epic poet Michael Madhusudan Dutt.",
        "location": "Forest Range, Jashore"
      },
      {
        "id": 3,
        "image": "images/districts/jashore/tour-3.webp",
        "name": "Jashore Cultural Heritage Museum",
        "nameBn": "যশোর লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Jashore district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Jashore"
      },
      {
        "id": 4,
        "image": "images/districts/jashore/tour-4.webp",
        "name": "Jashore Scenic Lake & Boating Resort",
        "nameBn": "যশোর মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Jashore district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Jashore"
      },
      {
        "id": 5,
        "image": "images/districts/jashore/tour-5.webp",
        "name": "Jashore Sunset Hilltop Viewpoint",
        "nameBn": "যশোর সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Jashore district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Jashore"
      }
    ]
  },
  {
    "id": 38,
    "slug": "jhenaidah",
    "en": "Jhenaidah",
    "bn": "ঝিনাইদহ",
    "div": "Khulna",
    "lat": 23.4891,
    "lng": 89.0874,
    "coordinates": "23.4891, 89.0874",
    "est": 1984,
    "area": "1,964.77 km²",
    "pop": "1.8M",
    "dist": "215 km",
    "route": "Via Padma Bridge expressway through Magura (approx. 4 hours by highway bus/car).",
    "tagline": "Jhenaidah (ঝিনাইদহ) is a picturesque and historically significant administrative district in Khulna Division, Bangladesh.",
    "heroImage": "images/districts/jhenaidah/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/jhenaidah/carousel-1.webp",
        "title": "Jhenaidah Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Khulna Division"
      },
      {
        "id": 2,
        "image": "images/districts/jhenaidah/carousel-2.webp",
        "title": "Historic Monuments of Jhenaidah",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/jhenaidah/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/jhenaidah/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/jhenaidah/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/jhenaidah/hist-1.webp",
        "name": "Naldanga Temple Complex",
        "nameBn": "Naldanga Temple Complex (ঝিনাইদহ)",
        "category": "Royal Heritage",
        "desc": "Naldanga Temple Complex is one of the most prominent historical monuments in Jhenaidah district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Jhenaidah Sadar, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/jhenaidah/hist-2.webp",
        "name": "Shailkupa Shahi Mosque",
        "nameBn": "Shailkupa Shahi Mosque (ঝিনাইদহ)",
        "category": "Historic Mosque",
        "desc": "Shailkupa Shahi Mosque is one of the most prominent historical monuments in Jhenaidah district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Jhenaidah"
      },
      {
        "id": 3,
        "image": "images/districts/jhenaidah/hist-3.webp",
        "name": "Jhenaidah Colonial Court & Mint",
        "nameBn": "ঝিনাইদহ ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Jhenaidah district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Jhenaidah"
      },
      {
        "id": 4,
        "image": "images/districts/jhenaidah/hist-4.webp",
        "name": "Jhenaidah Archeological Mound",
        "nameBn": "ঝিনাইদহ প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Jhenaidah district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Jhenaidah"
      },
      {
        "id": 5,
        "image": "images/districts/jhenaidah/hist-5.webp",
        "name": "Jhenaidah Liberation War Memorial",
        "nameBn": "ঝিনাইদহ মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Jhenaidah district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Jhenaidah"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/jhenaidah/tour-1.webp",
        "name": "Dhol Samudra Dighi",
        "nameBn": "Dhol Samudra Dighi (ঝিনাইদহ)",
        "category": "Historic Lake",
        "desc": "Immense ancient waterbody associated with historical folk legends of self-sacrifice.",
        "location": "Jhenaidah Riverfront, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/jhenaidah/tour-2.webp",
        "name": "Johurul Haque Baor",
        "nameBn": "Johurul Haque Baor (ঝিনাইদহ)",
        "category": "Eco Wetland",
        "desc": "Johurul Haque Baor stands as an iconic tourist highlight in Jhenaidah district. Nestled in natural surroundings under Khulna Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Jhenaidah"
      },
      {
        "id": 3,
        "image": "images/districts/jhenaidah/tour-3.webp",
        "name": "Jhenaidah Cultural Heritage Museum",
        "nameBn": "ঝিনাইদহ লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Jhenaidah district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Jhenaidah"
      },
      {
        "id": 4,
        "image": "images/districts/jhenaidah/tour-4.webp",
        "name": "Jhenaidah Scenic Lake & Boating Resort",
        "nameBn": "ঝিনাইদহ মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Jhenaidah district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Jhenaidah"
      },
      {
        "id": 5,
        "image": "images/districts/jhenaidah/tour-5.webp",
        "name": "Jhenaidah Sunset Hilltop Viewpoint",
        "nameBn": "ঝিনাইদহ সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Jhenaidah district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Jhenaidah"
      }
    ]
  },
  {
    "id": 39,
    "slug": "khulna",
    "en": "Khulna",
    "bn": "খুলনা",
    "div": "Khulna",
    "lat": 22.5856,
    "lng": 89.4571,
    "coordinates": "22.5856, 89.4571",
    "est": 1882,
    "area": "4,394.46 km²",
    "pop": "2.4M",
    "dist": "220 km",
    "route": "Via Padma Bridge and Dhaka-Khulna Highway N8 (approx. 3.5 - 4 hrs), Sundarban Express train, or flight.",
    "tagline": "Khulna (খুলনা) is a picturesque and historically significant administrative district in Khulna Division, Bangladesh.",
    "heroImage": "images/districts/khulna/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/khulna/carousel-1.webp",
        "title": "Khulna Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Khulna Division"
      },
      {
        "id": 2,
        "image": "images/districts/khulna/carousel-2.webp",
        "title": "Historic Monuments of Khulna",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/khulna/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/khulna/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/khulna/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/khulna/hist-1.webp",
        "name": "Saint Joseph's Cathedral",
        "nameBn": "Saint Joseph's Cathedral (খুলনা)",
        "category": "Royal Heritage",
        "desc": "Historic 19th-century Roman Catholic church with classic European colonial arches.",
        "location": "Khulna Sadar, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/khulna/hist-2.webp",
        "name": "Shiromoni Historical War Memorial",
        "nameBn": "Shiromoni Historical War Memorial (খুলনা)",
        "category": "Historic Mosque",
        "desc": "Shiromoni Historical War Memorial is one of the most prominent historical monuments in Khulna district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Khulna"
      },
      {
        "id": 3,
        "image": "images/districts/khulna/hist-3.webp",
        "name": "Khulna Colonial Court & Mint",
        "nameBn": "খুলনা ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Khulna district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Khulna"
      },
      {
        "id": 4,
        "image": "images/districts/khulna/hist-4.webp",
        "name": "Khulna Archeological Mound",
        "nameBn": "খুলনা প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Khulna district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Khulna"
      },
      {
        "id": 5,
        "image": "images/districts/khulna/hist-5.webp",
        "name": "Khulna Liberation War Memorial",
        "nameBn": "খুলনা মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Khulna district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Khulna"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/khulna/tour-1.webp",
        "name": "Sundarbans National Forest Gateway",
        "nameBn": "Sundarbans National Forest Gateway (খুলনা)",
        "category": "UNESCO World Biosphere",
        "desc": "Sundarbans National Forest Gateway stands as an iconic tourist highlight in Khulna district. Nestled in natural surroundings under Khulna Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Khulna Riverfront, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/khulna/tour-2.webp",
        "name": "Khan Jahan Ali (Rupsha) Bridge",
        "nameBn": "Khan Jahan Ali (Rupsha) Bridge (খুলনা)",
        "category": "Scenic Sunset Point",
        "desc": "Sprawling suspension bridge offering panoramic river sunset views and riverside walkways.",
        "location": "Forest Range, Khulna"
      },
      {
        "id": 3,
        "image": "images/districts/khulna/tour-3.webp",
        "name": "Khulna Cultural Heritage Museum",
        "nameBn": "খুলনা লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Khulna district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Khulna"
      },
      {
        "id": 4,
        "image": "images/districts/khulna/tour-4.webp",
        "name": "Khulna Scenic Lake & Boating Resort",
        "nameBn": "খুলনা মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Khulna district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Khulna"
      },
      {
        "id": 5,
        "image": "images/districts/khulna/tour-5.webp",
        "name": "Khulna Sunset Hilltop Viewpoint",
        "nameBn": "খুলনা সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Khulna district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Khulna"
      }
    ]
  },
  {
    "id": 40,
    "slug": "kushtia",
    "en": "Kushtia",
    "bn": "কুষ্টিয়া",
    "div": "Khulna",
    "lat": 23.9229,
    "lng": 89.022,
    "coordinates": "23.9229, 89.0220",
    "est": 1984,
    "area": "1,608.80 km²",
    "pop": "2.0M",
    "dist": "210 km",
    "route": "Via Padma Bridge or Jamuna Bridge highway routes, or direct trains via Poradaha junction (4.5 hrs).",
    "tagline": "Kushtia (কুষ্টিয়া) is a picturesque and historically significant administrative district in Khulna Division, Bangladesh.",
    "heroImage": "images/districts/kushtia/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/kushtia/carousel-1.webp",
        "title": "Kushtia Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Khulna Division"
      },
      {
        "id": 2,
        "image": "images/districts/kushtia/carousel-2.webp",
        "title": "Historic Monuments of Kushtia",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/kushtia/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/kushtia/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/kushtia/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/kushtia/hist-1.webp",
        "name": "Lalon Shah Shrine (Chheuriya)",
        "nameBn": "Lalon Shah Shrine (Chheuriya) (কুষ্টিয়া)",
        "category": "Royal Heritage",
        "desc": "World-famous spiritual resting place and cultural academy of the mystic Baul saint Fakir Lalon Shah.",
        "location": "Kushtia Sadar, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/kushtia/hist-2.webp",
        "name": "Tagore Lodge & Kuthibari (Shilaidaha)",
        "nameBn": "Tagore Lodge & Kuthibari (Shilaidaha) (কুষ্টিয়া)",
        "category": "Historic Mosque",
        "desc": "Historic country residence where Nobel Laureate Rabindranath Tagore composed Gitanjali.",
        "location": "Old Town, Kushtia"
      },
      {
        "id": 3,
        "image": "images/districts/kushtia/hist-3.webp",
        "name": "Kushtia Colonial Court & Mint",
        "nameBn": "কুষ্টিয়া ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Kushtia district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Kushtia"
      },
      {
        "id": 4,
        "image": "images/districts/kushtia/hist-4.webp",
        "name": "Kushtia Archeological Mound",
        "nameBn": "কুষ্টিয়া প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Kushtia district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Kushtia"
      },
      {
        "id": 5,
        "image": "images/districts/kushtia/hist-5.webp",
        "name": "Kushtia Liberation War Memorial",
        "nameBn": "কুষ্টিয়া মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Kushtia district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Kushtia"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/kushtia/tour-1.webp",
        "name": "Hardinge Bridge & Lalon Shah Bridge",
        "nameBn": "Hardinge Bridge & Lalon Shah Bridge (কুষ্টিয়া)",
        "category": "Engineering Landmarks",
        "desc": "Side-by-side century-old steel railway bridge and modern road bridge spanning the Padma.",
        "location": "Kushtia Riverfront, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/kushtia/tour-2.webp",
        "name": "Ghashi Lake & Gorai River Banks",
        "nameBn": "Ghashi Lake & Gorai River Banks (কুষ্টিয়া)",
        "category": "Nature Walk",
        "desc": "Tranquil river plains celebrated for sunset walks and traditional Baul folk music.",
        "location": "Forest Range, Kushtia"
      },
      {
        "id": 3,
        "image": "images/districts/kushtia/tour-3.webp",
        "name": "Kushtia Cultural Heritage Museum",
        "nameBn": "কুষ্টিয়া লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Kushtia district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Kushtia"
      },
      {
        "id": 4,
        "image": "images/districts/kushtia/tour-4.webp",
        "name": "Kushtia Scenic Lake & Boating Resort",
        "nameBn": "কুষ্টিয়া মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Kushtia district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Kushtia"
      },
      {
        "id": 5,
        "image": "images/districts/kushtia/tour-5.webp",
        "name": "Kushtia Sunset Hilltop Viewpoint",
        "nameBn": "কুষ্টিয়া সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Kushtia district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Kushtia"
      }
    ]
  },
  {
    "id": 41,
    "slug": "magura",
    "en": "Magura",
    "bn": "মাগুরা",
    "div": "Khulna",
    "lat": 23.4432,
    "lng": 89.4337,
    "coordinates": "23.4432, 89.4337",
    "est": 1984,
    "area": "1,048.61 km²",
    "pop": "1.0M",
    "dist": "165 km",
    "route": "Via Padma Bridge expressway through Faridpur (approx. 3 hours by direct bus or car).",
    "tagline": "Magura (মাগুরা) is a picturesque and historically significant administrative district in Khulna Division, Bangladesh.",
    "heroImage": "images/districts/magura/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/magura/carousel-1.webp",
        "title": "Magura Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Khulna Division"
      },
      {
        "id": 2,
        "image": "images/districts/magura/carousel-2.webp",
        "title": "Historic Monuments of Magura",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/magura/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/magura/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/magura/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/magura/hist-1.webp",
        "name": "Sreepur Zamindar Bari",
        "nameBn": "Sreepur Zamindar Bari (মাগুরা)",
        "category": "Royal Heritage",
        "desc": "Historical estate of local feudal landlords featuring ancient gates and defensive trenches.",
        "location": "Magura Sadar, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/magura/hist-2.webp",
        "name": "Mohammadpur Ancient Mosque & Fort",
        "nameBn": "Mohammadpur Ancient Mosque & Fort (মাগুরা)",
        "category": "Historic Mosque",
        "desc": "Mohammadpur Ancient Mosque & Fort is one of the most prominent historical monuments in Magura district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Magura"
      },
      {
        "id": 3,
        "image": "images/districts/magura/hist-3.webp",
        "name": "Magura Colonial Court & Mint",
        "nameBn": "মাগুরা ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Magura district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Magura"
      },
      {
        "id": 4,
        "image": "images/districts/magura/hist-4.webp",
        "name": "Magura Archeological Mound",
        "nameBn": "মাগুরা প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Magura district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Magura"
      },
      {
        "id": 5,
        "image": "images/districts/magura/hist-5.webp",
        "name": "Magura Liberation War Memorial",
        "nameBn": "মাগুরা মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Magura district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Magura"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/magura/tour-1.webp",
        "name": "Siddheswari Kali Temple",
        "nameBn": "Siddheswari Kali Temple (মাগুরা)",
        "category": "Sacred Heritage",
        "desc": "Ancient pilgrimage temple situated in serene rural surroundings beside ancient trees.",
        "location": "Magura Riverfront, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/magura/tour-2.webp",
        "name": "Gorai River Sands",
        "nameBn": "Gorai River Sands (মাগুরা)",
        "category": "River Exploration",
        "desc": "Gorai River Sands stands as an iconic tourist highlight in Magura district. Nestled in natural surroundings under Khulna Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Magura"
      },
      {
        "id": 3,
        "image": "images/districts/magura/tour-3.webp",
        "name": "Magura Cultural Heritage Museum",
        "nameBn": "মাগুরা লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Magura district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Magura"
      },
      {
        "id": 4,
        "image": "images/districts/magura/tour-4.webp",
        "name": "Magura Scenic Lake & Boating Resort",
        "nameBn": "মাগুরা মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Magura district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Magura"
      },
      {
        "id": 5,
        "image": "images/districts/magura/tour-5.webp",
        "name": "Magura Sunset Hilltop Viewpoint",
        "nameBn": "মাগুরা সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Magura district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Magura"
      }
    ]
  },
  {
    "id": 42,
    "slug": "meherpur",
    "en": "Meherpur",
    "bn": "মেহেরপুর",
    "div": "Khulna",
    "lat": 23.794,
    "lng": 88.7071,
    "coordinates": "23.7940, 88.7071",
    "est": 1984,
    "area": "751.62 km²",
    "pop": "0.7M",
    "dist": "250 km",
    "route": "Via Padma Bridge through Kushtia or Chuadanga (approx. 5 - 5.5 hours by highway bus).",
    "tagline": "Meherpur (মেহেরপুর) is a picturesque and historically significant administrative district in Khulna Division, Bangladesh.",
    "heroImage": "images/districts/meherpur/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/meherpur/carousel-1.webp",
        "title": "Meherpur Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Khulna Division"
      },
      {
        "id": 2,
        "image": "images/districts/meherpur/carousel-2.webp",
        "title": "Historic Monuments of Meherpur",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/meherpur/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/meherpur/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/meherpur/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/meherpur/hist-1.webp",
        "name": "Mujibnagar National Memorial Complex",
        "nameBn": "Mujibnagar National Memorial Complex (মেহেরপুর)",
        "category": "Royal Heritage",
        "desc": "Sacred historical site where the first provisional government of Bangladesh was sworn in in 1971.",
        "location": "Meherpur Sadar, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/meherpur/hist-2.webp",
        "name": "Amjhupi Nilkuthi",
        "nameBn": "Amjhupi Nilkuthi (মেহেরপুর)",
        "category": "Historic Mosque",
        "desc": "Amjhupi Nilkuthi is one of the most prominent historical monuments in Meherpur district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Meherpur"
      },
      {
        "id": 3,
        "image": "images/districts/meherpur/hist-3.webp",
        "name": "Meherpur Colonial Court & Mint",
        "nameBn": "মেহেরপুর ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Meherpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Meherpur"
      },
      {
        "id": 4,
        "image": "images/districts/meherpur/hist-4.webp",
        "name": "Meherpur Archeological Mound",
        "nameBn": "মেহেরপুর প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Meherpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Meherpur"
      },
      {
        "id": 5,
        "image": "images/districts/meherpur/hist-5.webp",
        "name": "Meherpur Liberation War Memorial",
        "nameBn": "মেহেরপুর মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Meherpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Meherpur"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/meherpur/tour-1.webp",
        "name": "Bhabapara Heritage Church",
        "nameBn": "Bhabapara Heritage Church (মেহেরপুর)",
        "category": "Colonial Heritage",
        "desc": "Bhabapara Heritage Church stands as an iconic tourist highlight in Meherpur district. Nestled in natural surroundings under Khulna Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Meherpur Riverfront, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/meherpur/tour-2.webp",
        "name": "Bhairab Riverfront",
        "nameBn": "Bhairab Riverfront (মেহেরপুর)",
        "category": "Nature & Border",
        "desc": "Bhairab Riverfront stands as an iconic tourist highlight in Meherpur district. Nestled in natural surroundings under Khulna Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Meherpur"
      },
      {
        "id": 3,
        "image": "images/districts/meherpur/tour-3.webp",
        "name": "Meherpur Cultural Heritage Museum",
        "nameBn": "মেহেরপুর লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Meherpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Meherpur"
      },
      {
        "id": 4,
        "image": "images/districts/meherpur/tour-4.webp",
        "name": "Meherpur Scenic Lake & Boating Resort",
        "nameBn": "মেহেরপুর মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Meherpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Meherpur"
      },
      {
        "id": 5,
        "image": "images/districts/meherpur/tour-5.webp",
        "name": "Meherpur Sunset Hilltop Viewpoint",
        "nameBn": "মেহেরপুর সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Meherpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Meherpur"
      }
    ]
  },
  {
    "id": 43,
    "slug": "narail",
    "en": "Narail",
    "bn": "নড়াইল",
    "div": "Khulna",
    "lat": 23.1301,
    "lng": 89.5801,
    "coordinates": "23.1301, 89.5801",
    "est": 1984,
    "area": "990.23 km²",
    "pop": "0.8M",
    "dist": "170 km",
    "route": "Via Padma Bridge and Kalna (Madhumati) Bridge expressway (approx. 2.5 - 3 hours).",
    "tagline": "Narail (নড়াইল) is a picturesque and historically significant administrative district in Khulna Division, Bangladesh.",
    "heroImage": "images/districts/narail/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/narail/carousel-1.webp",
        "title": "Narail Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Khulna Division"
      },
      {
        "id": 2,
        "image": "images/districts/narail/carousel-2.webp",
        "title": "Historic Monuments of Narail",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/narail/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/narail/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/narail/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/narail/hist-1.webp",
        "name": "SM Sultan Memorial & Art Gallery",
        "nameBn": "SM Sultan Memorial & Art Gallery (নড়াইল)",
        "category": "Royal Heritage",
        "desc": "Riverside sanctuary, boathouse, and museum celebrating the legendary master artist SM Sultan.",
        "location": "Narail Sadar, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/narail/hist-2.webp",
        "name": "Victoria Collegiate School Historic Building",
        "nameBn": "Victoria Collegiate School Historic Building (নড়াইল)",
        "category": "Historic Mosque",
        "desc": "Victoria Collegiate School Historic Building is one of the most prominent historical monuments in Narail district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Narail"
      },
      {
        "id": 3,
        "image": "images/districts/narail/hist-3.webp",
        "name": "Narail Colonial Court & Mint",
        "nameBn": "নড়াইল ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Narail district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Narail"
      },
      {
        "id": 4,
        "image": "images/districts/narail/hist-4.webp",
        "name": "Narail Archeological Mound",
        "nameBn": "নড়াইল প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Narail district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Narail"
      },
      {
        "id": 5,
        "image": "images/districts/narail/hist-5.webp",
        "name": "Narail Liberation War Memorial",
        "nameBn": "নড়াইল মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Narail district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Narail"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/narail/tour-1.webp",
        "name": "Chitra River & Otter Fishing Hub",
        "nameBn": "Chitra River & Otter Fishing Hub (নড়াইল)",
        "category": "Unique Cultural Heritage",
        "desc": "Rare living tradition of fishermen working alongside trained otters to catch fish.",
        "location": "Narail Riverfront, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/narail/tour-2.webp",
        "name": "Madhumati Bridge Plaza",
        "nameBn": "Madhumati Bridge Plaza (নড়াইল)",
        "category": "Modern Landmark",
        "desc": "Madhumati Bridge Plaza stands as an iconic tourist highlight in Narail district. Nestled in natural surroundings under Khulna Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Narail"
      },
      {
        "id": 3,
        "image": "images/districts/narail/tour-3.webp",
        "name": "Narail Cultural Heritage Museum",
        "nameBn": "নড়াইল লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Narail district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Narail"
      },
      {
        "id": 4,
        "image": "images/districts/narail/tour-4.webp",
        "name": "Narail Scenic Lake & Boating Resort",
        "nameBn": "নড়াইল মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Narail district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Narail"
      },
      {
        "id": 5,
        "image": "images/districts/narail/tour-5.webp",
        "name": "Narail Sunset Hilltop Viewpoint",
        "nameBn": "নড়াইল সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Narail district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Narail"
      }
    ]
  },
  {
    "id": 44,
    "slug": "satkhira",
    "en": "Satkhira",
    "bn": "সাতক্ষীরা",
    "div": "Khulna",
    "lat": 22.5129,
    "lng": 89.1198,
    "coordinates": "22.5129, 89.1198",
    "est": 1984,
    "area": "3,817.29 km²",
    "pop": "2.1M",
    "dist": "265 km",
    "route": "Via Padma Bridge through Khulna (approx. 5 hours) or direct highway coaches.",
    "tagline": "Satkhira (সাতক্ষীরা) is a picturesque and historically significant administrative district in Khulna Division, Bangladesh.",
    "heroImage": "images/districts/satkhira/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/satkhira/carousel-1.webp",
        "title": "Satkhira Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Khulna Division"
      },
      {
        "id": 2,
        "image": "images/districts/satkhira/carousel-2.webp",
        "title": "Historic Monuments of Satkhira",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/satkhira/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/satkhira/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/satkhira/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/satkhira/hist-1.webp",
        "name": "Ishwaripur Chanda Bhairab & Hamamkhana",
        "nameBn": "Ishwaripur Chanda Bhairab & Hamamkhana (সাতক্ষীরা)",
        "category": "Royal Heritage",
        "desc": "Remnants of Raja Pratapaditya’s 16th-century fortress, baths, and historical temple.",
        "location": "Satkhira Sadar, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/satkhira/hist-2.webp",
        "name": "Five-Dome Mosque of Jessoreshwari",
        "nameBn": "Five-Dome Mosque of Jessoreshwari (সাতক্ষীরা)",
        "category": "Historic Mosque",
        "desc": "Five-Dome Mosque of Jessoreshwari is one of the most prominent historical monuments in Satkhira district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Satkhira"
      },
      {
        "id": 3,
        "image": "images/districts/satkhira/hist-3.webp",
        "name": "Satkhira Colonial Court & Mint",
        "nameBn": "সাতক্ষীরা ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Satkhira district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Satkhira"
      },
      {
        "id": 4,
        "image": "images/districts/satkhira/hist-4.webp",
        "name": "Satkhira Archeological Mound",
        "nameBn": "সাতক্ষীরা প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Satkhira district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Satkhira"
      },
      {
        "id": 5,
        "image": "images/districts/satkhira/hist-5.webp",
        "name": "Satkhira Liberation War Memorial",
        "nameBn": "সাতক্ষীরা মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Satkhira district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Satkhira"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/satkhira/tour-1.webp",
        "name": "Sundarbans Kolagachia & Burigoalini",
        "nameBn": "Sundarbans Kolagachia & Burigoalini (সাতক্ষীরা)",
        "category": "Mangrove Wilderness",
        "desc": "Premier ecotourism entry point into the mangrove forest with suspension bridges and watchtowers.",
        "location": "Satkhira Riverfront, Khulna"
      },
      {
        "id": 2,
        "image": "images/districts/satkhira/tour-2.webp",
        "name": "Mandarbari Coastal Sea Beach",
        "nameBn": "Mandarbari Coastal Sea Beach (সাতক্ষীরা)",
        "category": "Pristine Coast",
        "desc": "Mandarbari Coastal Sea Beach stands as an iconic tourist highlight in Satkhira district. Nestled in natural surroundings under Khulna Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Satkhira"
      },
      {
        "id": 3,
        "image": "images/districts/satkhira/tour-3.webp",
        "name": "Satkhira Cultural Heritage Museum",
        "nameBn": "সাতক্ষীরা লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Satkhira district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Satkhira"
      },
      {
        "id": 4,
        "image": "images/districts/satkhira/tour-4.webp",
        "name": "Satkhira Scenic Lake & Boating Resort",
        "nameBn": "সাতক্ষীরা মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Satkhira district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Satkhira"
      },
      {
        "id": 5,
        "image": "images/districts/satkhira/tour-5.webp",
        "name": "Satkhira Sunset Hilltop Viewpoint",
        "nameBn": "সাতক্ষীরা সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Satkhira district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Satkhira"
      }
    ]
  },
  {
    "id": 45,
    "slug": "bogura",
    "en": "Bogura",
    "bn": "বগুড়া",
    "div": "Rajshahi",
    "lat": 24.8245,
    "lng": 89.3788,
    "coordinates": "24.8245, 89.3788",
    "est": 1821,
    "area": "2,898.68 km²",
    "pop": "3.7M",
    "dist": "200 km",
    "route": "Via Jamuna Bridge and Dhaka-Bogura 4-lane Highway N5 (approx. 4.5 hours by bus/train).",
    "tagline": "Bogura (বগুড়া) is a picturesque and historically significant administrative district in Rajshahi Division, Bangladesh.",
    "heroImage": "images/districts/bogura/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/bogura/carousel-1.webp",
        "title": "Bogura Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rajshahi Division"
      },
      {
        "id": 2,
        "image": "images/districts/bogura/carousel-2.webp",
        "title": "Historic Monuments of Bogura",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/bogura/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/bogura/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/bogura/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/bogura/hist-1.webp",
        "name": "Mahasthangarh (Ancient Pundranagara)",
        "nameBn": "Mahasthangarh (Ancient Pundranagara) (বগুড়া)",
        "category": "Royal Heritage",
        "desc": "Oldest fortified urban archaeological city in Bangladesh, dating from 3rd century BCE.",
        "location": "Bogura Sadar, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/bogura/hist-2.webp",
        "name": "Gokul Medh (Behula’s Basor Ghar)",
        "nameBn": "Gokul Medh (Behula’s Basor Ghar) (বগুড়া)",
        "category": "Historic Mosque",
        "desc": "Terraced stupa structure linked to the legendary folklore of Behula and Lakhindar.",
        "location": "Old Town, Bogura"
      },
      {
        "id": 3,
        "image": "images/districts/bogura/hist-3.webp",
        "name": "Bogura Colonial Court & Mint",
        "nameBn": "বগুড়া ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Bogura district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Bogura"
      },
      {
        "id": 4,
        "image": "images/districts/bogura/hist-4.webp",
        "name": "Bogura Archeological Mound",
        "nameBn": "বগুড়া প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Bogura district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Bogura"
      },
      {
        "id": 5,
        "image": "images/districts/bogura/hist-5.webp",
        "name": "Bogura Liberation War Memorial",
        "nameBn": "বগুড়া মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Bogura district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Bogura"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/bogura/tour-1.webp",
        "name": "Vasu Vihara & Museum",
        "nameBn": "Vasu Vihara & Museum (বগুড়া)",
        "category": "Archaeology",
        "desc": "Exquisite excavated Buddhist monastery complex and collection of ancient terracotta plaques.",
        "location": "Bogura Riverfront, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/bogura/tour-2.webp",
        "name": "Bogura Sweet Culture",
        "nameBn": "Bogura Sweet Culture (বগুড়া)",
        "category": "Culinary Landmark",
        "desc": "World-famous destination for rich traditional Bogura Curd (Doi) served in clay pots.",
        "location": "Forest Range, Bogura"
      },
      {
        "id": 3,
        "image": "images/districts/bogura/tour-3.webp",
        "name": "Bogura Cultural Heritage Museum",
        "nameBn": "বগুড়া লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Bogura district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Bogura"
      },
      {
        "id": 4,
        "image": "images/districts/bogura/tour-4.webp",
        "name": "Bogura Scenic Lake & Boating Resort",
        "nameBn": "বগুড়া মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Bogura district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Bogura"
      },
      {
        "id": 5,
        "image": "images/districts/bogura/tour-5.webp",
        "name": "Bogura Sunset Hilltop Viewpoint",
        "nameBn": "বগুড়া সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Bogura district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Bogura"
      }
    ]
  },
  {
    "id": 46,
    "slug": "joypurhat",
    "en": "Joypurhat",
    "bn": "জয়পুরহাট",
    "div": "Rajshahi",
    "lat": 25.0927,
    "lng": 89.0829,
    "coordinates": "25.0927, 89.0829",
    "est": 1984,
    "area": "965.88 km²",
    "pop": "1.0M",
    "dist": "270 km",
    "route": "Via Jamuna Bridge through Bogura (approx. 6 hrs) or direct intercity trains from Kamalapur.",
    "tagline": "Joypurhat (জয়পুরহাট) is a picturesque and historically significant administrative district in Rajshahi Division, Bangladesh.",
    "heroImage": "images/districts/joypurhat/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/joypurhat/carousel-1.webp",
        "title": "Joypurhat Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rajshahi Division"
      },
      {
        "id": 2,
        "image": "images/districts/joypurhat/carousel-2.webp",
        "title": "Historic Monuments of Joypurhat",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/joypurhat/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/joypurhat/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/joypurhat/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/joypurhat/hist-1.webp",
        "name": "Lockma Rajbari",
        "nameBn": "Lockma Rajbari (জয়পুরহাট)",
        "category": "Royal Heritage",
        "desc": "Colonial estate ruins of local zamindars boasting intricate brick vaults and tunnels.",
        "location": "Joypurhat Sadar, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/joypurhat/hist-2.webp",
        "name": "Asranga Dighi",
        "nameBn": "Asranga Dighi (জয়পুরহাট)",
        "category": "Historic Mosque",
        "desc": "Asranga Dighi is one of the most prominent historical monuments in Joypurhat district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Joypurhat"
      },
      {
        "id": 3,
        "image": "images/districts/joypurhat/hist-3.webp",
        "name": "Joypurhat Colonial Court & Mint",
        "nameBn": "জয়পুরহাট ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Joypurhat district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Joypurhat"
      },
      {
        "id": 4,
        "image": "images/districts/joypurhat/hist-4.webp",
        "name": "Joypurhat Archeological Mound",
        "nameBn": "জয়পুরহাট প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Joypurhat district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Joypurhat"
      },
      {
        "id": 5,
        "image": "images/districts/joypurhat/hist-5.webp",
        "name": "Joypurhat Liberation War Memorial",
        "nameBn": "জয়পুরহাট মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Joypurhat district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Joypurhat"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/joypurhat/tour-1.webp",
        "name": "Hili Land Port Border Point",
        "nameBn": "Hili Land Port Border Point (জয়পুরহাট)",
        "category": "Border Frontier",
        "desc": "Hili Land Port Border Point stands as an iconic tourist highlight in Joypurhat district. Nestled in natural surroundings under Rajshahi Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Joypurhat Riverfront, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/joypurhat/tour-2.webp",
        "name": "Nandail Dighi",
        "nameBn": "Nandail Dighi (জয়পুরহাট)",
        "category": "Nature & Wildlife",
        "desc": "Expansive water body surrounded by green embankments that host winter migratory birds.",
        "location": "Forest Range, Joypurhat"
      },
      {
        "id": 3,
        "image": "images/districts/joypurhat/tour-3.webp",
        "name": "Joypurhat Cultural Heritage Museum",
        "nameBn": "জয়পুরহাট লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Joypurhat district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Joypurhat"
      },
      {
        "id": 4,
        "image": "images/districts/joypurhat/tour-4.webp",
        "name": "Joypurhat Scenic Lake & Boating Resort",
        "nameBn": "জয়পুরহাট মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Joypurhat district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Joypurhat"
      },
      {
        "id": 5,
        "image": "images/districts/joypurhat/tour-5.webp",
        "name": "Joypurhat Sunset Hilltop Viewpoint",
        "nameBn": "জয়পুরহাট সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Joypurhat district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Joypurhat"
      }
    ]
  },
  {
    "id": 47,
    "slug": "naogaon",
    "en": "Naogaon",
    "bn": "নওগাঁ",
    "div": "Rajshahi",
    "lat": 24.8996,
    "lng": 88.7516,
    "coordinates": "24.8996, 88.7516",
    "est": 1984,
    "area": "3,435.67 km²",
    "pop": "2.7M",
    "dist": "260 km",
    "route": "Via Jamuna Bridge highway or intercity trains stopping at Santahar junction (5-6 hrs).",
    "tagline": "Naogaon (নওগাঁ) is a picturesque and historically significant administrative district in Rajshahi Division, Bangladesh.",
    "heroImage": "images/districts/naogaon/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/naogaon/carousel-1.webp",
        "title": "Naogaon Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rajshahi Division"
      },
      {
        "id": 2,
        "image": "images/districts/naogaon/carousel-2.webp",
        "title": "Historic Monuments of Naogaon",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/naogaon/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/naogaon/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/naogaon/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/naogaon/hist-1.webp",
        "name": "Somapura Mahavihara (Paharpur)",
        "nameBn": "Somapura Mahavihara (Paharpur) (নওগাঁ)",
        "category": "Royal Heritage",
        "desc": "UNESCO World Heritage Site: 8th-century colossal Buddhist monastery with 177 monk cells.",
        "location": "Naogaon Sadar, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/naogaon/hist-2.webp",
        "name": "Kusumba Mosque",
        "nameBn": "Kusumba Mosque (নওগাঁ)",
        "category": "Historic Mosque",
        "desc": "Known as the \"Black Gem of Bengal\", 1558 stone-clad Sultanate architectural masterpiece.",
        "location": "Old Town, Naogaon"
      },
      {
        "id": 3,
        "image": "images/districts/naogaon/hist-3.webp",
        "name": "Naogaon Colonial Court & Mint",
        "nameBn": "নওগাঁ ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Naogaon district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Naogaon"
      },
      {
        "id": 4,
        "image": "images/districts/naogaon/hist-4.webp",
        "name": "Naogaon Archeological Mound",
        "nameBn": "নওগাঁ প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Naogaon district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Naogaon"
      },
      {
        "id": 5,
        "image": "images/districts/naogaon/hist-5.webp",
        "name": "Naogaon Liberation War Memorial",
        "nameBn": "নওগাঁ মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Naogaon district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Naogaon"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/naogaon/tour-1.webp",
        "name": "Dubalhati Rajbari",
        "nameBn": "Dubalhati Rajbari (নওগাঁ)",
        "category": "Royal Palace",
        "desc": "Extensive palatial mansion of regional monarchs featuring 300 rooms and grand courtyards.",
        "location": "Naogaon Riverfront, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/naogaon/tour-2.webp",
        "name": "Alta Dighi National Park",
        "nameBn": "Alta Dighi National Park (নওগাঁ)",
        "category": "Nature Reserve",
        "desc": "Alta Dighi National Park stands as an iconic tourist highlight in Naogaon district. Nestled in natural surroundings under Rajshahi Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Naogaon"
      },
      {
        "id": 3,
        "image": "images/districts/naogaon/tour-3.webp",
        "name": "Naogaon Cultural Heritage Museum",
        "nameBn": "নওগাঁ লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Naogaon district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Naogaon"
      },
      {
        "id": 4,
        "image": "images/districts/naogaon/tour-4.webp",
        "name": "Naogaon Scenic Lake & Boating Resort",
        "nameBn": "নওগাঁ মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Naogaon district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Naogaon"
      },
      {
        "id": 5,
        "image": "images/districts/naogaon/tour-5.webp",
        "name": "Naogaon Sunset Hilltop Viewpoint",
        "nameBn": "নওগাঁ সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Naogaon district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Naogaon"
      }
    ]
  },
  {
    "id": 48,
    "slug": "natore",
    "en": "Natore",
    "bn": "নাটোর",
    "div": "Rajshahi",
    "lat": 24.3803,
    "lng": 89.0868,
    "coordinates": "24.3803, 89.0868",
    "est": 1984,
    "area": "1,900.20 km²",
    "pop": "1.8M",
    "dist": "200 km",
    "route": "Via Jamuna Bridge and Sirajganj-Natore highway or direct intercity trains (approx. 4.5 hrs).",
    "tagline": "Natore (নাটোর) is a picturesque and historically significant administrative district in Rajshahi Division, Bangladesh.",
    "heroImage": "images/districts/natore/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/natore/carousel-1.webp",
        "title": "Natore Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rajshahi Division"
      },
      {
        "id": 2,
        "image": "images/districts/natore/carousel-2.webp",
        "title": "Historic Monuments of Natore",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/natore/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/natore/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/natore/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/natore/hist-1.webp",
        "name": "Uttara Gonobhaban (Dighapatia Palace)",
        "nameBn": "Uttara Gonobhaban (Dighapatia Palace) (নাটোর)",
        "category": "Royal Heritage",
        "desc": "Magnificent 18th-century Italianate royal palace, official northern residence of the President.",
        "location": "Natore Sadar, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/natore/hist-2.webp",
        "name": "Natore Rajbari (Rani Bhabani Palace)",
        "nameBn": "Natore Rajbari (Rani Bhabani Palace) (নাটোর)",
        "category": "Historic Mosque",
        "desc": "Natore Rajbari (Rani Bhabani Palace) is one of the most prominent historical monuments in Natore district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Natore"
      },
      {
        "id": 3,
        "image": "images/districts/natore/hist-3.webp",
        "name": "Natore Colonial Court & Mint",
        "nameBn": "নাটোর ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Natore district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Natore"
      },
      {
        "id": 4,
        "image": "images/districts/natore/hist-4.webp",
        "name": "Natore Archeological Mound",
        "nameBn": "নাটোর প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Natore district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Natore"
      },
      {
        "id": 5,
        "image": "images/districts/natore/hist-5.webp",
        "name": "Natore Liberation War Memorial",
        "nameBn": "নাটোর মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Natore district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Natore"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/natore/tour-1.webp",
        "name": "Chalan Beel Aquatic Expanse",
        "nameBn": "Chalan Beel Aquatic Expanse (নাটোর)",
        "category": "Wetland Eco-Wonder",
        "desc": "Largest inland wetland basin in Bangladesh, a paradise for boating and freshwater fish.",
        "location": "Natore Riverfront, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/natore/tour-2.webp",
        "name": "Kachagolla Sweet Heritage",
        "nameBn": "Kachagolla Sweet Heritage (নাটোর)",
        "category": "Culinary Delight",
        "desc": "Kachagolla Sweet Heritage stands as an iconic tourist highlight in Natore district. Nestled in natural surroundings under Rajshahi Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Natore"
      },
      {
        "id": 3,
        "image": "images/districts/natore/tour-3.webp",
        "name": "Natore Cultural Heritage Museum",
        "nameBn": "নাটোর লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Natore district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Natore"
      },
      {
        "id": 4,
        "image": "images/districts/natore/tour-4.webp",
        "name": "Natore Scenic Lake & Boating Resort",
        "nameBn": "নাটোর মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Natore district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Natore"
      },
      {
        "id": 5,
        "image": "images/districts/natore/tour-5.webp",
        "name": "Natore Sunset Hilltop Viewpoint",
        "nameBn": "নাটোর সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Natore district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Natore"
      }
    ]
  },
  {
    "id": 49,
    "slug": "chapainawabganj",
    "en": "Chapainawabganj",
    "bn": "চাঁপাইনবাবগঞ্জ",
    "div": "Rajshahi",
    "lat": 24.7156,
    "lng": 88.2641,
    "coordinates": "24.7156, 88.2641",
    "est": 1984,
    "area": "1,702.56 km²",
    "pop": "1.8M",
    "dist": "310 km",
    "route": "Via Jamuna Bridge through Rajshahi (approx. 6.5 hours by direct express buses or train).",
    "tagline": "Chapainawabganj (চাঁপাইনবাবগঞ্জ) is a picturesque and historically significant administrative district in Rajshahi Division, Bangladesh.",
    "heroImage": "images/districts/chapainawabganj/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/chapainawabganj/carousel-1.webp",
        "title": "Chapainawabganj Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rajshahi Division"
      },
      {
        "id": 2,
        "image": "images/districts/chapainawabganj/carousel-2.webp",
        "title": "Historic Monuments of Chapainawabganj",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/chapainawabganj/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/chapainawabganj/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/chapainawabganj/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/chapainawabganj/hist-1.webp",
        "name": "Choto Sona Mosque (Small Golden Mosque)",
        "nameBn": "Choto Sona Mosque (Small Golden Mosque) (চাঁপাইনবাবগঞ্জ)",
        "category": "Royal Heritage",
        "desc": "Choto Sona Mosque (Small Golden Mosque) is one of the most prominent historical monuments in Chapainawabganj district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Chapainawabganj Sadar, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/chapainawabganj/hist-2.webp",
        "name": "Darasbari Mosque & Madrasa",
        "nameBn": "Darasbari Mosque & Madrasa (চাঁপাইনবাবগঞ্জ)",
        "category": "Historic Mosque",
        "desc": "Darasbari Mosque & Madrasa is one of the most prominent historical monuments in Chapainawabganj district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Chapainawabganj"
      },
      {
        "id": 3,
        "image": "images/districts/chapainawabganj/hist-3.webp",
        "name": "Chapainawabganj Colonial Court & Mint",
        "nameBn": "চাঁপাইনবাবগঞ্জ ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Chapainawabganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Chapainawabganj"
      },
      {
        "id": 4,
        "image": "images/districts/chapainawabganj/hist-4.webp",
        "name": "Chapainawabganj Archeological Mound",
        "nameBn": "চাঁপাইনবাবগঞ্জ প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Chapainawabganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Chapainawabganj"
      },
      {
        "id": 5,
        "image": "images/districts/chapainawabganj/hist-5.webp",
        "name": "Chapainawabganj Liberation War Memorial",
        "nameBn": "চাঁপাইনবাবগঞ্জ মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Chapainawabganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Chapainawabganj"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/chapainawabganj/tour-1.webp",
        "name": "Mango Capital of Bangladesh",
        "nameBn": "Mango Capital of Bangladesh (চাঁপাইনবাবগঞ্জ)",
        "category": "Agri-Tourism",
        "desc": "Mango Capital of Bangladesh stands as an iconic tourist highlight in Chapainawabganj district. Nestled in natural surroundings under Rajshahi Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Chapainawabganj Riverfront, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/chapainawabganj/tour-2.webp",
        "name": "Mahananda River Promenade",
        "nameBn": "Mahananda River Promenade (চাঁপাইনবাবগঞ্জ)",
        "category": "Riverside Views",
        "desc": "Mahananda River Promenade stands as an iconic tourist highlight in Chapainawabganj district. Nestled in natural surroundings under Rajshahi Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Chapainawabganj"
      },
      {
        "id": 3,
        "image": "images/districts/chapainawabganj/tour-3.webp",
        "name": "Chapainawabganj Cultural Heritage Museum",
        "nameBn": "চাঁপাইনবাবগঞ্জ লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Chapainawabganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Chapainawabganj"
      },
      {
        "id": 4,
        "image": "images/districts/chapainawabganj/tour-4.webp",
        "name": "Chapainawabganj Scenic Lake & Boating Resort",
        "nameBn": "চাঁপাইনবাবগঞ্জ মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Chapainawabganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Chapainawabganj"
      },
      {
        "id": 5,
        "image": "images/districts/chapainawabganj/tour-5.webp",
        "name": "Chapainawabganj Sunset Hilltop Viewpoint",
        "nameBn": "চাঁপাইনবাবগঞ্জ সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Chapainawabganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Chapainawabganj"
      }
    ]
  },
  {
    "id": 50,
    "slug": "pabna",
    "en": "Pabna",
    "bn": "পাবনা",
    "div": "Rajshahi",
    "lat": 24.0532,
    "lng": 89.3853,
    "coordinates": "24.0532, 89.3853",
    "est": 1832,
    "area": "2,371.50 km²",
    "pop": "2.7M",
    "dist": "160 km",
    "route": "Via Jamuna Bridge or Paturia-Daulatdia ferry highway link (approx. 3.5 - 4 hours).",
    "tagline": "Pabna (পাবনা) is a picturesque and historically significant administrative district in Rajshahi Division, Bangladesh.",
    "heroImage": "images/districts/pabna/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/pabna/carousel-1.webp",
        "title": "Pabna Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rajshahi Division"
      },
      {
        "id": 2,
        "image": "images/districts/pabna/carousel-2.webp",
        "title": "Historic Monuments of Pabna",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/pabna/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/pabna/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/pabna/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/pabna/hist-1.webp",
        "name": "Tarash Rajbari",
        "nameBn": "Tarash Rajbari (পাবনা)",
        "category": "Royal Heritage",
        "desc": "Colonial estate in Pabna town showcasing neoclassical columns and inner courtyards.",
        "location": "Pabna Sadar, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/pabna/hist-2.webp",
        "name": "Anukulchandra Satsang Ashram (Himaitpur)",
        "nameBn": "Anukulchandra Satsang Ashram (Himaitpur) (পাবনা)",
        "category": "Historic Mosque",
        "desc": "Spiritual headquarters and birth memorial of prominent philosopher Thakur Anukulchandra.",
        "location": "Old Town, Pabna"
      },
      {
        "id": 3,
        "image": "images/districts/pabna/hist-3.webp",
        "name": "Pabna Colonial Court & Mint",
        "nameBn": "পাবনা ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Pabna district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Pabna"
      },
      {
        "id": 4,
        "image": "images/districts/pabna/hist-4.webp",
        "name": "Pabna Archeological Mound",
        "nameBn": "পাবনা প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Pabna district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Pabna"
      },
      {
        "id": 5,
        "image": "images/districts/pabna/hist-5.webp",
        "name": "Pabna Liberation War Memorial",
        "nameBn": "পাবনা মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Pabna district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Pabna"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/pabna/tour-1.webp",
        "name": "Hardinge Bridge & Paksey Resort",
        "nameBn": "Hardinge Bridge & Paksey Resort (পাবনা)",
        "category": "Historic Steel Bridge",
        "desc": "Hardinge Bridge & Paksey Resort stands as an iconic tourist highlight in Pabna district. Nestled in natural surroundings under Rajshahi Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Pabna Riverfront, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/pabna/tour-2.webp",
        "name": "Rupkatha Cinema & Town Heritage",
        "nameBn": "Rupkatha Cinema & Town Heritage (পাবনা)",
        "category": "Cultural Heritage",
        "desc": "One of the oldest cultural towns of northern Bengal celebrated for sweets and arts.",
        "location": "Forest Range, Pabna"
      },
      {
        "id": 3,
        "image": "images/districts/pabna/tour-3.webp",
        "name": "Pabna Cultural Heritage Museum",
        "nameBn": "পাবনা লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Pabna district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Pabna"
      },
      {
        "id": 4,
        "image": "images/districts/pabna/tour-4.webp",
        "name": "Pabna Scenic Lake & Boating Resort",
        "nameBn": "পাবনা মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Pabna district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Pabna"
      },
      {
        "id": 5,
        "image": "images/districts/pabna/tour-5.webp",
        "name": "Pabna Sunset Hilltop Viewpoint",
        "nameBn": "পাবনা সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Pabna district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Pabna"
      }
    ]
  },
  {
    "id": 51,
    "slug": "rajshahi",
    "en": "Rajshahi",
    "bn": "রাজশাহী",
    "div": "Rajshahi",
    "lat": 24.4658,
    "lng": 88.6514,
    "coordinates": "24.4658, 88.6514",
    "est": 1772,
    "area": "2,425.37 km²",
    "pop": "2.9M",
    "dist": "250 km",
    "route": "Via Jamuna Bridge 4-lane Highway N502 (approx. 5 hrs), Padma Express train (5.5 hrs), or 40-min flight.",
    "tagline": "Rajshahi (রাজশাহী) is a picturesque and historically significant administrative district in Rajshahi Division, Bangladesh.",
    "heroImage": "images/districts/rajshahi/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/rajshahi/carousel-1.webp",
        "title": "Rajshahi Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rajshahi Division"
      },
      {
        "id": 2,
        "image": "images/districts/rajshahi/carousel-2.webp",
        "title": "Historic Monuments of Rajshahi",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/rajshahi/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/rajshahi/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/rajshahi/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/rajshahi/hist-1.webp",
        "name": "Bagha Mosque",
        "nameBn": "Bagha Mosque (রাজশাহী)",
        "category": "Royal Heritage",
        "desc": "1523 Sultanate architectural wonder famed for exquisite terracotta carvings on burnt clay bricks.",
        "location": "Rajshahi Sadar, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/rajshahi/hist-2.webp",
        "name": "Varendra Research Museum",
        "nameBn": "Varendra Research Museum (রাজশাহী)",
        "category": "Historic Mosque",
        "desc": "Oldest museum in Bangladesh (est. 1910) housing ancient stone sculptures and epigraphs.",
        "location": "Old Town, Rajshahi"
      },
      {
        "id": 3,
        "image": "images/districts/rajshahi/hist-3.webp",
        "name": "Rajshahi Colonial Court & Mint",
        "nameBn": "রাজশাহী ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Rajshahi district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Rajshahi"
      },
      {
        "id": 4,
        "image": "images/districts/rajshahi/hist-4.webp",
        "name": "Rajshahi Archeological Mound",
        "nameBn": "রাজশাহী প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Rajshahi district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Rajshahi"
      },
      {
        "id": 5,
        "image": "images/districts/rajshahi/hist-5.webp",
        "name": "Rajshahi Liberation War Memorial",
        "nameBn": "রাজশাহী মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Rajshahi district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Rajshahi"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/rajshahi/tour-1.webp",
        "name": "Padma River Embankment (T-Groin)",
        "nameBn": "Padma River Embankment (T-Groin) (রাজশাহী)",
        "category": "Riverside Promenade",
        "desc": "Spectacular landscaped embankment for evening sunset strolls across the wide Padma.",
        "location": "Rajshahi Riverfront, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/rajshahi/tour-2.webp",
        "name": "Silk City Mills & Mango Gardens",
        "nameBn": "Silk City Mills & Mango Gardens (রাজশাহী)",
        "category": "Craft & Harvest",
        "desc": "Silk City Mills & Mango Gardens stands as an iconic tourist highlight in Rajshahi district. Nestled in natural surroundings under Rajshahi Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Rajshahi"
      },
      {
        "id": 3,
        "image": "images/districts/rajshahi/tour-3.webp",
        "name": "Rajshahi Cultural Heritage Museum",
        "nameBn": "রাজশাহী লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Rajshahi district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Rajshahi"
      },
      {
        "id": 4,
        "image": "images/districts/rajshahi/tour-4.webp",
        "name": "Rajshahi Scenic Lake & Boating Resort",
        "nameBn": "রাজশাহী মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Rajshahi district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Rajshahi"
      },
      {
        "id": 5,
        "image": "images/districts/rajshahi/tour-5.webp",
        "name": "Rajshahi Sunset Hilltop Viewpoint",
        "nameBn": "রাজশাহী সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Rajshahi district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Rajshahi"
      }
    ]
  },
  {
    "id": 52,
    "slug": "sirajganj",
    "en": "Sirajganj",
    "bn": "সিরাজগঞ্জ",
    "div": "Rajshahi",
    "lat": 24.3916,
    "lng": 89.5996,
    "coordinates": "24.3916, 89.5996",
    "est": 1984,
    "area": "2,497.92 km²",
    "pop": "3.3M",
    "dist": "135 km",
    "route": "Via Dhaka-Tangail Highway crossing Bangabandhu Jamuna Bridge (approx. 2.5 - 3 hours).",
    "tagline": "Sirajganj (সিরাজগঞ্জ) is a picturesque and historically significant administrative district in Rajshahi Division, Bangladesh.",
    "heroImage": "images/districts/sirajganj/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/sirajganj/carousel-1.webp",
        "title": "Sirajganj Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rajshahi Division"
      },
      {
        "id": 2,
        "image": "images/districts/sirajganj/carousel-2.webp",
        "title": "Historic Monuments of Sirajganj",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/sirajganj/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/sirajganj/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/sirajganj/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/sirajganj/hist-1.webp",
        "name": "Navaratna Temple (Hatikumrul)",
        "nameBn": "Navaratna Temple (Hatikumrul) (সিরাজগঞ্জ)",
        "category": "Royal Heritage",
        "desc": "Ancient nine-spired Hindu terracotta architectural monument dating from the 18th century.",
        "location": "Sirajganj Sadar, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/sirajganj/hist-2.webp",
        "name": "Rabindra Memorial Museum (Shahjadpur)",
        "nameBn": "Rabindra Memorial Museum (Shahjadpur) (সিরাজগঞ্জ)",
        "category": "Historic Mosque",
        "desc": "Country manor of Rabindranath Tagore where he wrote some of his most famous poems.",
        "location": "Old Town, Sirajganj"
      },
      {
        "id": 3,
        "image": "images/districts/sirajganj/hist-3.webp",
        "name": "Sirajganj Colonial Court & Mint",
        "nameBn": "সিরাজগঞ্জ ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Sirajganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Sirajganj"
      },
      {
        "id": 4,
        "image": "images/districts/sirajganj/hist-4.webp",
        "name": "Sirajganj Archeological Mound",
        "nameBn": "সিরাজগঞ্জ প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Sirajganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Sirajganj"
      },
      {
        "id": 5,
        "image": "images/districts/sirajganj/hist-5.webp",
        "name": "Sirajganj Liberation War Memorial",
        "nameBn": "সিরাজগঞ্জ মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Sirajganj district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Sirajganj"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/sirajganj/tour-1.webp",
        "name": "Bangabandhu Jamuna Bridge Plaza",
        "nameBn": "Bangabandhu Jamuna Bridge Plaza (সিরাজগঞ্জ)",
        "category": "Modern Engineering",
        "desc": "Bangabandhu Jamuna Bridge Plaza stands as an iconic tourist highlight in Sirajganj district. Nestled in natural surroundings under Rajshahi Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Sirajganj Riverfront, Rajshahi"
      },
      {
        "id": 2,
        "image": "images/districts/sirajganj/tour-2.webp",
        "name": "Jamuna Riverside Eco Park",
        "nameBn": "Jamuna Riverside Eco Park (সিরাজগঞ্জ)",
        "category": "Eco Leisure",
        "desc": "Riverside promenades with boat rides, sunset views, and local handloom cloth markets.",
        "location": "Forest Range, Sirajganj"
      },
      {
        "id": 3,
        "image": "images/districts/sirajganj/tour-3.webp",
        "name": "Sirajganj Cultural Heritage Museum",
        "nameBn": "সিরাজগঞ্জ লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Sirajganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Sirajganj"
      },
      {
        "id": 4,
        "image": "images/districts/sirajganj/tour-4.webp",
        "name": "Sirajganj Scenic Lake & Boating Resort",
        "nameBn": "সিরাজগঞ্জ মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Sirajganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Sirajganj"
      },
      {
        "id": 5,
        "image": "images/districts/sirajganj/tour-5.webp",
        "name": "Sirajganj Sunset Hilltop Viewpoint",
        "nameBn": "সিরাজগঞ্জ সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Sirajganj district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Sirajganj"
      }
    ]
  },
  {
    "id": 53,
    "slug": "dinajpur",
    "en": "Dinajpur",
    "bn": "দিনাজপুর",
    "div": "Rangpur",
    "lat": 25.6299,
    "lng": 88.7869,
    "coordinates": "25.6299, 88.7869",
    "est": 1786,
    "area": "3,444.30 km²",
    "pop": "3.2M",
    "dist": "340 km",
    "route": "Via Jamuna Bridge Highway N5 (approx. 7 hours) or Drutojan/Ekota Express trains (8 hrs).",
    "tagline": "Dinajpur (দিনাজপুর) is a picturesque and historically significant administrative district in Rangpur Division, Bangladesh.",
    "heroImage": "images/districts/dinajpur/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/dinajpur/carousel-1.webp",
        "title": "Dinajpur Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rangpur Division"
      },
      {
        "id": 2,
        "image": "images/districts/dinajpur/carousel-2.webp",
        "title": "Historic Monuments of Dinajpur",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/dinajpur/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/dinajpur/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/dinajpur/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/dinajpur/hist-1.webp",
        "name": "Kantajew Temple (Kantanagar)",
        "nameBn": "Kantajew Temple (Kantanagar) (দিনাজপুর)",
        "category": "Royal Heritage",
        "desc": "Sublime 1752 terracotta temple completely covered in thousands of intricate terracotta plaques.",
        "location": "Dinajpur Sadar, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/dinajpur/hist-2.webp",
        "name": "Nayabad Mosque",
        "nameBn": "Nayabad Mosque (দিনাজপুর)",
        "category": "Historic Mosque",
        "desc": "Historic 1793 mosque built by the Muslim artisans who constructed the Kantajew temple.",
        "location": "Old Town, Dinajpur"
      },
      {
        "id": 3,
        "image": "images/districts/dinajpur/hist-3.webp",
        "name": "Dinajpur Colonial Court & Mint",
        "nameBn": "দিনাজপুর ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Dinajpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Dinajpur"
      },
      {
        "id": 4,
        "image": "images/districts/dinajpur/hist-4.webp",
        "name": "Dinajpur Archeological Mound",
        "nameBn": "দিনাজপুর প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Dinajpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Dinajpur"
      },
      {
        "id": 5,
        "image": "images/districts/dinajpur/hist-5.webp",
        "name": "Dinajpur Liberation War Memorial",
        "nameBn": "দিনাজপুর মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Dinajpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Dinajpur"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/dinajpur/tour-1.webp",
        "name": "Ramsagar National Park",
        "nameBn": "Ramsagar National Park (দিনাজপুর)",
        "category": "Historic Lake & Forest",
        "desc": "Largest historic man-made water reservoir in Bangladesh surrounded by deer and tree gardens.",
        "location": "Dinajpur Riverfront, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/dinajpur/tour-2.webp",
        "name": "Dinajpur Rajbari",
        "nameBn": "Dinajpur Rajbari (দিনাজপুর)",
        "category": "Royal Ruins",
        "desc": "Sprawling royal estate featuring historic Durbar hall, temples, and ornamental gates.",
        "location": "Forest Range, Dinajpur"
      },
      {
        "id": 3,
        "image": "images/districts/dinajpur/tour-3.webp",
        "name": "Dinajpur Cultural Heritage Museum",
        "nameBn": "দিনাজপুর লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Dinajpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Dinajpur"
      },
      {
        "id": 4,
        "image": "images/districts/dinajpur/tour-4.webp",
        "name": "Dinajpur Scenic Lake & Boating Resort",
        "nameBn": "দিনাজপুর মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Dinajpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Dinajpur"
      },
      {
        "id": 5,
        "image": "images/districts/dinajpur/tour-5.webp",
        "name": "Dinajpur Sunset Hilltop Viewpoint",
        "nameBn": "দিনাজপুর সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Dinajpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Dinajpur"
      }
    ]
  },
  {
    "id": 54,
    "slug": "gaibandha",
    "en": "Gaibandha",
    "bn": "গাইবান্ধা",
    "div": "Rangpur",
    "lat": 25.2987,
    "lng": 89.5059,
    "coordinates": "25.2987, 89.5059",
    "est": 1984,
    "area": "2,179.27 km²",
    "pop": "2.5M",
    "dist": "280 km",
    "route": "Via Jamuna Bridge and Bogura highway or direct intercity trains (approx. 6 hours).",
    "tagline": "Gaibandha (গাইবান্ধা) is a picturesque and historically significant administrative district in Rangpur Division, Bangladesh.",
    "heroImage": "images/districts/gaibandha/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/gaibandha/carousel-1.webp",
        "title": "Gaibandha Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rangpur Division"
      },
      {
        "id": 2,
        "image": "images/districts/gaibandha/carousel-2.webp",
        "title": "Historic Monuments of Gaibandha",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/gaibandha/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/gaibandha/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/gaibandha/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/gaibandha/hist-1.webp",
        "name": "Bardhankuti Ancient Palace",
        "nameBn": "Bardhankuti Ancient Palace (গাইবান্ধা)",
        "category": "Royal Heritage",
        "desc": "Centuries-old ruins of the royal estate of Raja Gobinda dating back to the 16th century.",
        "location": "Gaibandha Sadar, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/gaibandha/hist-2.webp",
        "name": "Mirerbagh Shahi Mosque",
        "nameBn": "Mirerbagh Shahi Mosque (গাইবান্ধা)",
        "category": "Historic Mosque",
        "desc": "Mirerbagh Shahi Mosque is one of the most prominent historical monuments in Gaibandha district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Gaibandha"
      },
      {
        "id": 3,
        "image": "images/districts/gaibandha/hist-3.webp",
        "name": "Gaibandha Colonial Court & Mint",
        "nameBn": "গাইবান্ধা ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Gaibandha district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Gaibandha"
      },
      {
        "id": 4,
        "image": "images/districts/gaibandha/hist-4.webp",
        "name": "Gaibandha Archeological Mound",
        "nameBn": "গাইবান্ধা প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Gaibandha district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Gaibandha"
      },
      {
        "id": 5,
        "image": "images/districts/gaibandha/hist-5.webp",
        "name": "Gaibandha Liberation War Memorial",
        "nameBn": "গাইবান্ধা মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Gaibandha district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Gaibandha"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/gaibandha/tour-1.webp",
        "name": "Balasi Ghat on the Brahmaputra",
        "nameBn": "Balasi Ghat on the Brahmaputra (গাইবান্ধা)",
        "category": "River Life",
        "desc": "Historic river port with vast sandbars, ferry services, and fresh water river views.",
        "location": "Gaibandha Riverfront, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/gaibandha/tour-2.webp",
        "name": "Gai Bandha Eco Park",
        "nameBn": "Gai Bandha Eco Park (গাইবান্ধা)",
        "category": "Nature Leisure",
        "desc": "Gai Bandha Eco Park stands as an iconic tourist highlight in Gaibandha district. Nestled in natural surroundings under Rangpur Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Gaibandha"
      },
      {
        "id": 3,
        "image": "images/districts/gaibandha/tour-3.webp",
        "name": "Gaibandha Cultural Heritage Museum",
        "nameBn": "গাইবান্ধা লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Gaibandha district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Gaibandha"
      },
      {
        "id": 4,
        "image": "images/districts/gaibandha/tour-4.webp",
        "name": "Gaibandha Scenic Lake & Boating Resort",
        "nameBn": "গাইবান্ধা মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Gaibandha district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Gaibandha"
      },
      {
        "id": 5,
        "image": "images/districts/gaibandha/tour-5.webp",
        "name": "Gaibandha Sunset Hilltop Viewpoint",
        "nameBn": "গাইবান্ধা সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Gaibandha district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Gaibandha"
      }
    ]
  },
  {
    "id": 55,
    "slug": "kurigram",
    "en": "Kurigram",
    "bn": "কুড়িগ্রাম",
    "div": "Rangpur",
    "lat": 25.7907,
    "lng": 89.6953,
    "coordinates": "25.7907, 89.6953",
    "est": 1984,
    "area": "2,245.04 km²",
    "pop": "2.3M",
    "dist": "350 km",
    "route": "Via Jamuna Bridge and Rangpur highway or Kurigram Express direct intercity train (8-9 hrs).",
    "tagline": "Kurigram (কুড়িগ্রাম) is a picturesque and historically significant administrative district in Rangpur Division, Bangladesh.",
    "heroImage": "images/districts/kurigram/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/kurigram/carousel-1.webp",
        "title": "Kurigram Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rangpur Division"
      },
      {
        "id": 2,
        "image": "images/districts/kurigram/carousel-2.webp",
        "title": "Historic Monuments of Kurigram",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/kurigram/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/kurigram/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/kurigram/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/kurigram/hist-1.webp",
        "name": "Shonahat Historic Railway Bridge",
        "nameBn": "Shonahat Historic Railway Bridge (কুড়িগ্রাম)",
        "category": "Royal Heritage",
        "desc": "British-era 1887 steel bridge across the Dudhkumar River with remarkable engineering.",
        "location": "Kurigram Sadar, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/kurigram/hist-2.webp",
        "name": "Chandamari Mosque",
        "nameBn": "Chandamari Mosque (কুড়িগ্রাম)",
        "category": "Historic Mosque",
        "desc": "Chandamari Mosque is one of the most prominent historical monuments in Kurigram district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Kurigram"
      },
      {
        "id": 3,
        "image": "images/districts/kurigram/hist-3.webp",
        "name": "Kurigram Colonial Court & Mint",
        "nameBn": "কুড়িগ্রাম ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Kurigram district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Kurigram"
      },
      {
        "id": 4,
        "image": "images/districts/kurigram/hist-4.webp",
        "name": "Kurigram Archeological Mound",
        "nameBn": "কুড়িগ্রাম প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Kurigram district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Kurigram"
      },
      {
        "id": 5,
        "image": "images/districts/kurigram/hist-5.webp",
        "name": "Kurigram Liberation War Memorial",
        "nameBn": "কুড়িগ্রাম মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Kurigram district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Kurigram"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/kurigram/tour-1.webp",
        "name": "Chilmari River Port on Brahmaputra",
        "nameBn": "Chilmari River Port on Brahmaputra (কুড়িগ্রাম)",
        "category": "Historic River Port",
        "desc": "Legendary river port celebrated in Abbasuddin’s timeless folk song \"Oki Gariyal Bhai\".",
        "location": "Kurigram Riverfront, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/kurigram/tour-2.webp",
        "name": "Dharla River Promenade",
        "nameBn": "Dharla River Promenade (কুড়িগ্রাম)",
        "category": "Riverside Vistas",
        "desc": "Dharla River Promenade stands as an iconic tourist highlight in Kurigram district. Nestled in natural surroundings under Rangpur Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Kurigram"
      },
      {
        "id": 3,
        "image": "images/districts/kurigram/tour-3.webp",
        "name": "Kurigram Cultural Heritage Museum",
        "nameBn": "কুড়িগ্রাম লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Kurigram district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Kurigram"
      },
      {
        "id": 4,
        "image": "images/districts/kurigram/tour-4.webp",
        "name": "Kurigram Scenic Lake & Boating Resort",
        "nameBn": "কুড়িগ্রাম মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Kurigram district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Kurigram"
      },
      {
        "id": 5,
        "image": "images/districts/kurigram/tour-5.webp",
        "name": "Kurigram Sunset Hilltop Viewpoint",
        "nameBn": "কুড়িগ্রাম সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Kurigram district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Kurigram"
      }
    ]
  },
  {
    "id": 56,
    "slug": "lalmonirhat",
    "en": "Lalmonirhat",
    "bn": "লালমনিরহাট",
    "div": "Rangpur",
    "lat": 26.0574,
    "lng": 89.2409,
    "coordinates": "26.0574, 89.2409",
    "est": 1984,
    "area": "1,241.46 km²",
    "pop": "1.4M",
    "dist": "360 km",
    "route": "Via Jamuna Bridge through Rangpur or Lalmoni Express direct intercity train (approx. 8 hrs).",
    "tagline": "Lalmonirhat (লালমনিরহাট) is a picturesque and historically significant administrative district in Rangpur Division, Bangladesh.",
    "heroImage": "images/districts/lalmonirhat/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/lalmonirhat/carousel-1.webp",
        "title": "Lalmonirhat Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rangpur Division"
      },
      {
        "id": 2,
        "image": "images/districts/lalmonirhat/carousel-2.webp",
        "title": "Historic Monuments of Lalmonirhat",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/lalmonirhat/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/lalmonirhat/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/lalmonirhat/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/lalmonirhat/hist-1.webp",
        "name": "Harano Masjid (Lost Mosque of 69 AH)",
        "nameBn": "Harano Masjid (Lost Mosque of 69 AH) (লালমনিরহাট)",
        "category": "Royal Heritage",
        "desc": "Ancient subterranean mosque discovered in 1986, indicating early Islamic arrival in Bengal.",
        "location": "Lalmonirhat Sadar, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/lalmonirhat/hist-2.webp",
        "name": "Mogholhat Historic Border Railway",
        "nameBn": "Mogholhat Historic Border Railway (লালমনিরহাট)",
        "category": "Historic Mosque",
        "desc": "Mogholhat Historic Border Railway is one of the most prominent historical monuments in Lalmonirhat district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Lalmonirhat"
      },
      {
        "id": 3,
        "image": "images/districts/lalmonirhat/hist-3.webp",
        "name": "Lalmonirhat Colonial Court & Mint",
        "nameBn": "লালমনিরহাট ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Lalmonirhat district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Lalmonirhat"
      },
      {
        "id": 4,
        "image": "images/districts/lalmonirhat/hist-4.webp",
        "name": "Lalmonirhat Archeological Mound",
        "nameBn": "লালমনিরহাট প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Lalmonirhat district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Lalmonirhat"
      },
      {
        "id": 5,
        "image": "images/districts/lalmonirhat/hist-5.webp",
        "name": "Lalmonirhat Liberation War Memorial",
        "nameBn": "লালমনিরহাট মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Lalmonirhat district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Lalmonirhat"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/lalmonirhat/tour-1.webp",
        "name": "Tin Bigha Corridor & Dahagram",
        "nameBn": "Tin Bigha Corridor & Dahagram (লালমনিরহাট)",
        "category": "Sovereign Frontier",
        "desc": "Historic enclave territory connected by the Tin Bigha corridor near the northern border.",
        "location": "Lalmonirhat Riverfront, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/lalmonirhat/tour-2.webp",
        "name": "Teesta River Sandbanks",
        "nameBn": "Teesta River Sandbanks (লালমনিরহাট)",
        "category": "Nature & River",
        "desc": "Sweeping seasonal sand islands in the Teesta River perfect for quiet exploration.",
        "location": "Forest Range, Lalmonirhat"
      },
      {
        "id": 3,
        "image": "images/districts/lalmonirhat/tour-3.webp",
        "name": "Lalmonirhat Cultural Heritage Museum",
        "nameBn": "লালমনিরহাট লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Lalmonirhat district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Lalmonirhat"
      },
      {
        "id": 4,
        "image": "images/districts/lalmonirhat/tour-4.webp",
        "name": "Lalmonirhat Scenic Lake & Boating Resort",
        "nameBn": "লালমনিরহাট মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Lalmonirhat district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Lalmonirhat"
      },
      {
        "id": 5,
        "image": "images/districts/lalmonirhat/tour-5.webp",
        "name": "Lalmonirhat Sunset Hilltop Viewpoint",
        "nameBn": "লালমনিরহাট সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Lalmonirhat district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Lalmonirhat"
      }
    ]
  },
  {
    "id": 57,
    "slug": "nilphamari",
    "en": "Nilphamari",
    "bn": "নীলফামারী",
    "div": "Rangpur",
    "lat": 26.0247,
    "lng": 88.9295,
    "coordinates": "26.0247, 88.9295",
    "est": 1984,
    "area": "1,580.85 km²",
    "pop": "1.9M",
    "dist": "370 km",
    "route": "Via Jamuna Bridge through Rangpur, or direct Nilsagar Express train from Dhaka (approx. 8 hrs).",
    "tagline": "Nilphamari (নীলফামারী) is a picturesque and historically significant administrative district in Rangpur Division, Bangladesh.",
    "heroImage": "images/districts/nilphamari/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/nilphamari/carousel-1.webp",
        "title": "Nilphamari Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rangpur Division"
      },
      {
        "id": 2,
        "image": "images/districts/nilphamari/carousel-2.webp",
        "title": "Historic Monuments of Nilphamari",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/nilphamari/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/nilphamari/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/nilphamari/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/nilphamari/hist-1.webp",
        "name": "Chini Mosque (Saidpur Porcelain Mosque)",
        "nameBn": "Chini Mosque (Saidpur Porcelain Mosque) (নীলফামারী)",
        "category": "Royal Heritage",
        "desc": "Stunning 1863 mosque encrusted with thousands of imported porcelain china pieces and marbles.",
        "location": "Nilphamari Sadar, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/nilphamari/hist-2.webp",
        "name": "Dharmapal Garh",
        "nameBn": "Dharmapal Garh (নীলফামারী)",
        "category": "Historic Mosque",
        "desc": "Excavated ancient capital site and fortifications associated with King Dharmapala.",
        "location": "Old Town, Nilphamari"
      },
      {
        "id": 3,
        "image": "images/districts/nilphamari/hist-3.webp",
        "name": "Nilphamari Colonial Court & Mint",
        "nameBn": "নীলফামারী ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Nilphamari district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Nilphamari"
      },
      {
        "id": 4,
        "image": "images/districts/nilphamari/hist-4.webp",
        "name": "Nilphamari Archeological Mound",
        "nameBn": "নীলফামারী প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Nilphamari district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Nilphamari"
      },
      {
        "id": 5,
        "image": "images/districts/nilphamari/hist-5.webp",
        "name": "Nilphamari Liberation War Memorial",
        "nameBn": "নীলফামারী মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Nilphamari district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Nilphamari"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/nilphamari/tour-1.webp",
        "name": "Teesta Barrage (Dalia)",
        "nameBn": "Teesta Barrage (Dalia) (নীলফামারী)",
        "category": "Engineering Wonder",
        "desc": "Largest modern irrigation barrage in Bangladesh spanning the mighty Teesta River.",
        "location": "Nilphamari Riverfront, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/nilphamari/tour-2.webp",
        "name": "Nilsagar Historic Dighi",
        "nameBn": "Nilsagar Historic Dighi (নীলফামারী)",
        "category": "Eco Reservoir",
        "desc": "Sprawling ancient water reservoir renowned for hosting thousands of migratory winter birds.",
        "location": "Forest Range, Nilphamari"
      },
      {
        "id": 3,
        "image": "images/districts/nilphamari/tour-3.webp",
        "name": "Nilphamari Cultural Heritage Museum",
        "nameBn": "নীলফামারী লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Nilphamari district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Nilphamari"
      },
      {
        "id": 4,
        "image": "images/districts/nilphamari/tour-4.webp",
        "name": "Nilphamari Scenic Lake & Boating Resort",
        "nameBn": "নীলফামারী মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Nilphamari district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Nilphamari"
      },
      {
        "id": 5,
        "image": "images/districts/nilphamari/tour-5.webp",
        "name": "Nilphamari Sunset Hilltop Viewpoint",
        "nameBn": "নীলফামারী সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Nilphamari district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Nilphamari"
      }
    ]
  },
  {
    "id": 58,
    "slug": "panchagarh",
    "en": "Panchagarh",
    "bn": "পঞ্চগড়",
    "div": "Rangpur",
    "lat": 26.2851,
    "lng": 88.5755,
    "coordinates": "26.2851, 88.5755",
    "est": 1984,
    "area": "1,404.63 km²",
    "pop": "1.1M",
    "dist": "440 km",
    "route": "Via Panchagarh Express direct intercity train (approx. 9.5 hrs) or highway express coaches.",
    "tagline": "Panchagarh (পঞ্চগড়) is a picturesque and historically significant administrative district in Rangpur Division, Bangladesh.",
    "heroImage": "images/districts/panchagarh/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/panchagarh/carousel-1.webp",
        "title": "Panchagarh Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rangpur Division"
      },
      {
        "id": 2,
        "image": "images/districts/panchagarh/carousel-2.webp",
        "title": "Historic Monuments of Panchagarh",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/panchagarh/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/panchagarh/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/panchagarh/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/panchagarh/hist-1.webp",
        "name": "Mirzapur Shahi Mosque",
        "nameBn": "Mirzapur Shahi Mosque (পঞ্চগড়)",
        "category": "Royal Heritage",
        "desc": "Historic Mughal mosque built in 1656 with decorative minarets and terracotta artwork.",
        "location": "Panchagarh Sadar, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/panchagarh/hist-2.webp",
        "name": "Bhitargarh Ancient Fortified City",
        "nameBn": "Bhitargarh Ancient Fortified City (পঞ্চগড়)",
        "category": "Historic Mosque",
        "desc": "Largest ancient fortified urban site in Bangladesh, spanning over 25 square kilometers.",
        "location": "Old Town, Panchagarh"
      },
      {
        "id": 3,
        "image": "images/districts/panchagarh/hist-3.webp",
        "name": "Panchagarh Colonial Court & Mint",
        "nameBn": "পঞ্চগড় ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Panchagarh district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Panchagarh"
      },
      {
        "id": 4,
        "image": "images/districts/panchagarh/hist-4.webp",
        "name": "Panchagarh Archeological Mound",
        "nameBn": "পঞ্চগড় প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Panchagarh district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Panchagarh"
      },
      {
        "id": 5,
        "image": "images/districts/panchagarh/hist-5.webp",
        "name": "Panchagarh Liberation War Memorial",
        "nameBn": "পঞ্চগড় মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Panchagarh district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Panchagarh"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/panchagarh/tour-1.webp",
        "name": "Tetulia & Kanchenjunga Peak View",
        "nameBn": "Tetulia & Kanchenjunga Peak View (পঞ্চগড়)",
        "category": "Himalayan Mountain View",
        "desc": "Breathtaking viewpoint where snow-capped Himalayan peaks of Kanchenjunga are visible in autumn.",
        "location": "Panchagarh Riverfront, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/panchagarh/tour-2.webp",
        "name": "Banglabandha Zero Point & Plains Tea",
        "nameBn": "Banglabandha Zero Point & Plains Tea (পঞ্চগড়)",
        "category": "Border & Tea Estates",
        "desc": "Banglabandha Zero Point & Plains Tea stands as an iconic tourist highlight in Panchagarh district. Nestled in natural surroundings under Rangpur Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Panchagarh"
      },
      {
        "id": 3,
        "image": "images/districts/panchagarh/tour-3.webp",
        "name": "Panchagarh Cultural Heritage Museum",
        "nameBn": "পঞ্চগড় লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Panchagarh district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Panchagarh"
      },
      {
        "id": 4,
        "image": "images/districts/panchagarh/tour-4.webp",
        "name": "Panchagarh Scenic Lake & Boating Resort",
        "nameBn": "পঞ্চগড় মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Panchagarh district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Panchagarh"
      },
      {
        "id": 5,
        "image": "images/districts/panchagarh/tour-5.webp",
        "name": "Panchagarh Sunset Hilltop Viewpoint",
        "nameBn": "পঞ্চগড় সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Panchagarh district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Panchagarh"
      }
    ]
  },
  {
    "id": 59,
    "slug": "rangpur",
    "en": "Rangpur",
    "bn": "রংপুর",
    "div": "Rangpur",
    "lat": 25.6497,
    "lng": 89.2368,
    "coordinates": "25.6497, 89.2368",
    "est": 1772,
    "area": "2,370.45 km²",
    "pop": "3.1M",
    "dist": "300 km",
    "route": "Via Jamuna Bridge 4-lane Highway N5 (approx. 6 hrs), Rangpur Express train, or 45-min flight to Saidpur.",
    "tagline": "Rangpur (রংপুর) is a picturesque and historically significant administrative district in Rangpur Division, Bangladesh.",
    "heroImage": "images/districts/rangpur/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/rangpur/carousel-1.webp",
        "title": "Rangpur Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rangpur Division"
      },
      {
        "id": 2,
        "image": "images/districts/rangpur/carousel-2.webp",
        "title": "Historic Monuments of Rangpur",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/rangpur/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/rangpur/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/rangpur/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/rangpur/hist-1.webp",
        "name": "Tajhat Palace",
        "nameBn": "Tajhat Palace (রংপুর)",
        "category": "Royal Heritage",
        "desc": "Spectacular early 20th-century neoclassical royal palace now housing a magnificent antiquities museum.",
        "location": "Rangpur Sadar, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/rangpur/hist-2.webp",
        "name": "Carmichael College Historic Campus",
        "nameBn": "Carmichael College Historic Campus (রংপুর)",
        "category": "Historic Mosque",
        "desc": "Architectural landmark built in 1916 blending Indo-Saracenic and colonial architecture.",
        "location": "Old Town, Rangpur"
      },
      {
        "id": 3,
        "image": "images/districts/rangpur/hist-3.webp",
        "name": "Rangpur Colonial Court & Mint",
        "nameBn": "রংপুর ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Rangpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Rangpur"
      },
      {
        "id": 4,
        "image": "images/districts/rangpur/hist-4.webp",
        "name": "Rangpur Archeological Mound",
        "nameBn": "রংপুর প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Rangpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Rangpur"
      },
      {
        "id": 5,
        "image": "images/districts/rangpur/hist-5.webp",
        "name": "Rangpur Liberation War Memorial",
        "nameBn": "রংপুর মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Rangpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Rangpur"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/rangpur/tour-1.webp",
        "name": "Chikli Beel Water Leisure",
        "nameBn": "Chikli Beel Water Leisure (রংপুর)",
        "category": "Urban Water Park",
        "desc": "Vibrant city lake featuring speedboats, floating walkways, and illuminated gardens.",
        "location": "Rangpur Riverfront, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/rangpur/tour-2.webp",
        "name": "Vinnya Jagat Eco Amusement Park",
        "nameBn": "Vinnya Jagat Eco Amusement Park (রংপুর)",
        "category": "Family Theme Park",
        "desc": "Expansive countryside amusement and eco resort with landscaped gardens and rides.",
        "location": "Forest Range, Rangpur"
      },
      {
        "id": 3,
        "image": "images/districts/rangpur/tour-3.webp",
        "name": "Rangpur Cultural Heritage Museum",
        "nameBn": "রংপুর লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Rangpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Rangpur"
      },
      {
        "id": 4,
        "image": "images/districts/rangpur/tour-4.webp",
        "name": "Rangpur Scenic Lake & Boating Resort",
        "nameBn": "রংপুর মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Rangpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Rangpur"
      },
      {
        "id": 5,
        "image": "images/districts/rangpur/tour-5.webp",
        "name": "Rangpur Sunset Hilltop Viewpoint",
        "nameBn": "রংপুর সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Rangpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Rangpur"
      }
    ]
  },
  {
    "id": 60,
    "slug": "thakurgaon",
    "en": "Thakurgaon",
    "bn": "ঠাকুরগাঁও",
    "div": "Rangpur",
    "lat": 25.9906,
    "lng": 88.3456,
    "coordinates": "25.9906, 88.3456",
    "est": 1984,
    "area": "1,809.52 km²",
    "pop": "1.5M",
    "dist": "400 km",
    "route": "Via Jamuna Bridge through Dinajpur or direct intercity trains from Kamalapur (approx. 9 hrs).",
    "tagline": "Thakurgaon (ঠাকুরগাঁও) is a picturesque and historically significant administrative district in Rangpur Division, Bangladesh.",
    "heroImage": "images/districts/thakurgaon/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/thakurgaon/carousel-1.webp",
        "title": "Thakurgaon Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Rangpur Division"
      },
      {
        "id": 2,
        "image": "images/districts/thakurgaon/carousel-2.webp",
        "title": "Historic Monuments of Thakurgaon",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/thakurgaon/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/thakurgaon/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/thakurgaon/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/thakurgaon/hist-1.webp",
        "name": "Jamalpur Shahi Mosque",
        "nameBn": "Jamalpur Shahi Mosque (ঠাকুরগাঁও)",
        "category": "Royal Heritage",
        "desc": "Colonial Mughal-era mosque known for three large ribbed domes and elevated terrace.",
        "location": "Thakurgaon Sadar, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/thakurgaon/hist-2.webp",
        "name": "Ranishankail King’s Palace",
        "nameBn": "Ranishankail King’s Palace (ঠাকুরগাঁও)",
        "category": "Historic Mosque",
        "desc": "Ranishankail King’s Palace is one of the most prominent historical monuments in Thakurgaon district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Thakurgaon"
      },
      {
        "id": 3,
        "image": "images/districts/thakurgaon/hist-3.webp",
        "name": "Thakurgaon Colonial Court & Mint",
        "nameBn": "ঠাকুরগাঁও ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Thakurgaon district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Thakurgaon"
      },
      {
        "id": 4,
        "image": "images/districts/thakurgaon/hist-4.webp",
        "name": "Thakurgaon Archeological Mound",
        "nameBn": "ঠাকুরগাঁও প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Thakurgaon district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Thakurgaon"
      },
      {
        "id": 5,
        "image": "images/districts/thakurgaon/hist-5.webp",
        "name": "Thakurgaon Liberation War Memorial",
        "nameBn": "ঠাকুরগাঁও মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Thakurgaon district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Thakurgaon"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/thakurgaon/tour-1.webp",
        "name": "Baliadangi 200-Year Surya Puri Mango Tree",
        "nameBn": "Baliadangi 200-Year Surya Puri Mango Tree (ঠাকুরগাঁও)",
        "category": "Natural Wonder",
        "desc": "Ancient living mango tree spanning more than 2 bighas with dozens of rooted branches.",
        "location": "Thakurgaon Riverfront, Rangpur"
      },
      {
        "id": 2,
        "image": "images/districts/thakurgaon/tour-2.webp",
        "name": "Fun City Eco Park",
        "nameBn": "Fun City Eco Park (ঠাকুরগাঁও)",
        "category": "Eco Tourism",
        "desc": "Fun City Eco Park stands as an iconic tourist highlight in Thakurgaon district. Nestled in natural surroundings under Rangpur Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Thakurgaon"
      },
      {
        "id": 3,
        "image": "images/districts/thakurgaon/tour-3.webp",
        "name": "Thakurgaon Cultural Heritage Museum",
        "nameBn": "ঠাকুরগাঁও লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Thakurgaon district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Thakurgaon"
      },
      {
        "id": 4,
        "image": "images/districts/thakurgaon/tour-4.webp",
        "name": "Thakurgaon Scenic Lake & Boating Resort",
        "nameBn": "ঠাকুরগাঁও মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Thakurgaon district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Thakurgaon"
      },
      {
        "id": 5,
        "image": "images/districts/thakurgaon/tour-5.webp",
        "name": "Thakurgaon Sunset Hilltop Viewpoint",
        "nameBn": "ঠাকুরগাঁও সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Thakurgaon district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Thakurgaon"
      }
    ]
  },
  {
    "id": 61,
    "slug": "jamalpur",
    "en": "Jamalpur",
    "bn": "জামালপুর",
    "div": "Mymensingh",
    "lat": 24.9732,
    "lng": 89.8463,
    "coordinates": "24.9732, 89.8463",
    "est": 1978,
    "area": "2,031.98 km²",
    "pop": "2.5M",
    "dist": "145 km",
    "route": "Via Dhaka-Tangail-Jamalpur Highway or Brahmaputra/Jamuna Express train from Dhaka (3.5 - 4 hrs).",
    "tagline": "Jamalpur (জামালপুর) is a picturesque and historically significant administrative district in Mymensingh Division, Bangladesh.",
    "heroImage": "images/districts/jamalpur/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/jamalpur/carousel-1.webp",
        "title": "Jamalpur Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Mymensingh Division"
      },
      {
        "id": 2,
        "image": "images/districts/jamalpur/carousel-2.webp",
        "title": "Historic Monuments of Jamalpur",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/jamalpur/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/jamalpur/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/jamalpur/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/jamalpur/hist-1.webp",
        "name": "Gandhi Ashram (Jigatala)",
        "nameBn": "Gandhi Ashram (Jigatala) (জামালপুর)",
        "category": "Royal Heritage",
        "desc": "Historic socio-political retreat established during the non-cooperation and anti-British movement.",
        "location": "Jamalpur Sadar, Mymensingh"
      },
      {
        "id": 2,
        "image": "images/districts/jamalpur/hist-2.webp",
        "name": "Lojpoti Zamindar Palace",
        "nameBn": "Lojpoti Zamindar Palace (জামালপুর)",
        "category": "Historic Mosque",
        "desc": "Lojpoti Zamindar Palace is one of the most prominent historical monuments in Jamalpur district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Jamalpur"
      },
      {
        "id": 3,
        "image": "images/districts/jamalpur/hist-3.webp",
        "name": "Jamalpur Colonial Court & Mint",
        "nameBn": "জামালপুর ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Jamalpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Jamalpur"
      },
      {
        "id": 4,
        "image": "images/districts/jamalpur/hist-4.webp",
        "name": "Jamalpur Archeological Mound",
        "nameBn": "জামালপুর প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Jamalpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Jamalpur"
      },
      {
        "id": 5,
        "image": "images/districts/jamalpur/hist-5.webp",
        "name": "Jamalpur Liberation War Memorial",
        "nameBn": "জামালপুর মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Jamalpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Jamalpur"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/jamalpur/tour-1.webp",
        "name": "Old Brahmaputra Riverside Promenade",
        "nameBn": "Old Brahmaputra Riverside Promenade (জামালপুর)",
        "category": "Scenic Riverfront",
        "desc": "Old Brahmaputra Riverside Promenade stands as an iconic tourist highlight in Jamalpur district. Nestled in natural surroundings under Mymensingh Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Jamalpur Riverfront, Mymensingh"
      },
      {
        "id": 2,
        "image": "images/districts/jamalpur/tour-2.webp",
        "name": "Nakshi Kantha Artisan Villages",
        "nameBn": "Nakshi Kantha Artisan Villages (জামালপুর)",
        "category": "Folk Craft Capital",
        "desc": "Nakshi Kantha Artisan Villages stands as an iconic tourist highlight in Jamalpur district. Nestled in natural surroundings under Mymensingh Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Jamalpur"
      },
      {
        "id": 3,
        "image": "images/districts/jamalpur/tour-3.webp",
        "name": "Jamalpur Cultural Heritage Museum",
        "nameBn": "জামালপুর লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Jamalpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Jamalpur"
      },
      {
        "id": 4,
        "image": "images/districts/jamalpur/tour-4.webp",
        "name": "Jamalpur Scenic Lake & Boating Resort",
        "nameBn": "জামালপুর মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Jamalpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Jamalpur"
      },
      {
        "id": 5,
        "image": "images/districts/jamalpur/tour-5.webp",
        "name": "Jamalpur Sunset Hilltop Viewpoint",
        "nameBn": "জামালপুর সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Jamalpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Jamalpur"
      }
    ]
  },
  {
    "id": 62,
    "slug": "mymensingh",
    "en": "Mymensingh",
    "bn": "ময়মনসিংহ",
    "div": "Mymensingh",
    "lat": 24.6991,
    "lng": 90.4286,
    "coordinates": "24.6991, 90.4286",
    "est": 1787,
    "area": "4,363.48 km²",
    "pop": "5.3M",
    "dist": "120 km",
    "route": "Via Dhaka-Mymensingh 4-lane Highway N3 (approx. 2.5 - 3 hours) or commuter trains.",
    "tagline": "Mymensingh (ময়মনসিংহ) is a picturesque and historically significant administrative district in Mymensingh Division, Bangladesh.",
    "heroImage": "images/districts/mymensingh/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/mymensingh/carousel-1.webp",
        "title": "Mymensingh Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Mymensingh Division"
      },
      {
        "id": 2,
        "image": "images/districts/mymensingh/carousel-2.webp",
        "title": "Historic Monuments of Mymensingh",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/mymensingh/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/mymensingh/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/mymensingh/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/mymensingh/hist-1.webp",
        "name": "Shashi Lodge (Mymensingh Rajbari)",
        "nameBn": "Shashi Lodge (Mymensingh Rajbari) (ময়মনসিংহ)",
        "category": "Royal Heritage",
        "desc": "Exquisite neoclassical 19th-century royal palace adorned with European crystal and marble Venus statue.",
        "location": "Mymensingh Sadar, Mymensingh"
      },
      {
        "id": 2,
        "image": "images/districts/mymensingh/hist-2.webp",
        "name": "Alexander Castle (Lohar Kuthi)",
        "nameBn": "Alexander Castle (Lohar Kuthi) (ময়মনসিংহ)",
        "category": "Historic Mosque",
        "desc": "Colonial iron palace where Rabindranath Tagore and Lord Curzon stayed during their visits.",
        "location": "Old Town, Mymensingh"
      },
      {
        "id": 3,
        "image": "images/districts/mymensingh/hist-3.webp",
        "name": "Mymensingh Colonial Court & Mint",
        "nameBn": "ময়মনসিংহ ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Mymensingh district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Mymensingh"
      },
      {
        "id": 4,
        "image": "images/districts/mymensingh/hist-4.webp",
        "name": "Mymensingh Archeological Mound",
        "nameBn": "ময়মনসিংহ প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Mymensingh district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Mymensingh"
      },
      {
        "id": 5,
        "image": "images/districts/mymensingh/hist-5.webp",
        "name": "Mymensingh Liberation War Memorial",
        "nameBn": "ময়মনসিংহ মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Mymensingh district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Mymensingh"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/mymensingh/tour-1.webp",
        "name": "Brahmaputra Riverfront & Park",
        "nameBn": "Brahmaputra Riverfront & Park (ময়মনসিংহ)",
        "category": "Scenic Waterway",
        "desc": "Picturesque public park along the Old Brahmaputra River filled with traditional wooden boats.",
        "location": "Mymensingh Riverfront, Mymensingh"
      },
      {
        "id": 2,
        "image": "images/districts/mymensingh/tour-2.webp",
        "name": "Zainul Abedin Art Gallery & BAU Campus",
        "nameBn": "Zainul Abedin Art Gallery & BAU Campus (ময়মনসিংহ)",
        "category": "Art & Green Campus",
        "desc": "Zainul Abedin Art Gallery & BAU Campus stands as an iconic tourist highlight in Mymensingh district. Nestled in natural surroundings under Mymensingh Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Forest Range, Mymensingh"
      },
      {
        "id": 3,
        "image": "images/districts/mymensingh/tour-3.webp",
        "name": "Mymensingh Cultural Heritage Museum",
        "nameBn": "ময়মনসিংহ লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Mymensingh district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Mymensingh"
      },
      {
        "id": 4,
        "image": "images/districts/mymensingh/tour-4.webp",
        "name": "Mymensingh Scenic Lake & Boating Resort",
        "nameBn": "ময়মনসিংহ মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Mymensingh district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Mymensingh"
      },
      {
        "id": 5,
        "image": "images/districts/mymensingh/tour-5.webp",
        "name": "Mymensingh Sunset Hilltop Viewpoint",
        "nameBn": "ময়মনসিংহ সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Mymensingh district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Mymensingh"
      }
    ]
  },
  {
    "id": 63,
    "slug": "netrokona",
    "en": "Netrokona",
    "bn": "নেত্রকোনা",
    "div": "Mymensingh",
    "lat": 24.8708,
    "lng": 90.8446,
    "coordinates": "24.8708, 90.8446",
    "est": 1984,
    "area": "2,744.28 km²",
    "pop": "2.3M",
    "dist": "160 km",
    "route": "Via Mymensingh highway or Haor Express intercity train from Dhaka (approx. 4 - 4.5 hours).",
    "tagline": "Netrokona (নেত্রকোনা) is a picturesque and historically significant administrative district in Mymensingh Division, Bangladesh.",
    "heroImage": "images/districts/netrokona/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/netrokona/carousel-1.webp",
        "title": "Netrokona Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Mymensingh Division"
      },
      {
        "id": 2,
        "image": "images/districts/netrokona/carousel-2.webp",
        "title": "Historic Monuments of Netrokona",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/netrokona/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/netrokona/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/netrokona/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/netrokona/hist-1.webp",
        "name": "Roail Bari Ancient Fort",
        "nameBn": "Roail Bari Ancient Fort (নেত্রকোনা)",
        "category": "Royal Heritage",
        "desc": "Archaeological fortress site dating back to the Baro-Bhuiyan era with terracotta relics.",
        "location": "Netrokona Sadar, Mymensingh"
      },
      {
        "id": 2,
        "image": "images/districts/netrokona/hist-2.webp",
        "name": "Ranikhong Catholic Church",
        "nameBn": "Ranikhong Catholic Church (নেত্রকোনা)",
        "category": "Historic Mosque",
        "desc": "Ranikhong Catholic Church is one of the most prominent historical monuments in Netrokona district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Netrokona"
      },
      {
        "id": 3,
        "image": "images/districts/netrokona/hist-3.webp",
        "name": "Netrokona Colonial Court & Mint",
        "nameBn": "নেত্রকোনা ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Netrokona district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Netrokona"
      },
      {
        "id": 4,
        "image": "images/districts/netrokona/hist-4.webp",
        "name": "Netrokona Archeological Mound",
        "nameBn": "নেত্রকোনা প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Netrokona district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Netrokona"
      },
      {
        "id": 5,
        "image": "images/districts/netrokona/hist-5.webp",
        "name": "Netrokona Liberation War Memorial",
        "nameBn": "নেত্রকোনা মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Netrokona district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Netrokona"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/netrokona/tour-1.webp",
        "name": "Birishiri Ceramic Hills & Turquoise Lake",
        "nameBn": "Birishiri Ceramic Hills & Turquoise Lake (নেত্রকোনা)",
        "category": "Natural Wonder",
        "desc": "Birishiri Ceramic Hills & Turquoise Lake stands as an iconic tourist highlight in Netrokona district. Nestled in natural surroundings under Mymensingh Division, it offers travelers picturesque landscapes, tranquil recreation, and cultural exploration.",
        "location": "Netrokona Riverfront, Mymensingh"
      },
      {
        "id": 2,
        "image": "images/districts/netrokona/tour-2.webp",
        "name": "Someshwari River & Garo Hills",
        "nameBn": "Someshwari River & Garo Hills (নেত্রকোনা)",
        "category": "Riverside & Hills",
        "desc": "Shallow transparent mountain river flanked by verdant hills and indigenous Garo culture.",
        "location": "Forest Range, Netrokona"
      },
      {
        "id": 3,
        "image": "images/districts/netrokona/tour-3.webp",
        "name": "Netrokona Cultural Heritage Museum",
        "nameBn": "নেত্রকোনা লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Netrokona district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Netrokona"
      },
      {
        "id": 4,
        "image": "images/districts/netrokona/tour-4.webp",
        "name": "Netrokona Scenic Lake & Boating Resort",
        "nameBn": "নেত্রকোনা মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Netrokona district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Netrokona"
      },
      {
        "id": 5,
        "image": "images/districts/netrokona/tour-5.webp",
        "name": "Netrokona Sunset Hilltop Viewpoint",
        "nameBn": "নেত্রকোনা সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Netrokona district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Netrokona"
      }
    ]
  },
  {
    "id": 64,
    "slug": "sherpur",
    "en": "Sherpur",
    "bn": "শেরপুর",
    "div": "Mymensingh",
    "lat": 25.0823,
    "lng": 90.0745,
    "coordinates": "25.0823, 90.0745",
    "est": 1984,
    "area": "1,359.87 km²",
    "pop": "1.5M",
    "dist": "180 km",
    "route": "Via Dhaka-Mymensingh Highway extending north to Sherpur town (approx. 4 hours by highway bus).",
    "tagline": "Sherpur (শেরপুর) is a picturesque and historically significant administrative district in Mymensingh Division, Bangladesh.",
    "heroImage": "images/districts/sherpur/hero.webp",
    "carousel": [
      {
        "id": 1,
        "image": "images/districts/sherpur/carousel-1.webp",
        "title": "Sherpur Heritage & Landscapes",
        "subtitle": "Panoramic beauty across Mymensingh Division"
      },
      {
        "id": 2,
        "image": "images/districts/sherpur/carousel-2.webp",
        "title": "Historic Monuments of Sherpur",
        "subtitle": "Ancient landmarks dating back across generations"
      },
      {
        "id": 3,
        "image": "images/districts/sherpur/carousel-3.webp",
        "title": "Riverine Corridors & Nature",
        "subtitle": "Verdant waters and lush environmental biodiversity"
      },
      {
        "id": 4,
        "image": "images/districts/sherpur/carousel-4.webp",
        "title": "Cultural Life & Traditions",
        "subtitle": "Vibrant indigenous folklore, artisans, and community markets"
      },
      {
        "id": 5,
        "image": "images/districts/sherpur/carousel-5.webp",
        "title": "Scenic Trails & Landmarks",
        "subtitle": "Famous travel destinations and peaceful viewpoints"
      }
    ],
    "hist": [
      {
        "id": 1,
        "image": "images/districts/sherpur/hist-1.webp",
        "name": "Mysore Rajbari Ruins",
        "nameBn": "Mysore Rajbari Ruins (শেরপুর)",
        "category": "Royal Heritage",
        "desc": "Historic palace remains of local landlords featuring subterranean vaults and archways.",
        "location": "Sherpur Sadar, Mymensingh"
      },
      {
        "id": 2,
        "image": "images/districts/sherpur/hist-2.webp",
        "name": "Nalitabari Ancient Mosque",
        "nameBn": "Nalitabari Ancient Mosque (শেরপুর)",
        "category": "Historic Mosque",
        "desc": "Nalitabari Ancient Mosque is one of the most prominent historical monuments in Sherpur district. The site preserves centuries-old heritage, intricate regional brickwork, and rich cultural traditions attracting historians and visitors from across Bangladesh.",
        "location": "Old Town, Sherpur"
      },
      {
        "id": 3,
        "image": "images/districts/sherpur/hist-3.webp",
        "name": "Sherpur Colonial Court & Mint",
        "nameBn": "শেরপুর ঔপনিবেশিক আদালত ও টাকশাল",
        "category": "Colonial Architecture",
        "desc": "Renowned historical heritage site in Sherpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Court Road, Sherpur"
      },
      {
        "id": 4,
        "image": "images/districts/sherpur/hist-4.webp",
        "name": "Sherpur Archeological Mound",
        "nameBn": "শেরপুর প্রত্নতাত্ত্বিক ঢিবি",
        "category": "Ancient Archaeology",
        "desc": "Renowned historical heritage site in Sherpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Archaeological Site, Sherpur"
      },
      {
        "id": 5,
        "image": "images/districts/sherpur/hist-5.webp",
        "name": "Sherpur Liberation War Memorial",
        "nameBn": "শেরপুর মুক্তিযুদ্ধ স্মৃতিসৌধ",
        "category": "National Memorial",
        "desc": "Renowned historical heritage site in Sherpur district, preserving cultural treasures and significant archaeological architecture from antiquity and the colonial era.",
        "location": "Central Park, Sherpur"
      }
    ],
    "tour": [
      {
        "id": 1,
        "image": "images/districts/sherpur/tour-1.webp",
        "name": "Gajni Vacation Center (Garo Hills)",
        "nameBn": "Gajni Vacation Center (Garo Hills) (শেরপুর)",
        "category": "Eco Hill Resort",
        "desc": "Scenic hillside recreation park with watchtowers, artificial lakes, and forest trails.",
        "location": "Sherpur Riverfront, Mymensingh"
      },
      {
        "id": 2,
        "image": "images/districts/sherpur/tour-2.webp",
        "name": "Madhutila Eco Park",
        "nameBn": "Madhutila Eco Park (শেরপুর)",
        "category": "Border Wilderness",
        "desc": "Lush forested hills bordering Meghalaya with hanging bridges and wildlife viewing spots.",
        "location": "Forest Range, Sherpur"
      },
      {
        "id": 3,
        "image": "images/districts/sherpur/tour-3.webp",
        "name": "Sherpur Cultural Heritage Museum",
        "nameBn": "শেরপুর লোকশিল্প ও ঐতিহ্য জাদুঘর",
        "category": "Cultural Center",
        "desc": "A celebrated tourism highlight in Sherpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Town Center, Sherpur"
      },
      {
        "id": 4,
        "image": "images/districts/sherpur/tour-4.webp",
        "name": "Sherpur Scenic Lake & Boating Resort",
        "nameBn": "শেরপুর মনোরম হ্রদ ও রিসোর্ট",
        "category": "Lakeside Resort",
        "desc": "A celebrated tourism highlight in Sherpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Lake View, Sherpur"
      },
      {
        "id": 5,
        "image": "images/districts/sherpur/tour-5.webp",
        "name": "Sherpur Sunset Hilltop Viewpoint",
        "nameBn": "শেরপুর সূর্যাস্ত ভিউপয়েন্ট",
        "category": "Panoramic Vista",
        "desc": "A celebrated tourism highlight in Sherpur district, offering panoramic vistas, peaceful natural retreats, and scenic photography spots.",
        "location": "Hill Ridge, Sherpur"
      }
    ]
  }
];

if (typeof window !== 'undefined') {
  window.LOCAL_DISTRICTS = LOCAL_DISTRICTS;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { LOCAL_DISTRICTS };
}
