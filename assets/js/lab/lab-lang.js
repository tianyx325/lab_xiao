/* Lab language preference — aligns with new-api's i18next detector pipeline:
 *
 *  - detection order: [localStorage, navigator] then fallback to site default
 *  - code normalization: zh-Hans / zh-CN / zh-TW / zh-HK / zh-MO → zh,
 *    en / en-US / en-GB → en, unknown codes fall back (whitelist = site
 *    languages only)
 *  - explicit choice cached to localStorage on every navbar language switch
 *  - first-visit redirect applies ONLY on language roots
 *    (site-base and site-base+"en/"), so deep links are never hijacked
 *
 *  Hugo serves both languages statically (defaultContentLanguage zh at the
 *  site base, en at base+"en/"). The base is injected by Hugo via <body
 *  data-base> (== relURL "/") so it works both at a domain root and under a
 *  sub-path such as GitHub Pages (/lab_xiao/). No hardcoded root path.
 */
(function () {
  'use strict';

  var STORE_KEY = 'lab:lang:v1';
  var REDIRECT_GUARD = 'lab:lang:redirected';
  var FALLBACK = 'zh'; /* defaultContentLanguage */
  var WHITELIST = ['zh', 'en'];

  /* Base path of the site, injected by Hugo via <body data-base> (== relURL
     "/"). Normalize to a single trailing slash. The attribute is always
     present on pages that load this script; "/" is a safe last resort. */
  function siteBase() {
    var raw = (document.body && document.body.getAttribute('data-base')) || '/';
    if (!raw) raw = '/';
    if (raw.charAt(raw.length - 1) !== '/') raw += '/';
    return raw;
  }
  var BASE = siteBase();
  /* Language roots relative to the injected base. zh is the default
     language served at the base itself; en lives under base+"en/". */
  var ROOTS = { zh: BASE, en: BASE + 'en/' };

  function normalize(raw) {
    if (!raw) return '';
    var code = String(raw).trim().toLowerCase().replace('_', '-');
    if (code.indexOf('zh') === 0) return 'zh'; /* zh-Hans/zh-CN/zh-TW/zh-HK/zh-MO */
    if (code.indexOf('en') === 0) return 'en'; /* en / en-US / en-GB */
    return WHITELIST.indexOf(code) > -1 ? code : '';
  }

  function currentLang() {
    return normalize(document.documentElement.getAttribute('lang')) || FALLBACK;
  }

  function storedLang() {
    try {
      return normalize(localStorage.getItem(STORE_KEY));
    } catch (e) {
      return '';
    }
  }

  function browserLang() {
    var langs = navigator.languages || [navigator.language || ''];
    for (var i = 0; i < langs.length; i++) {
      var hit = normalize(langs[i]);
      if (hit) return hit;
    }
    return '';
  }

  /* Cache explicit choices made through the navbar language dropdown. */
  document.addEventListener('click', function (ev) {
    var link = ev.target.closest('.i18n-dropdown a[data-lang]');
    if (!link) return;
    try {
      localStorage.setItem(STORE_KEY, link.getAttribute('data-lang'));
    } catch (e) { /* noop */ }
  });

  /* First visit on a language root: honor stored / browser preference.
     Per-session guard prevents redirect loops if something odd happens. */
  var cur = currentLang();
  var root = ROOTS[cur];
  if (!root) return;

  var path = location.pathname;
  var trimmedRoot = root.replace(/\/+$/, '');
  var atRoot = path === root || path === trimmedRoot;
  if (!atRoot) return;

  try {
    if (sessionStorage.getItem(REDIRECT_GUARD)) return;
  } catch (e) { /* noop */ }

  var want = storedLang() || browserLang() || FALLBACK;
  if (want && want !== cur) {
    try {
      sessionStorage.setItem(REDIRECT_GUARD, '1');
    } catch (e) { /* noop */ }
    location.replace(ROOTS[want]);
  }
})();
