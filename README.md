# Local Host — Explore Bangladesh District by District 🇧🇩

> An interactive, responsive, and modern vector map and district profile portal for exploring all 64 districts of Bangladesh. Built with authentic geographic, demographic, and transit records.

---

## 🌟 Key Features

- **Interactive Vector SVG Map**:
  - Full vector rendering of all 64 districts of Bangladesh.
  - Hover / Touch inspection with real-time highlights (**Flag Green** for hover, **Flag Red** for active selection).
  - Smart clamped floating tooltip strictly bounded inside the map container.
  - Dedicated **In-Map District Detail Inspector HUD** displaying bilingual names, division, distance from Dhaka, total area, and population with direct profile navigation.

- **Responsive Mobile & Desktop Experience**:
  - **Mobile (< 1024px)**: Segmented View Controller (`[ 🗺️ Interactive Map ]` vs `[ 📋 64 Districts List ]`) to prevent endless vertical scrolling. Tap-friendly targets (min 42px) and zero horizontal overflow.
  - **Desktop (≥ 1024px)**: Dual-column grid with a sticky searchable sidebar on the left and interactive map dashboard on the right.

- **Dedicated District Profile Pages (`#/district/<slug>`)**:
  - Complete read-only viewer profile for every district.
  - Prominent top and bottom `← Back to Home` rollback buttons.
  - 4 Key Metrics: Formation year, total geographic span, census population, and distance from Dhaka.
  - Route and Transit breakdown (Highway bus, Railway links, Private vehicle, Waterway launch).
  - 4-Box Visual Gallery (16:9 fixed aspect ratio) with curated archives and coming soon displays.
  - Historical places, heritage landmarks, and tourist attraction highlights.

- **National Identity & Theming**:
  - Bangladesh Flag color palette: Forest Green (`#006A4E` / `#059669`), Sun Red (`#F42A41`), and clean neutral surfaces.
  - Interactive **Dark Mode ↔ Light Mode** toggle with instant persistence via `localStorage`.
  - Local **Kalpurush** Bengali font (`fonts/kalpurush.woff2`) for authentic Bengali typography and **Plus Jakarta Sans** for English.

- **Dynamic Data API & Offline Cache**:
  - Connects to public BD-APIs (`https://bdapis.com/api/v1.2/districts`) for live coordinate updates.
  - Built-in comprehensive 64-district fallback schema for instant offline reliability.

---

## 📁 Project Structure

```text
EzzeMap/
├── fonts/
│   └── kalpurush.woff2         # Local Bengali font
├── app.js                      # Application logic, routing, theme, and map events
├── district-data.js            # 64 districts data schema and SVG vector paths
├── index.html                  # Responsive HTML5 layout with Tailwind CSS
├── server.js                   # Lightweight Node.js local static server
├── .gitignore                  # Git ignore rules
└── README.md                   # Documentation
```

---

## 🚀 Getting Started

### 1. Run with Node.js
Clone the repository and launch the built-in server:
```bash
git clone https://github.com/ImranHasan13421/EzzeMap.git
cd EzzeMap
node server.js
```
Then open your browser at:
```
http://localhost:3000
```

### 2. Run with VS Code Live Server / Static Hosting
You can also open `index.html` directly or serve it using any static HTTP server (e.g., Live Server, Nginx, Vercel, or GitHub Pages).

---

## 🛠️ Tech Stack

- **Markup & Styling**: HTML5, Tailwind CSS (via CDN)
- **Typography**: Local Kalpurush font (Bengali) + Google Font Plus Jakarta Sans (English)
- **Icons**: Lucide Icons CDN
- **Logic**: Vanilla JavaScript (ES6+, URL Hash routing, Web APIs)
- **Backend / Server**: Lightweight Node.js `http` module

---

## 📄 License
MIT License. Free for open-source exploration and learning.
