/* Lab theme sync
 *
 * Vendor wowchemy.js only binds click handlers to the *first*
 * .js-set-theme-* nodes (the mobile drawer). Desktop dropdown items
 * never received listeners, so Theme ▾ appeared dead on PC.
 *
 * This module owns every theme click: persist wcTheme + named key,
 * toggle body.dark, sync theme-color, mark active UI. Vendor's own
 * listeners (drawer) remain; double-apply is idempotent.
 */
(function () {
  'use strict';

  var META_SELECTOR = 'meta[name="theme-color"]';
  var NAMED_KEY = 'lab:theme:v1:mode';
  var NAME_TO_INT = { light: '0', dark: '1', system: '2' };
  var INT_TO_NAME = { 0: 'light', 1: 'dark', 2: 'system' };

  function ensureMeta() {
    var meta = document.querySelector(META_SELECTOR);
    if (!meta) {
      meta = document.createElement('meta');
      meta.setAttribute('name', 'theme-color');
      document.head.appendChild(meta);
    }
    return meta;
  }

  function syncThemeColor() {
    var meta = ensureMeta();
    var bg = getComputedStyle(document.body).backgroundColor;
    if (bg && bg !== 'rgba(0, 0, 0, 0)') meta.setAttribute('content', bg);
  }

  function readIntMode() {
    try {
      return parseInt(localStorage.getItem('wcTheme') || '2', 10);
    } catch (e) {
      return 2;
    }
  }

  function siteDefaultDark() {
    return !!(window.wc && window.wc.isSiteThemeDark);
  }

  function resolveDark(mode) {
    if (mode === 0) return false;
    if (mode === 1) return true;
    if (window.matchMedia('(prefers-color-scheme: dark)').matches) return true;
    if (window.matchMedia('(prefers-color-scheme: light)').matches) return false;
    return siteDefaultDark();
  }

  function syncHljs(isDark) {
    var light = document.querySelector('link[title=hl-light]');
    var dark = document.querySelector('link[title=hl-dark]');
    if (!light && !dark) return;
    if (light) light.disabled = !!isDark;
    if (dark) dark.disabled = !isDark;
  }

  function markActiveTheme() {
    var mode = readIntMode();
    var nodes = document.querySelectorAll(
      '.js-set-theme-light, .js-set-theme-dark, .js-set-theme-auto'
    );
    for (var i = 0; i < nodes.length; i++) {
      var el = nodes[i];
      var active =
        (mode === 0 && el.classList.contains('js-set-theme-light')) ||
        (mode === 1 && el.classList.contains('js-set-theme-dark')) ||
        (mode === 2 && el.classList.contains('js-set-theme-auto'));
      el.classList.toggle('dropdown-item-active', active);
      el.classList.toggle('is-current', active);
      if (active) el.setAttribute('aria-current', 'true');
      else el.removeAttribute('aria-current');
    }
  }

  function applyThemeMode(mode) {
    var isDark = resolveDark(mode);
    var name = INT_TO_NAME[mode] || 'system';
    try {
      localStorage.setItem('wcTheme', String(mode));
      localStorage.setItem(NAMED_KEY, name);
    } catch (e) { /* storage unavailable */ }

    document.body.classList.toggle('dark', isDark);
    syncHljs(isDark);
    markActiveTheme();
    syncThemeColor();
    document.dispatchEvent(
      new CustomEvent('wcThemeChange', { detail: { isDarkTheme: function () { return isDark; } } })
    );
  }

  function reconcileKeys() {
    try {
      var wcTheme = localStorage.getItem('wcTheme');
      var named = localStorage.getItem(NAMED_KEY);
      if (!wcTheme && named && NAME_TO_INT[named]) {
        localStorage.setItem('wcTheme', NAME_TO_INT[named]);
      } else if (wcTheme !== null && !named) {
        var n = INT_TO_NAME[readIntMode()];
        if (n) localStorage.setItem(NAMED_KEY, n);
      }
    } catch (e) { /* noop */ }
  }

  document.addEventListener('click', function (ev) {
    var link = ev.target.closest('.js-set-theme-light, .js-set-theme-dark, .js-set-theme-auto');
    if (!link) return;
    ev.preventDefault();
    var mode = link.classList.contains('js-set-theme-light')
      ? 0
      : link.classList.contains('js-set-theme-dark')
        ? 1
        : 2;
    applyThemeMode(mode);
  });

  document.addEventListener('wcThemeChange', function () {
    syncThemeColor();
    markActiveTheme();
  });

  reconcileKeys();
  syncThemeColor();
  markActiveTheme();
})();
