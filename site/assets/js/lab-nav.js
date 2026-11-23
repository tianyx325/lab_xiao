(function () {
  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }
  ready(function () {
    var toggle = document.querySelector("[data-lab-nav-toggle]");
    var panel = document.getElementById("navbar-content");
    if (toggle && panel) {
      toggle.addEventListener("click", function () {
        var open = panel.classList.toggle("is-open");
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
    }
    document.querySelectorAll("[data-lab-dropdown]").forEach(function (btn) {
      var wrap = btn.closest(".dropdown");
      if (!wrap) return;
      btn.addEventListener("click", function (e) {
        e.stopPropagation();
        var open = wrap.classList.toggle("is-open");
        btn.setAttribute("aria-expanded", open ? "true" : "false");
      });
    });
    document.addEventListener("click", function () {
      document.querySelectorAll(".dropdown.is-open").forEach(function (el) {
        el.classList.remove("is-open");
      });
    });
  });
})();
