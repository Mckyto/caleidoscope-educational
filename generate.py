# -*- coding: utf-8 -*-
"""Script principal de generare a paginilor pentru Caleidoscope Educational.ro"""

from kit import head, footer, category_card, CATEGORIES, DOMAINS, LANGS, svg

PRODUCTS = [
    dict(id=1, title="Engleză pentru începători A1–A2: 200 de exerciții + vocabular", cat="limbi-straine-vocabular", dom="limbi-straine", lang="Engleză", level="A1–A2", fmt="PDF", pages="124 pagini", price=49, old=69, badge="Bestseller", rating=4.9, votes=214, icon="globe"),
    dict(id=2, title="Gramatica limbii germane explicată simplu – Nivel A1–B1", cat="limbi-straine-vocabular", dom="limbi-straine", lang="Germană", level="A1–B1", fmt="PDF", pages="98 pagini", price=45, old=60, badge="", rating=4.8, votes=156, icon="globe"),
    dict(id=6, title="Rezumat „Romeo și Julieta” – Shakespeare (analiză + personaje)", cat="rezumate-si-eseuri", dom="literatura", lang="Română", level="Liceu", fmt="PDF", pages="32 pagini", price=19, old=25, badge="Bestseller", rating=4.9, votes=389, icon="file"),
    dict(id=7, title="Eseu argumentativ complet: „Moara cu noroc” de Ioan Slavici", cat="rezumate-si-eseuri", dom="literatura", lang="Română", level="Bacalaureat", fmt="PDF", pages="24 pagini", price=25, old=35, badge="Esențial", rating=4.9, votes=512, icon="file"),
    dict(id=10, title="Fișe de lucru Matematică clasa a V-a – 200 de exerciții cu barem", cat="exercitii-si-fise-de-lucru", dom="psihologie", lang="Română", level="Primar/Gimnaziu", fmt="PDF", pages="110 pagini", price=35, old=45, badge="", rating=4.8, votes=203, icon="edit"),
    dict(id=12, title="Introducere în Psihologia Cognitivă – Note de curs și sinteze", cat="schite-si-conspecte", dom="psihologie", lang="Română", level="Studenți", fmt="PDF", pages="160 pagini", price=69, old=90, badge="Popular", rating=4.9, votes=175, icon="notes"),
    dict(id=13, title="Ghid practic de Drept Civil: Contracte și Obligații", cat="literatura-de-specialitate", dom="drept", lang="Română", level="Universitar", fmt="PDF", pages="210 pagini", price=89, old=120, badge="Avansat", rating=4.9, votes=230, icon="shield"),
]

def build_index():
    cat_html = "".join(category_card(slug, title, desc, icon, grad) for slug, title, desc, icon, grad in CATEGORIES)
    domains_html = "".join(f'<a href="produse.html?dom={slug}">{name} {svg(icon, 16, 2)}</a>' for name, slug, icon in DOMAINS)
    langs_html = "".join(f'<a href="produse.html?lang={lang}">{lang}</a>' for lang in LANGS)

    html = head("Caleidoscope Educational.ro — Resurse educaționale", "Materiale educaționale, cărți, exerciții, rezumate, eseuri.", "home") + f"""
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="badge-pill">✨ Platformă educațională 100% digitală</span>
      <h1>Tot ce ai nevoie pentru <span class="grad-text" style="color:#fff">învățare, dezvoltare și succes!</span></h1>
      <p class="lead">Materiale educaționale, cărți, exerciții, rezumate, eseuri, hărți, ghiduri și audiobookuri — pentru toate nivelurile și toate domeniile de interes.</p>
      
      <form class="searchbar" action="produse.html" method="GET">
        <input type="text" name="q" placeholder="Caută resurse, de ex. rezumat Romeo și Julieta">
        <button type="submit">Caută</button>
      </form>
    </div>

    <div class="dom-list">
      <h3>Domenii populare</h3>
      {domains_html}
    </div>

    <div class="promo-card">
      <h2>Învață în ritmul tău</h2>
      <p>Materiale create de profesori cu experiență, gata pentru descărcare instantă pe orice dispozitiv.</p>
    </div>

    <div class="lang-col">
      <h3>Limbi străine</h3>
      {langs_html}
    </div>
  </div>
</section>

<section class="trust">
  <div class="wrap trust-grid">
    <div class="trust-item">{svg("search", 24, 2)}<div><b>Acces rapid</b><small>Găsești ușor ce ai nevoie</small></div></div>
    <div class="trust-item">{svg("shield", 24, 2)}<div><b>Plată sigură</b><small>Tranzacții 100% securizate</small></div></div>
    <div class="trust-item">{svg("truck", 24, 2)}<div><b>Livrare instant</b><small>Acces imediat după comandă</small></div></div>
    <div class="trust-item">{svg("headset", 24, 2)}<div><b>Suport clienți</b><small>Suntem aici pentru tine</small></div></div>
    <div class="trust-item">{svg("check", 24, 2)}<div><b>Resurse verificate</b><small>Calitate și acuratețe garantate</small></div></div>
  </div>
</section>

<section class="wrap">
  <div class="sec-head">
    <span class="eyebrow">Categorii principale</span>
    <h2>Explorează categoriile noastre</h2>
    <p>Descoperă o lume întreagă de resurse educaționale, într-un singur loc!</p>
  </div>
  <div class="cat-grid">{cat_html}</div>
</section>

{footer()}
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: index.html")

def build_produse():
    html = head("Produse și Resurse — Caleidoscope Educational", "Catalog complet de materiale educaționale.", "produse") + f"""
