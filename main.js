// === NAVIGATION SYSTEM ===
const navLinks = document.querySelectorAll(".nav-link");
const sections = document.querySelectorAll("section[id]");

// Handle navigation clicks
navLinks.forEach((link) => {
  link.addEventListener("click", function (e) {
    // Let the default anchor behavior work
    // Don't preventDefault - we want smooth scroll

    // Update active state immediately
    navLinks.forEach((l) => l.classList.remove("active"));
    this.classList.add("active");
  });
});

// Update active nav link based on scroll position
function updateActiveNavOnScroll() {
  let currentSection = "";

  sections.forEach((section) => {
    const sectionTop = section.offsetTop;
    const sectionHeight = section.clientHeight;

    // Account for nav bar height
    if (window.scrollY >= sectionTop - 100) {
      currentSection = section.getAttribute("id");
    }
  });

  // Map special sections
  if (currentSection === "about") currentSection = "home";
  if (currentSection === "services") currentSection = "portfolio";

  // Update active class
  navLinks.forEach((link) => {
    link.classList.remove("active");
    if (link.getAttribute("href") === `#${currentSection}`) {
      link.classList.add("active");
    }
  });
}

// Listen for scroll
window.addEventListener("scroll", updateActiveNavOnScroll);

// Set initial active state
updateActiveNavOnScroll();

var swiper = new Swiper(".mySwiper", {
  pagination: {
    el: ".swiper-pagination",
    dynamicBullets: true,
  },
});

// Certificate Modal Logic
function viewCertificate(element, event) {
  if (event) event.preventDefault();
  const imgSrc = element.getAttribute("data-src");
  const modalImage = document.getElementById("certificateImage");
  const downloadBtn = document.getElementById("downloadCertificateBtn");

  if (modalImage && downloadBtn) {
    modalImage.src = imgSrc;
    downloadBtn.href = imgSrc;

    // Check if bootstrap is defined (it should be loaded via CDN)
    if (typeof bootstrap !== "undefined") {
      const modalEl = document.getElementById("certificateModal");
      const modal =
        bootstrap.Modal.getInstance(modalEl) || new bootstrap.Modal(modalEl);
      modal.show();
    } else {
      console.error("Bootstrap is not loaded");
    }
  }
}

// Preloader Logic
window.addEventListener("load", () => {
  const preloader = document.getElementById("preloader");
  if (preloader) {
    setTimeout(() => {
      preloader.classList.add("loaded");
    }, 500);
  }
});

// Typed JS
const typed = new Typed(".auto-type", {
  strings: [
    "Ethical Hacker",
    "Security Researcher",
    "Bug Hunter",
    "CTF Player",
  ],
  typeSpeed: 100,
  backSpeed: 50,
  loop: true,
});
