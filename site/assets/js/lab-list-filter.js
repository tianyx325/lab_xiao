/*! Client-side search/filter for lab section lists. */
(function () {
  function bind(root) {
    var search = root.querySelector("[data-lab-search]");
    var items = Array.prototype.slice.call(root.querySelectorAll("[data-lab-item]"));
    var empty = root.querySelector("[data-lab-empty]");
    var countEl = root.querySelector("[data-lab-count]");
    var filters = Array.prototype.slice.call(root.querySelectorAll("[data-lab-filter]"));

    function apply() {
      var q = (search && search.value ? search.value : "").trim().toLowerCase();
      var active = {};
      filters.forEach(function (el) {
        active[el.getAttribute("data-lab-filter")] = (el.value || "").trim();
      });
      var visible = 0;
      items.forEach(function (item) {
        var ok = true;
        if (q) {
          var hay = item.getAttribute("data-text") || "";
          ok = hay.indexOf(q) !== -1;
        }
        Object.keys(active).forEach(function (key) {
          if (!ok || !active[key]) return;
          if ((item.getAttribute("data-" + key) || "") !== active[key]) ok = false;
        });
        item.hidden = !ok;
        if (ok) visible += 1;
      });
      if (empty) empty.classList.toggle("hidden", visible !== 0);
      if (countEl) {
        countEl.textContent = visible + " / " + items.length;
      }
    }

    if (search) {
      search.addEventListener("input", apply);
    }
    filters.forEach(function (el) {
      el.addEventListener("change", apply);
    });
    apply();
  }

  document.addEventListener("DOMContentLoaded", function () {
    Array.prototype.forEach.call(document.querySelectorAll("[data-lab-list]"), bind);
  });
})();
