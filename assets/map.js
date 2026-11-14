/* Wong & Yip map: MapLibre + OpenFreeMap vector tiles in the firm's colours.
   Walking routes come from routing.openstreetmap.de and are baked into #map-data. */
(() => {
  const C = {
    land: '#f4f0ea',
    building: '#e4dcef',
    buildingLine: '#d3c7e2',
    park: '#e3ecd4',
    water: '#c9d6ef',
    road: '#ffffff',
    roadCase: '#ddd3e6',
    major: '#ffffff',
    majorCase: '#c7b8d8',
    rail: '#b8a9c9',
    label: '#360064',
    labelSoft: '#6b5a7c',
    halo: '#f4f0ea',
    route: '#ff9b00',
    routeCase: '#360064',
  };
  const name = ['coalesce', ['get', 'name:en'], ['get', 'name_en'], ['get', 'name']];
  const width = (a, b, c) => ['interpolate', ['exponential', 1.6], ['zoom'], 13, a, 16, b, 18, c];
  const major = ['match', ['get', 'class'], ['motorway', 'trunk', 'primary', 'secondary'], true, false];
  const minor = ['match', ['get', 'class'], ['tertiary', 'minor', 'service', 'street', 'residential'], true, false];

  const style = {
    version: 8,
    glyphs: 'https://tiles.openfreemap.org/fonts/{fontstack}/{range}.pbf',
    sources: { omt: { type: 'vector', url: 'https://tiles.openfreemap.org/planet' } },
    layers: [
      { id: 'land', type: 'background', paint: { 'background-color': C.land } },
      { id: 'park', type: 'fill', source: 'omt', 'source-layer': 'park', paint: { 'fill-color': C.park } },
      { id: 'green', type: 'fill', source: 'omt', 'source-layer': 'landuse', filter: ['match', ['get', 'class'], ['park', 'grass', 'cemetery', 'pitch', 'playground'], true, false], paint: { 'fill-color': C.park } },
      { id: 'water', type: 'fill', source: 'omt', 'source-layer': 'water', paint: { 'fill-color': C.water } },
      { id: 'waterway', type: 'line', source: 'omt', 'source-layer': 'waterway', paint: { 'line-color': C.water, 'line-width': ['interpolate', ['linear'], ['zoom'], 13, 1.5, 18, 8] } },
      { id: 'building', type: 'fill', source: 'omt', 'source-layer': 'building', minzoom: 13, paint: { 'fill-color': C.building, 'fill-outline-color': C.buildingLine } },
      { id: 'rail', type: 'line', source: 'omt', 'source-layer': 'transportation', filter: ['match', ['get', 'class'], ['rail', 'transit'], true, false], paint: { 'line-color': C.rail, 'line-width': 1.4, 'line-dasharray': [3, 2] } },
      { id: 'road-case', type: 'line', source: 'omt', 'source-layer': 'transportation', filter: minor, layout: { 'line-cap': 'round', 'line-join': 'round' }, paint: { 'line-color': C.roadCase, 'line-width': width(1.5, 6, 20) } },
      { id: 'major-case', type: 'line', source: 'omt', 'source-layer': 'transportation', filter: major, layout: { 'line-cap': 'round', 'line-join': 'round' }, paint: { 'line-color': C.majorCase, 'line-width': width(3, 10, 30) } },
      { id: 'road', type: 'line', source: 'omt', 'source-layer': 'transportation', filter: minor, layout: { 'line-cap': 'round', 'line-join': 'round' }, paint: { 'line-color': C.road, 'line-width': width(1, 4.5, 17) } },
      { id: 'major', type: 'line', source: 'omt', 'source-layer': 'transportation', filter: major, layout: { 'line-cap': 'round', 'line-join': 'round' }, paint: { 'line-color': C.major, 'line-width': width(2, 8, 27) } },
      { id: 'road-label', type: 'symbol', source: 'omt', 'source-layer': 'transportation_name', minzoom: 15, layout: { 'symbol-placement': 'line', 'text-field': name, 'text-font': ['Noto Sans Regular'], 'text-size': 11 }, paint: { 'text-color': C.labelSoft, 'text-halo-color': C.halo, 'text-halo-width': 1.4 } },
      { id: 'area-label', type: 'symbol', source: 'omt', 'source-layer': 'place', filter: ['match', ['get', 'class'], ['suburb', 'quarter', 'neighbourhood'], true, false], layout: { 'text-field': ['upcase', name], 'text-font': ['Noto Sans Bold'], 'text-size': 11, 'text-letter-spacing': 0.18, 'text-max-width': 8 }, paint: { 'text-color': C.labelSoft, 'text-halo-color': C.halo, 'text-halo-width': 1.4 } },
    ],
  };

  const el = (html, cls) => { const d = document.createElement('div'); d.className = cls; d.innerHTML = html; return d; };

  window.wyMap = (box) => {
    const data = JSON.parse(document.getElementById('map-data').textContent);
    const { maplibregl } = window;
    const holder = document.createElement('div');
    holder.className = 'mapbox';
    box.appendChild(holder);
    const phone = window.matchMedia('(max-width: 760px)').matches;
    const map = new maplibregl.Map({
      container: holder, style, center: data.home, zoom: 15, maxZoom: 18, minZoom: 12,
      dragRotate: false, pitchWithRotate: false, cooperativeGestures: true, attributionControl: { compact: true },
    });
    map.touchZoomRotate.disableRotation();
    if (!phone) map.addControl(new maplibregl.NavigationControl({ showCompass: false }), 'top-left');

    const bounds = new maplibregl.LngLatBounds(data.home, data.home);
    data.routes.forEach((r) => r.coords.forEach((c) => bounds.extend(c)));
    const fit = () => map.fitBounds(bounds, { padding: phone ? { top: 50, bottom: 40, left: 30, right: 30 } : { top: 70, bottom: 50, left: 70, right: 70 }, duration: 0, maxZoom: 16 });
    fit();
    let touched = false;
    map.on('dragstart', () => { touched = true; });
    map.on('zoomstart', (e) => { if (e.originalEvent) touched = true; });
    window.addEventListener('resize', () => { if (!touched) fit(); });

    map.on('load', () => {
      const fc = { type: 'FeatureCollection', features: data.routes.map((r) => ({ type: 'Feature', properties: {}, geometry: { type: 'LineString', coordinates: r.coords } })) };
      map.addSource('routes', { type: 'geojson', data: fc });
      map.addLayer({ id: 'route-case', type: 'line', source: 'routes', layout: { 'line-cap': 'round', 'line-join': 'round' }, paint: { 'line-color': C.routeCase, 'line-width': 6, 'line-opacity': 0.25 } });
      map.addLayer({ id: 'route', type: 'line', source: 'routes', layout: { 'line-cap': 'round', 'line-join': 'round' }, paint: { 'line-color': C.route, 'line-width': 3.5, 'line-dasharray': [1.2, 1.2] } });
    });

    data.routes.forEach((r) => {
      new maplibregl.Marker({ element: el(`<span class="dot"></span><span class="t">${r.name} · ${r.min}′</span>`, 'map-stn'), anchor: 'left', offset: [-7, 0] })
        .setLngLat(r.start).addTo(map);
    });
    new maplibregl.Marker({ element: el(`<span class="pin"><img src="${data.mark}" alt=""></span><span class="pin-label">${data.label}</span>`, 'map-pin'), anchor: 'top', offset: [0, -29] })
      .setLngLat(data.home).addTo(map);
    return map;
  };
})();
