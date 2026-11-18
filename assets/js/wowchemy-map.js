/*************************************************
 * Lab map override — China-accessible tiles
 * (OSM tile.openstreetmap.org is often unreachable)
 **************************************************/

function wgs84ToGcj02(lng, lat) {
  const a = 6378245.0;
  const ee = 0.00669342162296594323;
  const outOfChina = (lng < 72.004 || lng > 137.8347 || lat < 0.8293 || lat > 55.8271);
  if (outOfChina) return [lng, lat];

  function transformLat(x, y) {
    let r =
      -100.0 +
      2.0 * x +
      3.0 * y +
      0.2 * y * y +
      0.1 * x * y +
      0.2 * Math.sqrt(Math.abs(x));
    r += ((20.0 * Math.sin(6.0 * x * Math.PI) + 20.0 * Math.sin(2.0 * x * Math.PI)) * 2.0) / 3.0;
    r += ((20.0 * Math.sin(y * Math.PI) + 40.0 * Math.sin((y / 3.0) * Math.PI)) * 2.0) / 3.0;
    r += ((160.0 * Math.sin((y / 12.0) * Math.PI) + 320 * Math.sin((y * Math.PI) / 30.0)) * 2.0) / 3.0;
    return r;
  }

  function transformLng(x, y) {
    let r =
      300.0 +
      x +
      2.0 * y +
      0.1 * x * x +
      0.1 * x * y +
      0.1 * Math.sqrt(Math.abs(x));
    r += ((20.0 * Math.sin(6.0 * x * Math.PI) + 20.0 * Math.sin(2.0 * x * Math.PI)) * 2.0) / 3.0;
    r += ((20.0 * Math.sin(x * Math.PI) + 40.0 * Math.sin((x / 3.0) * Math.PI)) * 2.0) / 3.0;
    r += ((150.0 * Math.sin((x / 12.0) * Math.PI) + 300.0 * Math.sin((x / 30.0) * Math.PI)) * 2.0) / 3.0;
    return r;
  }

  let dLat = transformLat(lng - 105.0, lat - 35.0);
  let dLng = transformLng(lng - 105.0, lat - 35.0);
  const radLat = (lat / 180.0) * Math.PI;
  let magic = Math.sin(radLat);
  magic = 1 - ee * magic * magic;
  const sqrtMagic = Math.sqrt(magic);
  dLat = (dLat * 180.0) / (((a * (1 - ee)) / (magic * sqrtMagic)) * Math.PI);
  dLng = (dLng * 180.0) / ((a / sqrtMagic) * Math.cos(radLat) * Math.PI);
  return [lng + dLng, lat + dLat];
}

function val(id, fallback) {
  const el = document.getElementById(id);
  return el && el.value != null && el.value !== '' ? el.value : fallback;
}

function initMap() {
  const mapEl = document.getElementById('map');
  if (!mapEl) return;
  if (typeof L === 'undefined') {
    console.warn('[lab-map] Leaflet (L) is not loaded; check custom_head amap assets.');
    return;
  }

  const provider = val('map-provider', 'mapnik');
  const lat = parseFloat(val('map-lat', '0'));
  const lng = parseFloat(val('map-lng', '0'));
  const zoom = parseInt(val('map-zoom', '15'), 10) || 15;
  const address = val('map-dir', '');
  const apiKey = val('map-api-key', '');
  // Absolute image dir (must end with /). Do NOT use Icon.Default.mergeOptions
  // with full URLs — Default._getIconUrl prepends imagePath (often CDN),
  // producing broken paths like cdn.../images//vendor/leaflet/images/...
  const imgBase = val('map-leaflet-img', '/vendor/leaflet/images/').replace(/\/?$/, '/');
  if (L.Icon && L.Icon.Default) {
    L.Icon.Default.imagePath = imgBase;
  }
  const markerIcon = L.icon({
    iconUrl: imgBase + 'marker-icon.png',
    iconRetinaUrl: imgBase + 'marker-icon-2x.png',
    shadowUrl: imgBase + 'marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    tooltipAnchor: [16, -28],
    shadowSize: [41, 41],
  });

  if (provider === 'google' && typeof GMaps !== 'undefined') {
    const map = new GMaps({
      div: '#map',
      lat: lat,
      lng: lng,
      zoom: zoom,
      zoomControl: true,
      zoomControlOpt: { style: 'SMALL', position: 'TOP_LEFT' },
      streetViewControl: false,
      mapTypeControl: false,
      gestureHandling: 'cooperative',
    });
    map.addMarker({
      lat: lat,
      lng: lng,
      click: function () {
        window.open(
          'https://www.google.com/maps/place/' + encodeURIComponent(address) + '/@' + lat + ',' + lng + '/',
          '_blank',
        );
      },
      title: address,
    });
    return;
  }

  let viewLat = lat;
  let viewLng = lng;
  let tileLayer;

  if (provider === 'mapbox' && apiKey.length) {
    tileLayer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
      attribution:
        'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, Imagery © <a href="http://mapbox.com">Mapbox</a>',
      tileSize: 512,
      maxZoom: 18,
      zoomOffset: -1,
      id: 'mapbox/streets-v11',
      accessToken: apiKey,
    });
  } else {
    // amap / mapnik / 其它非 google·mapbox → 高德底图（国内可访问）；坐标转 GCJ-02
    const gcj = wgs84ToGcj02(lng, lat);
    viewLng = gcj[0];
    viewLat = gcj[1];
    tileLayer = L.tileLayer(
      'https://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}',
      {
        subdomains: '1234',
        maxZoom: 18,
        attribution: '&copy; <a href="https://www.amap.com/">高德地图</a>',
      },
    );
  }

  const map = L.map(mapEl).setView([viewLat, viewLng], zoom);
  tileLayer.addTo(map);
  const marker = L.marker([viewLat, viewLng], { icon: markerIcon }).addTo(map);
  const amapLink =
    'https://uri.amap.com/marker?position=' +
    viewLng +
    ',' +
    viewLat +
    '&name=' +
    encodeURIComponent(address || '实验室') +
    '&coordinate=gaode&callnative=1';
  marker.bindPopup(
    (address ? address + '<br>' : '') +
      '<a href="' +
      amapLink +
      '" target="_blank" rel="noopener">在高德地图中打开</a>',
  );

  // Container may layout after fonts/CSS; force redraw
  setTimeout(function () {
    map.invalidateSize();
  }, 200);
  window.addEventListener('load', function () {
    map.invalidateSize();
  });
}

// type="module" is deferred — DOMContentLoaded may already have fired
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initMap);
} else {
  initMap();
}
