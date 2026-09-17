# -*- coding: utf-8 -*-
"""Script principal de generare a paginilor pentru Caleidoscope Educational.ro

Rulare:  python3 generate.py
Toate paginile sunt scrise în directorul curent (rădăcina repo-ului, servită de GitHub Pages).
"""

import json
from datetime import date

from kit import (head, footer, category_card, product_card, cat_title, svg,
                 CATEGORIES, DOMAINS, LANGS, PRODUCTS, GRADIENTS, DESCRIPTIONS, CAT_DESC, SITE_URL)

ARROW = svg("arrow", 17, 2)
CHECK = svg("check", 18, 2.4)

# Subset serializabil al produselor, folosit de paginile care randează pe client (produs, favorite, checkout)
PRODUCTS_JSON = json.dumps(
    [dict({k: p[k] for k in ("id", "title", "cat", "lang", "level", "fmt", "pages", "price", "old", "badge", "rating", "votes", "icon")},
          cattitle=cat_title(p["cat"]), desc=DESCRIPTIONS.get(p["id"], CAT_DESC)) for p in PRODUCTS],
    ensure_ascii=False)
GRADIENTS_JSON = json.dumps(GRADIENTS)

# Cupoane acceptate la checkout (cod -> procent reducere). Validate pe client (site static).
COUPONS = {"BUNVENIT10": 10, "SCOALA15": 15, "STUDENT20": 20}

# Script JS partajat: construiește un card de produs din obiectul JSON (identic vizual cu product_card din kit.py)
CARD_JS = """
var G=%s;
function esc(s){ return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/"/g,'&quot;') }
function ico(n,size){ var P={file:'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M8 13h8"/><path d="M8 17h5"/>',globe:'<circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',heart:'<path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1.1-1.1a5.5 5.5 0 0 0-7.8 7.8l8.9 8.9 8.8-8.8a5.5 5.5 0 0 0 0-7.8z"/>',cart:'<circle cx="9" cy="20" r="1.6"/><circle cx="18" cy="20" r="1.6"/><path d="M1 2h3l2.6 12.4a2 2 0 0 0 2 1.6h8.7a2 2 0 0 0 2-1.6L21 6H5"/>',book:'<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/>'};
  return '<svg width="'+size+'" height="'+size+'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">'+(P[n]||P.book)+'</svg>' }
function cardHTML(x){
  return '<article class="card reveal" data-id="'+x.id+'"><div class="cover" style="background:'+(G[x.icon]||G.file)+'">'
   +(x.badge?'<span class="tag">'+esc(x.badge)+'</span>':'')
   +'<button class="wish" data-id="'+x.id+'" aria-label="Favorite">'+ico('heart',16)+'</button>'
   +'<span class="fmt">'+esc(x.fmt)+'</span><a class="cico" href="produs.html?id='+x.id+'">'+ico(x.icon,28)+'</a></div>'
   +'<div class="card-body"><span class="cat">'+esc(x.cattitle)+'</span><h3><a href="produs.html?id='+x.id+'">'+esc(x.title)+'</a></h3>'
   +'<div class="meta"><span>'+ico('file',13)+' '+esc(x.pages)+'</span><span>'+ico('globe',13)+' '+esc(x.lang)+'</span><span class="level-pill">'+esc(x.level)+'</span></div>'
   +'<div class="rating">★ '+x.rating+' <small>('+x.votes+')</small></div></div>'
   +'<div class="card-foot"><div class="price">'+x.price+' LEI '+(x.old?'<small>'+x.old+' LEI</small>':'')+'<div class="price-note">descărcare instantă</div></div>'
   +'<button class="add" data-id="'+x.id+'" data-title="'+esc(x.title)+'" data-price="'+x.price+'">'+ico('cart',15)+' Adaugă</button></div></article>';
}
""" % GRADIENTS_JSON


def write(name, html):
    with open(name, "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: %s" % name)


def page_head(title, crumb, lead=""):
    return """
<div class="page-head"><div class="wrap">
  <div class="breadcrumb"><a href="index.html">Acasă</a> › <span>%s</span></div>
  <h1>%s</h1>
  %s
</div></div>""" % (crumb, title, "<p>%s</p>" % lead if lead else "")


# ------------------------------------------------------------------ INDEX
def build_index():
    cats = "".join(category_card(*c) for c in CATEGORIES)
    dom_map = {"Limbi străine": "limbi-straine-vocabular", "Literatură": "rezumate-si-eseuri"}
    doms = "".join('<a href="produse.html?cat=%s">%s<span>→</span></a>' % (dom_map.get(n, "literatura-de-specialitate"), n)
                   for n, s, i in DOMAINS)
    langs = "".join('<a href="produse.html?lang=%s">%s</a>' % (l, l) for l in LANGS[:5])
    chips = "".join('<a class="chip" href="produse.html?q=%s">%s</a>' % (c, c)
                    for c in ["exerciții", "eseuri", "limbi străine", "licență", "disertație", "audiobook"])
    best = "".join(product_card(p) for p in sorted(PRODUCTS, key=lambda x: -x["votes"])[:8])
    new = "".join(product_card(p) for p in [p for p in PRODUCTS if p["badge"] == "Nou"] + sorted(PRODUCTS, key=lambda x: -x["id"])[:4])[:4] or ""
    new = "".join(product_card(p) for p in sorted(PRODUCTS, key=lambda x: (x["badge"] != "Nou", -x["id"]))[:4])

    trust = [("bolt", "Acces rapid", "Găsești ușor ce ai nevoie"),
             ("lock", "Plată sigură", "Tranzacții 100% securizate"),
             ("truck", "Livrare instant", "Acces imediat după comandă"),
             ("headset", "Suport clienți", "Suntem aici pentru tine"),
             ("checkc", "Resurse verificate", "Calitate și acuratețe garantate")]
    trust_html = "".join('<div class="trust-item">%s<div><b>%s</b><small>%s</small></div></div>' % (svg(i, 24), t, s) for i, t, s in trust)

    steps = [("1. Cauți și alegi", "Filtrezi după materie, limbă, nivel sau format. Ai previzualizare cu cuprins și pagini-exemplu."),
             ("2. Plătești în siguranță", "Card, Apple/Google Pay sau transfer. Primești factura fiscală automat pe e-mail."),
             ("3. Descarci instant", "Linkul de descărcare apare în contul tău și în e-mail, valabil 12 luni, oricâte re-descărcări.")]
    steps_html = "".join('<div class="step reveal"><div class="num">%d</div><h3>%s</h3><p>%s</p></div>' % (i + 1, t, d) for i, (t, d) in enumerate(steps))

    testimonials = [("Ana M., profesoară", "Fișele de matematică pentru clasa a V-a mi-au economisit ore întregi de pregătire. Baremul e clar, exercițiile sunt gradate."),
                    ("Radu P., student", "Ghidul pentru tema de licență m-a scos din impas. Am ales tema în două zile, după luni de amânare."),
                    ("Ioana D., mamă", "Poveștile ilustrate au devenit ritualul nostru de seară. Copiii cer «încă una» în fiecare zi.")]
    testi_html = "".join('<div class="tile reveal"><div class="rating" style="margin-bottom:.6rem">★★★★★</div><p style="color:var(--ink-2);font-size:.95rem">„%s”</p><b style="display:block;margin-top:.9rem;font-size:.88rem">%s</b></div>' % (t, n) for n, t in testimonials)

    body = """
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow" style="color:#C4B5FD">Caleidoscope Educational.ro</span>
      <h1>Tot ce ai nevoie pentru învățare, dezvoltare și succes!</h1>
      <p class="lead">Materiale educaționale, cărți, exerciții, rezumate, eseuri, hărți, ghiduri, audiobooks și multe altele – pentru toate nivelurile și toate domeniile de interes.</p>
      <form class="searchbar" action="produse.html" method="get" role="search">
        <input type="search" name="q" placeholder='Caută resurse, de ex. rezumat Romeo și Julieta' aria-label="Caută resurse">
        <button type="submit">Caută</button>
      </form>
      <div class="chips">__CHIPS__</div>
      <span class="badge-pill">__STAR__ Resurse educaționale</span>
    </div>

    <div class="dom-list">
      <h3>Domenii</h3>
      __DOMS__
    </div>

    <div class="promo-card">
      <h2>Mai multă cunoaștere,<br>mai multe posibilități!</h2>
      <p>Învățăm azi, construim mâine! Alege resursa potrivită nivelului tău și transformă învățarea într-un proces simplu.</p>
      <div class="stats">
        <div class="stat"><b>1.200+</b><small>resurse</small></div>
        <div class="stat"><b>5</b><small>limbi străine</small></div>
        <div class="stat"><b>8</b><small>domenii</small></div>
      </div>
      <a class="btn btn-primary" style="width:100%;justify-content:center;margin-top:1.1rem" href="produse.html">Explorează catalogul __ARROW__</a>
    </div>

    <div class="lang-col">
      <h3>Limbi</h3>
      __LANGS__
    </div>
  </div>
</section>

<div class="trust"><div class="wrap trust-grid">__TRUST__</div></div>

<section>
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Catalog</span>
      <h2>Explorează categoriile noastre</h2>
      <p>Descoperă o lume întreagă de resurse educaționale, într-un singur loc!</p>
    </div>
    <div class="cat-grid">__CATS__</div>
  </div>
</section>

<section style="background:var(--bg)">
  <div class="wrap">
    <div class="sec-head">
      <span class="eyebrow">Cele mai descărcate</span>
      <h2>Resursele preferate de clienți</h2>
      <p>Descărcări instantanee, conținut verificat și actualizat periodic.</p>
    </div>
    <div class="prod-grid">__BEST__</div>
    <div style="text-align:center;margin-top:2rem"><a class="btn btn-primary" href="produse.html">Vezi toate produsele __ARROW__</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Noutăți</span><h2>Ultimele resurse adăugate</h2></div>
    <div class="prod-grid">__NEW__</div>
  </div>
</section>

<section style="background:var(--bg)">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Cum funcționează</span><h2>Trei pași până la resursa ta</h2></div>
    <div class="steps">__STEPS__</div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Păreri</span><h2>Ce spun cei care învață cu noi</h2></div>
    <div class="grid-3">__TESTI__</div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="cta-band">
      <h2>Primești 10% reducere la prima comandă</h2>
      <p>Abonează-te la newsletter și îți trimitem prin e-mail un cod de reducere, plus o fișă de lucru gratuită în fiecare săptămână.</p>
      <form class="form" onsubmit="event.preventDefault();Caleido.toast('Mulțumim! Codul tău: BUNVENIT10 (îl poți folosi acum la checkout).');this.reset();">
        <input type="email" required placeholder="Adresa ta de e-mail" aria-label="E-mail">
        <button type="submit">Vreau reducerea</button>
      </form>
      <small>Fără spam. Te poți dezabona oricând, dintr-un singur clic.</small>
    </div>
  </div>
</section>
"""
    for k, v in [("__CHIPS__", chips), ("__DOMS__", doms), ("__LANGS__", langs), ("__TRUST__", trust_html), ("__CATS__", cats),
                 ("__BEST__", best), ("__NEW__", new), ("__STEPS__", steps_html), ("__TESTI__", testi_html),
                 ("__STAR__", svg("star", 14, 2)), ("__ARROW__", ARROW)]:
        body = body.replace(k, v)
    write("index.html", head("Caleidoscope Educational.ro — Resurse educaționale, cărți, exerciții, rezumate, eseuri, hărți, audiobookuri",
                             "Tot ce ai nevoie pentru învățare, dezvoltare și succes: materiale educaționale, exerciții, rezumate, eseuri, hărți, ghiduri și audiobookuri.",
                             "home", page="") + body + footer())


