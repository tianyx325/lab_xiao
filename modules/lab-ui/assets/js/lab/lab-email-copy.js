/* Email tag — one-click copy.
   The advisor card renders the email as a pill button; clicking copies the
   address to the clipboard and flashes a "copied" state on the chip itself.
   Falls back to a hidden textarea + execCommand for older browsers / non-
   secure contexts where navigator.clipboard is unavailable. */
(function () {
  "use strict";

  function fallbackCopy(text, done) {
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.opacity = "0";
    ta.style.pointerEvents = "none";
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand("copy");
      done();
    } catch (err) {
      /* clipboard unavailable — leave the chip selected so the user can copy manually */
      ta.setSelectionRange(0, text.length);
    }
    document.body.removeChild(ta);
  }

  function flashCopied(btn) {
    var original = btn.textContent;
    var copied = document.documentElement.lang === "en" ? "Copied" : "已复制";
    btn.classList.add("is-copied");
    btn.textContent = copied;
    window.setTimeout(function () {
      btn.classList.remove("is-copied");
      btn.textContent = original;
    }, 1500);
  }

  document.addEventListener("click", function (e) {
    var btn = e.target.closest(".lab-member-email-tag");
    if (!btn) return;
    e.preventDefault();
    var email = btn.getAttribute("data-email") || btn.textContent.trim();
    var done = function () { flashCopied(btn); };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(email).then(done, function () {
        fallbackCopy(email, done);
      });
    } else {
      fallbackCopy(email, done);
    }
  });
})();
