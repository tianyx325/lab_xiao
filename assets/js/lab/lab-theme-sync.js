/* Lab theme sync — aligns switching behaviour with new-api (router.boguanwenlv.com):
 *
 *  1. Keep <meta name="theme-color"> in lockstep with the active mode.
 *     (new-api hardcodes #fff and never syncs; we sync from the computed
 *     body background so mobile browser chrome follows the real theme.)
 *  2. Mirror the vendor's integer mode storage (wcTheme: 0/1/2) to a named,
 *     versioned key (lab:theme:v1:mode ∈ light|dark|system) — readable
 *     semantics, matching newapi:theme:v1:mode, ready for future migration.
 *
 *  The vendor bundle (wowchemy-theming.js) already handles: persistence,
 *  whitelist validation, OS live-follow in auto mode, and the dropdown UI.
 *  It also dispatches `wcThemeChange` on every render (incl. init), which
 *  is the single hook we consume here.
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

  /* Read the effective body background so light/dark values come from the
     theme itself instead of hardcoded hex values. */
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

  /* One-time migration: if the vendor key was cleared but our named key
     survived (or vice versa), restore the missing side. */
  function reconcileKeys() {
    try {
      var wcTheme = localStorage.getItem('wcTheme');
      var named = localStorage.getItem(NAMED_KEY);
      if (!wcTheme && named && NAME_TO_INT[named]) {
        localStorage.setItem('wcTheme', NAME_TO_INT[named]);
      } else if (wcTheme !== null && !named) {
        var name = INT_TO_NAME[readIntMode()];
        if (name) localStorage.setItem(NAMED_KEY, name);
      }
    } catch (e) { /* storage unavailable — theme still works un-persisted */ }
  }

  /* Mirror every explicit choice into the named key. The vendor handler
     writes wcTheme itself; we only record the human-readable alias. */
  document.addEventListener('click', function (ev) {
    var link = ev.target.closest('.js-set-theme-light, .js-set-theme-dark, .js-set-theme-auto');
    if (!link) return;
    var name = link.classList.contains('js-set-theme-light')
      ? 'light'
      : link.classList.contains('js-set-theme-dark')
        ? 'dark'
        : 'system';
    try {
      localStorage.setItem(NAMED_KEY, name);
    } catch (e) { /* noop */ }
  });

  /* The vendor dispatches wcThemeChange on every theme render, including
     page init — this keeps theme-color correct in all four paths:
     init / manual light / manual dark / OS change while in auto. */
  document.addEventListener('wcThemeChange', function () {
    syncThemeColor();
  });

  reconcileKeys();
  syncThemeColor();
})();