# ------------------------------------------------------------------ PRODUSE (catalog cu filtre)
SHOP_JS = """
<script>
(function(){
  var grid=document.getElementById('grid');
  var cards=[].slice.call(grid.querySelectorAll('.card'));
  var out=document.getElementById('count'), empty=document.getElementById('empty'), chipsBox=document.getElementById('activeChips');
  var norm=function(s){ return (s||'').toLowerCase().normalize('NFD').replace(/[\\u0300-\\u036f]/g,'') };
  function val(name){ return [].slice.call(document.querySelectorAll('input[name="'+name+'"]:checked')).map(function(i){return i.value}); }
  function apply(push){
    var cats=val('cat'), langs=val('lang'), fmts=val('fmt'), lvls=val('level');
    var maxP=parseInt(document.getElementById('range').value,10);
    var q=norm(document.getElementById('q').value).trim();
    var sort=document.getElementById('sort').value, shown=0;
    cards.forEach(function(c){
      var ok=(!cats.length||cats.indexOf(c.dataset.cat)>-1)
          && (!langs.length||langs.indexOf(c.dataset.lang)>-1)
          && (!fmts.length||fmts.indexOf(c.dataset.fmt)>-1)
          && (!lvls.length||lvls.indexOf(c.dataset.level)>-1)
          && (parseInt(c.dataset.price,10)<=maxP)
          && (!q || norm(c.dataset.title).indexOf(q)>-1 || norm(c.dataset.cat).indexOf(q)>-1 || norm(c.dataset.lang).indexOf(q)>-1);
      c.style.display=ok?'':'none'; if(ok) shown++;
    });
    var by={ 'popular':function(a,b){return b.dataset.votes-a.dataset.votes}, 'rating':function(a,b){return b.dataset.rating-a.dataset.rating},
             'price-asc':function(a,b){return a.dataset.price-b.dataset.price}, 'price-desc':function(a,b){return b.dataset.price-a.dataset.price},
             'new':function(a,b){return b.dataset.id-a.dataset.id} };
    if(by[sort]){ cards.sort(by[sort]); cards.forEach(function(c){ grid.appendChild(c) }); }
    out.textContent=shown; empty.style.display=shown?'none':'block';
    /* chip-uri cu filtrele active */
    var chips=[];
    cats.forEach(function(v){ chips.push(['cat',v,document.querySelector('input[name=cat][value="'+v+'"]').parentNode.textContent.replace(/\\d+$/,'').trim()]) });
    langs.forEach(function(v){ chips.push(['lang',v,v]) }); fmts.forEach(function(v){ chips.push(['fmt',v,v]) }); lvls.forEach(function(v){ chips.push(['level',v,v]) });
    if(q) chips.push(['q','', '„'+document.getElementById('q').value+'”']);
    if(maxP<100) chips.push(['range','', 'până la '+maxP+' LEI']);
    chipsBox.innerHTML=chips.map(function(c){ return '<button class="chip" style="color:var(--violet);background:#F4F1FF;border-color:#DDD6FE" data-k="'+c[0]+'" data-v="'+c[1]+'">'+c[2]+' ✕</button>' }).join('');
    /* sincronizează URL-ul (fără reload) ca filtrele să poată fi partajate */
    if(push!==false){ var p=new URLSearchParams(); cats.forEach(function(v){p.append('cat',v)}); langs.forEach(function(v){p.append('lang',v)}); fmts.forEach(function(v){p.append('fmt',v)}); lvls.forEach(function(v){p.append('level',v)});
      if(q) p.set('q',document.getElementById('q').value); if(maxP<100) p.set('max',maxP); if(sort!=='popular') p.set('sort',sort);
      var qs=p.toString(); history.replaceState(null,'',location.pathname+(qs?'?'+qs:'')); }
  }
  chipsBox.addEventListener('click',function(e){ var b=e.target.closest('.chip'); if(!b) return;
    if(b.dataset.k==='q'){ document.getElementById('q').value='' } else if(b.dataset.k==='range'){ document.getElementById('range').value=100; document.getElementById('rangeVal').textContent='100 LEI' }
    else { var i=document.querySelector('input[name='+b.dataset.k+'][value="'+b.dataset.v+'"]'); if(i) i.checked=false } apply(); });
  document.querySelectorAll('.filters input[type=checkbox]').forEach(function(i){ i.addEventListener('change',apply) });
  document.getElementById('range').addEventListener('input',function(){ document.getElementById('rangeVal').textContent=this.value+' LEI'; apply(); });
  document.getElementById('q').addEventListener('input',apply);
  document.getElementById('sort').addEventListener('change',apply);
  document.getElementById('reset').addEventListener('click',function(){
    document.querySelectorAll('.filters input[type=checkbox]').forEach(function(i){i.checked=false});
    document.getElementById('range').value=100; document.getElementById('rangeVal').textContent='100 LEI';
    document.getElementById('q').value=''; document.getElementById('sort').value='popular'; apply();
  });
  var ft=document.getElementById('filtersToggle'), fl=document.querySelector('.filters');
  if(ft){ ft.addEventListener('click',function(){ fl.classList.toggle('open') }) }
  /* preluare parametri din URL: ?cat= ?lang= ?fmt= ?level= ?q= ?max= ?sort= */
  var params=new URLSearchParams(location.search);
  ['cat','lang','fmt','level'].forEach(function(k){ params.getAll(k).forEach(function(v){ var el=document.querySelector('input[name='+k+'][value="'+v+'"]'); if(el) el.checked=true }) });
  if(params.get('q')) document.getElementById('q').value=params.get('q');
  if(params.get('max')){ document.getElementById('range').value=params.get('max'); document.getElementById('rangeVal').textContent=params.get('max')+' LEI' }
  if(params.get('sort')) document.getElementById('sort').value=params.get('sort');
  apply(false);
})();
</script>
"""


