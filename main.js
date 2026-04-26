/* ============================================================
   main.js — Portfolio Script
   Preloader · Navigation · Scroll Reveal · Certificate Modal
   ============================================================ */

/* ── PRELOADER ─────────────────────────────────────────────── */
(function () {
  const preloader = document.getElementById('preloader');
  const bar       = document.getElementById('pl-bar');
  const pct       = document.getElementById('pl-pct');
  const lines     = ['pl-l1', 'pl-l2', 'pl-l3'];

  if (!preloader) return;

  let progress = 0;
  let lineIdx  = 0;

  // Show terminal lines one by one
  const lineTimer = setInterval(() => {
    if (lineIdx < lines.length) {
      const el = document.getElementById(lines[lineIdx]);
      if (el) el.classList.add('show');
      lineIdx++;
    } else {
      clearInterval(lineTimer);
    }
  }, 220);

  // Animate progress bar
  const progressTimer = setInterval(() => {
    const step = Math.random() * 14 + 6;
    progress = Math.min(progress + step, 100);
    if (bar) bar.style.width = progress + '%';
    if (pct) pct.textContent = Math.floor(progress) + '%';
    if (progress >= 100) clearInterval(progressTimer);
  }, 80);

  // Hide on load
  window.addEventListener('load', () => {
    // Ensure bar hits 100
    if (bar) bar.style.width = '100%';
    if (pct) pct.textContent = '100%';

    setTimeout(() => {
      preloader.classList.add('loaded');
      document.body.style.overflow = '';
      // Completely remove from layout after transition
      setTimeout(() => preloader.classList.add('done'), 750);
    }, 350);
  });

  // Fallback: always hide after 3.5s
  setTimeout(() => {
    preloader.classList.add('loaded');
    document.body.style.overflow = '';
    setTimeout(() => preloader.classList.add('done'), 750);
  }, 3500);

  // Prevent scroll during preload
  document.body.style.overflow = 'hidden';
})();

/* ── NAVIGATION ────────────────────────────────────────────── */
const navLinks = document.querySelectorAll('.nav-link');
const sections = document.querySelectorAll('section[id]');

navLinks.forEach((link) => {
  link.addEventListener('click', function () {
    navLinks.forEach((l) => l.classList.remove('active'));
    this.classList.add('active');
  });
});

function updateActiveNavOnScroll() {
  let current = '';
  sections.forEach((sec) => {
    // Determine which section is currently in view
    // Using a more accurate offset for smooth highlight
    if (window.scrollY >= sec.offsetTop - 300) {
      current = sec.getAttribute('id');
    }
  });

  // If scrolled to very top, force 'home'
  if (window.scrollY < 100) {
    current = 'home';
  }

  navLinks.forEach((link) => {
    link.classList.remove('active');
    if (link.getAttribute('href') === `#${current}`) {
      link.classList.add('active');
    }
  });
}

window.addEventListener('scroll', updateActiveNavOnScroll, { passive: true });
updateActiveNavOnScroll();

/* ── SCROLL REVEAL ─────────────────────────────────────────── */
const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { rootMargin: '0px', threshold: 0.12 }
);

// Expose globally so latest-articles.js can observe injected cards
window._revealObserver = revealObserver;

document.querySelectorAll('[data-animate]').forEach((el) => {
  revealObserver.observe(el);
});

/* ── LAZY IMAGES ───────────────────────────────────────────── */
if ('loading' in HTMLImageElement.prototype) {
  document.querySelectorAll('img[data-src]').forEach((img) => {
    img.src = img.dataset.src;
  });
} else {
  // Fallback IntersectionObserver for lazy images
  const imgObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        imgObserver.unobserve(img);
      }
    });
  });
  document.querySelectorAll('img[data-src]').forEach((img) => {
    imgObserver.observe(img);
  });
}

/* ── CERTIFICATE MODAL ─────────────────────────────────────── */
function viewCertificate(element, event) {
  if (event) event.preventDefault();
  const imgSrc    = element.getAttribute('data-src');
  const modalImg  = document.getElementById('certificateImage');
  const dlBtn     = document.getElementById('downloadCertificateBtn');

  if (modalImg && dlBtn) {
    modalImg.src = imgSrc;
    dlBtn.href   = imgSrc;

    if (typeof bootstrap !== 'undefined') {
      const modalEl = document.getElementById('certificateModal');
      const modal   = bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
      modal.show();
    }
  }
}

/* ── TYPED.JS ──────────────────────────────────────────────── */
// Wait for Typed.js to be available (it's deferred)
function initTyped() {
  if (typeof Typed !== 'undefined') {
    new Typed('.auto-type', {
      strings: [
        'Ethical Hacker',
        'Security Researcher',
        'Bug Hunter',
        'CTF Player',
        'Penetration Tester',
      ],
      typeSpeed: 60,
      backSpeed: 35,
      backDelay: 1800,
      loop: true,
    });
  } else {
    setTimeout(initTyped, 100);
  }
}
initTyped();

/* ── YEAR AUTO-UPDATE ──────────────────────────────────────── */
const yearEl = document.getElementById('currentYear');
if (yearEl) yearEl.textContent = new Date().getFullYear();

/* ── CONTACT FORM SUCCESS MESSAGE ──────────────────────────── */
const contactForm = document.getElementById('contact-form');
if (contactForm) {
  contactForm.addEventListener('submit', function () {
    const btn = this.querySelector('.my-contact-form-btn');
    if (btn) {
      btn.textContent = 'Sending...';
      btn.disabled = true;
    }
  });
}
