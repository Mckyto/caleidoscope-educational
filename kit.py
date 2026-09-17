# -*- coding: utf-8 -*-
"""Kit comun complet pentru site-ul Caleidoscope Educational.ro."""

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

/* ---------- HEADER ---------- */
.hdr{position:sticky;top:0;z-index:60;background:rgba(255,255,255,.92);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.hdr-in{display:flex;align-items:center;gap:1.2rem;height:76px}
.brand{display:flex;align-items:center;gap:.65rem;flex-shrink:0}
.brand-name{font-weight:800;font-size:1.32rem;letter-spacing:-.02em}
.brand-name span{color:var(--violet)}
.brand-sub{font-size:.66rem;letter-spacing:.06em;color:var(--muted);font-weight:600}
.nav{display:flex;align-items:center;gap:.15rem;margin-left:auto}
.nav a{position:relative;padding:.55rem .8rem;border-radius:12px;font-weight:600;font-size:.94rem;color:var(--ink-2);transition:.2s}
.nav a:hover{color:var(--violet);background:#F4F1FF}
.nav a.active{color:var(--violet);background:#F1EDFF}
.hdr-actions{display:flex;align-items:center;gap:.55rem;margin-left:.6rem}
.icon-btn{position:relative;width:42px;height:42px;border-radius:50%;display:grid;place-items:center;border:1.5px solid var(--line);transition:.2s}
.icon-btn:hover{border-color:var(--violet);background:#F6F3FF}
.cart-count{position:absolute;top:-4px;right:-4px;min-width:20px;height:20px;border-radius:999px;background:var(--pink);color:#fff;font-size:.7rem;font-weight:700;display:grid;place-items:center;padding:0 5px}

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

.dom-list{background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.24);border-radius:20px;padding:1.1rem;backdrop-filter:blur(6px)}
.dom-list h3{font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;opacity:.85;margin-bottom:.7rem;font-weight:700}
.dom-list a{display:flex;align-items:center;justify-content:space-between;gap:.6rem;padding:.55rem .7rem;border-radius:12px;font-weight:650;font-size:.92rem;transition:.2s}
.dom-list a:hover{background:rgba(255,255,255,.2);transform:translateX(3px)}

.promo-card{background:#fff;color:var(--ink);border-radius:22px;padding:1.5rem;box-shadow:0 26px 55px rgba(23,12,58,.35)}
.promo-card h2{font-size:1.35rem;line-height:1.25;font-weight:800}
.promo-card p{color:var(--muted);font-size:.92rem;margin-top:.5rem}

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
.sec-head .eyebrow{font-size:.78rem;letter-spacing:.18em;text-transform:uppercase;font-weight:700;color:var(--violet)}
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

/* ---------- FOOTER ---------- */
.ftr{background:#150F2B;color:#C7C2E0;padding:3.2rem 0 1.2rem;margin-top:2rem}
.ftr-top{display:grid;grid-template-columns:1.4fr 1fr 1fr 1.2fr;gap:2rem}
.ftr h4{color:#fff;font-size:.95rem;margin-bottom:.9rem;font-weight:750}
.ftr a{color:#C7C2E0;font-size:.9rem;transition:.2s}
.ftr a:hover{color:#fff;padding-left:3px}
.ftr ul{display:grid;gap:.45rem}
.ftr-btm{border-top:1px solid #2A2350;margin-top:2.2rem;padding-top:1.2rem;display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;font-size:.82rem;color:#9892B8}
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
    "search": '<circle cx="11" cy="11" r="8"/><path d="M21 21l-4.3-4.3"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/>',
    "truck": '<path d="M1 4h13v11H1z"/><path d="M14 8h4l3 3v4h-7"/><circle cx="5.5" cy="18.5" r="2"/><circle cx="18.5" cy="18.5" r="2"/>',
    "headset": '<path d="M4 14v-2a8 8 0 0 1 16 0v2"/><path d="M4 14h3v6H5a2 2 0 0 1-2-2z"/><path d="M20 14h-3v6h2a2 2 0 0 0 2-2z"/>',
    "star": '<path d="M12 2l2.6 7.4H22l-6.1 4.6 2.3 7.4L12 17l-6.2 4.4 2.3-7.4L2 9.4h7.4z"/>',
    "cart": '<circle cx="9" cy="20" r="1.6"/><circle cx="18" cy="20" r="1.6"/><path d="M1 2h3l2.6 12.4a2 2 0 0 0 2 1.6h8.7a2 2 0 0 0 2-1.6L21 6H5"/>',
    "user": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "menu": '<path d="M3 6h18"/><path d="M3 12h18"/><path d="M3 18h18"/>',
    "arrow": '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>',
    "check": '<path d="M20 6L9 17l-5-5"/>',
}

def svg(name, size=22, sw=1.9, cls=""):
    p = ICONS.get(name, ICONS["star"])
    return ('<svg class="%s" width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="%s" stroke-linecap="round" stroke-linejoin="round">%s</svg>' % (cls, size, size, sw, p))

CATEGORIES = [
    ("carti-si-materiale-scolare", "Cărți și materiale școlare", "Manuale auxiliare, culegeri, sinteze", "book", "linear-gradient(135deg,#6D28D9,#4F46E5)"),
    ("exercitii-si-fise-de-lucru", "Exerciții și fișe de lucru", "Fișe printabile cu exerciții și barem", "edit", "linear-gradient(135deg,#0EA5A4,#22C1A5)"),
    ("povesti-si-carti-de-lectura", "Povești și cărți de lectură", "Lecturi pentru copii + fișe", "story", "linear-gradient(135deg,#EC4899,#F472B6)"),
    ("harti-si-atlase", "Hărți și atlase", "Hărți printabile A4/A3, atlase", "map", "linear-gradient(135deg,#F59E0B,#FBBF24)"),
    ("rezumate-si-eseuri", "Rezumate și eseuri", "Rezumate, comentarii, eseuri", "file", "linear-gradient(135deg,#4F46E5,#6366F1)"),
    ("schite-si-conspecte", "Schițe și conspecte", "Structuri, scheme, conspecte", "notes", "linear-gradient(135deg,#7C3AED,#A78BFA)"),
    ("limbi-straine-vocabular", "Limbi străine – vocabular", "Cuvinte și expresii pe teme", "globe", "linear-gradient(135deg,#0EA5A4,#38BDF8)"),
    ("audiobookuri", "Audiobookuri", "Cărți audio și lecții MP3", "audio", "linear-gradient(135deg,#8B5CF6,#EC4899)"),
    ("licenta-si-disertatie", "Licență și disertație", "Ghiduri, structuri, bibliografii", "cap", "linear-gradient(135deg,#1D4ED8,#3B82F6)"),
    ("literatura-de-specialitate", "Literatură de specialitate", "Sinteze și ghiduri de studiu", "lib", "linear-gradient(135deg,#B45309,#F59E0B)"),
    ("planuri-de-lucru-stiintifice", "Planuri de lucru științifice", "Modele de plan, metodologie", "science", "linear-gradient(135deg,#0F766E,#14B8A6)"),
    ("si-multe-altele", "Și multe altele...", "Resurse personalizate la cerere", "star", "linear-gradient(135deg,#DB2777,#F472B6)"),
]

DOMAINS = [
    ("Limbi străine", "limbi-straine", "globe"),
    ("Literatură", "literatura", "book"),
    ("Psihologie", "psihologie", "file"),
    ("Drept", "drept", "shield"),
    ("Criminalistică", "criminalistica", "search"),
    ("Psihiatrie", "psihiatrie", "book"),
]

LANGS = ["Engleză", "Franceză", "Spaniolă", "Germană", "Italiană"]

def head(title, desc, active):
    return f"""<!DOCTYPE html>
<html lang="ro">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<style>{CSS}</style>
</head>
<body>
<header class="hdr" id="hdr">
  <div class="wrap hdr-in">
    <a class="brand" href="index.html">
      <svg width="40" height="40" viewBox="0 0 44 44" aria-hidden="true">
        <rect x="1" y="1" width="42" height="42" rx="13" fill="%236D28D9"/>
        <g stroke="%23fff" stroke-width="1.6" fill="none"><circle cx="22" cy="22" r="12"/><path d="M22 10l10.4 18H11.6z"/><path d="M22 34L11.6 16h20.8z"/></g>
        <circle cx="22" cy="22" r="3.4" fill="%230EA5A4"/>
      </svg>
      <span class="brand-txt">
        <span class="brand-name">Caleido<span>scope</span></span>
        <span class="brand-sub">Educational.ro · Resurse pentru un viitor mai bun</span>
      </span>
    </a>
    <nav class="nav" id="nav">
      <a href="index.html" class="{'active' if active=='home' else ''}">Acasă</a>
      <a href="produse.html" class="{'active' if active=='produse' else ''}">Produse</a>
      <a href="categorii.html" class="{'active' if active=='categorii' else ''}">Categorii</a>
      <a href="despre.html" class="{'active' if active=='despre' else ''}">Despre noi</a>
      <a href="blog.html" class="{'active' if active=='blog' else ''}">Blog</a>
      <a href="contact.html" class="{'active' if active=='contact' else ''}">Contact</a>
    </nav>
    <div class="hdr-actions">
      <a class="icon-btn" href="cont.html">{svg("user", 20)}</a>
      <button class="icon-btn" id="cartBtn" aria-label="Coș">{svg("cart", 20)}<span class="cart-count" id="cartCount">0</span></button>
    </div>
  </div>
</header>
"""

def footer():
    return """
<footer class="ftr">
  <div class="wrap">
    <div class="ftr-top">
      <div>
        <h4>Caleidoscope Educational</h4>
        <p>Materiale educaționale create de profesori și autori: exerciții, povești, rezumate, eseuri, hărți, audiobookuri.</p>
      </div>
      <div>
        <h4>Categorii</h4>
        <ul>
          <li><a href="produse.html">Cărți și materiale</a></li>
          <li><a href="produse.html">Exerciții și fișe</a></li>
          <li><a href="produse.html">Povești de lectură</a></li>
        </ul>
      </div>
      <div>
        <h4>Informații utile</h4>
        <ul>
          <li><a href="despre.html">Despre noi</a></li>
          <li><a href="contact.html">Contact</a></li>
          <li><a href="termeni.html">Termeni și condiții</a></li>
        </ul>
      </div>
      <div>
        <h4>Suport clienți</h4>
        <p>Luni–Vineri: 09:00 – 18:00<br>contact@caleidoscope-educational.ro</p>
      </div>
    </div>
    <div class="ftr-btm">
      <span>© 2026 Caleidoscope Educational.ro — Toate drepturile rezervate.</span>
    </div>
  </div>
</footer>
<div class="toast" id="toast"></div>
<script>
(function(){
  var key='caleido_cart';
  function getCart(){ try{ return JSON.parse(localStorage.getItem(key))||[] }catch(e){ return [] } }
  function paint(){ var el=document.getElementById('cartCount'); if(el){ el.textContent=getCart().length } }
  paint();
  var cartBtn = document.getElementById('cartBtn');
  if(cartBtn){ cartBtn.addEventListener('click', function(){ window.location.href = 'checkout.html'; }); }
})();
</script>
</body>
</html>
"""

def category_card(slug, title, desc, icon, grad):
    return f"""
    <a class="cat-card" href="produse.html?cat={slug}">
      <span class="cat-ico" style="background:{grad}">{svg(icon, 22)}</span>
      <h3>{title}</h3>
      <p>{desc}</p>
      <span class="go">Vezi produse →</span>
    </a>"""