def build_produse():
    def cnt(field):
        d = {}
        for p in PRODUCTS:
            d[p[field]] = d.get(p[field], 0) + 1
        return d

    def boxes(name, items, label=lambda k: k):
        return "".join('<label><input type="checkbox" name="%s" value="%s"> %s <span>%d</span></label>' % (name, k, label(k), v) for k, v in items)

    cats = boxes("cat", sorted(cnt("cat").items(), key=lambda x: -x[1]), cat_title)
    langs = boxes("lang", sorted(cnt("lang").items()))
    fmts = boxes("fmt", sorted(cnt("fmt").items(), key=lambda x: -x[1]))
    lvls = boxes("level", sorted(cnt("level").items(), key=lambda x: -x[1]))
    cards = "".join(product_card(p) for p in PRODUCTS)
    max_price = max(p["price"] for p in PRODUCTS)

    body = page_head("Toate resursele educaționale", "Catalog produse",
                     "Filtrează după categorie, limbă, nivel, format sau buget. Descărcare instantă după plată.") + """
<style>@media(max-width:900px){.filters{display:none}.filters.open{display:block}}</style>
<section><div class="wrap shop">
  <aside class="filters">
    <h3>Filtrează</h3>
    <div class="fgroup"><h4>Căutare</h4>
      <input type="search" id="q" placeholder="Caută după titlu..." aria-label="Caută" style="width:100%;border:1.5px solid var(--line);border-radius:12px;padding:.6rem .8rem;outline:0">
    </div>
    <div class="fgroup"><h4>Categorie</h4>__CATS__</div>
    <div class="fgroup"><h4>Limbă</h4>__LANGS__</div>
    <div class="fgroup"><h4>Nivel</h4>__LVLS__</div>
    <div class="fgroup"><h4>Format</h4>__FMTS__</div>
    <div class="fgroup">
      <h4>Preț maxim: <span id="rangeVal">100 LEI</span></h4>
      <input type="range" id="range" min="15" max="100" value="100" aria-label="Preț maxim" style="width:100%;accent-color:#6D28D9">
    </div>
    <button class="btn btn-ghost btn-sm" id="reset" style="width:100%;justify-content:center;margin-top:.6rem">Resetează filtrele</button>
  </aside>
  <div>
    <div class="shop-bar">
      <button class="btn btn-ghost btn-sm" id="filtersToggle" style="display:none">Filtre</button>
      <span class="count"><span id="count">__N__</span> <span>resurse găsite</span></span>
      <div class="chips" id="activeChips" style="margin:0"></div>
      <select id="sort" aria-label="Sortare">
        <option value="popular">Sortare: popularitate</option>
        <option value="rating">Rating</option>
        <option value="new">Cele mai noi</option>
        <option value="price-asc">Preț: crescător</option>
        <option value="price-desc">Preț: descrescător</option>
      </select>
    </div>
    <div class="prod-grid" id="grid">__CARDS__</div>
    <div class="empty" id="empty"><h3>Nu am găsit rezultate</h3><p>Încearcă să modifici filtrele sau caută altceva.</p></div>
  </div>
</div></section>
<style>@media(max-width:900px){#filtersToggle{display:inline-flex!important}}</style>
"""
    for k, v in [("__CATS__", cats), ("__LANGS__", langs), ("__FMTS__", fmts), ("__LVLS__", lvls), ("__CARDS__", cards), ("__N__", str(len(PRODUCTS)))]:
        body = body.replace(k, v)
    assert max_price <= 100, "Mărește max-ul slider-ului de preț"
    write("produse.html", head("Catalog resurse educaționale — Caleidoscope Educational.ro",
                               "Catalog complet de resurse educaționale: exerciții, fișe de lucru, rezumate, eseuri, hărți, audiobookuri, ghiduri de licență.",
                               "produse") + body + footer(SHOP_JS))


# ------------------------------------------------------------------ CATEGORII
def build_categorii():
    counts = {}
    for p in PRODUCTS:
        counts[p["cat"]] = counts.get(p["cat"], 0) + 1
    cats = "".join(category_card(s, t, "%s · %d resurse" % (d, counts.get(s, 0)) if counts.get(s) else d, i, g) for s, t, d, i, g in CATEGORIES)
    notes = {
        "Limbi străine": ("globe", "Vocabular pe teme, dialoguri, exerciții de gramatică și audio pentru engleză, franceză, spaniolă, germană și italiană.", "limbi-straine-vocabular"),
        "Literatură": ("book", "Rezumate, comentarii, eseuri, schițe de personaj și conspecte pentru autori români și universali.", "rezumate-si-eseuri"),
        "Psihologie": ("brain", "Sinteze de curs, fișe de concepte, ghiduri de cercetare și idei de teme pentru lucrări.", "licenta-si-disertatie"),
        "Drept": ("shield", "Structuri de lucrare, bibliografii, vocabular juridic și sinteze pe materii.", "licenta-si-disertatie"),
        "Criminalistică": ("search", "Ghiduri de studiu, metodologie de cercetare la fața locului și studii de caz.", "literatura-de-specialitate"),
        "Psihiatrie": ("heart", "Sinteze de specialitate, tabele de diagnostic și materiale pentru examene.", "literatura-de-specialitate"),
    }
    doms = "".join('<a class="tile reveal" href="produse.html?cat=%s"><span class="ico" style="background:linear-gradient(135deg,#6D28D9,#0EA5A4)">%s</span>'
                   '<h3>%s</h3><p>%s</p><ul><li>Rezumate și conspecte</li><li>Ghiduri de studiu</li><li>Idei de teme și structuri</li></ul></a>'
                   % (notes[n][2], svg(notes[n][0], 22), n, notes[n][1]) for n, s, i in DOMAINS)
    body = page_head("Toate categoriile de resurse", "Categorii",
                     "De la fișe de lucru pentru clasele primare până la ghiduri de licență, disertație și planuri de lucru științifice.") + """
<section><div class="wrap"><div class="cat-grid" style="grid-template-columns:repeat(4,1fr)">__CATS__</div></div></section>
<section style="background:var(--bg)"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Domenii</span><h2>Resurse organizate pe domenii</h2></div>
  <div class="grid-3">__DOMS__</div>
</div></section>
""".replace("__CATS__", cats).replace("__DOMS__", doms)
    write("categorii.html", head("Categorii de resurse educaționale — Caleidoscope Educational.ro",
                                 "Categorii: cărți și materiale școlare, exerciții, povești, hărți, rezumate, eseuri, audiobookuri, licență și disertație.",
                                 "categorii") + body + footer())


# ------------------------------------------------------------------ DESPRE
def build_despre():
    vals = [("checkc", "Conținut original", "Toate resursele sunt redactate de autori profesori; verificăm sursele și actualizăm materialele periodic."),
            ("bolt", "Claritate", "Explicăm simplu: structură, pași, exemple, barem. Fiecare material are cuprins și extras gratuit."),
            ("heart", "Utilizare corectă", "Resursele sunt pentru studiu individual. Încurajăm citarea corectă și nu oferim lucrări gata de predat."),
            ("lock", "Siguranță", "Plăți securizate, factură fiscală, datele tale protejate conform GDPR.")]
    tiles = "".join('<div class="tile reveal"><span class="ico" style="background:linear-gradient(135deg,#6D28D9,#0EA5A4)">%s</span><h3>%s</h3><p>%s</p></div>' % (svg(i, 22), t, d) for i, t, d in vals)
    body = page_head("Despre Caleidoscope Educational", "Despre noi",
                     "Un proiect construit pentru elevi, studenți, părinți și profesori care au nevoie de materiale clare, corecte și gata de folosit.") + """
<section><div class="wrap grid-2" style="align-items:center;gap:3rem">
  <div class="prose">
    <h2 style="margin-top:0">Povestea noastră</h2>
    <p>Caleidoscope Educational a pornit dintr-o nevoie foarte simplă: materialele bune sunt împrăștiate, greu de găsit și rareori adaptate nivelului celui care învață. Am adunat într-un singur loc exerciții, povești, rezumate, eseuri, hărți, conspecte, vocabular în limbi străine și audiobookuri – organizate pe materii, clase și niveluri.</p>
    <p>Lucrăm cu profesori și autori din învățământul preuniversitar și universitar, iar fiecare resursă trece printr-un proces de verificare: structură logică, acuratețea informațiilor, calitatea exemplului bun și a baremului de corectare.</p>
    <h3>Ce ne diferențiază</h3>
    <ul>
      <li>__C__ <span><b>Extras gratuit</b> pentru fiecare resursă, ca să știi exact ce cumperi.</span></li>
      <li>__C__ <span><b>Actualizări incluse</b> – versiunile noi le primești fără costuri suplimentare.</span></li>
      <li>__C__ <span><b>Organizare pe nivel</b>, nu doar pe materie: A1–B2, primar, gimnaziu, liceu, facultate.</span></li>
      <li>__C__ <span><b>Suport real</b> – răspundem la întrebări și adaptăm materialele la cerere.</span></li>
    </ul>
  </div>
  <div>
    <div class="cta-band" style="margin:0">
      <h2>„Mai multă cunoaștere, mai multe posibilități!”</h2>
      <p>Învățăm azi, construim mâine. Fiecare resursă pe care o descarci este un pas mic, dar sigur, spre obiectivul tău.</p>
      <div class="stats" style="margin-top:1.4rem">
        <div class="stat" style="background:rgba(255,255,255,.15)"><b style="color:#fff">1.200+</b><small style="color:rgba(255,255,255,.85)">resurse publicate</small></div>
        <div class="stat" style="background:rgba(255,255,255,.15)"><b style="color:#fff">4.9/5</b><small style="color:rgba(255,255,255,.85)">rating mediu</small></div>
        <div class="stat" style="background:rgba(255,255,255,.15)"><b style="color:#fff">3.500+</b><small style="color:rgba(255,255,255,.85)">clienți mulțumiți</small></div>
      </div>
    </div>
  </div>
</div></section>
<section style="background:var(--bg)"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Valorile noastre</span><h2>Cum lucrăm</h2></div>
  <div class="grid-4">__TILES__</div>
</div></section>
""".replace("__TILES__", tiles).replace("__C__", CHECK)
    write("despre.html", head("Despre noi — Caleidoscope Educational.ro",
                              "Cine suntem, cum selectăm resursele educaționale și de ce materialele noastre sunt diferite.", "despre") + body + footer())


