/*! Hub search/filter — server HTML by default; JSON index on first filter.
   Requires lab-filter-core.js */
(function () {
  'use strict';
  var F = window.LabFilter;
  if (!F) return;

  var grid = document.querySelector('[data-hub-grid]');
  if (!grid) return;

  if (location.hash === '#pat') {
    location.replace(grid.getAttribute('data-hub-pat-url'));
    return;
  }
  if (location.hash === '#award') {
    location.replace(grid.getAttribute('data-hub-award-url'));
    return;
  }

  var header = document.querySelector('.lab-list-header--hub');
  var search = header && header.querySelector('.filter-search');
  var selects = header ? Array.prototype.slice.call(header.querySelectorAll('.lab-filter-select')) : [];
  if (!search && !selects.length) return;

  var serverHTML = grid.innerHTML;
  var serverNav = document.querySelector('.lab-list-body > .lab-pagination');
  var pageSize = parseInt(grid.getAttribute('data-hub-page-size') || '12', 10);
  var section = F.normalizeSection(grid.getAttribute('data-hub-section'));
  var jsonURL = grid.getAttribute('data-hub-json');
  var prevLabel = grid.getAttribute('data-hub-prev') || 'Previous';
  var nextLabel = grid.getAttribute('data-hub-next') || 'Next';
  var records = null;
  var page = 1;
  var clientNav = null;
  var empty = null;
  var count = null;
  var countFormat = grid.getAttribute('data-hub-count-format') || '';

  function active() {
    if (search && search.value.trim()) return true;
    return selects.some(function (sel) {
      return sel.value && sel.value !== '*' && sel.value !== '';
    });
  }

  function ensureClientUI() {
    if (clientNav) return;
    clientNav = document.createElement('nav');
    clientNav.className = 'lab-pagination';
    clientNav.setAttribute('data-hub-client-nav', '');
    clientNav.hidden = true;
    var list = document.createElement('ul');
    list.className = 'lab-pagination-list';
    clientNav.appendChild(list);
    grid.insertAdjacentElement('afterend', clientNav);

    empty = document.createElement('div');
    empty.className = 'lab-filter-empty';
    empty.hidden = true;
    empty.setAttribute('role', 'status');
    empty.setAttribute('aria-live', 'polite');
    empty.textContent = grid.getAttribute('data-hub-empty') || 'No results';
    grid.insertAdjacentElement('afterend', empty);

    count = document.createElement('div');
    count.className = 'lab-filter-count';
    count.hidden = true;
    count.setAttribute('role', 'status');
    count.setAttribute('aria-live', 'polite');
    grid.insertAdjacentElement('beforebegin', count);
  }

  function matches(record) {
    if (F.normalizeSection(record.section) !== section) return false;
    var q = search ? search.value : '';
    if (!F.matchText(record.text, q)) return false;
    return selects.every(function (sel) {
      var value = sel.value;
      if (!value || value === '*') return true;
      return F.hasClassToken(record.classes, value);
    });
  }

  function renderNav(total) {
    ensureClientUI();
    var list = clientNav.querySelector('.lab-pagination-list');
    var show = F.renderPagination(list, {
      page: page,
      total: total,
      prevLabel: prevLabel,
      nextLabel: nextLabel,
      onPage: function (n) {
        page = n;
        render();
        grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
    clientNav.hidden = !show;
  }

  function render() {
    var hits = records.filter(matches);
    var pages = Math.max(1, Math.ceil(hits.length / pageSize));
    if (page > pages) page = pages;
    var start = (page - 1) * pageSize;
    grid.innerHTML = hits.slice(start, start + pageSize).map(function (record) {
      return '<div class="lab-list-item ' + record.classes + '">' + record.html + '</div>';
    }).join('');
    ensureClientUI();
    empty.hidden = hits.length !== 0;
    if (count && countFormat) {
      count.hidden = false;
      count.textContent = countFormat.replace('{n}', String(hits.length));
    }
    renderNav(pages);
    F.notifyGrid(grid);
  }

  function restore() {
    grid.innerHTML = serverHTML;
    if (serverNav) serverNav.hidden = false;
    if (clientNav) clientNav.hidden = true;
    if (empty) empty.hidden = true;
    if (count) count.hidden = true;
    F.notifyGrid(grid);
  }

  function setLoading(on) {
    grid.classList.toggle('is-indexing', on);
    if (search) {
      if (on) search.setAttribute('aria-busy', 'true');
      else search.removeAttribute('aria-busy');
    }
  }

  function update() {
    if (!active()) {
      restore();
      return;
    }
    if (serverNav) serverNav.hidden = true;
    if (records) {
      page = 1;
      render();
      return;
    }
    if (empty) empty.textContent = grid.getAttribute('data-hub-empty') || 'No results';
    setLoading(true);
    fetch(jsonURL)
      .then(function (response) {
        if (!response.ok) throw new Error('HTTP ' + response.status);
        return response.json();
      })
      .then(function (data) {
        records = data;
        page = 1;
        setLoading(false);
        render();
      })
      .catch(function () {
        setLoading(false);
        if (serverNav) serverNav.hidden = false;
        ensureClientUI();
        empty.textContent = grid.getAttribute('data-hub-error') || 'Filtering unavailable';
        empty.hidden = false;
        if (count) count.hidden = true;
        if (clientNav) clientNav.hidden = true;
      });
  }

  var updateDebounced = F.debounce(update, 200);
  if (search) search.addEventListener('input', updateDebounced);
  selects.forEach(function (sel) { sel.addEventListener('change', update); });
})();
