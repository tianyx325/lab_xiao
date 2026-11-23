/*************************************************
 * Lab map — Gaode (高德) tiles for China.
 * Shadows blox-bootstrap wowchemy-map.js when
 * features.map.provider is amap / mapnik / mapbox / google.
 **************************************************/

function initMap() {
  if (!$('#map').length) return;

  let map_provider = $('#map-provider').val();
  let lat = $('#map-lat').val();
  let lng = $('#map-lng').val();
  let zoom = parseInt($('#map-zoom').val(), 10);
  let address = $('#map-dir').val();
  let api_key = $('#map-api-key').val();
  let leafletImg = $('#map-leaflet-img').val();

  if (map_provider === 'google') {
    let map = new GMaps({
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

  if (typeof L === 'undefined') return;

  if (leafletImg) {
    L.Icon.Default.prototype.options.imagePath = leafletImg;
  }

  let map = L.map('map').setView([lat, lng], zoom);

  if (map_provider === 'amap') {
    // 高德矢量路网（国内可访问；坐标按 GCJ-02 理解）
    L.tileLayer('https://webrd0{s}.is.autonavi.com/appmaptile?lang=zh_cn&size=1&scale=1&style=8&x={x}&y={y}&z={z}', {
      maxZoom: 18,
      minZoom: 3,
      subdomains: '1234',
      attribution: '&copy; <a href="https://www.amap.com/">高德地图</a>',
    }).addTo(map);
  } else if (map_provider === 'mapbox' && api_key.length) {
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
      attribution:
        'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, Imagery © <a href="http://mapbox.com">Mapbox</a>',
      tileSize: 512,
      maxZoom: 18,
      zoomOffset: -1,
      id: 'mapbox/streets-v11',
      accessToken: api_key,
    }).addTo(map);
  } else {
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
    }).addTo(map);
  }

  let marker = L.marker([lat, lng]).addTo(map);
  if (map_provider === 'amap') {
    let amapUrl =
      'https://uri.amap.com/marker?position=' +
      encodeURIComponent(lng + ',' + lat) +
      '&name=' +
      encodeURIComponent(address || '');
    marker.bindPopup(
      (address ? address + '<p>' : '') +
        '<a href="' +
        amapUrl +
        '" target="_blank" rel="noopener">在高德地图中查看</a>' +
        (address ? '</p>' : ''),
    );
  } else {
    let url = lat + ',' + lng + '#map=' + zoom + '/' + lat + '/' + lng + '&layers=N';
    marker.bindPopup(
      address +
        '<p><a href="https://www.openstreetmap.org/directions?engine=osrm_car&route=' +
        url +
        '">Routing via OpenStreetMap</a></p>',
    );
  }
}

document.addEventListener('DOMContentLoaded', function () {
  initMap();
});