# ------------------------------------------------------------------ BLOG
POSTS = [
    ("Cum alegi tema de licență: 7 pași simpli", "Ghid", "linear-gradient(135deg,#6D28D9,#4F46E5)", "Lista scurtă, criteriile de alegere, discuția cu coordonatorul și cum verifici dacă ai surse suficiente.", "12 martie 2026", 6),
    ("Vocabularul de bază în engleză: primele 300 de cuvinte", "Limbi străine", "linear-gradient(135deg,#0EA5A4,#22C1A5)", "Cele mai frecvente cuvinte, grupate pe teme, cu exerciții rapide de fixare.", "4 martie 2026", 5),
    ("Structura unui eseu argumentativ (cu exemplu)", "Literatură", "linear-gradient(135deg,#EC4899,#F472B6)", "Introducere, argumente, contraargument și încheiere – model de 800 de cuvinte.", "25 februarie 2026", 7),
    ("5 tehnici de învățare care funcționează", "Studiu", "linear-gradient(135deg,#F59E0B,#FBBF24)", "Repetiția spațiată, recuperarea activă, intercalarea și altele – adaptate pentru elevi și studenți.", "18 februarie 2026", 6),
    ("Cum citești corect o hartă istorică", "Hărți", "linear-gradient(135deg,#1D4ED8,#3B82F6)", "Legenda, scara, orientarea și greșelile frecvente la analiza hărților de examen.", "9 februarie 2026", 4),
    ("Disertație în 30 de zile: plan de lucru pe zile", "Ghid", "linear-gradient(135deg,#0F766E,#14B8A6)", "Calendar realist, etape, livrabile și cum îți păstrezi ritmul fără nopți pierdute.", "1 februarie 2026", 8),
]


def build_blog():
    posts = "".join(
        '<article class="post reveal"><div class="thumb" style="background:%s">%s</div>'
        '<div class="body"><span class="tag">%s</span><h3><a href="blog.html">%s</a></h3><p>%s</p>'
        '<div class="foot"><span>%d min de citit</span><span>%s</span></div></div></article>'
        % (g, svg("book", 34, 1.6), cat, t, d, mins, dt) for t, cat, g, d, dt, mins in POSTS)
    body = page_head("Blog și ghiduri gratuite", "Blog", "Articole scurte, practice, scrise pentru elevi, studenți, părinți și profesori.") + """
<section><div class="wrap">
  <div class="grid-3">__POSTS__</div>
  <div class="cta-band" style="margin-top:3rem">
    <h2>Vrei resurse gratuite în fiecare săptămână?</h2>
    <p>Îți trimitem o fișă de lucru gratuită și un articol nou, direct în e-mail.</p>
    <a class="btn btn-white" href="contact.html">Abonează-te gratuit __ARROW__</a>
  </div>
</div></section>
""".replace("__POSTS__", posts).replace("__ARROW__", ARROW)
    write("blog.html", head("Blog — ghiduri și resurse educaționale gratuite | Caleidoscope Educational.ro",
                            "Articole despre învățare, teme de licență, eseuri, vocabular în limbi străine și metode de studiu.", "blog") + body + footer())


# ------------------------------------------------------------------ CONTACT
def build_contact():
    faqs = [("Cum primesc resursa după plată?", "Imediat după confirmarea plății, linkul de descărcare apare pe ecran și în e-mailul tău. Îl găsești oricând și în contul de client."),
            ("Pot folosi materialele la clasă?", "Da, pentru uz personal și didactic direct, la o singură clasă. Pentru multiplicare la nivel de școală sau pentru platforme, scrie-ne pentru o licență extinsă."),
            ("Oferiți lucrări de licență gata făcute?", "Nu. Oferim ghiduri, structuri, bibliografii, metodologie și idei de teme – instrumente care te ajută să scrii tu lucrarea. Livrarea unei lucrări gata de predat contravine regulamentelor universitare."),
            ("Emiteți factură fiscală?", "Da, fiecare comandă primește factură fiscală emisă automat și trimisă pe e-mail, inclusiv pentru persoane fizice."),
            ("Pot returna un produs digital?", "Conform OUG 34/2014, produsele digitale descărcate nu pot fi returnate după descărcare. Dacă materialul nu corespunde descrierii, îl înlocuim sau returnăm contravaloarea integral.")]
    faq_html = "".join('<details><summary>%s</summary><p>%s</p></details>' % (q, a) for q, a in faqs)
    faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}, ensure_ascii=False)
    body = page_head("Contactează-ne", "Contact",
                     "Întrebări despre o resursă, comenzi mai mari pentru școli sau o cerere personalizată? Îți răspundem în maximum 24 de ore lucrătoare.") + """
<section><div class="wrap contact-grid">
  <div class="form-card">
    <h2 style="font-size:1.25rem;font-weight:800;margin-bottom:1rem">Trimite-ne un mesaj</h2>
    <form id="contactForm" novalidate>
      <div class="field"><label for="c_name">Nume</label><input id="c_name" name="name" required minlength="2" placeholder="Ana Popescu"><span class="err">Te rugăm să introduci numele.</span></div>
      <div class="field"><label for="c_mail">E-mail</label><input id="c_mail" name="email" type="email" required placeholder="ana@exemplu.ro"><span class="err">Adresa de e-mail nu pare validă.</span></div>
      <div class="field"><label for="c_subj">Subiect</label>
        <select id="c_subj" name="subject"><option>Întrebare despre o resursă</option><option>Ofertă pentru școli / profesori</option><option>Material personalizat</option><option>Problemă cu o comandă</option><option>Altceva</option></select></div>
      <div class="field"><label for="c_msg">Mesaj</label><textarea id="c_msg" name="message" required minlength="10" placeholder="Cum te putem ajuta?"></textarea><span class="err">Scrie-ne câteva cuvinte (minimum 10 caractere).</span></div>
      <label class="consent"><input type="checkbox" id="c_gdpr" required> Sunt de acord cu prelucrarea datelor conform <a href="termeni.html#gdpr" style="text-decoration:underline">politicii de confidențialitate</a>.</label>
      <button class="btn btn-primary" type="submit">Trimite mesajul __ARROW__</button>
    </form>
  </div>
  <div>
    <div class="info-list">
      <div class="info-item"><span class="ico">__MAIL__</span><div><b>E-mail</b><span><a href="mailto:contact@caleidoscope-educational.ro">contact@caleidoscope-educational.ro</a></span></div></div>
      <div class="info-item"><span class="ico">__PHONE__</span><div><b>Telefon</b><span><a href="tel:+40700000000">+40 700 000 000</a></span></div></div>
      <div class="info-item"><span class="ico">__CLOCK__</span><div><b>Program suport</b><span>Luni–Vineri, 09:00 – 18:00</span></div></div>
      <div class="info-item"><span class="ico">__PIN__</span><div><b>Sediu</b><span>București, România</span></div></div>
    </div>
    <div class="tile" style="margin-top:1.2rem"><h3>Comenzi pentru școli și profesori</h3>
      <p>Dacă ai nevoie de licențe pentru mai mulți profesori, pachete pe clase sau materiale adaptate programei, îți facem o ofertă dedicată.</p>
      <a class="btn btn-ghost btn-sm" style="margin-top:.8rem" href="mailto:contact@caleidoscope-educational.ro?subject=Oferta%20scoli">Cere o ofertă __ARROW__</a>
    </div>
    <div class="faq" style="margin-top:1.4rem">
      <h3 style="font-weight:800;margin-bottom:.8rem">Întrebări frecvente</h3>
      __FAQ__
    </div>
  </div>
</div></section>
<script type="application/ld+json">__FAQLD__</script>
"""
    for k, v in [("__ARROW__", ARROW), ("__MAIL__", svg("mail", 20)), ("__PHONE__", svg("phone", 20)), ("__PIN__", svg("pin", 20)),
                 ("__CLOCK__", svg("clock", 20)), ("__FAQ__", faq_html), ("__FAQLD__", faq_ld)]:
        body = body.replace(k, v)
    js = """
<script>
(function(){
  var f=document.getElementById('contactForm');
  function check(el){ var ok=el.checkValidity(); el.closest('.field').classList.toggle('invalid',!ok); return ok }
  f.querySelectorAll('input,textarea').forEach(function(el){ el.addEventListener('input',function(){ if(el.closest('.field')) check(el) }) });
  f.addEventListener('submit',function(e){
    e.preventDefault(); var ok=true;
    f.querySelectorAll('.field input,.field textarea').forEach(function(el){ if(!check(el)) ok=false });
    if(!document.getElementById('c_gdpr').checked){ ok=false; Caleido.toast('Bifează acordul GDPR pentru a trimite mesajul.'); }
    if(!ok) return;
    /* Site static: deschidem clientul de e-mail pre-completat. Înlocuiește cu un endpoint (Formspree etc.) când există backend. */
    var d=new FormData(f), body='Nume: '+d.get('name')+'\\nE-mail: '+d.get('email')+'\\n\\n'+d.get('message');
    location.href='mailto:contact@caleidoscope-educational.ro?subject='+encodeURIComponent('[Site] '+d.get('subject'))+'&body='+encodeURIComponent(body);
    Caleido.toast('Mulțumim! Se deschide clientul tău de e-mail.'); f.reset();
  });
})();
</script>"""
    write("contact.html", head("Contact — Caleidoscope Educational.ro",
                               "Contactează echipa Caleidoscope Educational pentru întrebări, oferte pentru școli și resurse personalizate.", "contact") + body + footer(js))


