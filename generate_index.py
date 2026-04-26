import os

html_content = """<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Toufique Zaman Topu</title>
  <link rel="icon" type="image/svg+xml" href="assets/image/favicon.svg">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css" />
  <link rel="stylesheet" href="style.css" />
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.css" />
  <script src="https://unpkg.com/typed.js@2.1.0/dist/typed.umd.js"></script>
</head>

<body>
  <!-- Preloader -->
  <div id="preloader">
    <div class="loader-container">
      <div class="loader-ring"></div>
      <div class="loader-ring"></div>
      <span class="loader-text">TOPU</span>
    </div>
  </div>
  
  <nav>
    <ul>
      <li><a class="nav-link active" href="#home"><i class="bi bi-house-door"></i></a></li>
      <li><a class="nav-link" href="#about"><i class="bi bi-person"></i></a></li>
      <li><a class="nav-link" href="#experience"><i class="bi bi-tools"></i></a></li>
      <li><a class="nav-link" href="#portfolio"><i class="bi bi-briefcase"></i></a></li>
      <li><a class="nav-link" href="blog.html"><i class="bi bi-book"></i></a></li>
      <li><a class="nav-link" href="#contact"><i class="bi bi-chat-dots"></i></a></li>
    </ul>
  </nav>

  <!-- Hero Section  -->
  <section class="hero-section" id="home">
    <div class="container">
      <div class="hero-topbar" data-animate="fade-down">
        <div class="hero-available">
          <span class="pulse-dot"></span> Available for Projects
        </div>
        <div class="hero-location">
          <i class="bi bi-geo-alt"></i> Bangladesh
        </div>
      </div>
      
      <div class="hero-name-block stagger-children is-visible" data-animate="fade-up">
        <h1 class="hero-name">
          <span class="name-line">Toufique Zaman<span class="name-accent">.</span></span>
          <span class="name-line">Topu</span>
        </h1>
      </div>
      
      <div class="hero-role-block" data-animate="fade-up">
        <div class="hero-role-line">
          <span class="role-prefix">↘</span>
          <span>I'm a <span class="auto-type text-white fw-bold"></span></span>
        </div>
      </div>
      
      <div class="hero-info-strip" data-animate="fade-up" style="--d: 0.1s">
        <div class="info-item">
          <span class="info-label">Experience</span>
          <span class="info-value">2+ Years</span>
        </div>
        <span class="info-divider">/</span>
        <div class="info-item">
          <span class="info-label">Focus</span>
          <span class="info-value">Pentesting & WebSec</span>
        </div>
        <span class="info-divider">/</span>
        <div class="info-item">
          <span class="info-label">Organization</span>
          <span class="info-value">Founder, Bug Mohol</span>
        </div>
      </div>
      
      <div class="hero-footer-strip" data-animate="fade-up" style="--d: 0.2s">
        <div class="hero-socials">
          <a href="https://www.facebook.com/zamantopu.official/" target="_blank"><i class="bi bi-facebook"></i></a>
          <a href="https://www.instagram.com/zamantopu.official/" target="_blank"><i class="bi bi-instagram"></i></a>
          <a href="https://tryhackme.com/p/zamantopu" target="_blank" title="TryHackMe"><i class="bi bi-terminal-fill"></i></a>
          <a href="https://www.linkedin.com/in/zaman-topu/" target="_blank"><i class="bi bi-linkedin"></i></a>
        </div>
        <div class="hero-cta-group">
          <a href="#contact" class="btn-cta-primary">Let's Talk <i class="bi bi-arrow-right"></i></a>
          <a href="#about" class="btn-cta-ghost">View Profile</a>
        </div>
      </div>
      
      <div class="hero-scroll-hint" data-animate="fade-up" style="--d: 0.4s">
        Scroll to explore
        <div class="scroll-bar"></div>
      </div>
    </div>
  </section>
  
  <!-- Marquee -->
  <div class="marquee-section">
    <div class="marquee-track">
      <span>Penetration Testing</span><span class="sep">✸</span>
      <span>Vulnerability Assessment</span><span class="sep">✸</span>
      <span>Security Research</span><span class="sep">✸</span>
      <span>Bug Bounty Hunting</span><span class="sep">✸</span>
      <span>CTF Player</span><span class="sep">✸</span>
      <span>Penetration Testing</span><span class="sep">✸</span>
      <span>Vulnerability Assessment</span><span class="sep">✸</span>
      <span>Security Research</span><span class="sep">✸</span>
      <span>Bug Bounty Hunting</span><span class="sep">✸</span>
      <span>CTF Player</span><span class="sep">✸</span>
    </div>
  </div>

  <!-- About Section  -->
  <section id="about" class="section-block">
    <div class="container">
      <div class="row align-items-center g-5">
        <div class="col-12 col-md-4" data-animate="fade-right">
          <div class="about-photo-wrap">
            <div class="about-img">
              <img src="./assets/image/topu-portfolio.png" alt="" />
            </div>
          </div>
        </div>
        <div class="col-12 col-md-8" data-animate="fade-left">
          <span class="section-label">Biography</span>
          <h2 class="section-heading">Breaking systems to <em>secure</em> them.</h2>
          <div class="section-body">
            <p>I am a High School Student based in Bangladesh with a deep passion for Cybersecurity and Information Security. Unlike traditional developers, my focus lies in understanding how systems break to help secure them better.</p>
            <p>I founded and maintain <strong>Bug Mohol</strong>, a platform dedicated to demystifying cybersecurity. My mission is to bridge the gap between complex security concepts and the general public through educational content. Currently, I am actively studying Penetration Testing and Network Security.</p>
          </div>
          
          <div class="stats-row">
            <div class="stat-item">
              <span class="stat-num">2<span class="stat-unit">+</span></span>
              <span class="stat-label">Years Exp.</span>
            </div>
            <div class="stat-div"></div>
            <div class="stat-item">
              <span class="stat-num">10<span class="stat-unit">+</span></span>
              <span class="stat-label">CTFs Played</span>
            </div>
            <div class="stat-div"></div>
            <div class="stat-item">
              <span class="stat-num">50<span class="stat-unit">+</span></span>
              <span class="stat-label">Bugs Found</span>
            </div>
          </div>
          
          <a href="#contact" class="btn-inline-arrow">Start a conversation <i class="bi bi-arrow-right"></i></a>
        </div>
      </div>
    </div>
  </section>

  <!-- Experience -->
  <section id="experience" class="section-block">
    <div class="container">
      <span class="section-label" data-animate="fade-up">Capabilities</span>
      <h2 class="section-heading" data-animate="fade-up" style="--d: 0.1s">My Arsenal</h2>
      
      <div class="row g-4 mt-4">
        <div class="col-12 col-md-6" data-animate="slide-up" style="--d: 0.2s">
          <div class="skill-group-card">
            <div class="skill-group-title"><i class="bi bi-code-square"></i> Core Concepts & Languages</div>
            <div class="skill-tags">
              <span class="skill-tag">Python</span>
              <span class="skill-tag">Bash Scripting</span>
              <span class="skill-tag">Linux Admin</span>
              <span class="skill-tag">Networking</span>
              <span class="skill-tag">OWASP Top 10</span>
              <span class="skill-tag">Active Directory</span>
              <span class="skill-tag">Cryptography</span>
              <span class="skill-tag">C/C++</span>
            </div>
          </div>
        </div>
        <div class="col-12 col-md-6" data-animate="slide-up" style="--d: 0.3s">
          <div class="skill-group-card">
            <div class="skill-group-title"><i class="bi bi-terminal"></i> Security Tools</div>
            <div class="skill-tags">
              <span class="skill-tag">Burp Suite</span>
              <span class="skill-tag">Nmap</span>
              <span class="skill-tag">Metasploit</span>
              <span class="skill-tag">Wireshark</span>
              <span class="skill-tag">Nessus</span>
              <span class="skill-tag">Ghidra</span>
              <span class="skill-tag">Aircrack-ng</span>
              <span class="skill-tag">Zap Proxy</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Achievements Section -->
  <section id="achievements" class="section-block">
    <div class="container">
      <span class="section-label" data-animate="fade-up">Milestones</span>
      <h2 class="section-heading" data-animate="fade-up" style="--d: 0.1s">Achievements</h2>
      <div class="achievements__cards mt-5 stagger-children" data-animate="fade-up" style="--d: 0.2s">
        <article class="ach-card">
          <i class="bi bi-trophy"></i>
          <h4>Bug Bounty</h4>
          <small>Hall of Fame (Learning)</small>
        </article>
        <article class="ach-card">
          <i class="bi bi-flag"></i>
          <h4>CTF Player</h4>
          <small>Ranked in TryHackMe</small>
        </article>
        <article class="ach-card">
          <i class="bi bi-shield-check"></i>
          <h4>Bug Mohol</h4>
          <small>Founder & Educator</small>
        </article>
      </div>
    </div>
  </section>

  <!-- Certifications -->
  <section id="portfolio" class="section-block">
    <div class="container">
      <span class="section-label" data-animate="fade-up">Credentials</span>
      <h2 class="section-heading" data-animate="fade-up" style="--d: 0.1s">Certifications</h2>
      <div class="row g-4 mt-4">
        <div class="col-12 col-md-6 col-lg-4" data-animate="slide-up" style="--d: 0.2s">
          <div class="cert-card">
            <div class="cert-img">
              <img src="./assets/image/portfolio/Hour Of Code certifi 1 .jpg" alt="" />
            </div>
            <div class="cert-name">Hour of Code - Dance Party (2024)</div>
            <div class="cert-btns">
              <a href="#" class="cert-btn-outline" target="_blank">Verify</a>
              <a href="#" class="cert-btn-solid" onclick="viewCertificate(this, event)" data-src="./assets/image/portfolio/Hour Of Code certifi 1 .jpg">View</a>
            </div>
          </div>
        </div>
        <div class="col-12 col-md-6 col-lg-4" data-animate="slide-up" style="--d: 0.3s">
          <div class="cert-card">
            <div class="cert-img">
              <img src="./assets/image/portfolio/Hour of Code certifi 2.jpg" alt="" />
            </div>
            <div class="cert-name">Hour of Code - Frozen (Anna and Elsa)</div>
            <div class="cert-btns">
              <a href="#" class="cert-btn-outline" target="_blank">Verify</a>
              <a href="#" class="cert-btn-solid" onclick="viewCertificate(this, event)" data-src="./assets/image/portfolio/Hour of Code certifi 2.jpg">View</a>
            </div>
          </div>
        </div>
        <div class="col-12 col-md-6 col-lg-4" data-animate="slide-up" style="--d: 0.4s">
          <div class="cert-card">
            <div class="cert-img">
              <img src="./assets/image/portfolio/pimg-03.jpg" alt="" />
            </div>
            <div class="cert-name">CompTIA Security+ (SY0-601)</div>
            <div class="cert-btns">
              <a href="#" class="cert-btn-outline" target="_blank">Verify</a>
              <a href="#" class="cert-btn-solid" onclick="viewCertificate(this, event)" data-src="./assets/image/portfolio/pimg-03.jpg">View</a>
            </div>
          </div>
        </div>
        <div class="col-12 col-md-6 col-lg-4" data-animate="slide-up" style="--d: 0.5s">
          <div class="cert-card">
            <div class="cert-img">
              <img src="./assets/image/portfolio/pimg-04.jpg" alt="" />
            </div>
            <div class="cert-name">Cisco Certified Network Associate (CCNA)</div>
            <div class="cert-btns">
              <a href="#" class="cert-btn-outline" target="_blank">Verify</a>
              <a href="#" class="cert-btn-solid" onclick="viewCertificate(this, event)" data-src="./assets/image/portfolio/pimg-04.jpg">View</a>
            </div>
          </div>
        </div>
        <div class="col-12 col-md-6 col-lg-4" data-animate="slide-up" style="--d: 0.6s">
          <div class="cert-card">
            <div class="cert-img">
              <img src="./assets/image/portfolio/pimg-05.jpg" alt="" />
            </div>
            <div class="cert-name">Burp Suite Certified Practitioner</div>
            <div class="cert-btns">
              <a href="#" class="cert-btn-outline" target="_blank">Verify</a>
              <a href="#" class="cert-btn-solid" onclick="viewCertificate(this, event)" data-src="./assets/image/portfolio/pimg-05.jpg">View</a>
            </div>
          </div>
        </div>
        <div class="col-12 col-md-6 col-lg-4" data-animate="slide-up" style="--d: 0.7s">
          <div class="cert-card">
            <div class="cert-img">
              <img src="./assets/image/portfolio/pimg-06.jpg" alt="" />
            </div>
            <div class="cert-name">eLearnSecurity Junior Penetration Tester (eJPT)</div>
            <div class="cert-btns">
              <a href="#" class="cert-btn-outline" target="_blank">Verify</a>
              <a href="#" class="cert-btn-solid" onclick="viewCertificate(this, event)" data-src="./assets/image/portfolio/pimg-06.jpg">View</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Services  -->
  <section id="services" class="section-block">
    <div class="container">
      <span class="section-label" data-animate="fade-up">Offerings</span>
      <h2 class="section-heading" data-animate="fade-up" style="--d: 0.1s">Services</h2>
      <div class="row g-4 mt-4">
        <div class="col-12 col-md-4" data-animate="slide-up" style="--d: 0.2s">
          <div class="svc-card">
            <i class="bi bi-shield-lock svc-icon"></i>
            <h3 class="svc-title">Penetration Testing</h3>
            <ul class="svc-list">
              <li>Web Application Security</li>
              <li>Network Vulnerability Scan</li>
              <li>Wireless Network Security</li>
              <li>Social Engineering Tests</li>
              <li>Security Auditing</li>
            </ul>
          </div>
        </div>
        <div class="col-12 col-md-4" data-animate="slide-up" style="--d: 0.3s">
          <div class="svc-card">
            <i class="bi bi-search svc-icon"></i>
            <h3 class="svc-title">Vulnerability Assessment</h3>
            <ul class="svc-list">
              <li>Identifying Weaknesses</li>
              <li>Risk Assessment</li>
              <li>Compliance Checking</li>
              <li>Patch Management</li>
              <li>Threat Modeling</li>
            </ul>
          </div>
        </div>
        <div class="col-12 col-md-4" data-animate="slide-up" style="--d: 0.4s">
          <div class="svc-card">
            <i class="bi bi-bug svc-icon"></i>
            <h3 class="svc-title">Security Research</h3>
            <ul class="svc-list">
              <li>Exploit Development</li>
              <li>Zero-Day Analysis</li>
              <li>Tool Development</li>
              <li>OSINT</li>
              <li>Bug Bounty Hunting</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Latest Articles -->
  <section id="latest-articles" class="section-block">
    <div class="container">
      <div class="section-header-row" data-animate="fade-up">
        <div>
          <span class="section-label">Insights</span>
          <h2 class="section-heading mb-0">Latest Articles</h2>
        </div>
        <a href="blog.html" class="view-all-link">View all <i class="bi bi-arrow-right"></i></a>
      </div>
      <div class="row g-4">
        <div class="col-12 col-md-4" data-animate="fade-up" style="--d: 0.2s">
          <div class="blog-preview-card">
            <div class="blog-preview-content">
              <span class="category-badge-sm ctf">CTF Writeup</span>
              <h3>How I Solved TryHackMe's Advanced Web Challenge</h3>
              <p>A detailed walkthrough of exploiting SQL injection and privilege escalation in a complex web environment.</p>
              <a href="blog.html" class="read-more-link">Read More <i class="bi bi-arrow-right"></i></a>
            </div>
          </div>
        </div>
        <div class="col-12 col-md-4" data-animate="fade-up" style="--d: 0.3s">
          <div class="blog-preview-card">
            <div class="blog-preview-content">
              <span class="category-badge-sm bugbounty">বাগ বাউন্টি</span>
              <h3>আমার প্রথম বাগ বাউন্টি অভিজ্ঞতা</h3>
              <p>কিভাবে আমি একটি জনপ্রিয় ওয়েবসাইটে XSS দুর্বলতা খুঁজে পেয়েছি এবং আমার প্রথম বাগ বাউন্টি পুরস্কার জিতেছি তার গল্প।</p>
              <a href="blog.html" class="read-more-link">Read More <i class="bi bi-arrow-right"></i></a>
            </div>
          </div>
        </div>
        <div class="col-12 col-md-4" data-animate="fade-up" style="--d: 0.4s">
          <div class="blog-preview-card">
            <div class="blog-preview-content">
              <span class="category-badge-sm tutorial">টিউটোরিয়াল</span>
              <h3>পেনিট্রেশন টেস্টিং ল্যাব সেটআপ</h3>
              <p>VirtualBox এবং Kali Linux দিয়ে নিজের হ্যাকিং ল্যাব তৈরির সম্পূর্ণ গাইড, একেবারে শূন্য থেকে শুরু করার জন্য।</p>
              <a href="blog.html" class="read-more-link">Read More <i class="bi bi-arrow-right"></i></a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact  -->
  <section id="contact" class="section-block">
    <div class="container">
      <span class="section-label" data-animate="fade-up">Connect</span>
      <h2 class="section-heading" data-animate="fade-up" style="--d: 0.1s">Get in Touch</h2>
      <div class="contact-grid mt-5" data-animate="fade-up" style="--d: 0.2s">
        <div class="contact-info-block">
          <h3>Let's start a project together.</h3>
          <p class="text-secondary mb-4" style="color: var(--color-light)!important;">Feel free to reach out for collaborations, freelance projects, or just a friendly chat.</p>
          
          <a href="mailto:topu7252@gmail.com" class="contact-detail">
            <i class="bi bi-envelope"></i>
            <div class="contact-detail-body">
              <small>Email</small>
              <span>topu7252@gmail.com</span>
            </div>
          </a>
          <a href="https://t.me/anonymousnexus" class="contact-detail">
            <i class="bi bi-telegram"></i>
            <div class="contact-detail-body">
              <small>Telegram</small>
              <span>@anonymousnexus</span>
            </div>
          </a>
          <a href="https://wa.me/+8801824989454" class="contact-detail">
            <i class="bi bi-whatsapp"></i>
            <div class="contact-detail-body">
              <small>WhatsApp</small>
              <span>+8801824989454</span>
            </div>
          </a>
        </div>
        <div class="contact-form-block my-contact-form">
          <form action="https://formsubmit.co/topu7252@gmail.com" method="POST" id="contact-form">
            <div>
              <input type="text" id="name" name="name" placeholder="Name" required />
            </div>
            <div>
              <input type="email" name="email" id="email" placeholder="Email" required />
            </div>
            <div>
              <textarea name="message" id="message" placeholder="Message" required></textarea>
            </div>
            <input type="hidden" name="_captcha" value="false" />
            <input type="hidden" name="_template" value="table" />
            <button class="my-contact-form-btn" type="submit">
              Send Message
            </button>
          </form>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer  -->
  <footer id="footer" class="jg-footer">
    <div class="jg-footer__body">
      <div class="container">
        <div class="row align-items-center py-4">
          <div class="col-12 col-md-7">
            <div class="jg-footer__logo">Toufique Zaman Topu</div>
            <div class="jg-footer__meta mt-2">
              <span>Cybersecurity Researcher</span>
              <span class="jg-footer__meta-sep">&#x2016;</span>
              <span>Developer &amp; Founder, Bug Mohol</span>
            </div>
            <div class="jg-footer__copy mt-1">
              &copy;<span id="currentYear">2026</span> Toufique Zaman Topu &mdash; All Rights Reserved.
            </div>
          </div>
          <div class="col-12 col-md-5 text-md-end mt-4 mt-md-0">
            <div class="jg-footer__follow-label">Follow Me</div>
            <div class="jg-footer__socials">
              <a href="https://www.facebook.com/zamantopu.official/" target="_blank" title="Facebook"><i class="bi bi-facebook"></i></a>
              <a href="https://www.instagram.com/zamantopu.official/" target="_blank" title="Instagram"><i class="bi bi-instagram"></i></a>
              <a href="https://www.linkedin.com/in/zaman-topu/" target="_blank" title="LinkedIn"><i class="bi bi-linkedin"></i></a>
              <a href="https://tryhackme.com/p/zamantopu" target="_blank" title="TryHackMe"><i class="bi bi-terminal-fill"></i></a>
              <a href="https://github.com/zaman-topu" target="_blank" title="GitHub"><i class="bi bi-github"></i></a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="jg-footer__navbar">
      <div class="container">
        <div class="jg-footer__navlinks">
          <a href="#about">About Me</a>
          <a href="#contact">Contact</a>
          <a href="#experience">Experience</a>
          <a href="#portfolio">Certifications</a>
          <a href="#achievements">Achievements</a>
          <a href="blog.html">Blog</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Certificate Modal -->
  <div class="modal fade" id="certificateModal" tabindex="-1" aria-labelledby="certificateModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
      <div class="modal-content" style="background: var(--color-surface); border: 1px solid var(--color-border);">
        <div class="modal-header border-0">
          <h5 class="modal-title text-white" id="certificateModalLabel">Certificate View</h5>
          <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body text-center">
          <img src="" id="certificateImage" class="img-fluid rounded" alt="Certificate Preview">
        </div>
        <div class="modal-footer border-0">
          <a href="#" id="downloadCertificateBtn" class="btn btn-cta-primary" download>Download</a>
          <button type="button" class="btn btn-cta-ghost" data-bs-dismiss="modal">Close</button>
        </div>
      </div>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-bundle.min.js"></script>
  <script src="./main.js"></script>
</body>
</html>"""

with open(r"d:\from c\topu's portfolio\index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
