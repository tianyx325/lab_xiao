/*! Member profile: expand collapsed works lists ("查看更多"). */
(function () {
  document.addEventListener("click", function (e) {
    var btn = e.target && e.target.closest ? e.target.closest("[data-lab-works-more]") : null;
    if (!btn) return;
    var section = btn.closest(".lab-member-section");
    if (!section) return;
    section.querySelectorAll(".lab-member-works-extra").forEach(function (li) {
      li.hidden = false;
      li.classList.remove("lab-member-works-extra");
    });
    btn.remove();
  });
})();