# ------------------------------------------------------------------ CHECKOUT
def build_checkout():
    body = page_head("Coș și finalizare comandă", "Checkout", "Verifică produsele, aplică un cod de reducere și completează datele de facturare.") + """
<section><div class="wrap" id="checkoutWrap">
<div class="grid-2" id="checkoutGrid" style="grid-template-columns:1.25fr .9fr;align-items:start">
  <div>
    <div class="tile">
      <h3 style="display:flex;justify-content:space-between;align-items:center">Produsele din coș <button class="btn btn-ghost btn-sm" id="clearCart" style="display:none">Golește coșul</button></h3>
      <div id="cartItems"></div>
    </div>
    <div class="form-card" id="billing" style="margin-top:1.2rem;display:none">
      <h3 style="font-weight:800;margin-bottom:1rem">Date de facturare</h3>
      <form id="orderForm" novalidate>
        <div class="grid-2" style="gap:0 1rem">
          <div class="field"><label for="o_name">Nume complet</label><input id="o_name" required minlength="3" autocomplete="name" placeholder="Ana Popescu"><span class="err">Introdu numele complet.</span></div>
          <div class="field"><label for="o_mail">E-mail (aici primești linkul de descărcare)</label><input id="o_mail" type="email" required autocomplete="email" placeholder="ana@exemplu.ro"><span class="err">Adresa de e-mail nu pare validă.</span></div>
        </div>
        <div class="grid-2" style="gap:0 1rem">
          <div class="field"><label for="o_phone">Telefon (opțional)</label><input id="o_phone" type="tel" autocomplete="tel" placeholder="07xx xxx xxx"></div>
          <div class="field"><label for="o_city">Localitate</label><input id="o_city" required autocomplete="address-level2" placeholder="București"><span class="err">Introdu localitatea.</span></div>
        </div>
        <label class="consent" style="margin:.2rem 0 1rem"><input type="checkbox" id="o_firm"> Doresc factură pe firmă</label>
        <div id="firmBox" style="display:none" class="grid-2">
          <div class="field"><label for="o_cui">CUI</label><input id="o_cui" placeholder="RO12345678"></div>
          <div class="field"><label for="o_firmname">Denumire firmă</label><input id="o_firmname" placeholder="Școala Gimnazială Nr. 1"></div>
        </div>
        <h4 style="font-size:.8rem;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin:.4rem 0 .5rem">Metodă de plată</h4>
        <div class="pay-opts">
          <label><input type="radio" name="pay" value="card" checked><span>__CARD__ Card bancar</span></label>
          <label><input type="radio" name="pay" value="wallet"><span>__BOLT__ Apple / Google Pay</span></label>
          <label><input type="radio" name="pay" value="transfer"><span>__FILE__ Transfer bancar</span></label>
        </div>
        <label class="consent"><input type="checkbox" id="o_terms" required> Am citit și sunt de acord cu <a href="termeni.html" style="text-decoration:underline">termenii și condițiile</a> și sunt de acord ca livrarea conținutului digital să înceapă imediat, pierzând dreptul de retragere.</label>
      </form>
    </div>
  </div>
  <aside class="tile" id="summary" style="position:sticky;top:96px">
    <h3>Sumar comandă</h3>
    <div style="margin-top:.8rem">
      <div class="sum-row"><span>Subtotal (<span id="sumQty">0</span> produse)</span><b id="sumSub">0 LEI</b></div>
      <div class="sum-row disc" id="discRow" style="display:none"><span>Reducere <span id="discCode"></span></span><b id="sumDisc">-0 LEI</b></div>
      <div class="sum-row"><span>Livrare</span><b style="color:#059669">Gratuit (digital)</b></div>
      <div class="sum-row total"><span>Total</span><span id="sumTotal" style="color:var(--violet)">0 LEI</span></div>
      <div class="price-note" style="text-align:right">TVA inclus</div>
    </div>
    <div class="coupon"><input id="coupon" placeholder="Cod de reducere" aria-label="Cod de reducere"><button class="btn btn-ghost btn-sm" id="applyCoupon">Aplică</button></div>
    <button class="btn btn-primary" id="placeOrder" style="width:100%;justify-content:center;padding:.9rem">__LOCK__ Plasează comanda</button>
    <p style="font-size:.78rem;color:var(--muted);margin-top:.8rem;text-align:center">Plată securizată · Factură automată · Descărcare instantă</p>
    <div style="display:flex;gap:.4rem;justify-content:center;margin-top:.6rem;flex-wrap:wrap">
      <span class="level-pill">VISA</span><span class="level-pill">Mastercard</span><span class="level-pill">Apple Pay</span><span class="level-pill">Google Pay</span>
    </div>
  </aside>
</div>
</div></section>
""".replace("__CARD__", svg("card", 20)).replace("__BOLT__", svg("bolt", 20)).replace("__FILE__", svg("file", 20)).replace("__LOCK__", svg("lock", 18, 2.2))
    js = """
<script>
(function(){
  var COUPONS=%s, DATA=%s;
  var box=document.getElementById('cartItems'), billing=document.getElementById('billing'), grid=document.getElementById('checkoutGrid');
  var coupon=(function(){ try{ return JSON.parse(sessionStorage.getItem('caleido_coupon')) }catch(e){ return null } })();
  var money=function(n){ return (Math.round(n*100)/100).toLocaleString('ro-RO')+' LEI' };
  var esc=function(s){ return String(s).replace(/</g,'&lt;').replace(/"/g,'&quot;') };
  function meta(id){ return DATA.filter(function(x){return String(x.id)===String(id)})[0] }
  function render(){
    var cart=Caleido.getCart(), sub=0, qty=0;
    if(!cart.length){
      box.innerHTML='<div style="text-align:center;padding:2rem 0;color:var(--muted)"><p style="font-size:1.05rem;font-weight:700;color:var(--ink)">Coșul tău este gol.</p><p style="margin:.4rem 0 1.2rem">Explorează catalogul și adaugă resursele de care ai nevoie.</p><a class="btn btn-primary" href="produse.html">Vezi catalogul</a></div>';
      billing.style.display='none'; document.getElementById('clearCart').style.display='none';
    } else {
      box.innerHTML=cart.map(function(it){ var m=meta(it.id)||{}; sub+=it.price*it.qty; qty+=it.qty;
        return '<div class="cart-line" data-id="'+it.id+'"><div class="t"><a href="produs.html?id='+it.id+'">'+esc(it.title)+'</a><small>'+esc(m.fmt||'')+(m.pages?' · '+esc(m.pages):'')+' · '+money(it.price)+' / buc.</small></div>'
          +'<div class="qty"><button data-d="-1" aria-label="Scade">−</button><span>'+it.qty+'</span><button data-d="1" aria-label="Crește">+</button></div>'
          +'<b style="min-width:80px;text-align:right">'+money(it.price*it.qty)+'</b>'
          +'<button class="rm" data-rm="1" aria-label="Elimină">✕</button></div>' }).join('');
      billing.style.display='block'; document.getElementById('clearCart').style.display='inline-flex';
    }
    var disc=0;
    if(coupon && COUPONS[coupon]){ disc=sub*COUPONS[coupon]/100; document.getElementById('discRow').style.display='flex'; document.getElementById('discCode').textContent='('+coupon+' · -'+COUPONS[coupon]+'%%)'; document.getElementById('sumDisc').textContent='-'+money(disc); document.getElementById('coupon').value=coupon; }
    else { document.getElementById('discRow').style.display='none' }
    document.getElementById('sumQty').textContent=qty; document.getElementById('sumSub').textContent=money(sub); document.getElementById('sumTotal').textContent=money(sub-disc);
    document.getElementById('placeOrder').disabled=!cart.length; document.getElementById('placeOrder').style.opacity=cart.length?'1':'.5';
  }
  box.addEventListener('click',function(e){
    var line=e.target.closest('.cart-line'); if(!line) return; var id=line.dataset.id, cart=Caleido.getCart();
    var it=cart.filter(function(x){return x.id===id})[0]; if(!it) return;
    if(e.target.closest('[data-rm]')){ cart=cart.filter(function(x){return x.id!==id}); Caleido.toast('Produs eliminat din coș'); }
    else if(e.target.closest('[data-d]')){ it.qty+=parseInt(e.target.closest('[data-d]').dataset.d,10); if(it.qty<1) cart=cart.filter(function(x){return x.id!==id}); }
    Caleido.setCart(cart); render();
  });
  document.getElementById('clearCart').addEventListener('click',function(){ if(confirm('Golești coșul?')){ Caleido.setCart([]); render(); } });
  document.getElementById('applyCoupon').addEventListener('click',function(){
    var c=document.getElementById('coupon').value.trim().toUpperCase();
    if(!c){ coupon=null; sessionStorage.removeItem('caleido_coupon'); render(); return }
    if(COUPONS[c]){ coupon=c; sessionStorage.setItem('caleido_coupon',JSON.stringify(c)); Caleido.toast('Cod aplicat: -'+COUPONS[c]+'%%'); } else { Caleido.toast('Codul nu este valid sau a expirat.'); }
    render();
  });
  document.getElementById('o_firm').addEventListener('change',function(){ document.getElementById('firmBox').style.display=this.checked?'grid':'none' });
  function check(el){ var ok=el.checkValidity(); var f=el.closest('.field'); if(f) f.classList.toggle('invalid',!ok); return ok }
  document.querySelectorAll('#orderForm .field input').forEach(function(el){ el.addEventListener('input',function(){ check(el) }) });
  document.getElementById('placeOrder').addEventListener('click',function(){
    var cart=Caleido.getCart(); if(!cart.length) return;
    var ok=true; document.querySelectorAll('#orderForm .field input[required]').forEach(function(el){ if(!check(el)) ok=false });
    if(!ok){ Caleido.toast('Completează câmpurile marcate.'); if(billing.scrollIntoView) billing.scrollIntoView({behavior:'smooth',block:'start'}); return }
    if(!document.getElementById('o_terms').checked){ Caleido.toast('Te rugăm să accepți termenii și condițiile.'); return }
    var no='CE-'+new Date().getFullYear()+'-'+String(Math.floor(Math.random()*900000)+100000);
    var total=document.getElementById('sumTotal').textContent, mail=document.getElementById('o_mail').value;
    var orders=(function(){ try{ return JSON.parse(localStorage.getItem('caleido_orders'))||[] }catch(e){ return [] } })();
    orders.unshift({no:no,date:new Date().toISOString(),items:cart,total:total,email:mail,coupon:coupon||null}); localStorage.setItem('caleido_orders',JSON.stringify(orders));
    Caleido.setCart([]); sessionStorage.removeItem('caleido_coupon');
    /* Demo: aici s-ar face redirect către procesatorul de plăți. */
    grid.innerHTML='<div class="success" style="grid-column:1/-1"><div class="ok"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></div>'
      +'<h2>Mulțumim! Comanda '+no+' a fost înregistrată.</h2><p>Total: <b>'+total+'</b>. Vei primi factura și linkurile de descărcare pe <b>'+esc(mail)+'</b>. (Demo: nu s-a efectuat nicio plată reală.)</p>'
      +'<div style="display:flex;gap:.6rem;justify-content:center;margin-top:1.4rem;flex-wrap:wrap"><a class="btn btn-primary" href="cont.html">Vezi comanda în cont</a><a class="btn btn-ghost" href="produse.html">Continuă cumpărăturile</a></div></div>';
    window.scrollTo({top:0,behavior:'smooth'});
  });
  window.addEventListener('cart:change',render); window.addEventListener('storage',render);
  render();
})();
</script>""" % (json.dumps(COUPONS), PRODUCTS_JSON)
    write("checkout.html", head("Checkout — Caleidoscope Educational.ro", "Finalizare comandă: coș, cod de reducere, date de facturare.", "produse", page="checkout.html", noindex=True) + body + footer(js))


