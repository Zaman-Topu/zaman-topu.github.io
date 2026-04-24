# 📝 নতুন ব্লগ পোস্ট লেখার সম্পূর্ণ গাইড

## 🎯 দুই ধরনের পোস্ট

### ১. ব্লগ লিস্টে শুধু কার্ড যুক্ত করা (সহজ)

- `blog-post-template.html` ব্যবহার করুন
- শুধু `blog.html` এ যুক্ত করুন
- পুরো পোস্ট লিখার দরকার নেই

### ২. সম্পূর্ণ ব্লগ পোস্ট (Permalink সহ)

- `NEW-POST-TEMPLATE.html` ব্যবহার করুন
- আলাদা পেজ তৈরি হবে
- SEO এবং Share করার সুবিধা
- **এটাই রেকমেন্ডেড!**

---

## 🚀 সম্পূর্ণ পোস্ট তৈরির ধাপ

### ধাপ ১: Permalink ঠিক করুন

**Permalink** = আপনার পোস্টের URL

উদাহরণ:

- ভালো: `my-first-ctf-writeup`
- ভালো: `sql-injection-tutorial`
- খারাপ: `My First CTF` (স্পেস নয়)
- খারাপ: `আমার_প্রথম_পোস্ট` (বাংলা নয়)

**নিয়ম:**

- শুধু ছোট হাতের ইংরেজি অক্ষর (a-z)
- স্পেসের জায়গায় হাইফেন (-)
- সংক্ষিপ্ত এবং বোঝা যায় এমন

---

### ধাপ ২: SEO তথ্য ভরাট করুন

#### A. SEO Title (৬০ অক্ষরের মধ্যে)

Google এ যা দেখাবে।

✅ ভালো:

```
How I Solved TryHackMe's Advanced Web Challenge
```

❌ খারাপ:

```
My Amazing CTF Journey That Changed My Life Forever And Ever
```

#### B. SEO Description (১৬০ অক্ষরের মধ্যে)

Google এ Title এর নিচে যা দেখাবে।

✅ ভালো:

```
A detailed walkthrough of exploiting SQL injection and privilege escalation in a realistic web application environment on TryHackMe.
```

#### C. SEO Keywords (৫-১০টি)

Google এর জন্য। কমা দিয়ে আলাদা করুন।

উদাহরণ:

```
CTF, TryHackMe, SQL Injection, Privilege Escalation, Web Security
```

---

### ধাপ ৩: Category বেছে নিন

| Category    | ব্যবহার করুন যদি  | Badge Color |
| ----------- | ----------------- | ----------- |
| `ctf`       | CTF writeup হয়   | 🔴 লাল      |
| `bugbounty` | Bug bounty হয়    | 🔵 নীল      |
| `tutorial`  | শেখানোর পোস্ট হয় | 🟡 হলুদ     |
| `news`      | Security news হয় | 🟣 বেগুনি   |

---

### ধাপ ৪: পোস্ট লিখুন

#### HTML Tags যা ব্যবহার করবেন:

**বড় শিরোনাম:**

```html
<h2>আপনার শিরোনাম</h2>
```

**প্যারাগ্রাফ:**

```html
<p>আপনার লেখা...</p>
```

**বুলেট লিস্ট:**

```html
<ul>
  <li>প্রথম পয়েন্ট</li>
  <li>দ্বিতীয় পয়েন্ট</li>
</ul>
```

**নাম্বার লিস্ট:**

```html
<ol>
  <li>প্রথম ধাপ</li>
  <li>দ্বিতীয় ধাপ</li>
</ol>
```

**কোড দেখানো:**

```html
<div class="code-block">
  <pre><code>nmap -sV target-ip</code></pre>
</div>
```

**Info Box (নীল):**

```html
<div class="alert-box info">
  <i class="bi bi-info-circle"></i>
  <div><strong>Pro Tip:</strong> আপনার টিপস</div>
</div>
```

**Success Box (সবুজ):**

```html
<div class="alert-box success">
  <i class="bi bi-check-circle"></i>
  <div><strong>Success!</strong> আপনার মেসেজ</div>
</div>
```

**Warning Box (হলুদ):**

```html
<div class="alert-box warning">
  <i class="bi bi-exclamation-triangle"></i>
  <div><strong>Warning!</strong> সতর্কতা</div>
</div>
```

---

### ধাপ ৫: ফাইল সেভ করুন

1. **File → Save As**
2. **File name:** আপনার-permalink.html
   - উদাহরণ: `my-first-ctf.html`
3. **Save in:** `blog/` ফোল্ডার
   - পুরো পাথ: `c:/Users/atonm/Downloads/topu's portfolio/blog/`
4. **Save**

---

### ধাপ ৬: blog.html এ লিংক যুক্ত করুন

1. `blog.html` খুলুন
2. একটি blog card এর "Read More" লিংক খুঁজুন:

```html
<a href="#" class="read-more-btn"></a>
```

3. `#` এর জায়গায় আপনার ফাইলের পাথ দিন:

```html
<a href="blog/my-first-ctf.html" class="read-more-btn"></a>
```

4. সেভ করুন!

---

## ✅ Checklist

পোস্ট পাবলিশের আগে চেক করুন:

- [ ] Permalink সঠিক আছে (ছোট হাতের অক্ষর, হাইফেন)
- [ ] SEO Title ৬০ অক্ষরের মধ্যে
- [ ] SEO Description ১৬০ অক্ষরের মধ্যে
- [ ] Keywords দিয়েছি
- [ ] Category সঠিক
- [ ] তারিখ দিয়েছি
- [ ] Reading time দিয়েছি
- [ ] পোস্ট লিখেছি
- [ ] `blog/` ফোল্ডারে সেভ করেছি
- [ ] `blog.html` এ লিংক যুক্ত করেছি

---

## 📁 ফাইল স্ট্রাকচার

```
topu's portfolio/
├── blog.html (মূল ব্লগ লিস্ট)
├── blog/
│   ├── my-first-ctf.html
│   ├── sql-injection-tutorial.html
│   └── tryhackme-advanced-web-challenge.html (উদাহরণ)
└── NEW-POST-TEMPLATE.html (টেম্পলেট)
```

---

## 🎓 উদাহরণ দেখুন

`blog/tryhackme-advanced-web-challenge.html` ফাইলটি খুলে দেখুন - এটি একটি সম্পূর্ণ উদাহরণ পোস্ট!

এখন আপনি সহজেই সম্পূর্ণ ব্লগ পোস্ট তৈরি করতে পারবেন! 🎉