<div class="wrap" style="padding: 3rem 0 5rem;">
  <div style="margin-bottom: 2rem;">
    <span class="eyebrow">Catalog complet</span>
    <h1 style="font-size: 2.2rem; font-weight: 800; margin-top: .3rem;" id="pageTitle">Toate resursele educaționale</h1>
    <p style="color: var(--muted); margin-top: .4rem;">Materiale verificate, gata pentru descărcare instantă.</p>
  </div>

  <div style="display: grid; grid-template-columns: 260px 1fr; gap: 2rem; align-items: start;">
    <aside style="background: #F8F7FF; padding: 1.5rem; border-radius: 18px; border: 1.5px solid var(--line);">
      <h3 style="font-size: 1rem; font-weight: 750; margin-bottom: 1rem;">Filtrează după</h3>
      <div style="display: grid; gap: .75rem;">
        <a href="produse.html" style="font-weight: 600; font-size: .92rem; color: var(--violet);">✨ Toate produsele</a>
        <h4 style="font-size: .8rem; text-transform: uppercase; color: var(--muted); margin-top: .8rem; letter-spacing: .08em;">Categorii</h4>
        {"".join(f'<a href="produse.html?cat={s}" style="font-size:.9rem; color: var(--ink-2);">{t}</a>' for s, t, _, _, _ in CATEGORIES)}
      </div>
    </aside>

    <div>
      <div id="prodGrid" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.5rem;"></div>
      <div id="noResults" style="display: none; text-align: center; padding: 4rem 0; color: var(--muted);">
        <h3>Nu am găsit niciun produs în această categorie.</h3>
        <p style="margin-top: .5rem;"><a href="produse.html" style="color: var(--violet); font-weight: 600;">Vezi toate produsele →</a></p>
      </div>
    </div>
  </div>
</div>