# ------------------------------------------------------------------ PRODUS (detaliu dinamic, ?id=)
def build_produs():
    body = """
<div class="page-head"><div class="wrap breadcrumb"><a href="index.html">Acasă</a> › <a href="produse.html">Produse</a> › <a id="crumbCat" href="produse.html">Categorie</a> › <span id="crumb">Produs</span></div></div>
<section><div class="wrap" id="detail">
  <div class="grid-2"><div class="skel" style="height:320px"></div><div><div class="skel" style="height:34px;width:70%%;margin-bottom:1rem"></div><div class="skel" style="height:20px;width:40%%"></div></div></div>
</div></section>
<section style="background:var(--bg);padding-top:3rem"><div class="wrap">
  <div class="sec-head" style="margin-bottom:1.6rem"><span class="eyebrow">Recomandate</span><h2>Resurse similare</h2></div>
  <div class="prod-grid" id="related"></div>
</div></section>
"""
    js = """
<script>
var DATA=%s;
%s
(function(){
  var id=parseInt((new URLSearchParams(location.search)).get('id')||'0',10);
  var p=DATA.filter(function(x){return x.id===id})[0];
  var box=document.getElementById('detail');
  if(!p){
    box.innerHTML='<div class="p404" style="padding:3rem 0"><b class="grad-text">404</b><h1>Resursa nu există</h1><p>Poate a fost mutată sau linkul este greșit.</p><a class="btn btn-primary" style="margin-top:1.2rem" href="produse.html">Vezi tot catalogul</a></div>';
    document.title='Resursă negăsită — Caleidoscope Educational.ro'; document.getElementById('related').innerHTML=DATA.slice(0,4).map(cardHTML).join(''); Caleido.paint(); Caleido.reveal(); return;
  }
  document.title=p.title+' — Caleidoscope Educational.ro';
  var md=document.querySelector('meta[name=description]'); if(md) md.setAttribute('content',p.desc);
  var ogt=document.querySelector('meta[property="og:title"]'); if(ogt) ogt.setAttribute('content',p.title);
  var ogd=document.querySelector('meta[property="og:description"]'); if(ogd) ogd.setAttribute('content',p.desc);
  var can=document.querySelector('link[rel=canonical]'); if(can) can.setAttribute('href',can.getAttribute('href').split('?')[0]+'?id='+p.id);
  document.getElementById('crumb').textContent=p.title.length>48?p.title.slice(0,48)+'…':p.title;
  var cc=document.getElementById('crumbCat'); cc.textContent=p.cattitle; cc.href='produse.html?cat='+p.cat;
  var disc=p.old?Math.round((1-p.price/p.old)*100):0;
  var stars=function(r){ var f=Math.round(r); return '★★★★★'.slice(0,f)+'<span style="color:#D0D5DD">'+'★★★★★'.slice(f)+'</span>' };
  var wished=Caleido.getWish().indexOf(String(p.id))>-1;
  box.innerHTML=
   '<div class="grid-2" style="align-items:start;gap:2.4rem">'
   +'<div><div class="cover" style="height:340px;border-radius:22px;background:'+(G[p.icon]||G.file)+'">'
   +(p.badge?'<span class="tag" style="top:1rem;left:1rem">'+esc(p.badge)+'</span>':'')+(disc?'<span class="tag" style="top:1rem;right:1rem;left:auto;background:var(--pink);color:#fff">-'+disc+'%%</span>':'')
   +'<span class="fmt" style="bottom:1rem;right:1rem">'+esc(p.fmt)+'</span><span class="cico" style="width:96px;height:96px">'+ico(p.icon,46)+'</span></div>'
   +'<div class="spec"><div><b>Format</b>'+esc(p.fmt)+'</div><div><b>Dimensiune</b>'+esc(p.pages)+'</div><div><b>Nivel</b>'+esc(p.level)+'</div><div><b>Limbă</b>'+esc(p.lang)+'</div></div>'
   +'<div class="tile" style="margin-top:1rem"><h3>Ce primești</h3><ul class="desc-list"><li>Fișier '+esc(p.fmt)+' — '+esc(p.pages)+', optimizat pentru print A4</li><li>Extras gratuit (3 pagini) înainte de cumpărare</li><li>Actualizări gratuite timp de 12 luni</li><li>Licență de utilizare personală / o clasă</li><li>Factură fiscală automată pe e-mail</li></ul></div></div>'
   +'<div><a href="produse.html?cat='+p.cat+'" class="eyebrow">'+esc(p.cattitle)+'</a>'
   +'<h1 style="font-size:1.75rem;font-weight:800;margin:.5rem 0 .6rem;line-height:1.2;letter-spacing:-.01em">'+esc(p.title)+'</h1>'
   +'<div class="rating" style="font-size:.95rem">'+stars(p.rating)+' <b style="color:var(--ink);margin-left:.3rem">'+p.rating+'</b> <small>('+p.votes+' recenzii)</small></div>'
   +'<div class="price" style="font-size:2.1rem;margin:1rem 0 .3rem;display:flex;align-items:baseline;gap:.7rem">'+p.price+' LEI '+(p.old?'<small style="font-size:1rem;display:inline">'+p.old+' LEI</small>':'')+'</div>'
   +'<div class="price-note">TVA inclus · descărcare instantă · factură fiscală automată</div>'
   +'<div style="display:flex;gap:.6rem;margin:1.4rem 0;flex-wrap:wrap;align-items:center">'
   +'<div class="qty" style="height:46px"><button id="qm" aria-label="Scade">−</button><span id="qv">1</span><button id="qp" aria-label="Crește">+</button></div>'
   +'<button class="btn btn-primary" id="addBig" style="padding:.85rem 1.5rem">'+ico('cart',18)+' Adaugă în coș</button>'
   +'<button class="btn btn-ghost wish" id="wishBig" data-id="'+p.id+'" style="position:static;width:auto;height:auto;border-radius:999px;background:#fff">'+ico('heart',18)+' <span>'+(wished?'La favorite':'Favorite')+'</span></button></div>'
   +'<div class="tile"><h3>Descriere</h3><p style="margin-top:.5rem;color:var(--ink-2)">'+esc(p.desc)+'</p>'
   +'<p style="margin-top:.7rem;color:var(--muted);font-size:.9rem">După plată, primești pe e-mail factura și linkul de descărcare, valabil 12 luni, cu re-descărcări nelimitate.</p></div>'
   +'<div class="faq" style="margin-top:1.2rem"><details open><summary>Cum folosesc materialul?</summary><p>Îl descarci, îl poți tipări sau folosi pe tabletă/laptop. Este optimizat pentru print A4.</p></details>'
   +'<details><summary>Pot folosi materialul la clasă?</summary><p>Da, la nivelul unei clase. Pentru școli oferim licențe extinse — vezi pagina de contact.</p></details>'
   +'<details><summary>Lucrările sunt gata de predat?</summary><p>Nu. Oferim ghiduri, structuri și instrumente de lucru, nu lucrări redactate integral.</p></details></div>'
   +'<div style="margin-top:1rem;font-size:.85rem;color:var(--muted)">Distribuie: <a href="https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(location.href)+'" target="_blank" rel="noopener" style="color:var(--violet);font-weight:700">Facebook</a> · <a href="https://wa.me/?text='+encodeURIComponent(p.title+' '+location.href)+'" target="_blank" rel="noopener" style="color:var(--violet);font-weight:700">WhatsApp</a> · <a href="#" id="copyLink" style="color:var(--violet);font-weight:700">Copiază linkul</a></div>'
   +'</div></div>';
  var q=1, qv=document.getElementById('qv');
  document.getElementById('qm').onclick=function(){ q=Math.max(1,q-1); qv.textContent=q };
  document.getElementById('qp').onclick=function(){ q=Math.min(20,q+1); qv.textContent=q };
  document.getElementById('addBig').onclick=function(){ Caleido.addToCart(p.id,p.title,p.price,q) };
  document.getElementById('copyLink').onclick=function(e){ e.preventDefault(); navigator.clipboard&&navigator.clipboard.writeText(location.href).then(function(){ Caleido.toast('Link copiat!') }) };
  window.addEventListener('wish:change',function(){ document.querySelector('#wishBig span').textContent=Caleido.getWish().indexOf(String(p.id))>-1?'La favorite':'Favorite' });
  /* recent vizualizate (max 8) */
  try{ var rv=JSON.parse(localStorage.getItem('caleido_recent'))||[]; rv=[p.id].concat(rv.filter(function(x){return x!==p.id})).slice(0,8); localStorage.setItem('caleido_recent',JSON.stringify(rv)) }catch(e){}
  /* similare: aceeași categorie, apoi aceeași limbă, apoi populare */
  var rel=DATA.filter(function(x){return x.cat===p.cat&&x.id!==p.id});
  if(rel.length<4) rel=rel.concat(DATA.filter(function(x){return x.lang===p.lang&&x.id!==p.id&&rel.indexOf(x)<0}));
  if(rel.length<4) rel=rel.concat(DATA.filter(function(x){return x.id!==p.id&&rel.indexOf(x)<0}).sort(function(a,b){return b.votes-a.votes}));
  document.getElementById('related').innerHTML=rel.slice(0,4).map(cardHTML).join('');
  /* JSON-LD Product */
  var ld=document.createElement('script'); ld.type='application/ld+json';
  ld.text=JSON.stringify({"@context":"https://schema.org","@type":"Product","name":p.title,"description":p.desc,"category":p.cattitle,"inLanguage":"ro",
    "aggregateRating":{"@type":"AggregateRating","ratingValue":p.rating,"reviewCount":p.votes},
    "offers":{"@type":"Offer","priceCurrency":"RON","price":p.price,"availability":"https://schema.org/InStock","url":location.href}});
  document.head.appendChild(ld);
  Caleido.paint(); Caleido.reveal();
})();
</script>""" % (PRODUCTS_JSON, CARD_JS)
    write("produs.html", head("Produs — Caleidoscope Educational.ro", "Detalii resursă educațională, extras gratuit și descărcare instantă.", "produse", page="produs.html") + body + footer(js))


