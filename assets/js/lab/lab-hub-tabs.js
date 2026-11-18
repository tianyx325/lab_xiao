/*! Outputs hub tabs: switch the visible category panel. Zero deps;
    WAI-ARIA tabs pattern (click + arrow-key roving focus). The selected
    panel is mirrored in the URL hash (#pub / #pat / #award) so old section
    URLs and deep links land on the right tab. */
(function () {
  var tablist = document.querySelector('.lab-hub-tabs');
  if (!tablist) return;

  /* Progressive enhancement: mark the page as JS-enabled only once this
     script actually runs. CSS uses this to collapse inactive panels; without
     it every panel stays open (no-JS fallback). */
  var page = document.querySelector('.lab-list-page--overview');
  if (page) page.classList.add('js-enabled');

  var tabs = Array.prototype.slice.call(tablist.querySelectorAll('[role="tab"]'));
  /* One filter row per category lives in the sticky band; show only the
     active tab's row. */
  var filterRows = Array.prototype.slice.call(document.querySelectorAll('[data-filter-for]'));
  /* The award panel is a full-width poster grid; papers and patents are
     888px media rows, so the band column follows the active panel (see
     .js-enabled data-lab-wide handling in select()). */

  function keyOf(tab) {
    return (tab.getAttribute('aria-controls') || '').replace('lab-hub-panel-', '');
  }

  function select(tab, syncHash, animate) {
    var activePanel = tab.getAttribute('aria-controls');
    /* Slides the selected-category thumb in the segmented track */
    tablist.style.setProperty('--lab-hub-index', tabs.indexOf(tab));
    tabs.forEach(function (t) {
      var panel = document.getElementById(t.getAttribute('aria-controls'));
      var active = t === tab;
      t.setAttribute('aria-selected', active ? 'true' : 'false');
      t.tabIndex = active ? 0 : -1;
      if (panel) {
        panel.hidden = !active;
        if (active && animate) {
          panel.classList.remove('is-revealing');
          void panel.offsetWidth; /* restart the clip-path reveal */
          panel.classList.add('is-revealing');
        }
      }
    });
    filterRows.forEach(function (row) {
      row.hidden = row.getAttribute('data-filter-for') !== activePanel;
    });
    if (page) {
      if (activePanel === 'lab-hub-panel-award') page.setAttribute('data-lab-wide', '');
      else page.removeAttribute('data-lab-wide');
    }
    if (syncHash && history.replaceState) {
      history.replaceState(null, '', '#' + keyOf(tab));
    }
  }

  tabs.forEach(function (tab, i) {
    tab.addEventListener('click', function () { select(tab, true, true); });
    tab.addEventListener('keydown', function (e) {
      var next = null;
      if (e.key === 'ArrowRight') next = tabs[(i + 1) % tabs.length];
      else if (e.key === 'ArrowLeft') next = tabs[(i - 1 + tabs.length) % tabs.length];
      else if (e.key === 'Home') next = tabs[0];
      else if (e.key === 'End') next = tabs[tabs.length - 1];
      if (next) {
        e.preventDefault();
        next.focus();
        select(next, true, true);
      }
    });
  });

  /* Establish the initial collapsed state. Panels ship open (no-JS safe), so
     with JS we must explicitly hide all but the selected one. A deep link
     (/publications/#pat, or a year anchor #pat-y2025) picks that tab. */
  var initial = tabs[0];
  var hash = (location.hash || '').replace('#', '');
  if (hash) {
    var match = tabs.filter(function (t) {
      var key = keyOf(t);
      return hash === key || hash.indexOf(key + '-') === 0;
    })[0];
    if (match) initial = match;
  }
  if (initial) select(initial, false);
})();
