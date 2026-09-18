# -*- coding: utf-8 -*-
"""Kit comun pentru site-ul Caleidoscope Educational.ro (CSS, iconite, date, header/footer)."""

CSS = r"""
:root{
  --violet:#6D28D9; --violet-2:#7C3AED; --indigo:#4F46E5;
  --teal:#0EA5A4; --pink:#EC4899; --amber:#F59E0B; --lime:#84CC16;
  --ink:#101828; --ink-2:#1D2939; --muted:#667085; --line:#E7E4F5;
  --bg:#F8F7FF; --white:#fff;
  --grad:linear-gradient(135deg,#4F46E5 0%,#6D28D9 45%,#7C3AED 72%,#0EA5A4 130%);
  --radius:18px; --shadow:0 10px 30px rgba(16,24,40,.08); --shadow-lg:0 22px 60px rgba(76,29,149,.18);
  --grad-text:linear-gradient(90deg,#6D28D9,#0EA5A4);
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{
  font-family:"Segoe UI",Roboto,"Helvetica Neue",Arial,"Noto Sans",sans-serif;
  color:var(--ink);background:var(--white);line-height:1.6;
  -webkit-font-smoothing:antialiased;
}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
ul{list-style:none}
button{font:inherit;cursor:pointer;border:0;background:none;color:inherit}
input,select,textarea{font:inherit;color:inherit}
.wrap{width:min(1280px,92vw);margin:0 auto}
.grad-text{background:var(--grad-text);-webkit-background-clip:text;background-clip:text;color:transparent}
.eyebrow{font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;font-weight:700;color:var(--violet)}
.btn{display:inline-flex;align-items:center;gap:.55rem;padding:.72rem 1.15rem;border-radius:999px;font-weight:650;font-size:.95rem;transition:.22s transform,.22s box-shadow,.22s background}
.btn-primary{background:var(--grad);color:#fff;box-shadow:0 10px 22px rgba(109,40,217,.32)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 16px 30px rgba(109,40,217,.4)}
.btn-ghost{background:#fff;color:var(--violet);border:1.5px solid var(--line)}
.btn-ghost:hover{border-color:var(--violet);transform:translateY(-2px)}
.btn-white{background:#fff;color:var(--violet)}
.btn-white:hover{transform:translateY(-2px)}
.btn-sm{padding:.5rem .85rem;font-size:.85rem}

/* ---------- HEADER ---------- */
.hdr{position:sticky;top:0;z-index:60;background:rgba(255,255,255,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.hdr.scrolled{box-shadow:0 6px 24px rgba(16,24,40,.07)}
.hdr-in{display:flex;align-items:center;gap:1.2rem;height:76px}
.brand{display:flex;align-items:center;gap:.65rem;flex-shrink:0}
.brand-txt{display:flex;flex-direction:column;line-height:1.05}
.brand-name{font-weight:800;font-size:1.32rem;letter-spacing:-.02em}
.brand-name span{color:var(--violet)}
.brand-sub{font-size:.66rem;letter-spacing:.06em;color:var(--muted);font-weight:600}
.nav{display:flex;align-items:center;gap:.15rem;margin-left:auto}
.nav a{position:relative;padding:.55rem .8rem;border-radius:12px;font-weight:600;font-size:.94rem;color:var(--ink-2);transition:.2s}
.nav a:hover{color:var(--violet);background:#F4F1FF}
.nav a.active{color:var(--violet);background:#F1EDFF}
.drop{position:relative}
.drop-panel{position:absolute;top:115%;left:0;min-width:270px;background:#fff;border:1px solid var(--line);border-radius:16px;box-shadow:var(--shadow-lg);padding:.55rem;display:none;grid-template-columns:1fr;gap:.15rem;z-index:70}
.drop:hover .drop-panel{display:grid}
.drop-panel a{display:flex;gap:.6rem;align-items:flex-start;padding:.6rem .7rem;border-radius:12px;font-size:.9rem;font-weight:600}
.drop-panel a:hover{background:#F6F3FF}
.drop-panel a small{display:block;font-weight:500;color:var(--muted);font-size:.78rem}
.hdr-actions{display:flex;align-items:center;gap:.55rem;margin-left:.6rem}
.icon-btn{position:relative;width:42px;height:42px;border-radius:50%;display:grid;place-items:center;border:1.5px solid var(--line);transition:.2s}
.icon-btn:hover{border-color:var(--violet);background:#F6F3FF}
.cart-count{position:absolute;top:-4px;right:-4px;min-width:20px;height:20px;border-radius:999px;background:var(--pink);color:#fff;font-size:.7rem;font-weight:700;display:grid;place-items:center;padding:0 5px}
.nav-toggle{display:none;width:44px;height:44px;border-radius:12px;border:1.5px solid var(--line);place-items:center}

/* ---------- HERO ---------- */
.hero{position:relative;background:var(--grad);color:#fff;overflow:hidden;padding:3.4rem 0 3.2rem}
.hero:before,.hero:after{content:"";position:absolute;border-radius:50%;filter:blur(10px);opacity:.28;pointer-events:none}
.hero:before{width:520px;height:520px;background:radial-gradient(circle,#fff,transparent 65%);top:-190px;left:-120px}
.hero:after{width:620px;height:620px;background:radial-gradient(circle,#0EA5A4,transparent 62%);bottom:-330px;right:-140px;opacity:.35}
.hero-grid{position:relative;display:grid;grid-template-columns:1.65fr .85fr 1.05fr .42fr;gap:1.7rem;align-items:start}
.hero h1{font-size:clamp(2rem,3.1vw,3rem);line-height:1.1;font-weight:800;letter-spacing:-.02em;margin-top:1.4rem}
.hero p.lead{font-size:1.02rem;color:rgba(255,255,255,.9);max-width:44rem;margin-top:1rem}
.searchbar{display:flex;gap:.5rem;background:#fff;border-radius:999px;padding:.42rem;margin-top:1.6rem;max-width:640px;box-shadow:0 18px 40px rgba(16,24,40,.22)}
.searchbar input{flex:1;border:0;outline:0;padding:.7rem 1.1rem;font-size:.95rem;border-radius:999px;background:transparent}
.searchbar input::placeholder{color:#98A2B3}
.searchbar button{background:var(--grad);color:#fff;font-weight:700;border-radius:999px;padding:.75rem 1.5rem}
.searchbar button:hover{filter:brightness(1.07)}
.chips{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:1rem}
.chip{background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.32);color:#fff;padding:.34rem .85rem;border-radius:999px;font-size:.84rem;font-weight:600;backdrop-filter:blur(4px);transition:.2s}
.chip:hover{background:#fff;color:var(--violet)}
.badge-pill{display:inline-flex;align-items:center;gap:.5rem;background:rgba(255,255,255,.18);border:1px solid rgba(255,255,255,.35);padding:.42rem 1rem;border-radius:999px;font-weight:800;letter-spacing:.14em;font-size:.74rem;text-transform:uppercase;margin-top:1.5rem}
.dom-list{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.24);border-radius:20px;padding:1.1rem;backdrop-filter:blur(6px)}
.dom-list h3{font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;opacity:.85;margin-bottom:.7rem;font-weight:700}
.dom-list a{display:flex;align-items:center;justify-content:space-between;gap:.6rem;padding:.55rem .7rem;border-radius:12px;font-weight:650;font-size:.92rem;transition:.2s}
.dom-list a:hover{background:rgba(255,255,255,.2);transform:translateX(3px)}
.dom-list a span{font-size:.75rem;opacity:.75;font-weight:600}
.promo-card{background:#fff;color:var(--ink);border-radius:22px;padding:1.5rem;box-shadow:0 26px 55px rgba(23,12,58,.35)}
.promo-card h2{font-size:1.35rem;line-height:1.25;font-weight:800;letter-spacing:-.01em}
.promo-card p{color:var(--muted);font-size:.92rem;margin-top:.5rem}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:.6rem;margin-top:1.1rem}
.stat{background:#F7F5FF;border-radius:14px;padding:.7rem;text-align:center}
.stat b{display:block;font-size:1.22rem;color:var(--violet)}
.stat small{font-size:.7rem;color:var(--muted);font-weight:600}
.lang-col{display:grid;gap:.55rem}
.lang-col a{display:flex;align-items:center;gap:.45rem;background:rgba(255,255,255,.15);border:1px solid rgba(255,255,255,.3);border-radius:14px;padding:.6rem .5rem;font-weight:700;font-size:.85rem;justify-content:center;transition:.2s}
.lang-col a:hover{background:#fff;color:var(--violet);transform:translateY(-2px)}
.lang-col h3{font-size:.68rem;letter-spacing:.14em;text-transform:uppercase;opacity:.85;text-align:center;margin-bottom:.1rem;font-weight:700}

/* ---------- TRUST ---------- */
.trust{background:#fff;border-bottom:1px solid var(--line)}
.trust-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:1rem;padding:1.5rem 0}
.trust-item{display:flex;gap:.75rem;align-items:flex-start}
.trust-item svg{flex-shrink:0;color:var(--violet);margin-top:2px}
.trust-item b{display:block;font-size:.92rem}
.trust-item small{color:var(--muted);font-size:.8rem}

/* ---------- SECTIONS ---------- */
section{padding:4rem 0}
.sec-head{text-align:center;max-width:640px;margin:0 auto 2.4rem}
.sec-head h2{font-size:clamp(1.6rem,2.4vw,2.15rem);font-weight:800;letter-spacing:-.02em;margin-top:.4rem}
.sec-head p{color:var(--muted);margin-top:.6rem}

/* categories */
.cat-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:1rem}
.cat-card{background:#fff;border:1.5px solid var(--line);border-radius:var(--radius);padding:1.15rem 1rem;transition:.25s;display:flex;flex-direction:column;gap:.6rem;min-height:170px}
.cat-card:hover{transform:translateY(-6px);box-shadow:var(--shadow-lg);border-color:transparent}
.cat-ico{width:46px;height:46px;border-radius:14px;display:grid;place-items:center;color:#fff}
.cat-card h3{font-size:.98rem;font-weight:750;line-height:1.25}
.cat-card p{font-size:.8rem;color:var(--muted);margin-top:-.3rem}
.cat-card .go{margin-top:auto;font-size:.84rem;font-weight:700;color:var(--violet);display:flex;align-items:center;gap:.35rem}
.cat-card:hover .go svg{transform:translateX(3px)}
.cat-card .go svg{transition:.2s}

/* products */
.prod-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1.2rem}
.card{background:#fff;border:1.5px solid var(--line);border-radius:var(--radius);overflow:hidden;display:flex;flex-direction:column;transition:.25s}
.card:hover{transform:translateY(-5px);box-shadow:var(--shadow-lg);border-color:transparent}
.cover{height:130px;display:grid;place-items:center;position:relative;color:#fff}
.cover .cico{width:56px;height:56px;border-radius:16px;background:rgba(255,255,255,.22);display:grid;place-items:center;backdrop-filter:blur(3px)}
.cover .tag{position:absolute;top:.6rem;left:.6rem;background:rgba(255,255,255,.92);color:var(--ink);font-size:.68rem;font-weight:800;padding:.22rem .55rem;border-radius:999px;letter-spacing:.04em}
.cover .fmt{position:absolute;bottom:.6rem;right:.6rem;background:rgba(16,24,40,.55);font-size:.7rem;font-weight:700;padding:.2rem .5rem;border-radius:8px;letter-spacing:.04em}
.card-body{padding:1rem;display:flex;flex-direction:column;gap:.45rem;flex:1}
.card-body .cat{font-size:.72rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--violet)}
.card-body h3{font-size:.98rem;font-weight:700;line-height:1.3}
.card-body .meta{font-size:.8rem;color:var(--muted);display:flex;flex-wrap:wrap;gap:.5rem}
.card-body .meta span{display:inline-flex;align-items:center;gap:.25rem}
.card-foot{margin-top:auto;padding:1rem;border-top:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;gap:.5rem}
.price{font-weight:800;font-size:1.12rem}
.price small{display:block;font-size:.72rem;color:var(--muted);font-weight:600;text-decoration:line-through}
.price-note{font-size:.7rem;color:var(--muted);font-weight:600}
.add{display:inline-flex;align-items:center;gap:.35rem;background:var(--violet);color:#fff;font-weight:700;font-size:.85rem;padding:.55rem .9rem;border-radius:999px;transition:.2s}
.add:hover{background:var(--indigo);transform:translateY(-2px)}
.rating{display:flex;align-items:center;gap:.25rem;font-size:.8rem;color:var(--amber);font-weight:700}
.rating small{color:var(--muted);font-weight:600}

/* steps */
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4rem}
.step{background:#fff;border:1.5px solid var(--line);border-radius:var(--radius);padding:1.5rem;position:relative}
.step .num{width:44px;height:44px;border-radius:14px;background:var(--grad);color:#fff;display:grid;place-items:center;font-weight:800;margin-bottom:.9rem}
.step h3{font-size:1.05rem;font-weight:750}
.step p{color:var(--muted);font-size:.9rem;margin-top:.4rem}

/* cta band */
.cta-band{background:var(--grad);color:#fff;border-radius:26px;padding:2.6rem;text-align:center;position:relative;overflow:hidden;margin:1rem 0 0}
.cta-band h2{font-size:1.7rem;font-weight:800}
.cta-band p{opacity:.9;margin:.6rem auto 1.3rem;max-width:560px}
.cta-band .btn-white{padding:.85rem 1.6rem}
.cta-band .form{display:flex;gap:.5rem;max-width:520px;margin:0 auto;background:#fff;padding:.4rem;border-radius:999px}
.cta-band .form input{flex:1;border:0;outline:0;padding:.7rem 1rem;border-radius:999px}
.cta-band .form button{background:var(--grad);color:#fff;font-weight:700;border-radius:999px;padding:.7rem 1.4rem}
.cta-band small{display:block;opacity:.8;font-size:.78rem;margin-top:.8rem}

/* ---------- SHOP LAYOUT ---------- */
.shop{display:grid;grid-template-columns:260px 1fr;gap:1.8rem;align-items:start}
.filters{background:#fff;border:1.5px solid var(--line);border-radius:var(--radius);padding:1.2rem;position:sticky;top:96px}
.filters h3{font-size:1rem;font-weight:750;margin-bottom:.8rem}
.fgroup{border-top:1px solid var(--line);padding:.9rem 0}
.fgroup:first-of-type{border-top:0;padding-top:0}
.fgroup h4{font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:.6rem;font-weight:800}
.fgroup label{display:flex;align-items:center;gap:.55rem;font-size:.9rem;padding:.25rem 0;cursor:pointer}
.fgroup input[type=checkbox]{accent-color:var(--violet);width:16px;height:16px}
.fgroup label span{color:var(--muted);font-size:.8rem;margin-left:auto}
.shop-bar{display:flex;align-items:center;gap:1rem;flex-wrap:wrap;margin-bottom:1.2rem;background:#fff;border:1.5px solid var(--line);border-radius:14px;padding:.75rem 1rem}
.shop-bar .count{font-weight:700;font-size:.92rem}
.shop-bar .count span{color:var(--muted);font-weight:600}
.shop-bar select{margin-left:auto;border:1.5px solid var(--line);border-radius:999px;padding:.5rem 1rem;outline:0;background:#fff}
.empty{display:none;text-align:center;padding:3rem;color:var(--muted)}

/* ---------- CONTENT PAGES ---------- */
.page-head{background:var(--bg);border-bottom:1px solid var(--line);padding:2.6rem 0}
.page-head h1{font-size:clamp(1.7rem,2.6vw,2.3rem);font-weight:800;letter-spacing:-.02em;margin-top:.4rem}
.page-head p{color:var(--muted);max-width:640px;margin-top:.5rem}
.breadcrumb{font-size:.82rem;color:var(--muted);display:flex;gap:.4rem;align-items:center}
.breadcrumb a:hover{color:var(--violet)}
.prose{max-width:760px}
.prose h2{font-size:1.35rem;font-weight:800;margin:2rem 0 .7rem}
.prose h3{font-size:1.08rem;font-weight:750;margin:1.4rem 0 .5rem}
.prose p{color:var(--ink-2);margin-bottom:.9rem}
.prose ul{display:grid;gap:.5rem;margin:.6rem 0 1.1rem}
.prose li{display:flex;gap:.55rem;color:var(--ink-2)}
.prose li svg{flex-shrink:0;margin-top:4px;color:var(--teal)}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:1.6rem}
.grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2rem}
.grid-4{display:grid;grid-template-columns:repeat(4,1fr);gap:1.2rem}
.tile{background:#fff;border:1.5px solid var(--line);border-radius:var(--radius);padding:1.4rem}
.tile .ico{width:46px;height:46px;border-radius:14px;display:grid;place-items:center;color:#fff;margin-bottom:.9rem}
.tile h3{font-size:1.02rem;font-weight:750}
.tile p{color:var(--muted);font-size:.9rem;margin-top:.35rem}
.tile ul{margin-top:.7rem;display:grid;gap:.35rem}
.tile li{font-size:.86rem;color:var(--ink-2);display:flex;gap:.4rem}
.tile li:before{content:"✓";color:var(--teal);font-weight:800}

/* blog */
.post{background:#fff;border:1.5px solid var(--line);border-radius:var(--radius);overflow:hidden;transition:.25s;display:flex;flex-direction:column}
.post:hover{transform:translateY(-5px);box-shadow:var(--shadow-lg)}
.post .thumb{height:140px;display:grid;place-items:center;color:#fff;font-weight:800;font-size:1.6rem;letter-spacing:.06em}
.post .body{padding:1.1rem;display:flex;flex-direction:column;gap:.5rem;flex:1}
.post .body .tag{font-size:.7rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--violet)}
.post h3{font-size:1.02rem;font-weight:750;line-height:1.3}
.post p{font-size:.88rem;color:var(--muted)}
.post .foot{margin-top:auto;font-size:.8rem;color:var(--muted);display:flex;justify-content:space-between;border-top:1px solid var(--line);padding-top:.7rem}

/* contact */
.contact-grid{display:grid;grid-template-columns:1fr 1fr;gap:2rem;align-items:start}
.form-card{background:#fff;border:1.5px solid var(--line);border-radius:var(--radius);padding:1.6rem}
.field{display:grid;gap:.35rem;margin-bottom:1rem}
.field label{font-size:.86rem;font-weight:700}
.field input,.field textarea,.field select{border:1.5px solid var(--line);border-radius:12px;padding:.7rem .9rem;outline:0;transition:.2s;width:100%}
.field input:focus,.field textarea:focus,.field select:focus{border-color:var(--violet);box-shadow:0 0 0 4px rgba(109,40,217,.1)}
.field textarea{min-height:130px;resize:vertical}
.consent{display:flex;gap:.6rem;font-size:.82rem;color:var(--muted);align-items:flex-start;margin:.4rem 0 1rem}
.consent input{margin-top:3px;accent-color:var(--violet)}
.info-list{display:grid;gap:.9rem;margin-top:1.2rem}
.info-item{display:flex;gap:.8rem;align-items:flex-start}
.info-item .ico{width:42px;height:42px;border-radius:12px;background:#F4F1FF;color:var(--violet);display:grid;place-items:center;flex-shrink:0}
.info-item b{display:block;font-size:.94rem}
.info-item span{font-size:.87rem;color:var(--muted)}
.faq details{border:1.5px solid var(--line);border-radius:14px;padding:1rem 1.1rem;margin-bottom:.7rem;background:#fff}
.faq summary{font-weight:700;cursor:pointer;list-style:none;display:flex;justify-content:space-between;gap:1rem}
.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:"+";color:var(--violet);font-weight:800}
.faq details[open] summary:after{content:"–"}
.faq p{color:var(--muted);font-size:.9rem;margin-top:.7rem}

/* ---------- FOOTER ---------- */
.ftr{background:#150F2B;color:#C7C2E0;padding:3.2rem 0 1.2rem;margin-top:2rem}
.ftr-top{display:grid;grid-template-columns:1.4fr 1fr 1fr 1.2fr;gap:2rem}
.ftr h4{color:#fff;font-size:.95rem;margin-bottom:.9rem;font-weight:750}
.ftr a{color:#C7C2E0;font-size:.9rem;transition:.2s}
.ftr a:hover{color:#fff;padding-left:3px}
.ftr ul{display:grid;gap:.45rem}
.ftr-logo{display:flex;align-items:center;gap:.6rem;margin-bottom:.9rem}
.ftr-logo .brand-name{color:#fff}
.ftr-logo .brand-name span{color:#A78BFA}
.ftr-tag{font-size:.9rem;line-height:1.6}
.ftr .social{display:flex;gap:.5rem;margin-top:1rem}
.ftr .social a{width:38px;height:38px;border-radius:50%;border:1px solid #332A57;display:grid;place-items:center}
.ftr .social a:hover{background:#6D28D9;border-color:#6D28D9;padding:0}
.ftr-btm{border-top:1px solid #2A2350;margin-top:2.2rem;padding-top:1.2rem;display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;font-size:.82rem;color:#9892B8}
.ftr-btm ul{display:flex;gap:1.1rem;flex-wrap:wrap}
.ftr .note{font-size:.78rem;color:#8B85AD;margin-top:.6rem}

/* ---------- MISC ---------- */
.cookie{position:fixed;bottom:1rem;left:1rem;right:1rem;max-width:520px;background:#fff;border:1.5px solid var(--line);border-radius:18px;box-shadow:var(--shadow-lg);padding:1.1rem;z-index:90;display:none;gap:.8rem}
.cookie.show{display:flex;flex-direction:column}
.cookie p{font-size:.86rem;color:var(--muted)}
.cookie .row{display:flex;gap:.6rem;margin-top:.4rem}
.toast{position:fixed;bottom:1.5rem;right:1.5rem;background:var(--ink);color:#fff;padding:.85rem 1.2rem;border-radius:14px;box-shadow:var(--shadow-lg);z-index:99;opacity:0;transform:translateY(12px);transition:.3s;pointer-events:none;font-size:.9rem}
.toast.show{opacity:1;transform:none}
.reveal{opacity:0;transform:translateY(14px);transition:.6s}
.reveal.in{opacity:1;transform:none}

/* ---------- WISHLIST / QTY / CHECKOUT / 404 ---------- */
.wish{position:absolute;top:.6rem;right:.6rem;width:34px;height:34px;border-radius:50%;background:rgba(255,255,255,.92);color:var(--ink);display:grid;place-items:center;transition:.2s;z-index:2}
.wish:hover{transform:scale(1.08);color:var(--pink)}
.wish.on{color:var(--pink)}
.wish.on svg{fill:var(--pink)}
.cover .fmt{bottom:.6rem;right:.6rem}
.cart-line{display:grid;grid-template-columns:1fr auto auto auto;gap:.8rem;align-items:center;padding:.8rem 0;border-bottom:1px solid var(--line)}
.cart-line .t{font-weight:650;font-size:.92rem;line-height:1.3}
.cart-line .t small{display:block;color:var(--muted);font-weight:600;font-size:.76rem}
.qty{display:inline-flex;align-items:center;border:1.5px solid var(--line);border-radius:999px;overflow:hidden}
.qty button{width:30px;height:30px;font-weight:800;color:var(--violet)}
.qty button:hover{background:#F4F1FF}
.qty span{min-width:26px;text-align:center;font-weight:700;font-size:.9rem}
.rm{color:var(--muted);width:30px;height:30px;border-radius:50%;display:grid;place-items:center}
.rm:hover{background:#FEF2F2;color:#DC2626}
.sum-row{display:flex;justify-content:space-between;padding:.45rem 0;font-size:.92rem;color:var(--ink-2)}
.sum-row.total{border-top:1px solid var(--line);margin-top:.5rem;padding-top:.9rem;font-weight:800;font-size:1.15rem;color:var(--ink)}
.sum-row.disc{color:#059669;font-weight:700}
.coupon{display:flex;gap:.5rem;margin:.9rem 0}
.coupon input{flex:1;border:1.5px solid var(--line);border-radius:12px;padding:.6rem .8rem;outline:0;text-transform:uppercase}
.coupon input:focus{border-color:var(--violet)}
.field .err{font-size:.78rem;color:#DC2626;display:none}
.field.invalid input{border-color:#DC2626}
.field.invalid .err{display:block}
.pay-opts{display:grid;grid-template-columns:repeat(3,1fr);gap:.5rem;margin:.4rem 0 1rem}
.pay-opts label{border:1.5px solid var(--line);border-radius:12px;padding:.6rem;text-align:center;font-size:.85rem;font-weight:700;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:.3rem}
.pay-opts input{display:none}
.pay-opts input:checked+span{color:var(--violet)}
.pay-opts label:has(input:checked){border-color:var(--violet);background:#F6F3FF}
.success{text-align:center;max-width:560px;margin:0 auto;padding:2rem 0}
.success .ok{width:84px;height:84px;border-radius:50%;background:var(--grad);color:#fff;display:grid;place-items:center;margin:0 auto 1.2rem}
.success h2{font-size:1.7rem;font-weight:800}
.success p{color:var(--muted);margin-top:.6rem}
.p404{text-align:center;padding:5rem 0}
.p404 b{font-size:6rem;font-weight:800;line-height:1;display:block}
.p404 h1{font-size:1.6rem;margin:.6rem 0 .4rem}
.p404 p{color:var(--muted)}
.skel{background:linear-gradient(90deg,#F3F0FF 25%,#EAE6FA 50%,#F3F0FF 75%);background-size:200% 100%;animation:sh 1.2s infinite;border-radius:14px}
@keyframes sh{0%{background-position:200% 0}100%{background-position:-200% 0}}
.back-top{position:fixed;right:1.5rem;bottom:5rem;width:44px;height:44px;border-radius:50%;background:#fff;border:1.5px solid var(--line);box-shadow:var(--shadow);display:grid;place-items:center;color:var(--violet);opacity:0;pointer-events:none;transition:.3s;z-index:80}
.back-top.show{opacity:1;pointer-events:auto}
.level-pill{display:inline-block;background:#F4F1FF;color:var(--violet);font-size:.72rem;font-weight:800;padding:.15rem .55rem;border-radius:999px}
.spec{display:grid;grid-template-columns:1fr 1fr;gap:.6rem;margin-top:.8rem}
.spec div{background:#F8F7FF;border-radius:12px;padding:.6rem .8rem;font-size:.86rem}
.spec div b{display:block;font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.desc-list{display:grid;gap:.4rem;margin-top:.6rem}
.desc-list li{display:flex;gap:.5rem;font-size:.9rem;color:var(--ink-2)}
.desc-list li:before{content:"✓";color:var(--teal);font-weight:800}
@media(max-width:560px){
  .cart-line{grid-template-columns:1fr auto;row-gap:.4rem}
  .pay-opts{grid-template-columns:1fr}
}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}}

@media(max-width:1200px){
  .hero-grid{grid-template-columns:1fr 1fr;gap:1.4rem}
  .cat-grid{grid-template-columns:repeat(4,1fr)}
  .prod-grid{grid-template-columns:repeat(3,1fr)}
  .trust-grid{grid-template-columns:repeat(3,1fr)}
  .grid-4{grid-template-columns:repeat(2,1fr)}
}
@media(max-width:900px){
  .nav,.hdr-actions .only-desktop{display:none}
  .nav-toggle{display:grid}
  .hdr-in{height:68px}
  .nav.open{display:flex;flex-direction:column;position:absolute;top:76px;left:0;right:0;background:#fff;border-bottom:1px solid var(--line);padding:1rem;gap:.2rem;box-shadow:var(--shadow);align-items:stretch}
  .nav.open a{padding:.7rem .9rem;font-size:1rem}
  .hero-grid{grid-template-columns:1fr}
  .lang-col{grid-template-columns:repeat(5,1fr);display:grid}
  .lang-col h3{display:none}
  .cat-grid{grid-template-columns:repeat(2,1fr)}
  .prod-grid{grid-template-columns:repeat(2,1fr)}
  .shop{grid-template-columns:1fr}
  .filters{position:static}
  .grid-2,.grid-3,.steps,.contact-grid,.ftr-top{grid-template-columns:1fr}
  .trust-grid{grid-template-columns:repeat(2,1fr)}
}
@media(max-width:560px){
  .prod-grid,.cat-grid{grid-template-columns:1fr}
  .searchbar{flex-direction:column;border-radius:20px;padding:.6rem}
  .searchbar input{width:100%}
  .cta-band{padding:1.8rem 1.2rem}
  .cta-band .form{flex-direction:column;border-radius:20px}
}
"""