# ------------------------------------------------------------------ FAVORITE
def build_favorite():
    body = page_head("Resursele tale favorite", "Favorite", "Lista se salvează în browserul tău. Adaugă produse apăsând pe inimioară.") + """
<section><div class="wrap">
  <div class="shop-bar" id="wishBar" style="display:none"><span class="count"><span id="wishN">0</span> <span>resurse salvate</span></span><button class="btn btn-ghost btn-sm" id="wishAll" style="margin-left:auto">Adaugă toate în coș</button><button class="btn btn-ghost btn-sm" id="wishClear">Golește lista</button></div>
  <div class="prod-grid" id="wishGrid"></div>
  <div class="empty" id="wishEmpty" style="display:block"><h3>Nu ai încă produse favorite</h3><p>Apasă pe ♥ de pe orice card pentru a-l salva aici.</p><a class="btn btn-primary" style="margin-top:1rem" href="produse.html">Explorează catalogul</a></div>
</div></section>
<section style="background:var(--bg)" id="recentSec" style="display:none"><div class="wrap">
  <div class="sec-head" style="margin-bottom:1.6rem"><span class="eyebrow">Istoric</span><h2>Vizualizate recent</h2></div>
  <div class="prod-grid" id="recentGrid"></div>
</div></section>
"""
    js = """
<script>
var DATA=%s;
%s
(function(){
  function byId(id){ return DATA.filter(function(x){return String(x.id)===String(id)})[0] }
  function render(){
    var w=Caleido.getWish().map(byId).filter(Boolean);
    document.getElementById('wishGrid').innerHTML=w.map(cardHTML).join('');
    document.getElementById('wishEmpty').style.display=w.length?'none':'block'; document.getElementById('wishBar').style.display=w.length?'flex':'none';
    document.getElementById('wishN').textContent=w.length;
    var rv=[]; try{ rv=(JSON.parse(localStorage.getItem('caleido_recent'))||[]).map(byId).filter(Boolean) }catch(e){}
    document.getElementById('recentSec').style.display=rv.length?'block':'none'; document.getElementById('recentGrid').innerHTML=rv.map(cardHTML).join('');
    Caleido.paint(); Caleido.reveal();
  }
  document.getElementById('wishAll').onclick=function(){ var c=Caleido.getCart(); Caleido.getWish().map(byId).filter(Boolean).forEach(function(p){ var f=c.filter(function(x){return x.id===String(p.id)})[0]; if(f) f.qty++; else c.push({id:String(p.id),title:p.title,price:p.price,qty:1}) }); Caleido.setCart(c); Caleido.toast('Toate favoritele au fost adăugate în coș'); };
  document.getElementById('wishClear').onclick=function(){ if(confirm('Golești lista de favorite?')){ localStorage.setItem('caleido_wish','[]'); render(); } };
  window.addEventListener('wish:change',render); window.addEventListener('storage',render); render();
})();
</script>""" % (PRODUCTS_JSON, CARD_JS)
    write("favorite.html", head("Favorite — Caleidoscope Educational.ro", "Resursele tale salvate.", "favorite", page="favorite.html", noindex=True) + body + footer(js))


# ------------------------------------------------------------------ TERMENI
def build_termeni():
    body = page_head("Termeni, confidențialitate și retur", "Informații legale", "Documente-cadru pe care le personalizezi cu datele firmei înainte de publicare.") + """
<section><div class="wrap prose">
  <div class="tile" style="border-color:#F59E0B;background:#FFFBEB;margin-bottom:2rem">
    <b>⚠️ Text demonstrativ.</b> Aceste pagini sunt un model de structură. Completează datele reale (denumire, CUI, sediu, e-mail, procesator de plăți) și, ideal, verifică-le cu un avocat sau consultant GDPR înainte de lansare.
  </div>
  <p style="font-size:.85rem;color:var(--muted)">Cuprins: <a href="#termeni" style="color:var(--violet)">Termeni</a> · <a href="#gdpr" style="color:var(--violet)">Confidențialitate</a> · <a href="#retur" style="color:var(--violet)">Retur</a> · <a href="#litigii" style="color:var(--violet)">Litigii</a> · <a href="#cookies" style="color:var(--violet)">Cookie-uri</a></p>

  <h2 id="termeni">1. Termeni și condiții</h2>
  <p>Prezentul document reglementează utilizarea site-ului caleidoscope-educational.ro și vânzarea resurselor educaționale în format digital, comercializate de [DENUMIRE OPERATOR], persoană juridică/persoană fizică autorizată cu sediul în [ADRESĂ], CUI [CUI], nr. Registrul Comerțului [J40/…/2026].</p>
  <h3>1.1 Comanda și plata</h3>
  <ul>
    <li>__C__ <span>Prețurile sunt exprimate în RON și includ TVA.</span></li>
    <li>__C__ <span>Plata se face online, prin procesatorul de plăți agreat (card, Apple Pay / Google Pay sau transfer bancar).</span></li>
    <li>__C__ <span>Contractul se consideră încheiat la confirmarea plății; livrarea este electronică, prin link de descărcare.</span></li>
  </ul>
  <h3>1.2 Licență de utilizare</h3>
  <p>Resursele se vând cu licență <b>personală, netransmisibilă</b>, pentru uz educațional. Este interzisă redistribuirea, revânzarea, publicarea integrală sau parțială pe alte site-uri, grupuri sau platforme, precum și utilizarea în scop comercial fără o licență extinsă scrisă.</p>
  <h3>1.3 Exonerare privind utilizarea academică</h3>
  <p>Materialele destinate lucrărilor de licență/disertație (structuri, bibliografii, metodologie, idei de teme) sunt <b>instrumente de studiu</b>. Nu furnizăm lucrări redactate integral, gata de predat. Clientul răspunde de respectarea regulamentelor instituției de învățământ și a normelor de etică academică.</p>
  <h3>1.4 Proprietate intelectuală</h3>
  <p>Conținutul resurselor, grafica, textele și înregistrările audio sunt protejate de Legea nr. 8/1996 privind dreptul de autor. Orice încălcare atrage răspunderea civilă și penală.</p>

  <h2 id="gdpr">2. Politica de confidențialitate (GDPR)</h2>
  <p>Operator: [DENUMIRE OPERATOR], contact: [E-MAIL], telefon: [TELEFON].</p>
  <ul>
    <li>__C__ <span><b>Date colectate:</b> nume, e-mail, telefon (opțional), adresa de facturare, istoricul comenzilor, date tehnice (IP, tip dispozitiv, cookie-uri).</span></li>
    <li>__C__ <span><b>Scopuri și temei:</b> executarea contractului (facturare, livrare), obligații legale fiscale, interes legitim (securitate, prevenirea fraudelor), consimțământ (newsletter, marketing).</span></li>
    <li>__C__ <span><b>Destinatari:</b> procesatorul de plăți, serviciul de facturare, furnizorul de e-mail marketing, servicii de hosting/analitică.</span></li>
    <li>__C__ <span><b>Durata:</b> datele de facturare se păstrează 10 ani (obligație legală), cele de marketing până la retragerea consimțământului.</span></li>
    <li>__C__ <span><b>Drepturi:</b> acces, rectificare, ștergere, restricționare, portabilitate, opoziție, retragerea consimțământului, plângere la ANSPDCP.</span></li>
  </ul>

  <h2 id="retur">3. Politica de retur</h2>
  <p>Conform OUG 34/2014, dreptul de retragere nu se aplică conținutului digital livrat prin descărcare atunci când clientul și-a dat acordul expres pentru descărcare înainte de expirarea termenului de 14 zile. Dacă resursa nu corespunde descrierii sau este deteriorată tehnic, o înlocuim sau returnăm integral contravaloarea, la solicitarea trimisă la [E-MAIL].</p>

  <h2 id="litigii">4. Soluționarea litigiilor</h2>
  <p>Poți apela la <b>SAL</b> (Soluționarea Alternativă a Litigiilor – ANPC) sau la platforma europeană <b>SOL/ODR</b>. Ne poți scrie oricând la [E-MAIL].</p>

  <h2 id="cookies">5. Cookie-uri și stocare locală</h2>
  <p>Folosim stocare locală în browser (localStorage) strict necesară pentru funcționarea coșului, a listei de favorite și pentru reținerea preferinței tale privind cookie-urile. Cu acordul tău, putem folosi și cookie-uri de analiză și marketing. Îți poți schimba opțiunea oricând din setările browserului sau <a href="#" onclick="localStorage.removeItem('caleido_cookie');location.reload();return false" style="color:var(--violet);text-decoration:underline">reafișând bannerul de cookie-uri</a>.</p>
</div></section>
""".replace("__C__", svg("check", 17, 2.4))
    write("termeni.html", head("Termeni și condiții, confidențialitate și retur — Caleidoscope Educational.ro",
                               "Termeni și condiții, politică de confidențialitate, retur și cookies pentru Caleidoscope Educational.ro.", "termeni") + body + footer())


