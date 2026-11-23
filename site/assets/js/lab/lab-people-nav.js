/*! People page group filter — a dropdown in the title band replaces the old
    chip anchor nav: pick a group (or subgroup) to show only that block;
    全部 shows everything. Options mirror the rendered headings, so empty
    groups never appear. Enhancement only: no JS → full list unchanged. */
(function () {
  var page = document.querySelector('.lab-list-page--people');
  if (!page) return;
  var scope = page.querySelector('.lab-list-body');
  var slot = page.querySelector('.lab-list-header-aside');
  if (!scope || !slot) return;

  var headings = Array.prototype.slice.call(
    scope.querySelectorAll('.lab-people-group-title, .lab-people-subgroup-title')
  );
  if (!headings.length) return;

  var select = document.createElement('select');
  select.className = 'lab-people-select lab-filter-control';
  select.setAttribute('aria-label', slot.getAttribute('data-label') || '按分组筛选');

  var all = document.createElement('option');
  all.value = '';
  all.textContent = slot.getAttribute('data-all') || '全部';
  select.appendChild(all);

  headings.forEach(function (h, i) {
    if (!h.id) h.id = 'people-group-' + i;
    var opt = document.createElement('option');
    opt.value = h.id;
    opt.textContent = h.textContent.trim();
    select.appendChild(opt);
  });

  /* A subgroup owns its heading plus every sibling up to the next subgroup. */
  function blockOf(h) {
    var nodes = [h];
    var n = h.nextElementSibling;
    while (n && !n.classList.contains('lab-people-subgroup-title')) {
      nodes.push(n);
      n = n.nextElementSibling;
    }
    return nodes;
  }

  function apply(id) {
    var target = id ? document.getElementById(id) : null;
    var isSub = !!(target && target.classList.contains('lab-people-subgroup-title'));
    Array.prototype.forEach.call(scope.querySelectorAll('.lab-people-group'), function (sec) {
      var keep = !target || sec.contains(target);
      sec.hidden = !keep;
      if (!keep) return;
      Array.prototype.forEach.call(sec.querySelectorAll('.lab-people-subgroup-title'), function (h) {
        var show = !isSub || h === target;
        blockOf(h).forEach(function (el) { el.hidden = !show; });
      });
    });
    var scroller = document.querySelector('.page-body');
    if (scroller && scroller.scrollTo) scroller.scrollTo({ top: 0, behavior: 'auto' });
    else if (scope.scrollTo) scope.scrollTo({ top: 0, behavior: 'auto' });
  }

  select.addEventListener('change', function () { apply(select.value); });
  slot.appendChild(select);
})();