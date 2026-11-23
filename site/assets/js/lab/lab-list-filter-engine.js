/*! DOM list filter/pagination — requires lab-filter-core.js */
(function () {
  'use strict';
  var F = window.LabFilter;
  if (!F) return;

  var roots = Array.prototype.slice.call(document.querySelectorAll('[data-lab-filter-root]'));
  if (!roots.length) return;

  var i18nNode = document.getElementById('lab-filter-i18n');
  var i18n = { empty: 'No results', clear: 'Clear', pagination: 'Pagination', prev: 'Previous', next: 'Next' };
  if (i18nNode) {
    try { i18n = Object.assign(i18n, JSON.parse(i18nNode.textContent || '{}')); } catch (e) { /* keep defaults */ }
  }

  function init(root) {
    var pageSize = parseInt(root.getAttribute('data-page-size') || '12', 10) || 12;
    var items = Array.prototype.slice.call(root.querySelectorAll('.lab-list-item'));
    var scope = root.closest('[data-lab-list-scope]');
    var panel = root.closest('[role="tabpanel"]');
    var host = panel ? document.querySelector('[data-filter-for="' + panel.id + '"]') : null;
    var controlScope = host ||
      (scope && scope.querySelector('.lab-list-filters') ? scope : null) ||
      root.closest('.lab-list-page') || document;
    var search = controlScope.querySelector('.lab-list-filters .filter-search');
    var selects = Array.prototype.slice.call(controlScope.querySelectorAll('.lab-list-filters .lab-filter-select'));
    var page = 1;

    var empty = document.createElement('div');
    empty.className = 'lab-filter-empty';
    empty.setAttribute('hidden', '');
    empty.setAttribute('role', 'status');
    empty.setAttribute('aria-live', 'polite');
    var emptyText = document.createElement('p');
    emptyText.className = 'lab-filter-empty-text';
    emptyText.textContent = i18n.empty;
    var emptyClear = document.createElement('button');
    emptyClear.type = 'button';
    emptyClear.className = 'lab-filter-clear';
    emptyClear.textContent = i18n.clear;
    empty.appendChild(emptyText);
    empty.appendChild(emptyClear);

    var nav = document.createElement('nav');
    nav.className = 'lab-pagination';
    nav.setAttribute('aria-label', i18n.pagination);
    nav.setAttribute('hidden', '');
    var list = document.createElement('ul');
    list.className = 'lab-pagination-list';
    nav.appendChild(list);
    root.insertAdjacentElement('afterend', nav);
    root.insertAdjacentElement('afterend', empty);

    var yearHeads = Array.prototype.slice.call(root.querySelectorAll('.lab-year-head'));

    function matched() {
      return items.filter(function (item) {
        return !item.classList.contains('is-filtered-out');
      });
    }

    function scrollToTop() {
      var scroller = document.querySelector('.page-body');
      if (scroller && scroller.scrollHeight > scroller.clientHeight + 1) {
        scroller.scrollTo({ top: 0, behavior: 'smooth' });
        return;
      }
      var target = controlScope.querySelector('.lab-list-filters') ||
        document.querySelector('.lab-list-header');
      if (target && target.scrollIntoView) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    function render() {
      var hits = matched();
      var pages = Math.max(1, Math.ceil(hits.length / pageSize));
      if (page > pages) page = pages;
      if (page < 1) page = 1;
      var start = (page - 1) * pageSize;
      hits.forEach(function (item, i) {
        item.classList.toggle('is-paged-out', i < start || i >= start + pageSize);
      });
      if (hits.length === 0) empty.removeAttribute('hidden');
      else empty.setAttribute('hidden', '');

      var showNav = F.renderPagination(list, {
        page: page,
        total: pages,
        prevLabel: i18n.prev,
        nextLabel: i18n.next,
        onPage: function (n) {
          page = n;
          render();
          syncYearGroups();
          scrollToTop();
        }
      });
      if (showNav) nav.removeAttribute('hidden');
      else nav.setAttribute('hidden', '');
    }

    function yearVisible(y) {
      return items.some(function (item) {
        return item.classList.contains('year-' + y) &&
          !item.classList.contains('is-filtered-out') &&
          !item.classList.contains('is-paged-out');
      });
    }

    function syncYearGroups() {
      yearHeads.forEach(function (head) {
        head.hidden = !yearVisible(head.getAttribute('data-year'));
      });
    }

    function applyFilter(resetPage) {
      var q = search && search.value ? search.value : '';
      var groups = {};
      selects.forEach(function (sel) {
        groups[sel.getAttribute('data-filter-group')] = sel.value || '*';
      });
      items.forEach(function (item) {
        var ok = true;
        Object.keys(groups).forEach(function (g) {
          if (!F.hasClassToken(item.className, groups[g])) ok = false;
        });
        if (ok && !F.matchText(item.textContent || '', q)) ok = false;
        item.classList.toggle('is-filtered-out', !ok);
      });
      if (resetPage) page = 1;
      render();
      syncYearGroups();
    }

    emptyClear.addEventListener('click', function () {
      if (search) search.value = '';
      selects.forEach(function (sel) {
        sel.value = sel.options && sel.options.length ? sel.options[0].value : '';
      });
      debounced.cancel();
      applyFilter(true);
    });

    var debounced = F.debounce(function () { applyFilter(true); }, 200);
    if (search) search.addEventListener('input', debounced);
    selects.forEach(function (sel) {
      sel.addEventListener('change', function () { applyFilter(true); });
    });
    applyFilter(false);
  }

  roots.forEach(init);
})();
