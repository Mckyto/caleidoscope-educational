# -*- coding: utf-8 -*-
"""Kit comun pentru site-ul Caleidoscope Educational.ro (CSS, iconițe, date, header/footer)."""

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
.hdr-actions{display:flex;align-items:center;gap:.55rem;margin-left:.6rem}
.icon-btn{position:relative;width:42px;height:42px;border-radius:50%;display:grid;place-items:center;border:1.5px solid var(--line);transition:.2s}
.icon-btn:hover{border-color:var(--violet);background:#F6F3FF}
.cart-count{position:absolute;top:-4px;right:-4px;min-width:20px;height:20px;border-radius:999px;background:var(--pink);color:#fff;font-size:.7rem;font-weight:700;display:grid;place-items:center;padding:0 5px}

/* ---------- FOOTER ---------- */
.ftr{background:#150F2B;color:#C7C2E0;padding:3.2rem 0 1.2rem;margin-top:2rem}
.ftr-top{display:grid;grid-template-columns:1.4fr 1fr 1fr 1.2fr;gap:2rem}
.ftr h4{color:#fff;font-size:.95rem;margin-bottom:.9rem;font-weight:750}
.ftr a{color:#C7C2E0;font-size:.9rem;transition:.2s}
.ftr a:hover{color:#fff;padding-left:3px}
.ftr ul{display:grid;gap:.45rem}
.ftr-btm{border-top:1px solid #2A2350;margin-top:2.2rem;padding-top:1.2rem;display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;font-size:.82rem;color:#9892B8}

/* ---------- MISC ---------- */
.toast{position:fixed;bottom:1.5rem;right:1.5rem;background:var(--ink);color:#fff;padding:.85rem 1.2rem;border-radius:14px;box-shadow:var(--shadow-lg);z-index:99;opacity:0;transform:translateY(12px);transition:.3s;pointer-events:none;font-size:.9rem}
.toast.show{opacity:1;transform:none}
"""

ICONS = {
    "book": '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>',
    "edit": '<path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4z"/>',
    "story": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
    "map": '<path d="M1 6l7-3 8 3 7-3v15l-7 3-8-3-7 3z"/><path d="M8 3v15"/><path d="M16 6v15"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M8 13h8"/><path d="M8 17h5"/>',
    "notes": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M8 8h8"/><path d="M8 12h8"/><path d="M8 16h5"/>',
    "globe": '<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    "star": '<path d="M12 2l2.6 7.4H22l-6.1 4.6 2.3 7.4L12 17l-6.2 4.4 2.3-7.4L2 9.4h7.4z"/>',
    "cart": '<circle cx="9" cy="20" r="1.6"/><circle cx="18" cy="20" r="1.6"/><path d="M1 2h3l2.6 12.4a2 2 0 0 0 2 1.6h8.7a2 2 0 0 0 2-1.6L21 6H5"/>',
    "user": '<path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
    "menu": '<path d="M3 6h18"/><path d="M3 12h18"/><path d="M3 18h18"/>',
    "arrow": '<path d="M5 12h14"/><path d="M13 6l6 6-6 6"/>',
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
]

DOMAINS = ["Limbi străine", "Literatură", "Psihologie", "Drept"]
LANGS = ["Engleză", "Franceză", "Română"]

PRODUCTS = [
    dict(id=1, title="Engleză pentru începători A1–A2: 200 de exerciții + vocabular", cat="carti-si-materiale-scolare", lang="Engleză", level="A1–A2", fmt="PDF", pages="124 pagini", price=49, old=69, badge="Bestseller", rating=4.9, votes=214, icon="globe"),
    dict(id=6, title="Rezumat „Romeo și Julieta” – Shakespeare (analiză + personaje)", cat="rezumate-si-eseuri", lang="Română", level="Liceu", fmt="PDF", pages="32 pagini", price=19, old=25, badge="Bestseller", rating=4.9, votes=389, icon="file"),
    dict(id=10, title="Fișe de lucru Matematică clasa a V-a – 200 de exerciții cu barem", cat="exercitii-si-fise-de-lucru", lang="Română", level="Primar/Gimnaziu", fmt="PDF", pages="110 pagini", price=35, old=45, badge="", rating=4.8, votes=203, icon="edit"),
]

def cat_title(slug):
    for s, t, d, i, g in CATEGORIES:
        if s == slug:
            return t
    return "Resurse"

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
      <span class="brand-name">Caleido<span>scope</span></span>
    </a>
    <nav class="nav" id="nav">
      <a href="index.html">Acasă</a>
      <a href="produse.html">Produse</a>
      <a href="categorii.html">Categorii</a>
      <a href="despre.html">Despre noi</a>
      <a href="contact.html">Contact</a>
    </nav>
    <div class="hdr-actions">
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
        <p>Materiale educaționale create de profesori și autori.</p>
      </div>
    </div>
    <div class="ftr-btm">
      <span>© 2026 Caleidoscope Educational.ro</span>
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

def product_card(p):
    return f"""<div class="card"><h3>{p['title']}</h3><p>{p['price']} LEI</p></div>"""

def category_card(slug, title, desc, icon, grad):
    return f"""<div class="cat-card"><h3>{title}</h3><p>{desc}</p></div>"""