<script>
const PRODUCTS = {PRODUCTS};
function renderProducts() {{
  const params = new URLSearchParams(window.location.search);
  const cat = params.get('cat');
  const dom = params.get('dom');
  const lang = params.get('lang');
  const q = params.get('q');

  let filtered = PRODUCTS;
  let title = "Toate resursele educaționale";

  if(cat) {{ filtered = PRODUCTS.filter(p => p.cat === cat); title = "Categorie: " + cat.replace(/-/g, ' '); }}
  else if(dom) {{ filtered = PRODUCTS.filter(p => p.dom === dom); title = "Domeniu: " + dom.replace(/-/g, ' '); }}
  else if(lang) {{ filtered = PRODUCTS.filter(p => p.lang === lang); title = "Limba: " + lang; }}
  else if(q) {{ filtered = PRODUCTS.filter(p => p.title.toLowerCase().includes(q.toLowerCase())); title = "Rezultate căutare: \"" + q + "\""; }}

  document.getElementById('pageTitle').textContent = title.charAt(0).toUpperCase() + title.slice(1);
  const grid = document.getElementById('prodGrid');
  const noRes = document.getElementById('noResults');

  if(filtered.length === 0) {{ grid.innerHTML = ''; noRes.style.display = 'block'; return; }}

  noRes.style.display = 'none';
  grid.innerHTML = filtered.map(p => `
    <div style="background:#fff; border:1.5px solid var(--line); border-radius:18px; padding:1.4rem; display:flex; flex-direction:column; gap:.8rem; box-shadow:var(--shadow);">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <span style="background:#F1EDFF; color:var(--violet); font-size:.75rem; font-weight:700; padding:.25rem .7rem; border-radius:999px;">${{p.fmt}}</span>
        <span style="font-size:.8rem; color:var(--muted); font-weight:600;">⭐ ${{p.rating}} (${{p.votes}})</span>
      </div>
      <h3 style="font-size:1.02rem; font-weight:750; line-height:1.35;"><a href="produs.html?id=${{p.id}}" style="color:var(--ink);">${{p.title}}</a></h3>
      <div style="font-size:.85rem; color:var(--muted); display:flex; gap:1rem;"><span>📚 ${{p.pages}}</span><span>🌐 ${{p.lang}}</span></div>
      <div style="margin-top:auto; display:flex; align-items:center; justify-content:space-between; padding-top:.8rem; border-top:1px solid var(--line);">
        <div><span style="font-size:1.25rem; font-weight:800; color:var(--violet);">${{p.price}} LEI</span></div>
        <button onclick="addToCart(${{p.id}})" style="background:var(--grad); color:#fff; font-weight:700; font-size:.88rem; padding:.55rem 1rem; border-radius:999px;">Adaugă în coș</button>
      </div>
    </div>
  `).join('');
}}
function addToCart(id) {{
  let cart = [];
  try {{ cart = JSON.parse(localStorage.getItem('caleido_cart')) || []; }} catch(e){{}}
  if(!cart.includes(id)) {{
    cart.push(id);
    localStorage.setItem('caleido_cart', JSON.stringify(cart));
    const countEl = document.getElementById('cartCount');
    if(countEl) countEl.textContent = cart.length;
    alert("Produsul a fost adăugat în coș!");
  }} else {{ alert("Produsul este deja în coș!"); }}
}}
renderProducts();
</script>
""" + footer()
    with open("produse.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: produse.html")

def build_categorii():
    cat_cards = "".join(category_card(slug, title, desc, icon, grad) for slug, title, desc, icon, grad in CATEGORIES)
    html = head("Categorii — Caleidoscope Educational", "Explorează toate categoriile de resurse educaționale.", "categorii") + f"""
<div class="wrap" style="padding: 3rem 0 5rem;">
  <div class="sec-head" style="margin-bottom: 3rem;">
    <span class="eyebrow">Index Categorii</span>
    <h2>Toate domeniile și categoriile educaționale</h2>
    <p>Alege categoria dorită pentru a explora materialele disponibile.</p>
  </div>
  <div class="cat-grid">{cat_cards}</div>
</div>
""" + footer()
    with open("categorii.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: categorii.html")

def build_despre():
    html = head("Despre noi — Caleidoscope Educational", "Află povestea platformei Caleidoscope Educational.", "despre") + f"""
<div class="wrap" style="padding: 4rem 0 6rem; max-width: 800px;">
  <span class="eyebrow">Despre proiect</span>
  <h1 style="font-size: 2.5rem; font-weight: 800; margin-top: .4rem; margin-bottom: 1.5rem;">Misiunea noastră pentru educație</h1>
  <p style="font-size: 1.1rem; line-height: 1.7; color: var(--ink-2); margin-bottom: 1.2rem;">
    <b>Caleidoscope Educational</b> s-a născut din pasiune pentru învățare și din dorința de a pune la dispoziția elevilor, studenților și profesorilor materiale didactice de cea mai înaltă calitate, clare și ușor de parcurs.
  </p>
  <p style="font-size: 1.1rem; line-height: 1.7; color: var(--ink-2); margin-bottom: 1.2rem;">
    Fiecare resursă — fie că este vorba despre culegeri de exerciții, sinteze pentru examene, eseuri structurate sau ghiduri de limbi străine — este concepută cu rigurozitate academică și adaptată cerințelor actuale.
  </p>
</div>
""" + footer()
    with open("despre.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: despre.html")

def build_contact():
    html = head("Contact — Caleidoscope Educational", "Ia legătura cu echipa noastră.", "contact") + f"""
<div class="wrap" style="padding: 4rem 0 6rem; max-width: 700px;">
  <span class="eyebrow">Contactează-ne</span>
  <h1 style="font-size: 2.5rem; font-weight: 800; margin-top: .4rem; margin-bottom: 1rem;">Suntem aici pentru tine</h1>
  <p style="color: var(--muted); margin-bottom: 2rem;">Ai întrebări despre materiale sau comenzi? Scrie-ne un mesaj.</p>
  
  <div style="background: #F8F7FF; border: 1.5px solid var(--line); border-radius: 20px; padding: 2rem;">
    <div style="margin-bottom: 1.2rem;"><b>Email suport:</b> contact@caleidoscope-educational.ro</div>
    <div style="margin-bottom: 1.2rem;"><b>Program:</b> Luni – Vineri, 09:00 – 18:00</div>
    <div><b>Livrare:</b> Instant prin descărcare digitală (PDF / Audio).</div>
  </div>