ICONS = {
    "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
    "edit": '<path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4z"/>',
    "story": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
    "map": '<path d="M1 6l7-3 8 3 7-3v15l-7 3-8-3-7 3z"/><path d="M8 3v15"/><path d="M16 6v15"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M8 13h8"/><path d="M8 17h5"/>',
    "notes": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 8h8"/><path d="M8 12h8"/><path d="M8 16h5"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "audio": '<path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3z"/><path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"/>',
    "cap": '<path d="M22 10L12 5 2 10l10 5 10-5z"/><path d="M6 12v5c0 1.7 2.7 3 6 3s6-1.3 6-3v-5"/>',
    "lib": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/><path d="M9 7h7"/>',
    "science": '<path d="M9 3h6"/><path d="M10 3v6L5 19a2 2 0 0 0 1.7 3h10.6A2 2 0 0 0 19 19l-5-10V3"/><path d="M7.5 14h9"/>',
    "brain": '<path d="M12 5a3 3 0 0 0-6 0 3 3 0 0 0-2 5 3 3 0 0 0 1 5.8V19a2 2 0 0 0 2 2h1v-6"/><path d="M12 5a3 3 0 0 1 6 0 3 3 0 0 1 2 5 3 3 0 0 1-1 5.8V19a2 2 0 0 1-2 2h-1v-6"/><path d="M12 5v14"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
    "search": '<circle cx="11" cy="11" r="8"/><path d="M21 21l-4.3-4.3"/>',
    "heart": '<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 0 0-7.8 7.8l8.9 8.9 8.8-8.8a5.5 5.5 0 0 0 0-7.8z"/>',
    "star": '<path d="M12 2l2.6 7.4H22l-6.1 4.6 2.3 7.4L12 17l-6.2 4.4 2.3-7.4L2 9.4h7.4z"/>',
    "bolt": '<path d="M13 2L3 14h9l-1 8 10-12h-9z"/>',
    "shield2": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    "lock": '<rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/>',
    "card": '<rect x="2" y="5" width="20" height="14" rx="3"/><path d="M2 10h20"/><path d="M6 15h3"/>',
    "truck": '<path d="M1 4h13v11H1z"/><path d="M14 8h4l3 3v4h-7"/><circle cx="5.5" cy="18.5" r="2"/><circle cx="18.5" cy="18.5" r="2"/>',
    "headset": '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><path d="M4 14h3v6H5a2 2 0 0 1-2-2z"/><path d="M20 14h-3v6h2a2 2 0 0 0 2-2z"/>',
    "check": '<path d="M20 6L9 17l-5-5"/>',
    "checkc": '<circle cx="12" cy="12" r="10"/><path d="M8 12l3 3 6-6"/>',
    "arrow": '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 6 10-6"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "pin": '<path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "cart": '<circle cx="9" cy="20" r="1.6"/><circle cx="18" cy="20" r="1.6"/><path d="M1 2h3l2.6 12.4a2 2 0 0 0 2 1.6h8.7a2 2 0 0 0 2-1.6L21 6H5"/>',
    "user": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "menu": '<path d="M3 6h18"/><path d="M3 12h18"/><path d="M3 18h18"/>',
    "insta": '<rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/>',
    "fb": '<path d="M15 3h-2.5A4.5 4.5 0 0 0 8 7.5V10H5v4h3v8h4v-8h3l1-4h-4V7.5A.5.5 0 0 1 12.5 7H15z"/>',
    "yt": '<rect x="2" y="5" width="20" height="14" rx="4"/><path d="M10 9l6 3-6 3z"/>',
    "in": '<rect x="2" y="2" width="20" height="20" rx="3"/><path d="M7 10v7"/><circle cx="7" cy="7" r="1"/><path d="M11 17v-4a2 2 0 0 1 4 0v4"/>',
    "tt": '<path d="M14 3v11a4 4 0 1 1-4-4"/><path d="M14 3h3a5 5 0 0 0 4 4"/>',
    "pin2": '<path d="M12 17v5"/><path d="M9 3h6l-1 6 4 3v2H6v-2l4-3z"/>',
}

