/**
 * blog-posts-data.js  —  Post Registry
 * ─────────────────────────────────────
 * Add new posts at the TOP of the array (newest first).
 * Fields:
 *   file      — path relative to index.html
 *   title     — post title
 *   excerpt   — short description (1-2 sentences)
 *   category  — 'ctf' | 'bugbounty' | 'tutorial' | 'research'
 *   label     — display name for the badge
 *   date      — formatted date string
 *   readTime  — e.g. '5 min read' or '৫ মিনিট'
 *   lang      — 'en' | 'bn'
 */
window.BLOG_POSTS = [
  {
    file:     'blog/amar-prothom-bug-bounty.html',
    title:    'আমার প্রথম বাগ বাউন্টি অভিজ্ঞতা',
    excerpt:  'কিভাবে আমি একটি জনপ্রিয় ওয়েবসাইটে XSS দুর্বলতা খুঁজে পেয়েছি এবং আমার প্রথম বাগ বাউন্টি পুরস্কার জিতেছি তার গল্প।',
    category: 'bugbounty',
    label:    'বাগ বাউন্টি',
    date:     '৮ ফেব্রুয়ারি, ২০২৬',
    readTime: '৮ মিনিট',
    lang:     'bn',
  },
  {
    file:     'blog/tryhackme-advanced-web-challenge.html',
    title:    "How I Solved TryHackMe's Advanced Web Challenge",
    excerpt:  'A detailed walkthrough of exploiting SQL injection and privilege escalation in a complex web environment on TryHackMe.',
    category: 'ctf',
    label:    'CTF Writeup',
    date:     'February 10, 2026',
    readTime: '5 min read',
    lang:     'en',
  },
  {
    file:     'blog/penetration-testing-lab-setup.html',
    title:    'পেনিট্রেশন টেস্টিং ল্যাব সেটআপ',
    excerpt:  'VirtualBox এবং Kali Linux দিয়ে নিজের হ্যাকিং ল্যাব তৈরির সম্পূর্ণ গাইড, একেবারে শূন্য থেকে শুরু করার জন্য।',
    category: 'tutorial',
    label:    'টিউটোরিয়াল',
    date:     '১৫ ফেব্রুয়ারি, ২০২৬',
    readTime: '১০ মিনিট',
    lang:     'bn',
  },
];
