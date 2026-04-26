/**
 * latest-articles.js
 * Renders the Latest Articles grid from window.BLOG_POSTS[]
 * defined in blog-posts-data.js (must load first, no defer).
 */
(function () {
  'use strict';

  var CONTAINER_ID = 'latest-articles-grid';
  var MAX_POSTS = 3;

  function escHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function buildCard(post, delay) {
    var isBn = (post.lang === 'bn');
    var fontStyle = isBn ? "font-family:'Hind Siliguri','Noto Sans Bengali',sans-serif;" : '';
    var arrow = '<svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>';

    return '<div class="col-12 col-md-4" data-animate="fade-up" style="--d:' + delay + 's">'
      + '<div class="blog-preview-card">'
      + '<div class="blog-preview-content">'
      + '<span class="la-badge" style="' + fontStyle + '">' + escHtml(post.label) + '</span>'
      + '<h3 style="' + fontStyle + '">' + escHtml(post.title) + '</h3>'
      + '<p style="' + fontStyle + '">' + escHtml(post.excerpt) + '</p>'
      + '<div class="la-meta">'
      + '<span class="la-date" style="' + fontStyle + '">' + escHtml(post.date) + '</span>'
      + '<span class="la-sep">·</span>'
      + '<span class="la-read" style="' + fontStyle + '">' + escHtml(post.readTime) + '</span>'
      + '</div>'
      + '<a href="' + escHtml(post.file) + '" class="read-more-link" style="' + fontStyle + '">'
      + (isBn ? 'আরো পড়ুন' : 'Read More') + ' ' + arrow
      + '</a>'
      + '</div></div></div>';
  }

  function render() {
    var grid = document.getElementById(CONTAINER_ID);
    if (!grid) return;

    var posts = window.BLOG_POSTS;
    if (!posts || !Array.isArray(posts) || posts.length === 0) {
      grid.innerHTML = '<div class="col-12" style="text-align:center;padding:3rem 0;color:rgba(255,255,255,.25);font-family:var(--font-mono);font-size:.8rem;">No articles yet.</div>';
      return;
    }

    var delays = [0.05, 0.15, 0.25];
    var html = '';
    var count = Math.min(posts.length, MAX_POSTS);
    for (var i = 0; i < count; i++) {
      html += buildCard(posts[i], delays[i] || 0.1);
    }
    grid.innerHTML = html;

    // Hook into scroll-reveal observer if available
    setTimeout(function () {
      var obs = window._revealObserver;
      if (obs) {
        grid.querySelectorAll('[data-animate]').forEach(function (el) {
          obs.observe(el);
        });
      } else {
        // Fallback: just show them immediately
        grid.querySelectorAll('[data-animate]').forEach(function (el) {
          el.classList.add('is-visible');
        });
      }
    }, 50);
  }

  // Run as soon as DOM is ready — works whether deferred or not
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', render);
  } else {
    render();
  }

})();