def svg(name, size=22, sw=1.9, cls=""):
    p = ICONS.get(name, ICONS["star"])
    return ('<svg class="%s" width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % (cls, size, size, sw, p))

CATEGORIES = [
    ("carti-si-materiale-scolare", "Cărți și materiale școlare", "Manuale auxiliare, culegeri, sinteze pe materii", "book", "linear-gradient(135deg,#6D28D9,#4F46E5)"),
    ("exercitii-si-fise-de-lucru", "Exerciții și fișe de lucru", "Fișe printabile cu exerciții și barem", "edit", "linear-gradient(135deg,#0EA5A4,#22C1A5)"),
    ("povesti-si-carti-de-lectura", "Povești și cărți de lectură", "Lecturi pentru copii + fișe de înțelegere", "story", "linear-gradient(135deg,#EC4899,#F472B6)"),
    ("harti-si-atlase", "Hărți și atlase", "Hărți printabile A4/A3, atlase tematice", "map", "linear-gradient(135deg,#F59E0B,#FBBF24)"),
    ("rezumate-si-eseuri", "Rezumate și eseuri", "Rezumate, comentarii, eseuri argumentative", "file", "linear-gradient(135deg,#4F46E5,#6366F1)"),
    ("schite-si-conspecte", "Schițe și conspecte", "Structuri, scheme, conspecte de curs", "notes", "linear-gradient(135deg,#7C3AED,#A78BFA)"),
    ("limbi-straine-vocabular", "Limbi străine – vocabular", "Cuvinte și expresii pe teme, A1–B2", "globe", "linear-gradient(135deg,#0EA5A4,#38BDF8)"),
    ("audiobookuri", "Audiobookuri", "Cărți audio și lecții ascultate, MP3", "audio", "linear-gradient(135deg,#8B5CF6,#EC4899)"),
    ("licenta-si-disertatie", "Licență și disertație", "Ghiduri, structuri, bibliografii, teme", "cap", "linear-gradient(135deg,#1D4ED8,#3B82F6)"),
    ("literatura-de-specialitate", "Literatură de specialitate", "Sinteze și ghiduri de studiu pe domenii", "lib", "linear-gradient(135deg,#B45309,#F59E0B)"),
    ("planuri-de-lucru-stiintifice", "Planuri de lucru științifice", "Modele de plan, metodologie, etape", "science", "linear-gradient(135deg,#0F766E,#14B8A6)"),
    ("si-multe-altele", "Și multe altele...", "Resurse personalizate la cerere", "star", "linear-gradient(135deg,#DB2777,#F472B6)"),
]

DOMAINS = [
    ("Limbi străine", "limbi-straine", "globe"),
    ("Literatură", "literatura", "book"),
    ("Psihologie", "psihologie", "brain"),
    ("Drept", "drept", "shield"),
    ("Criminalistică", "criminalistica", "search"),
    ("Psihiatrie", "psihiatrie", "heart"),
]

LANGS = ["Engleză", "Franceză", "Spaniolă", "Germană", "Italiană", "Română"]

PRODUCTS = [
    dict(id=1, title="Engleză pentru începători A1–A2: 200 de exerciții + vocabular", cat="limbi-straine-vocabular", lang="Engleză", level="A1–A2", fmt="PDF", pages="124 pagini", price=49, old=69, badge="Bestseller", rating=4.9, votes=214, icon="globe"),
    dict(id=2, title="500 de cuvinte esențiale în franceză – vocabular ilustrat", cat="limbi-straine-vocabular", lang="Franceză", level="A1", fmt="PDF", pages="78 pagini", price=39, old=0, badge="Nou", rating=4.8, votes=96, icon="globe"),
    dict(id=3, title="Spaniolă de la zero: 60 de lecții cu dialoguri și exerciții", cat="limbi-straine-vocabular", lang="Spaniolă", level="A1–A2", fmt="PDF", pages="150 pagini", price=45, old=59, badge="", rating=4.7, votes=131, icon="globe"),
    dict(id=4, title="Germană A1: vocabular pe teme + 80 de fișe de lucru", cat="limbi-straine-vocabular", lang="Germană", level="A1", fmt="PDF", pages="96 pagini", price=45, old=0, badge="", rating=4.8, votes=88, icon="globe"),
    dict(id=5, title="Italiană pentru călătorii: expresii utile + audio", cat="limbi-straine-vocabular", lang="Italiană", level="A1–A2", fmt="PDF + MP3", pages="62 pagini · 55 min", price=55, old=75, badge="Pachet", rating=4.9, votes=142, icon="globe"),
    dict(id=6, title="Rezumat „Romeo și Julieta” – Shakespeare (analiză + personaje)", cat="rezumate-si-eseuri", lang="Română", level="Liceu", fmt="PDF", pages="32 pagini", price=19, old=25, badge="Bestseller", rating=4.9, votes=389, icon="file"),
    dict(id=7, title="Eseu: tema și viziunea despre lume în „Moromeții”", cat="rezumate-si-eseuri", lang="Română", level="Bac", fmt="PDF", pages="26 pagini", price=24, old=0, badge="", rating=4.8, votes=176, icon="file"),
    dict(id=8, title="Rezumat „Ion” de Liviu Rebreanu + fișe de personaje", cat="rezumate-si-eseuri", lang="Română", level="Liceu", fmt="PDF", pages="38 pagini", price=22, old=0, badge="", rating=4.7, votes=154, icon="file"),
    dict(id=9, title="Schițe și conspecte: Literatura română, clasa a IX-a", cat="schite-si-conspecte", lang="Română", level="Liceu", fmt="PDF", pages="84 pagini", price=29, old=0, badge="", rating=4.6, votes=97, icon="notes"),
    dict(id=10, title="Fișe de lucru Matematică clasa a V-a – 200 de exerciții cu barem", cat="exercitii-si-fise-de-lucru", lang="Română", level="Primar/Gimnaziu", fmt="PDF", pages="110 pagini", price=35, old=45, badge="", rating=4.8, votes=203, icon="edit"),
    dict(id=11, title="Limba română clasele I–IV: pachet complet de fișe", cat="exercitii-si-fise-de-lucru", lang="Română", level="Primar", fmt="PDF", pages="180 pagini", price=39, old=55, badge="Bestseller", rating=4.9, votes=267, icon="edit"),
    dict(id=12, title="30 de povești ilustrate pentru copii (4–9 ani)", cat="povesti-si-carti-de-lectura", lang="Română", level="Preșcolari", fmt="PDF", pages="92 pagini", price=45, old=0, badge="", rating=4.9, votes=188, icon="story"),
    dict(id=13, title="Povești educative + exerciții de înțelegere a textului", cat="povesti-si-carti-de-lectura", lang="Română", level="Primar", fmt="PDF", pages="74 pagini", price=32, old=0, badge="", rating=4.7, votes=121, icon="story"),
    dict(id=14, title="Hartă politică Europa – printabilă A3 (alb/negru + color)", cat="harti-si-atlase", lang="Română", level="Toate", fmt="PDF", pages="6 fișiere", price=25, old=0, badge="", rating=4.8, votes=76, icon="map"),
    dict(id=15, title="Atlas istoric: harta României 1918–1940", cat="harti-si-atlase", lang="Română", level="Liceu", fmt="PDF", pages="22 pagini", price=29, old=0, badge="", rating=4.7, votes=54, icon="map"),
    dict(id=16, title="Audiobook: Povești de noapte bună, volumul 1", cat="audiobookuri", lang="Română", level="3–8 ani", fmt="MP3", pages="3 h 10 min", price=35, old=49, badge="Audio", rating=4.9, votes=143, icon="audio"),
    dict(id=17, title="Audiobook: Engleză pentru începători – ascultă și repetă", cat="audiobookuri", lang="Engleză", level="A1", fmt="MP3", pages="2 h 25 min", price=49, old=65, badge="Audio", rating=4.8, votes=119, icon="audio"),
    dict(id=18, title="Cum alegi tema de licență (Psihologie) – ghid + 60 de idei", cat="licenta-si-disertatie", lang="Română", level="Studenți", fmt="PDF", pages="48 pagini", price=59, old=0, badge="Bestseller", rating=4.9, votes=211, icon="cap"),
    dict(id=19, title="Structură de disertație – Drept penal (model + bibliografie)", cat="licenta-si-disertatie", lang="Română", level="Master", fmt="PDF", pages="42 pagini", price=69, old=89, badge="", rating=4.8, votes=104, icon="cap"),
    dict(id=20, title="120 de teme de licență: Psihologie, Drept, Criminalistică", cat="licenta-si-disertatie", lang="Română", level="Studenți", fmt="PDF", pages="56 pagini", price=79, old=99, badge="Nou", rating=4.9, votes=167, icon="cap"),
    dict(id=21, title="Plan de lucru științific: model complet + exemplu redactat", cat="planuri-de-lucru-stiintifice", lang="Română", level="Studenți", fmt="PDF + DOCX", pages="34 pagini", price=55, old=0, badge="", rating=4.7, votes=92, icon="science"),
    dict(id=22, title="Introducere în psihiatrie – sinteze de studiu", cat="literatura-de-specialitate", lang="Română", level="Studenți", fmt="PDF", pages="132 pagini", price=65, old=0, badge="", rating=4.8, votes=87, icon="brain"),
    dict(id=23, title="Criminalistica pe înțelesul tuturor: ghid de studiu ilustrat", cat="literatura-de-specialitate", lang="Română", level="Studenți", fmt="PDF", pages="108 pagini", price=59, old=75, badge="", rating=4.9, votes=133, icon="search"),
    dict(id=24, title="Vocabular juridic: engleză–franceză pentru juriști", cat="limbi-straine-vocabular", lang="Engleză", level="B1–B2", fmt="PDF", pages="64 pagini", price=49, old=0, badge="", rating=4.7, votes=63, icon="lib"),
    dict(id=25, title="Sinteze de Biologie pentru clasa a XII-a: 12 unități + 300 de întrebări", cat="carti-si-materiale-scolare", lang="Română", level="Liceu", fmt="PDF", pages="118 pagini", price=45, old=0, badge="Nou", rating=4.8, votes=41, icon="book"),
    dict(id=26, title="Matematică clasa a VIII-a: 250 de exerciții gradate cu barem", cat="carti-si-materiale-scolare", lang="Română", level="Primar/Gimnaziu", fmt="PDF", pages="132 pagini", price=42, old=55, badge="", rating=4.7, votes=67, icon="book"),
    dict(id=27, title="Enunțuri de bac Matematică: 40 de subiecte rezolvate pas cu pas", cat="exercitii-si-fise-de-lucru", lang="Română", level="Bac", fmt="PDF", pages="96 pagini", price=49, old=65, badge="Bestseller", rating=4.9, votes=88, icon="edit"),
    dict(id=28, title="Rezumat „Balul mitomanilor” – Marin Preda (structură + personaje)", cat="rezumate-si-eseuri", lang="Română", level="Liceu", fmt="PDF", pages="30 pagini", price=19, old=0, badge="", rating=4.8, votes=35, icon="file"),
    dict(id=29, title="Eseu: conflictul generațiilor în „Ion” – model + 3 variante", cat="rezumate-si-eseuri", lang="Română", level="Bac", fmt="PDF", pages="18 pagini", price=22, old=0, badge="", rating=4.7, votes=28, icon="file"),
    dict(id=30, title="Conspecte: Istoria României și a românilor, clasa a XII-a", cat="schite-si-conspecte", lang="Română", level="Liceu", fmt="PDF", pages="88 pagini", price=32, old=0, badge="Nou", rating=4.7, votes=24, icon="notes"),
    dict(id=31, title="Atlas geografic mondial: 24 de hărți tematice printabile A3", cat="harti-si-atlase", lang="Română", level="Toate", fmt="PDF", pages="24 fișiere", price=29, old=39, badge="", rating=4.8, votes=31, icon="map"),
    dict(id=32, title="Audiobook: Povești populare românești, volumul 2 (24 de povești)", cat="audiobookuri", lang="Română", level="3–8 ani", fmt="MP3", pages="2 h 45 min", price=35, old=0, badge="Audio", rating=4.9, votes=47, icon="audio"),
    dict(id=33, title="Ghid de documentare: norme APA 7 + 120 de exemple de citare", cat="licenta-si-disertatie", lang="Română", level="Studenți", fmt="PDF + DOCX", pages="38 pagini", price=39, old=0, badge="Nou", rating=4.8, votes=22, icon="cap"),
    dict(id=34, title="Drept constituțional – sinteze de studiu pentru facultate", cat="literatura-de-specialitate", lang="Română", level="Studenți", fmt="PDF", pages="96 pagini", price=59, old=75, badge="", rating=4.8, votes=38, icon="shield"),
    dict(id=35, title="Schiță ilustrată: „O scrisoare pierdută” de I.L. Caragiale – analiză completă", cat="schite-si-conspecte", lang="Română", level="Liceu", fmt="PDF", pages="1 fișă A3", price=19, old=0, badge="Nou", rating=4.9, votes=12, icon="story"),
    dict(id=36, title="Schiță ilustrată: „Plumb” de George Bacovia – analiză completă", cat="schite-si-conspecte", lang="Română", level="Liceu", fmt="PDF", pages="1 fișă A3", price=19, old=0, badge="Nou", rating=4.8, votes=9, icon="book"),
    dict(id=37, title="Rezumat „Enigma Otiliei” – G. Călinescu (structură + personaje)", cat="rezumate-si-eseuri", lang="Română", level="Liceu", fmt="PDF", pages="34 pagini", price=19, old=0, badge="", rating=4.8, votes=52, icon="file"),
    dict(id=38, title="Eseu: umorul ca critică a societății în „O scrisoare pierdută”", cat="rezumate-si-eseuri", lang="Română", level="Bac", fmt="PDF", pages="20 pagini", price=22, old=0, badge="", rating=4.7, votes=31, icon="file"),
    dict(id=39, title="Schiță ilustrată: „Ispita” de Ion Slavici – analiză completă", cat="schite-si-conspecte", lang="Română", level="Liceu", fmt="PDF", pages="1 fișă A3", price=19, old=0, badge="Nou", rating=4.9, votes=11, icon="story"),
    dict(id=40, title="Schiță ilustrată: „Fuga” de George Bacovia – analiză completă", cat="schite-si-conspecte", lang="Română", level="Liceu", fmt="PDF", pages="1 fișă A3", price=19, old=0, badge="Nou", rating=4.8, votes=9, icon="book"),
    dict(id=41, title="Fișe de lucru: Fizică clasa a IX-a – 120 de exerciții cu barem", cat="exercitii-si-fise-de-lucru", lang="Română", level="Primar/Gimnaziu", fmt="PDF", pages="88 pagini", price=35, old=0, badge="", rating=4.7, votes=64, icon="edit"),
    dict(id=42, title="Matematică clasa a VI-a: 180 de exerciții – fracții și procente cu barem", cat="exercitii-si-fise-de-lucru", lang="Română", level="Primar/Gimnaziu", fmt="PDF", pages="104 pagini", price=35, old=45, badge="", rating=4.8, votes=73, icon="edit"),
    dict(id=43, title="Limba engleză clasa a VII-a: 90 de fișe de gramatică și vocabular", cat="exercitii-si-fise-de-lucru", lang="Engleză", level="Primar/Gimnaziu", fmt="PDF", pages="90 pagini", price=39, old=0, badge="Bestseller", rating=4.9, votes=95, icon="edit"),
    dict(id=44, title="25 de povești despre prietenie pentru copii (6–10 ani)", cat="povesti-si-carti-de-lectura", lang="Română", level="Primar", fmt="PDF", pages="86 pagini", price=39, old=0, badge="", rating=4.8, votes=58, icon="story"),
    dict(id=45, title="Ghid de comentariu: cărți de lectură, clasa a V-a + 12 fișe", cat="povesti-si-carti-de-lectura", lang="Română", level="Primar", fmt="PDF", pages="46 pagini", price=29, old=0, badge="Nou", rating=4.7, votes=14, icon="story"),
    dict(id=46, title="Harta fizică a României – detaliată, printabilă A3 (color + alb/negru)", cat="harti-si-atlase", lang="Română", level="Toate", fmt="PDF", pages="4 fișiere", price=19, old=25, badge="", rating=4.8, votes=43, icon="map"),
    dict(id=47, title="16 hărți de geografie economică pentru bac – fișe tematice", cat="harti-si-atlase", lang="Română", level="Liceu", fmt="PDF", pages="16 fișiere", price=25, old=0, badge="", rating=4.7, votes=36, icon="map"),
    dict(id=48, title="Audiobook: Poezie clasică română – 30 de poezii citite", cat="audiobookuri", lang="Română", level="Toate", fmt="MP3", pages="1 h 10 min", price=29, old=0, badge="Audio", rating=4.9, votes=66, icon="audio"),
    dict(id=49, title="Audiobook: Vocabular englez A2 – lecții audio + transcriere", cat="audiobookuri", lang="Engleză", level="A2", fmt="MP3", pages="1 h 40 min", price=39, old=0, badge="Audio", rating=4.8, votes=27, icon="audio"),
    dict(id=50, title="Cum redactezi un referat: structură, norme de redactare + exemple", cat="licenta-si-disertatie", lang="Română", level="Studenți", fmt="PDF", pages="36 pagini", price=29, old=0, badge="", rating=4.7, votes=48, icon="cap"),
    dict(id=51, title="Metodologia cercetării: chestionare, eșantionare, analize de bază", cat="licenta-si-disertatie", lang="Română", level="Studenți", fmt="PDF + DOCX", pages="44 pagini", price=45, old=59, badge="", rating=4.8, votes=39, icon="cap"),
    dict(id=52, title="Plan de cercetare de piață: model complet + chestionar editabil", cat="planuri-de-lucru-stiintifice", lang="Română", level="Studenți", fmt="PDF + DOCX", pages="40 pagini", price=49, old=0, badge="Nou", rating=4.8, votes=10, icon="science"),
    dict(id=53, title="Psihologia educației – sinteze de studiu pentru facultate", cat="literatura-de-specialitate", lang="Română", level="Studenți", fmt="PDF", pages="124 pagini", price=65, old=0, badge="Nou", rating=4.9, votes=18, icon="brain"),
    dict(id=54, title="800 de termeni psihologici: definiții esențiale + exemple de utilizare", cat="literatura-de-specialitate", lang="Română", level="Studenți", fmt="PDF", pages="156 pagini", price=59, old=0, badge="", rating=4.8, votes=57, icon="brain"),
    dict(id=55, title="Sinteze de Fizică pentru clasa a X-a + 200 de probleme rezolvate", cat="carti-si-materiale-scolare", lang="Română", level="Liceu", fmt="PDF", pages="108 pagini", price=45, old=0, badge="", rating=4.8, votes=61, icon="book"),
    dict(id=56, title="Chimie clasa a XI-a: 250 de probleme rezolvate pe capitole", cat="carti-si-materiale-scolare", lang="Română", level="Liceu", fmt="PDF", pages="126 pagini", price=49, old=65, badge="Bestseller", rating=4.9, votes=112, icon="book"),
]

# Descrieri scurte per produs (afișate pe pagina de produs; fallback pe categorie)
DESCRIPTIONS = {
    1: "200 de exerciții gradate de la A1 la A2, cu răspunsuri la final, vocabular tematic pe 20 de teme și mini-teste de verificare la fiecare 5 lecții.",
    2: "500 de cuvinte și expresii de bază în franceză, ilustrate și grupate pe teme (familie, oraș, mâncare, călătorii), cu exemple în propoziții și pronunție scrisă.",
    3: "60 de lecții scurte cu dialoguri realiste, explicații de gramatică pe înțelesul tuturor și exerciții cu cheie de rezolvare. Ideal pentru autodidacți.",
    4: "Vocabular german A1 organizat pe 16 teme, plus 80 de fișe de lucru printabile cu barem. Include listă de verbe neregulate și tabel de articole.",
    5: "Expresiile de care ai nevoie la aeroport, hotel, restaurant sau în oraș, cu fișiere audio înregistrate de vorbitori nativi pentru ascultare și repetare.",
    6: "Rezumat pe acte și scene, analiza temelor (iubire, destin, conflict), fișe pentru fiecare personaj și 10 citate-cheie explicate — pentru teză sau bac.",
    7: "Eseu complet de 4 pagini pe cerința tipică de bacalaureat, cu structura pe paragrafe evidențiată, plus 3 variante de introducere și încheiere.",
    8: "Rezumat pe capitole, fișe de personaje (Ion, Ana, Florica, Vasile Baciu), analiza celor două glasuri și un set de 15 întrebări de verificare.",
    9: "Conspecte sintetice pentru toate operele din programa clasei a IX-a: autor, context, temă, structură, personaje, citate — pe câte 2 pagini per operă.",
    10: "200 de exerciții pe toate capitolele clasei a V-a (numere naturale, fracții, geometrie), grupate pe 3 niveluri de dificultate, cu barem detaliat.",
    11: "Peste 180 de fișe pentru clasele I–IV: citire, scriere, ortografie, părți de vorbire, compuneri. Fiecare fișă este printabilă A4 și are răspunsuri.",
    12: "30 de povești originale ilustrate color, cu morală explicată și 3 întrebări de discuție la finalul fiecărei povești. Potrivite pentru citit seara.",
    13: "Povești scurte urmate de exerciții de înțelegere a textului: întrebări cu răspuns scurt, adevărat/fals, ordonare de evenimente și vocabular.",
    14: "Hartă politică a Europei actualizată, în variante A3 și A4, color și alb-negru (pentru colorat), plus versiune mută pentru evaluare.",
    15: "22 de hărți comentate ale României interbelice: granițe, județe, evoluția teritorială, cu cronologie și explicații pentru fiecare hartă.",
    16: "3 ore de povești citite calm, cu fundal sonor discret, împărțite în 20 de piste. Ideal pentru rutina de seară a copiilor de 3–8 ani.",
    17: "Lecții audio de tip „ascultă și repetă”, cu pauze pentru exersare, transcriere PDF inclusă și vocabular de bază pentru conversații simple.",
    18: "Ghid pas cu pas pentru alegerea temei: criterii, discuția cu coordonatorul, verificarea surselor, plus 60 de idei de teme organizate pe ramuri.",
    19: "Model complet de structură pentru disertație în drept penal: capitole, subcapitole, metodologie, bibliografie orientativă și greșeli frecvente.",
    20: "120 de teme actuale, fiecare cu o descriere scurtă, întrebări de cercetare posibile și 3–5 surse de pornire. Împărțite pe cele trei domenii.",
    21: "Model de plan de lucru științific cu toate secțiunile explicate + un exemplu redactat integral. Include fișier DOCX editabil pentru propriul plan.",
    22: "Sinteze pe cele mai importante capitole din psihiatrie: clasificări, criterii de diagnostic, tratamente, cu tabele comparative și scheme.",
    23: "Ghid ilustrat de criminalistică: cercetarea locului faptei, urme, identificare, expertize. Cu studii de caz și întrebări de autoevaluare.",
    24: "Termeni juridici uzuali în engleză și franceză, cu traducere, definiție și exemplu de utilizare în context. Organizat pe ramuri de drept.",
    25: "Cele 12 unități ale programului de clasa a XII-a, sintetizate pe scheme, tabele comparative și definiții-cheie, cu 25 de întrebări de verificare și barem pentru fiecare unitate.",
    26: "250 de exerciții pe toate capitolele clasei a VIII-a (aritmetică, expresii algebrice, ecuații și inecuații, geometrie), pe 3 niveluri de dificultate, cu barem detaliat și soluții rezolvate.",
    27: "40 de subiecte de tip bac, rezolvate pas cu pas, organizate pe capitole: aritmetică, algebră, geometrie, funcții și statistica descriptivă, cu traseu de rezolvare pentru fiecare subiect.",
    28: "Structura romanului (cadrele narative, naratorii), rezumat pe capitole, fișe de personaje (Vlad, Mărgărit, Păstorel Țigancă) și citate-cheie explicate pentru eseu.",
    29: "Eseu-model pe cerința clasică de bacalaureat, cu planul argumentelor evidențiat, 3 variante de introducere și încheiere și 10 citate cu trimitere la text, pentru a-ți construi propriul eseu.",
    30: "Conspecte pe fiecare unitate a programa: date-cheie, personalități, cauze și consecințe ale marilor evenimente, tabele cronologice și 10 întrebări de verificare pe unitate.",
    31: "24 de hărți tematice ale lumii (relief, climă, vegetație, populație, economia regiunilor), printabile A3 color și alb-negru, plus variante mute pentru evaluarea la clasă.",
    32: "24 de povești populare românești clasice, citite cu voce blândă, cu fundal sonor discret. Împărțite în 24 de piste, perfecte pentru rutina de seară sau orele de citire.",
    33: "Normele APA 7 explicate pas cu pas, cu 120 de exemple de citare (cărți, articole, surse online), un model editabil de bibliografie în DOCX și cele mai frecvente erori de documentare.",
    34: "Sinteze pe capitolele fundamentale: sistemul de stat, drepturile și libertățile fundamentale, controlul constituțional, instituțiile statului român, cu jurisprudența-cheie evidențiată.",
    35: "Fișă de studiu vizuală pentru piesa lui I.L. Caragiale: context literar, personaje și conflicte, structura celor 4 acte (44 de scene), limbajul și tipurile de comic, tema, didascaliile, moralurile și locul cu timpul — printabilă pe A3, ideală pentru studiu sau pentru clasă.",
    36: "Fișă de studiu vizuală pentru poezia lui George Bacovia: context literar, tema și simbolul plumbului, structura și particularitățile de construcție, analiza conținutului, tipurile de imagini, particularitățile stilistice și viziunea despre lume — printabilă pe A3, ideală pentru studiu sau pentru clasă.",
    37: "Rezumat pe capitole și cadre narative, fișe de personaje (Otilia, Alexandru, Tătic, Mama, Goe, Ștefănuca), tema și 12 citate-cheie comentate pentru eseu.",
    38: "Eseu-model pe cerința tipică de bacalaureat: planul argumentelor evidențiat, 3 variante de introducere și încheiere, 8 citate cu trimitere la text și observații despre tipurile de comic caragialian.",
    39: "Fișă de studiu vizuală pentru nuvela lui Ion Slavici: context literar, personaje (Tudor, Elena, Gherghina), conflictul interior, structura narativă, tema și mesajul moral — printabilă pe A3, ideală pentru studiu sau pentru clasă.",
    40: "Fișă de studiu vizuală pentru poezia lui George Bacovia: context simbolist, simbolurile (ceasul, vântul, lumina), structura, analiza conținutului și particularitățile stilistice — printabilă pe A3, ideală pentru studiu sau pentru clasă.",
    41: "120 de exerciții pe capitolele clasei a IX-a (cinematică, dinamica, presiune, energie), pe 3 niveluri de dificultate, cu barem detaliat și scheme auxiliare.",
    42: "180 de exerciții pe numerele raționale, fracții, procente și probleme de aplicare, cu barem detaliat și 20 de probleme rezolvate pas cu pas.",
    43: "90 de fișe printabile: prezentul, trecutul și viitorul, comparativul, vocabular pe 12 teme, cu răspunsuri și exerciții de consolidare la finalul fiecărei unități.",
    44: "25 de povești originale despre prietenie, cooperare și încredere, cu ilustrații color, morală explicată și 3 întrebări de discuție la finalul fiecărei povești.",
    45: "Metoda comentariului textului explicată pas cu pas, 5 modele de comentariu pentru cărțile de lectură ale clasei a V-a și 12 fișe de înțelegere cu răspunsuri.",
    46: "Harta fizică a României în detaliu (munți, câmpii, depresiuni, hidrografie), printabilă A3 color și alb-negru, plus variantă mută pentru evaluare la clasă.",
    47: "16 hărți tematice pentru bacalaureat (resurse, industrie, transport, agricultură, turism), cu legenda explicată și 20 de întrebări de analiză a hărților.",
    48: "30 de poezii clasice românești citite calm, cu fundal sonor discret, împărțite în 30 de piste — pentru relaxare, memorare sau ore de limba română.",
    49: "Lecții audio de vocabular pe 20 de teme, cu pauze pentru repetare, transcriere PDF inclusă și mini-teste de verificare la fiecare unitate.",
    50: "Structura completă a referatului (introducere, cuprins, bibliografie), norme de redactare, 4 exemple de plan și cele mai frecvente erori de formă.",
    51: "Cum construiești un chestionar, cum alegi eșantionul și cum prezinți datele: cu exemple, tabele tip și un model de raport de cercetare.",
    52: "Model de plan de cercetare de piață cu obiective, ipoteze, metodologie și calendar, plus chestionar editabil în DOCX pentru propriul studiu.",
    53: "Sinteze pe capitolele fundamentale: dezvoltarea copilului, motivația învățării, stilurile de predare, climatul de clasă, cu scheme și 40 de întrebări de verificare.",
    54: "800 de termeni psihologici esențiali, cu definiții concise, exemple de utilizare și tabele de diferențiere a conceptelor apropiate — pentru examene și referate.",
    55: "Cele 6 unități ale clasei a X-a (cinematică, dinamica, echilibru, energie, oscilații), cu 200 de probleme rezolvate pas cu pas și barem la final.",
    56: "250 de probleme pe toate capitolele clasei a XI-a (starea gazoasă, legile chimice, reacții, soluții), rezolvate pas cu pas, cu barem și tabele auxiliare.",
}

CAT_DESC = "Material realizat de autori cu experiență didactică, structurat progresiv, cu explicații pas cu pas, exemple rezolvate și barem de corectare."

GRADIENTS = {
    "globe": "linear-gradient(135deg,#4F46E5,#0EA5A4)",
    "file": "linear-gradient(135deg,#6D28D9,#A78BFA)",
    "notes": "linear-gradient(135deg,#7C3AED,#EC4899)",
    "edit": "linear-gradient(135deg,#0EA5A4,#84CC16)",
    "story": "linear-gradient(135deg,#EC4899,#F59E0B)",
    "map": "linear-gradient(135deg,#F59E0B,#EF4444)",
    "audio": "linear-gradient(135deg,#8B5CF6,#EC4899)",
    "cap": "linear-gradient(135deg,#1D4ED8,#0EA5A4)",
    "science": "linear-gradient(135deg,#0F766E,#22C1A5)",
    "brain": "linear-gradient(135deg,#DB2777,#7C3AED)",
    "search": "linear-gradient(135deg,#334155,#0EA5A4)",
    "lib": "linear-gradient(135deg,#B45309,#F59E0B)",
    "book": "linear-gradient(135deg,#4F46E5,#6D28D9)",
    "shield": "linear-gradient(135deg,#334155,#4F46E5)",
    "star": "linear-gradient(135deg,#6D28D9,#EC4899)",
}

def cat_title(slug):
    for s, t, d, i, g in CATEGORIES:
        if s == slug:
            return t
    return "Resurse"

SITE_URL = "https://mckyto.github.io/caleidoscope-educational/"

def head(title, desc, active, page=None, noindex=False):
    """Generează <head> + header. `page` = numele fișierului (pentru canonical/OG)."""
    nav_items = [
        ("Acasă", "index.html", "home"),
        ("Produse", "produse.html", "produse"),
        ("Categorii", "categorii.html", "categorii"),
        ("Despre noi", "despre.html", "despre"),
        ("Blog", "blog.html", "blog"),
        ("Contact", "contact.html", "contact"),
    ]
    nav_html = []
    for label, href, key in nav_items:
        if key == "produse":
            drops = "".join(
                '<a href="produse.html?cat=%s">%s<small>%s</small></a>' % (s, t, d)
                for s, t, d, i, g in CATEGORIES[:6])
            nav_html.append(
                '<div class="drop"><a href="produse.html" class="%s">Produse ▾</a>'
                '<div class="drop-panel">%s<a href="produse.html" style="color:var(--violet)">Toate produsele →</a></div></div>'
                % ("active" if active == "produse" else "", drops))
        elif key == "categorii":
            drops = "".join(
                '<a href="produse.html?cat=%s">%s<small>%s</small></a>' % (s, t, d)
                for s, t, d, i, g in CATEGORIES[6:])
            nav_html.append(
                '<div class="drop"><a href="categorii.html" class="%s">Categorii ▾</a>'
                '<div class="drop-panel">%s<a href="categorii.html" style="color:var(--violet)">Toate categoriile →</a></div></div>'
                % ("active" if active == "categorii" else "", drops))
        else:
            nav_html.append('<a href="%s" class="%s">%s</a>' % (href, "active" if active == key else "", label))

    return """<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="theme-color" content="#6D28D9">
%(robots)s<link rel="canonical" href="%(canonical)s">
<link rel="icon" href="data:image/svg+xml,%%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 44 44'%%3E%%3Crect x='1' y='1' width='42' height='42' rx='13' fill='%%236D28D9'/%%3E%%3Cg stroke='%%23fff' stroke-width='1.6' fill='none'%%3E%%3Ccircle cx='22' cy='22' r='12'/%%3E%%3Cpath d='M22 10l10.4 18H11.6z'/%%3E%%3Cpath d='M22 34L11.6 16h20.8z'/%%3E%%3C/g%%3E%%3Ccircle cx='22' cy='22' r='3.4' fill='%%230EA5A4'/%%3E%%3C/svg%%3E">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Caleidoscope Educational.ro">
<meta property="og:title" content="%(title)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(canonical)s">
<meta property="og:locale" content="ro_RO">
<meta name="twitter:card" content="summary">
<script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"Caleidoscope Educational.ro","url":"%(site)s","potentialAction":{"@type":"SearchAction","target":"%(site)sproduse.html?q={search_term_string}","query-input":"required name=search_term_string"}}</script>
<style>%(css)s</style>
</head>
<body>
<header class="hdr" id="hdr">
  <div class="wrap hdr-in">
    <a class="brand" href="index.html" aria-label="Caleidoscope Educational">
      <svg width="40" height="40" viewBox="0 0 44 44" aria-hidden="true">
        <defs><linearGradient id="kg" x1="0" y1="0" x2="1" y2="1">
          <stop offset="0" stop-color="#4F46E5"/><stop offset="55" stop-color="#7C3AED"/><stop offset="1" stop-color="#0EA5A4"/>
        </linearGradient></defs>
        <rect x="1" y="1" width="42" height="42" rx="13" fill="url(#kg)"/>
        <g stroke="#fff" stroke-width="1.6" fill="none" opacity=".95">
          <circle cx="22" cy="22" r="12"/><path d="M22 10l10.4 18H11.6z"/><path d="M22 34L11.6 16h20.8z"/>
        </g>
        <circle cx="22" cy="22" r="3.4" fill="#fff"/>
      </svg>
      <span class="brand-txt">
        <span class="brand-name">Caleido<span>scope</span></span>
        <span class="brand-sub">Educational.ro · Resurse pentru un viitor mai bun</span>
      </span>
    </a>
    <nav class="nav" id="nav">%(nav)s</nav>
    <div class="hdr-actions">
      <a class="icon-btn only-desktop" href="cont.html" aria-label="Contul meu">%(user)s</a>
      <a class="icon-btn" href="favorite.html" aria-label="Favorite">%(heart)s<span class="cart-count" id="wishCount" style="background:var(--violet)">0</span></a>
      <button class="icon-btn" id="cartBtn" aria-label="Coșul meu">%(cart)s<span class="cart-count" id="cartCount">0</span></button>
      <button class="nav-toggle" id="navToggle" aria-label="Meniu">%(menu)s</button>
    </div>
  </div>
</header>
""" % dict(title=title.replace('"', "&quot;"), desc=desc.replace('"', "&quot;"), css=CSS, nav="".join(nav_html),
           user=svg("user", 20), heart=svg("heart", 20), cart=svg("cart", 20), menu=svg("menu", 22),
           canonical=SITE_URL + (page or (active + ".html" if active != "home" else "")),
           site=SITE_URL, robots='<meta name="robots" content="noindex">\n' if noindex else "")

FOOTER = """
<footer class="ftr">
  <div class="wrap">
    <div class="ftr-top">
      <div>
        <div class="ftr-logo">
          <svg width="38" height="38" viewBox="0 0 44 44" aria-hidden="true">
            <rect x="1" y="1" width="42" height="42" rx="13" fill="#6D28D9"/>
            <g stroke="#fff" stroke-width="1.6" fill="none"><circle cx="22" cy="22" r="12"/><path d="M22 10l10.4 18H11.6z"/><path d="M22 34L11.6 16h20.8z"/></g>
            <circle cx="22" cy="22" r="3.4" fill="#0EA5A4"/>
          </svg>
          <span class="brand-txt"><span class="brand-name">Caleido<span>scope</span></span><span class="brand-sub" style="color:#9892B8">Educational.ro</span></span>
        </div>
        <p class="ftr-tag">Pentru că fiecare descoperire te apropie de visurile tale!<br>
        Materiale educaționale create de profesori și autori: exerciții, povești, rezumate, eseuri, hărți, ghiduri, audiobookuri.</p>
      </div>
      <div>
        <h4>Categorii</h4>
        <ul>__CATLINKS__</ul>
      </div>
      <div>
        <h4>Informații utile</h4>
        <ul>
          <li><a href="despre.html">Despre noi</a></li>
          <li><a href="blog.html">Blog</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="termeni.html">Termeni și condiții</a></li>
          <li><a href="termeni.html">Politica de confidențialitate</a></li>
          <li><a href="termeni.html">Politica de retur</a></li>
        </ul>
      </div>
      <div>
        <h4>Suport clienți</h4>
        <ul>
          <li>Luni–Vineri: 09:00 – 18:00</li>
          <li><a href="mailto:contact@caleidoscope-educational.ro">contact@caleidoscope-educational.ro</a></li>
          <li><a href="tel:+40700000000">+40 700 000 000</a></li>
          <li>Livrare instantă prin descărcare</li>
        </ul>
      </div>
    </div>
    <div class="ftr-btm">
      <span>© 2026 Caleidoscope Educational.ro — Toate drepturile rezervate.</span>
      <ul><li><a href="termeni.html">Termeni</a></li><li><a href="termeni.html#gdpr">GDPR</a></li><li><a href="termeni.html#retur">Retur</a></li><li><a href="https://anpc.ro/ce-este-sal/" target="_blank" rel="noopener">ANPC – SAL</a></li><li><a href="https://ec.europa.eu/consumers/odr" target="_blank" rel="noopener">SOL/ODR</a></li></ul>
    </div>
  </div>
</footer>
<div class="toast" id="toast"></div>
<button class="back-top" id="backTop" aria-label="Sus">__UP__</button>
<div class="cookie" id="cookie" role="dialog" aria-label="Cookie-uri">
  <p><b>Folosim cookie-uri</b> strict necesare pentru coș și preferințe. Cu acordul tău, folosim și cookie-uri de analiză. Detalii în <a href="termeni.html#cookies" style="color:var(--violet);text-decoration:underline">politica de cookie-uri</a>.</p>
  <div class="row"><button class="btn btn-primary btn-sm" id="ckOk">Accept toate</button><button class="btn btn-ghost btn-sm" id="ckNo">Doar necesare</button></div>
</div>

<script>
/* ===== Caleido app: coș, favorite, UI ===== */
(function(){
  var KEY='caleido_cart', WKEY='caleido_wish', CKEY='caleido_cookie';
  function read(k){ try{ return JSON.parse(localStorage.getItem(k))||[] }catch(e){ return [] } }
  function write(k,v){ localStorage.setItem(k, JSON.stringify(v)); }
  function toast(msg){ var t=document.getElementById('toast'); if(!t) return; t.textContent=msg; t.classList.add('show'); clearTimeout(t._h); t._h=setTimeout(function(){t.classList.remove('show')},2600); }

  /* --- coș: [{id,title,price,qty}] (migrează formatul vechi fără qty) --- */
  function getCart(){
    var raw=read(KEY), out=[], seen={};
    raw.forEach(function(it){ var id=String(it.id); if(seen[id]){ seen[id].qty+=(it.qty||1) } else { seen[id]={id:id,title:it.title,price:parseFloat(it.price)||0,qty:it.qty||1}; out.push(seen[id]) } });
    return out;
  }
  function setCart(c){ write(KEY,c); paint(); window.dispatchEvent(new CustomEvent('cart:change')); }
  function addToCart(id,title,price,qty){
    var c=getCart(), f=c.filter(function(x){return x.id===String(id)})[0];
    if(f){ f.qty+=(qty||1) } else { c.push({id:String(id),title:title,price:parseFloat(price)||0,qty:qty||1}) }
    setCart(c); toast('„'+(title.length>38?title.slice(0,38)+'…':title)+'” a fost adăugat în coș');
  }
  function count(){ return getCart().reduce(function(s,x){return s+x.qty},0) }

  /* --- favorite: [id] --- */
  function getWish(){ return read(WKEY).map(String) }
  function toggleWish(id){
    var w=getWish(), i=w.indexOf(String(id));
    if(i>-1){ w.splice(i,1); toast('Eliminat din favorite') } else { w.push(String(id)); toast('Adăugat la favorite ♥') }
    write(WKEY,w); paint(); window.dispatchEvent(new CustomEvent('wish:change'));
    return i===-1;
  }

  function paint(){
    var el=document.getElementById('cartCount'); if(el){ el.textContent=count() }
    var w=document.getElementById('wishCount'); if(w){ var n=getWish().length; w.textContent=n; w.style.display=n?'grid':'none' }
    var ws=getWish();
    document.querySelectorAll('.wish').forEach(function(b){ b.classList.toggle('on', ws.indexOf(String(b.dataset.id))>-1) });
  }

  window.Caleido={getCart:getCart,setCart:setCart,addToCart:addToCart,getWish:getWish,toggleWish:toggleWish,toast:toast,paint:paint};

  /* --- delegare click: .add / .wish (merge și pentru elemente create dinamic) --- */
  document.addEventListener('click',function(e){
    var a=e.target.closest('.add[data-id]'); if(a){ e.preventDefault(); addToCart(a.dataset.id,a.dataset.title,a.dataset.price,1); return }
    var w=e.target.closest('.wish[data-id]'); if(w){ e.preventDefault(); toggleWish(w.dataset.id); }
  });
  paint();
  window.addEventListener('storage',paint);

  /* --- header / nav --- */
  var hdr=document.getElementById('hdr'), nav=document.getElementById('nav'), tg=document.getElementById('navToggle'), bt=document.getElementById('backTop');
  window.addEventListener('scroll',function(){ var y=window.scrollY; hdr.classList.toggle('scrolled',y>10); if(bt){ bt.classList.toggle('show',y>500) } },{passive:true});
  if(tg){ tg.addEventListener('click',function(){ var o=nav.classList.toggle('open'); tg.setAttribute('aria-expanded',o) }); }
  if(bt){ bt.addEventListener('click',function(){ window.scrollTo({top:0,behavior:'smooth'}) }) }
  var cartBtn=document.getElementById('cartBtn'); if(cartBtn){ cartBtn.addEventListener('click',function(){ location.href='checkout.html' }) }

  /* --- reveal la scroll --- */
  var io = (typeof window.IntersectionObserver==='function') ? new IntersectionObserver(function(es){ es.forEach(function(en){ if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target) } }) },{rootMargin:'0px 0px -8% 0px'}) : null;
  window.Caleido.reveal=function(){ document.querySelectorAll('.reveal:not(.in)').forEach(function(el){ io?io.observe(el):el.classList.add('in') }) };
  window.Caleido.reveal();

  /* --- cookie banner --- */
  var ck=document.getElementById('cookie');
  if(ck && !localStorage.getItem(CKEY)){ setTimeout(function(){ck.classList.add('show')},900);
    document.getElementById('ckOk').onclick=function(){ localStorage.setItem(CKEY,'all'); ck.classList.remove('show') };
    document.getElementById('ckNo').onclick=function(){ localStorage.setItem(CKEY,'necessary'); ck.classList.remove('show') };
  }
})();
</script>
</body>
</html>
"""

def footer(extra_js=""):
    """Footer + JS comun. `extra_js` = script specific paginii, injectat înainte de </body>."""
    catlinks = "".join('<li><a href="produse.html?cat=%s">%s</a></li>' % (s, t) for s, t, d, i, g in CATEGORIES[:6])
    up = svg("arrow", 18, 2.2).replace('<svg ', '<svg style="transform:rotate(-90deg)" ')
    return FOOTER.replace("__CATLINKS__", catlinks).replace("__UP__", up).replace("</body>", extra_js + "</body>")

def product_card(p):
    grad = GRADIENTS.get(p["icon"], GRADIENTS["star"])
    old = '<small>%d LEI</small>' % p["old"] if p.get("old") else ''
    badge = '<span class="tag">%s</span>' % p["badge"] if p.get("badge") else ''
    return """
    <article class="card reveal" data-id="%(id)d" data-cat="%(cat)s" data-lang="%(lang)s" data-level="%(level)s" data-fmt="%(fmt)s" data-price="%(price)d" data-votes="%(votes)s" data-rating="%(rating)s" data-title="%(title_lower)s">
      <div class="cover" style="background:%(grad)s">
        %(badge)s
        <button class="wish" data-id="%(id)d" aria-label="Adaugă la favorite">%(heart)s</button>
        <span class="fmt">%(fmt)s</span>
        <a class="cico" href="produs.html?id=%(id)d" aria-label="%(title_attr)s">%(icon)s</a>
      </div>
      <div class="card-body">
        <span class="cat">%(cattitle)s</span>
        <h3><a href="produs.html?id=%(id)d">%(title)s</a></h3>
        <div class="meta"><span>%(ficon)s %(pages)s</span><span>%(gicon)s %(lang)s</span><span class="level-pill">%(level)s</span></div>
        <div class="rating">★ %(rating)s <small>(%(votes)s)</small></div>
      </div>
      <div class="card-foot">
        <div class="price">%(price)d LEI %(old)s<div class="price-note">descărcare instantă</div></div>
        <button class="add" data-id="%(id)d" data-title="%(title_attr)s" data-price="%(price)d">%(cart)s Adaugă</button>
      </div>
    </article>""" % dict(
        cat=p["cat"], lang=p["lang"], level=p["level"], fmt=p["fmt"], price=p["price"],
        title=p["title"], title_attr=p["title"].replace('"', "&quot;"), title_lower=p["title"].lower().replace('"', "&quot;"), id=p["id"], grad=grad, heart=svg("heart", 16, 2),
        badge=badge, old=old, icon=svg(p["icon"], 28, 1.7), cattitle=cat_title(p["cat"]),
        ficon=svg("file", 13, 2), gicon=svg("globe", 13, 2),
        pages=p["pages"], rating=p["rating"], votes=p["votes"], cart=svg("cart", 15, 2))

def category_card(slug, title, desc, icon, grad):
    return """
    <a class="cat-card reveal" href="produse.html?cat=%s">
      <span class="cat-ico" style="background:%s">%s</span>
      <h3>%s</h3>
      <p>%s</p>
      <span class="go">Vezi produse %s</span>
    </a>""" % (slug, grad, svg(icon, 22), title, desc, svg("arrow", 16, 2))