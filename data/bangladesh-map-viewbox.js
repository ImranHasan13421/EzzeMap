/**
 * Bangladesh Vector Map ViewBox Coordinates
 * Absolute boundary definitions for geographic SVG polygon mapping
 */
const BANGLADESH_MAP_VIEWBOX = {
  x: -40,
  y: -35,
  w: 680,
  h: 918
};

// Global memory registry
if (typeof window !== 'undefined') {
  window.BANGLADESH_MAP_VIEWBOX = BANGLADESH_MAP_VIEWBOX;
}

if (typeof module !== 'undefined' && module.exports) {
  module.exports = { BANGLADESH_MAP_VIEWBOX };
}
