/*! Shared list/hub filter helpers — window.LabFilter */
(function (w) {
  'use strict';

  var SECTION_CANON = {
    publication: 'publications',
    publications: 'publications',
    project: 'projects',
    projects: 'projects',
    post: 'blog',
    blog: 'blog',
    patent: 'patent',
    award: 'award'
  };

  function normalizeSection(name) {
    var key = String(name || '').trim();
    return SECTION_CANON[key] || key;
  }

  function classToken(value) {
    return String(value || '').replace(/^\./, '');
  }

  function hasClassToken(className, value) {
    var token = classToken(value);
    if (!token || token === '*') return true;
    return (' ' + String(className || '') + ' ').indexOf(' ' + token + ' ') !== -1;
  }

  function matchText(haystack, query) {
    var q = String(query || '').trim().toLowerCase();
    if (!q) return true;
    return String(haystack || '').toLowerCase().indexOf(q) !== -1;
  }

  function debounce(fn, ms) {
    var t = 0;
    function wrapped() {
      var ctx = this;
      var args = arguments;
      w.clearTimeout(t);
      t = w.setTimeout(function () {
        t = 0;
        fn.apply(ctx, args);
      }, ms);
    }
    wrapped.cancel = function () {
      w.clearTimeout(t);
      t = 0;
    };
    return wrapped;
  }

  /**
   * Render prev / numbers / next into a <ul class="lab-pagination-list">.
   * opts: { page, total, prevLabel, nextLabel, onPage(n) }
   */
  function renderPagination(listEl, opts) {
    var page = opts.page | 0;
    var total = opts.total | 0;
    var onPage = opts.onPage;
    listEl.textContent = '';
    if (total <= 1) return false;

    function add(label, target, disabled, current, isText) {
      var li = document.createElement('li');
      li.className = 'lab-pagination-item';
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'lab-pagination-link' + (isText ? ' lab-pagination-link--text' : '');
      btn.textContent = label;
      if (disabled) {
        btn.disabled = true;
        btn.classList.add('is-disabled');
      }
      if (current) {
        btn.classList.add('is-current');
        btn.setAttribute('aria-current', 'page');
      }
      if (!disabled && !current && typeof onPage === 'function') {
        btn.addEventListener('click', function () { onPage(target); });
      }
      li.appendChild(btn);
      listEl.appendChild(li);
    }

    add(opts.prevLabel || 'Previous', page - 1, page <= 1, false, true);
    for (var i = 1; i <= total; i++) add(String(i), i, false, i === page, false);
    add(opts.nextLabel || 'Next', page + 1, page >= total, false, true);
    return true;
  }

  function notifyGrid(grid) {
    try {
      grid.dispatchEvent(new CustomEvent('lab:grid-change', { bubbles: true }));
    } catch (e) { /* ignore */ }
  }

  w.LabFilter = {
    normalizeSection: normalizeSection,
    classToken: classToken,
    hasClassToken: hasClassToken,
    matchText: matchText,
    debounce: debounce,
    renderPagination: renderPagination,
    notifyGrid: notifyGrid
  };
})(window);
