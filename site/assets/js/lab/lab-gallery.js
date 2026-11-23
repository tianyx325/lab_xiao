(() => {
  const roots = document.querySelectorAll("[data-lab-gallery-root]");
  if (!roots.length) return;
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  roots.forEach((root) => {
    const viewport = root.querySelector("[data-lab-gallery-viewport]");
    const track = root.querySelector(".lab-gallery-track");
    const prev = root.querySelector(".lab-gallery-prev");
    const next = root.querySelector(".lab-gallery-next");
    if (!viewport || !track) return;

    /* One click / key press advances by a full viewport page (3 visible items). */
    const pageSize = () => viewport.clientWidth;

    const syncButtons = () => {
      if (!prev || !next) return;
      const max = Math.max(0, viewport.scrollWidth - viewport.clientWidth - 1);
      prev.disabled = viewport.scrollLeft <= 1;
      next.disabled = viewport.scrollLeft >= max;
    };

    const scrollByDir = (dir) => {
      viewport.scrollBy({ left: dir * pageSize(), behavior: reduce ? "auto" : "smooth" });
    };

    prev?.addEventListener("click", () => scrollByDir(-1));
    next?.addEventListener("click", () => scrollByDir(1));
    viewport.addEventListener("scroll", () => syncButtons(), { passive: true });
    window.addEventListener("resize", () => syncButtons(), { passive: true });

    viewport.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft") {
        e.preventDefault();
        scrollByDir(-1);
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        scrollByDir(1);
      }
    });

    syncButtons();

    /* ── Zero-dependency lightbox (replaces the dropped fancybox branch) ──
       Thumbnails link to the lite (1400px) render; clicking opens it in a
       dialog overlay with caption and arrow-key navigation instead of
       navigating away to the raw image file. */
    const items = Array.prototype.slice.call(track.querySelectorAll(".lab-gallery-item a"));
    let lb = null;
    let lbIndex = 0;
    let lastFocus = null;

    const ensureLightbox = () => {
      if (lb) return lb;
      lb = document.createElement("div");
      lb.className = "lab-lightbox";
      lb.hidden = true;
      lb.setAttribute("role", "dialog");
      lb.setAttribute("aria-modal", "true");
      lb.setAttribute("aria-label", root.dataset.lbLabel || "Gallery");
      lb.innerHTML =
        '<button type="button" class="lab-lightbox-close" aria-label="' + (root.dataset.lbClose || "Close") + '">' +
        '  <span aria-hidden="true">×</span>' +
        "</button>" +
        '<figure class="lab-lightbox-body">' +
        '  <img class="lab-lightbox-img" src="" alt="" decoding="async">' +
        '  <figcaption class="lab-lightbox-caption"></figcaption>' +
        "</figure>" +
        '<button type="button" class="lab-lightbox-nav lab-lightbox-prev" aria-label="' + (root.dataset.lbPrev || "Previous") + '"><span aria-hidden="true">‹</span></button>' +
        '<button type="button" class="lab-lightbox-nav lab-lightbox-next" aria-label="' + (root.dataset.lbNext || "Next") + '"><span aria-hidden="true">›</span></button>';
      document.body.appendChild(lb);

      lb.querySelector(".lab-lightbox-close").addEventListener("click", closeLightbox);
      lb.querySelector(".lab-lightbox-prev").addEventListener("click", () => stepLightbox(-1));
      lb.querySelector(".lab-lightbox-next").addEventListener("click", () => stepLightbox(1));
      lb.addEventListener("click", (e) => {
        if (e.target === lb) closeLightbox();
      });
      return lb;
    };

    const renderLightbox = () => {
      const link = items[lbIndex];
      const img = lb.querySelector(".lab-lightbox-img");
      img.src = link.getAttribute("href");
      img.alt = link.querySelector("img")?.alt || "";
      lb.querySelector(".lab-lightbox-caption").textContent = link.dataset.caption || "";
      const single = items.length < 2;
      lb.querySelector(".lab-lightbox-prev").hidden = single;
      lb.querySelector(".lab-lightbox-next").hidden = single;
    };

    function openLightbox(i) {
      lastFocus = document.activeElement;
      lbIndex = i;
      ensureLightbox();
      renderLightbox();
      lb.hidden = false;
      document.body.classList.add("lab-lightbox-open");
      lb.querySelector(".lab-lightbox-close").focus();
      document.addEventListener("keydown", onLightboxKey);
    }

    function closeLightbox() {
      lb.hidden = true;
      document.body.classList.remove("lab-lightbox-open");
      document.removeEventListener("keydown", onLightboxKey);
      const img = lb.querySelector(".lab-lightbox-img");
      img.src = ""; /* release the lite render */
      if (lastFocus) lastFocus.focus();
    }

    function stepLightbox(dir) {
      lbIndex = (lbIndex + dir + items.length) % items.length;
      renderLightbox();
    }

    function onLightboxKey(e) {
      if (e.key === "Escape") {
        e.preventDefault();
        closeLightbox();
      } else if (e.key === "Tab") {
        var focusables = Array.prototype.slice.call(
          lb.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])')
        ).filter(function (el) { return !el.hidden && !el.disabled; });
        if (!focusables.length) return;
        var first = focusables[0];
        var last = focusables[focusables.length - 1];
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      } else if (e.key === "ArrowLeft") {
        e.preventDefault();
        stepLightbox(-1);
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        stepLightbox(1);
      }
    }

    items.forEach((link, i) => {
      link.addEventListener("click", (e) => {
        e.preventDefault();
        openLightbox(i);
      });
    });
  });
})();