</div>
""" + footer()
    with open("contact.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: contact.html")

def build_checkout():
    html = head("Finalizare comandă — Caleidoscope Educational", "Coș de cumpărături și finalizare comandă.", "produse") + f"""
<div class="wrap" style="padding: 3rem 0 6rem; max-width: 900px;">
  <span class="eyebrow">Checkout</span>
  <h1 style="font-size: 2.2rem; font-weight: 800; margin-top: .3rem; margin-bottom: 2rem;">Coșul tău de cumpărături</h1>

  <div style="display: grid; grid-template-columns: 1.4fr 1fr; gap: 2rem;">
    <div style="background: #fff; border: 1.5px solid var(--line); border-radius: 18px; padding: 1.5rem;">
      <h3 style="font-size: 1.1rem; font-weight: 750; margin-bottom: 1rem;">Produse selectate</h3>
      <div id="cartItems"><p style="color: var(--muted);">Coșul este gol.</p></div>
    </div>

    <div style="background: #F8F7FF; border: 1.5px solid var(--line); border-radius: 18px; padding: 1.5rem; height: fit-content;">
      <h3 style="font-size: 1.1rem; font-weight: 750; margin-bottom: 1rem;">Sumar comandă</h3>
      <div style="display: flex; justify-content:space-between; margin-bottom: 1rem; font-weight: 700; font-size: 1.1rem;">
        <span>Total de plată:</span>
        <span id="cartTotal" style="color: var(--violet);">0 LEI</span>
      </div>
      <button onclick="alert('Comandă plasată cu succes! Veți primi materialele pe email.')" style="width: 100%; background: var(--grad); color: #fff; font-weight: 700; padding: .8rem; border-radius: 999px;">Plasează comanda</button>
    </div>
  </div>
</div>

<script>
const PRODUCTS = {PRODUCTS};
function renderCart() {{
  let cart = [];
  try {{ cart = JSON.parse(localStorage.getItem('caleido_cart')) || []; }} catch(e){{}}
  const container = document.getElementById('cartItems');
  const totalEl = document.getElementById('cartTotal');

  if(cart.length === 0) {{
    container.innerHTML = '<p style="color: var(--muted);">Coșul tău este gol. Adaugă produse din catalog.</p>';
    totalEl.textContent = '0 LEI';
    return;
  }}

  let total = 0;
  container.innerHTML = cart.map(id => {{
    const p = PRODUCTS.find(item => item.id === id);
    if(!p) return '';
    total += p.price;
    return `
      <div style="display: flex; justify-content: space-between; align-items: center; padding: .8rem 0; border-bottom: 1px solid var(--line);">
        <div>
          <h4 style="font-size: .95rem; font-weight: 700;">${{p.title}}</h4>
          <span style="font-size: .8rem; color: var(--muted);">${{p.price}} LEI</span>
        </div>
        <button onclick="removeItem(${{p.id}})" style="color: var(--pink); font-size: .85rem; font-weight: 700;">Șterge</button>
      </div>
    `;
  }}).join('');
  totalEl.textContent = total + ' LEI';
}}
function removeItem(id) {{
  let cart = [];
  try {{ cart = JSON.parse(localStorage.getItem('caleido_cart')) || []; }} catch(e){{}}
  cart = cart.filter(i => i !== id);
  localStorage.setItem('caleido_cart', JSON.stringify(cart));
  renderCart();
}}
renderCart();
</script>
""" + footer()
    with open("checkout.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: checkout.html")

if __name__ == "__main__":
    build_index()
    build_produse()
    build_categorii()
    build_despre()
    build_contact()
    build_checkout()
    
    # Restul paginilor standard
    for p in ["blog", "termeni", "cont", "produs"]:
        html = head(p.capitalize() + " — Caleidoscope Educational", "Resurse educaționale", p) + f"""
        <div class="wrap" style="padding: 4rem 0 6rem; max-width: 800px;">
            <span class="eyebrow">Informații</span>
            <h1 style="font-size: 2.2rem; font-weight: 800; margin-top: .3rem; margin-bottom: 1rem;">{p.capitalize()}</h1>
            <p style="color: var(--muted); line-height: 1.6;">Această secțiune face parte din platforma educațională Caleidoscope. Conținutul este actualizat la zi pentru toți utilizatorii.</p>
        </div>
        """ + footer()
        with open(f"{p}.html", "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generat: {p}.html")
    print("Toate paginile au fost generate complet și profesional!")