# ------------------------------------------------------------------ CONT
def build_cont():
    body = page_head("Contul meu", "Contul meu", "Zona de client: comenzi, facturi, linkuri de descărcare și resursele salvate.") + """
<section><div class="wrap grid-2">
  <div>
    <div class="form-card">
      <h2 style="font-size:1.2rem;font-weight:800">Autentificare</h2>
      <p style="color:var(--muted);font-size:.9rem;margin:.4rem 0 1.2rem">Demo de interfață — se va conecta la sistemul de conturi al magazinului.</p>
      <form id="loginForm" novalidate>
        <div class="field"><label for="l_mail">E-mail</label><input id="l_mail" type="email" required placeholder="ana@exemplu.ro" autocomplete="email"><span class="err">Adresa de e-mail nu pare validă.</span></div>
        <div class="field"><label for="l_pass">Parolă</label><input id="l_pass" type="password" required minlength="6" placeholder="••••••••" autocomplete="current-password"><span class="err">Parola are minimum 6 caractere.</span></div>
        <button class="btn btn-primary" type="submit" style="width:100%;justify-content:center">Intră în cont __ARROW__</button>
      </form>
      <p style="font-size:.85rem;color:var(--muted);margin-top:1rem">Nu ai cont? Se creează automat la prima comandă.</p>
    </div>
  </div>
  <div>
    <div class="tile" id="ordersTile">
      <h3>Comenzile tale (pe acest dispozitiv)</h3>
      <div id="orders" style="margin-top:.8rem"></div>
    </div>
    <div class="tile" style="margin-top:1.2rem">
      <h3>Ce găsești în cont</h3>
      <ul>
        <li>Toate comenzile și facturile fiscale</li>
        <li>Linkuri de descărcare valabile 12 luni</li>
        <li>Versiunile actualizate ale resurselor cumpărate</li>
        <li>Lista de <a href="favorite.html" style="color:var(--violet);font-weight:700">favorite</a> și recomandări pe nivelul tău</li>
      </ul>
      <p style="color:var(--muted);font-size:.9rem;margin-top:1rem">Ai o problemă cu o comandă? <a href="contact.html" style="color:var(--violet);font-weight:700;text-decoration:underline">Scrie-ne</a>.</p>
    </div>
  </div>
</div></section>
""".replace("__ARROW__", ARROW)
    js = """
<script>
(function(){
  var f=document.getElementById('loginForm');
  f.addEventListener('submit',function(e){ e.preventDefault(); var ok=true;
    f.querySelectorAll('input').forEach(function(el){ var v=el.checkValidity(); el.closest('.field').classList.toggle('invalid',!v); if(!v) ok=false });
    if(ok) Caleido.toast('Demo: autentificarea va fi conectată la sistemul magazinului.'); });
  var orders=[]; try{ orders=JSON.parse(localStorage.getItem('caleido_orders'))||[] }catch(e){}
  var box=document.getElementById('orders');
  if(!orders.length){ box.innerHTML='<p style="color:var(--muted);font-size:.9rem">Nu ai comenzi înregistrate încă. <a href="produse.html" style="color:var(--violet);font-weight:700">Vezi catalogul</a>.</p>'; return }
  box.innerHTML=orders.slice(0,10).map(function(o){ var d=new Date(o.date);
    return '<details style="border:1.5px solid var(--line);border-radius:12px;padding:.7rem .9rem;margin-bottom:.6rem"><summary style="cursor:pointer;display:flex;justify-content:space-between;gap:1rem;font-weight:700;font-size:.9rem;list-style:none"><span>'+o.no+' <small style="color:var(--muted);font-weight:600">· '+d.toLocaleDateString('ro-RO')+'</small></span><span style="color:var(--violet)">'+o.total+'</span></summary>'
      +'<ul style="margin-top:.6rem;display:grid;gap:.3rem">'+o.items.map(function(i){ return '<li style="font-size:.86rem;display:flex;justify-content:space-between;gap:1rem"><a href="produs.html?id='+i.id+'">'+String(i.title).replace(/</g,'&lt;')+'</a><span style="white-space:nowrap">'+i.qty+' × '+i.price+' LEI</span></li>' }).join('')+'</ul>'
      +'<p style="font-size:.8rem;color:var(--muted);margin-top:.6rem">Linkurile de descărcare au fost trimise la '+String(o.email).replace(/</g,'&lt;')+' (demo).</p></details>' }).join('');
})();
</script>"""
    write("cont.html", head("Contul meu — Caleidoscope Educational.ro", "Autentificare în contul de client Caleidoscope Educational.", "cont", noindex=True) + body + footer(js))


# ------------------------------------------------------------------ 404 + SEO files
def build_404():
    body = """
<section><div class="wrap p404">
  <b class="grad-text">404</b>
  <h1>Pagina nu a fost găsită</h1>
  <p>Linkul poate fi greșit sau pagina a fost mutată. Încearcă o căutare sau întoarce-te acasă.</p>
  <form class="searchbar" action="produse.html" method="get" role="search" style="margin:1.6rem auto 0;box-shadow:var(--shadow)">
    <input type="search" name="q" placeholder="Caută o resursă…" aria-label="Caută"><button type="submit">Caută</button>
  </form>
  <div style="display:flex;gap:.6rem;justify-content:center;margin-top:1.4rem;flex-wrap:wrap"><a class="btn btn-primary" href="index.html">Pagina principală</a><a class="btn btn-ghost" href="produse.html">Catalog</a></div>
</div></section>
"""
    # Pe GitHub Pages, linkurile relative din 404 trebuie să fie absolute (pagina se servește de la orice adâncime).
    html = head("Pagina nu a fost găsită — Caleidoscope Educational.ro", "Eroare 404.", "home", page="404.html", noindex=True) + body + footer()
    html = html.replace('href="index.html"', 'href="%s"' % SITE_URL)
    for p in ["produse", "categorii", "despre", "blog", "contact", "cont", "favorite", "termeni", "checkout", "produs"]:
        html = html.replace('href="%s.html' % p, 'href="%s%s.html' % (SITE_URL, p)).replace('action="%s.html"' % p, 'action="%s%s.html"' % (SITE_URL, p))
    write("404.html", html)


def build_seo_files():
    today = date.today().isoformat()
    pages = [("", "1.0", "weekly"), ("produse.html", "0.9", "weekly"), ("categorii.html", "0.8", "monthly"), ("despre.html", "0.5", "yearly"),
             ("blog.html", "0.6", "weekly"), ("contact.html", "0.5", "yearly"), ("termeni.html", "0.3", "yearly")]
    pages += [("produs.html?id=%d" % p["id"], "0.7", "monthly") for p in PRODUCTS]
    pages += [("produse.html?cat=%s" % s, "0.6", "weekly") for s, t, d, i, g in CATEGORIES]
    urls = "".join('  <url><loc>%s%s</loc><lastmod>%s</lastmod><changefreq>%s</changefreq><priority>%s</priority></url>\n'
                   % (SITE_URL, u.replace("&", "&amp;"), today, cf, pr) for u, pr, cf in pages)
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    write("robots.txt", "User-agent: *\nAllow: /\nDisallow: /checkout.html\nDisallow: /cont.html\nDisallow: /favorite.html\n\nSitemap: %ssitemap.xml\n" % SITE_URL)
    with open(".nojekyll", "w") as f:
        f.write("")
    print("Generat: .nojekyll")


if __name__ == "__main__":
    build_index()
    build_produse()
    build_categorii()
    build_despre()
    build_blog()
    build_contact()
    build_checkout()
    build_produs()
    build_favorite()
    build_termeni()
    build_cont()
    build_404()
    build_seo_files()
    print("Toate paginile au fost generate complet!")
