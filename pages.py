# -*- coding: utf-8 -*-
"""Conținutul paginilor site-ului Caleidoscope Educational.ro."""
import json
from kit import (svg, CATEGORIES, DOMAINS, LANGS, PRODUCTS, head, footer,
                 product_card, category_card)


# ------------------------------------------------------------------ HOME
def page_index():
    cats = "".join(category_card(*c) for c in CATEGORIES)
    doms = "".join(
        '<a href="produse.html?cat=%s">%s<span>%s</span></a>' % (
            "limbi-straine-vocabular" if d == "Limbi străine" else
            "rezumate-si-eseuri" if d == "Literatură" else
            "literatura-de-specialitate",
            n, "→")
        for n, s, i in DOMAINS)
    langs = "".join('<a href="produse.html?lang=%s">%s</a>' % (l, l) for l in LANGS[:5])
    chips = "".join('<a class="chip" href="produse.html?q=%s">%s</a>' % (c, c)
                    for c in ["exerciții", "eseuri", "limbi străine", "licență", "disertație", "audiobook"])
    best = "".join(product_card(p) for p in sorted(PRODUCTS, key=lambda x: -x["votes"])[:8])

    trust = [
        ("bolt", "Acces rapid", "Găsești ușor ce ai nevoie"),
        ("lock", "Plată sigură", "Tranzacții 100% securizate"),
        ("truck", "Livrare instant", "Acces imediat după comandă"),
        ("headset", "Suport clienți", "Suntem aici pentru tine"),
        ("checkc", "Resurse verificate", "Calitate și acuratețe garantate"),
    ]
    trust_html = "".join(
        '<div class="trust-item">%s<div><b>%s</b><small>%s</small></div></div>' % (svg(i, 24), t, s)
        for i, t, s in trust)

    steps = [
        ("search", "1. Cauți și alegi", "Filtrezi după materie, limbă, nivel sau format. Ai previzualizare cu cuprins și pagini-exemplu."),
        ("lock", "2. Plătești în siguranță", "Card, Apple/Google Pay sau transfer. Primești factura fiscală automat pe e-mail."),
        ("bolt", "3. Descarci instant", "Linkul de descărcare apare în contul tău și în e-mail, valabil 12 luni, oricâte re-descărcări."),
    ]
    steps_html = "".join(
        '<div class="step reveal"><div class="num">%d</div><h3>%s</h3><p>%s</p></div>' % (i + 1, t, d)
        for i, (ic, t, d) in enumerate(steps))

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
      <a class="btn btn-primary" style="width:100%;justify-content:center;margin-top:1.1rem" href="produse.html">__ARROW__ Explorează catalogul</a>
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
    <div class="sec-head"><span class="eyebrow">Cum funcționează</span><h2>Trei pași până la resursa ta</h2></div>
    <div class="steps">__STEPS__</div>
  </div>
</section>

<section style="padding-top:0">
  <div class="wrap">
    <div class="cta-band">
      <h2>Primești 10% reducere la prima comandă</h2>
      <p>Abonează-te la newsletter și îți trimitem prin e-mail un cod de reducere, plus o fișă de lucru gratuită în fiecare săptămână.</p>
      <form class="form" onsubmit="event.preventDefault();var t=document.getElementById('toast');t.textContent='Mulțumim! Verifică-ți e-mailul pentru codul de reducere.';t.classList.add('show');setTimeout(function(){t.classList.remove('show')},3000);this.reset();">
        <input type="email" required placeholder="Adresa ta de e-mail">
        <button type="submit">Vreau reducerea</button>
      </form>
      <small>Fără spam. Te poți dezabona oricând, dintr-un singur clic.</small>
    </div>
  </div>
</section>
"""
    body = (body.replace("__CHIPS__", chips).replace("__DOMS__", doms).replace("__LANGS__", langs)
                .replace("__TRUST__", trust_html).replace("__CATS__", cats).replace("__BEST__", best)
                .replace("__STEPS__", steps_html).replace("__STAR__", svg("star", 14, 2))
                .replace("__ARROW__", svg("arrow", 17, 2)))
    return (head("Caleidoscope Educational.ro — Resurse educaționale, cărți, exerciții, rezumate, eseuri, hărți, audiobookuri",
                 "Tot ce ai nevoie pentru învățare, dezvoltare și succes: materiale educaționale, exerciții, rezumate, eseuri, hărți, ghiduri și audiobookuri.", "home")
            + body + footer())


# ------------------------------------------------------------------ PRODUSE
SHOP_JS = """
<script>
(function(){
  var cards=[].slice.call(document.querySelectorAll('#grid .card'));
  var out=document.getElementById('count');
  var empty=document.getElementById('empty');
  function val(name){ return [].slice.call(document.querySelectorAll('input[name="'+name+'"]:checked')).map(function(i){return i.value}); }
  function apply(){
    var cats=val('cat'), langs=val('lang'), fmts=val('fmt');
    var maxP=parseInt(document.getElementById('range').value,10);
    var q=(document.getElementById('q').value||'').toLowerCase().trim();
    var sort=document.getElementById('sort').value;
    var shown=0;
    cards.forEach(function(c){
      var ok=(!cats.length||cats.indexOf(c.dataset.cat)>-1)
          && (!langs.length||langs.indexOf(c.dataset.lang)>-1)
          && (!fmts.length||fmts.indexOf(c.dataset.fmt)>-1)
          && (parseInt(c.dataset.price,10)<=maxP)
          && (!q || c.dataset.title.indexOf(q)>-1 || c.dataset.cat.indexOf(q)>-1);
      c.style.display=ok?'':'none'; if(ok) shown++;
    });
    if(sort==='price-asc'){ cards.sort(function(a,b){return a.dataset.price-b.dataset.price}); }
    if(sort==='price-desc'){ cards.sort(function(a,b){return b.dataset.price-a.dataset.price}); }
    if(sort==='popular'){ cards.sort(function(a,b){return b.dataset.votes-a.dataset.votes}); }
    cards.forEach(function(c){ c.parentNode.appendChild(c); });
    out.textContent=shown;
    empty.style.display=shown?'none':'block';
  }
  document.querySelectorAll('.filters input').forEach(function(i){ i.addEventListener('change',apply) });
  document.getElementById('range').addEventListener('input',function(){ document.getElementById('rangeVal').textContent=this.value+' LEI'; apply(); });
  document.getElementById('q').addEventListener('input',apply);
  document.getElementById('sort').addEventListener('change',apply);
  document.getElementById('reset').addEventListener('click',function(){
    document.querySelectorAll('.filters input[type=checkbox]').forEach(function(i){i.checked=false});
    document.getElementById('range').value=100; document.getElementById('rangeVal').textContent='100 LEI';
    document.getElementById('q').value=''; apply();
  });
  // preluare parametri din URL (?cat= / ?q= / ?lang=)
  var params=new URLSearchParams(location.search);
  var c=params.get('cat'); if(c){ var el=document.querySelector('input[name=cat][value="'+c+'"]'); if(el){el.checked=true} }
  var l=params.get('lang'); if(l){ var el2=document.querySelector('input[name=lang][value="'+l+'"]'); if(el2){el2.checked=true} }
  var q2=params.get('q'); if(q2){ document.getElementById('q').value=q2 }
  apply();
})();
</script>
"""


def page_produse():
    def cnt(field):
        d = {}
        for p in PRODUCTS:
            d[p[field]] = d.get(p[field], 0) + 1
        return d

    ccount = cnt("cat")
    lcount = cnt("lang")
    fcount = cnt("fmt")

    def boxes(name, items):
        rows = []
        for k, v in items:
            rows.append('<label><input type="checkbox" name="%s" value="%s"> %s <span>%d</span></label>' % (name, k, k, v))
        return "".join(rows)

    cats = boxes("cat", sorted([(k, v) for k, v in ccount.items()], key=lambda x: -x[1]))
    langs = boxes("lang", sorted(lcount.items()))
    fmts = boxes("fmt", sorted(fcount.items(), key=lambda x: -x[1]))
    cards = "".join(product_card(p) for p in PRODUCTS)

    body = """
<div class="page-head"><div class="wrap">
  <div class="breadcrumb"><a href="index.html">Acasă</a> › <span>Catalog produse</span></div>
  <h1>Toate resursele educaționale</h1>
  <p>Filtrează după categorie, limbă, nivel, format sau buget. Descărcare instantă după plată.</p>
</div></div>

<section>
  <div class="wrap shop">
    <aside class="filters">
      <h3>Filtrează</h3>
      <div class="fgroup">
        <h4>Căutare</h4>
        <input type="search" id="q" placeholder="Caută după titlu..." style="width:100%;border:1.5px solid var(--line);border-radius:12px;padding:.6rem .8rem;outline:0">
      </div>
      <div class="fgroup"><h4>Categorie</h4>__CATS__</div>
      <div class="fgroup"><h4>Limbă</h4>__LANGS__</div>
      <div class="fgroup"><h4>Format</h4>__FMTS__</div>
      <div class="fgroup">
        <h4>Preț maxim: <span id="rangeVal">100 LEI</span></h4>
        <input type="range" id="range" min="15" max="100" value="100" style="width:100%;accent-color:#6D28D9">
      </div>
      <button class="btn btn-ghost btn-sm" id="reset" style="width:100%;justify-content:center;margin-top:.6rem">Resetează filtrele</button>
    </aside>

    <div>
      <div class="shop-bar">
        <span class="count"><span id="count">__N__</span> resurse găsite</span>
        <select id="sort">
          <option value="popular">Sortare: popularitate</option>
          <option value="price-asc">Preț: crescător</option>
          <option value="price-desc">Preț: descrescător</option>
        </select>
      </div>
      <div class="prod-grid" id="grid">__CARDS__</div>
      <div class="empty" id="empty">
        <h3>Nu am găsit rezultate</h3>
        <p>Încearcă să modifici filtrele sau caută altceva.</p>
      </div>
    </div>
  </div>
</section>
"""
    body = (body.replace("__CATS__", cats).replace("__LANGS__", langs).replace("__FMTS__", fmts)
                .replace("__CARDS__", cards).replace("__N__", str(len(PRODUCTS))))
    return (head("Catalog resurse educaționale — Caleidoscope Educational.ro",
                 "Catalog complet de resurse educaționale: exerciții, fișe de lucru, rezumate, eseuri, hărți, audiobookuri, ghiduri de licență.", "produse")
            + body + footer().replace("</body>", SHOP_JS + "</body>"))


# ------------------------------------------------------------------ CATEGORII
def page_categorii():
    cats = "".join(category_card(*c) for c in CATEGORIES)
    body = """
<div class="page-head"><div class="wrap">
  <div class="breadcrumb"><a href="index.html">Acasă</a> › <span>Categorii</span></div>
  <h1>Toate categoriile de resurse</h1>
  <p>De la fișe de lucru pentru clasele primare până la ghiduri de licență, disertație și planuri de lucru științifice.</p>
</div></div>
<section><div class="wrap">
  <div class="cat-grid" style="grid-template-columns:repeat(4,1fr)">__CATS__</div>
</div></section>
<section style="background:var(--bg)"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Domenii</span><h2>Resurse organizate pe domenii</h2></div>
  <div class="grid-3">
    __DOMS__
  </div>
</div></section>
"""
    doms = ""
    notes = {
        "Limbi străine": ("globe", "Vocabular pe teme, dialoguri, exerciții de gramatică și audio pentru engleză, franceză, spaniolă, germană și italiană."),
        "Literatură": ("book", "Rezumate, comentarii, eseuri, schițe de personaj și conspecte pentru autori români și universali."),
        "Psihologie": ("brain", "Sinteze de curs, fișe de concepte, ghiduri de cercetare și idei de teme pentru lucrări."),
        "Drept": ("shield", "Structuri de lucrare, bibliografii, vocabular juridic și sinteze pe materii."),
        "Criminalistică": ("search", "Ghiduri de studiu, metodologie de cercetare la fața locului și studii de caz."),
        "Psihiatrie": ("heart", "Sinteze de specialitate, tabele de diagnostic și materiale pentru examene."),
    }
    for n, s, i in DOMAINS:
        ic, txt = notes[n]
        doms += ('<div class="tile reveal"><span class="ico" style="background:%s">%s</span>'
                 '<h3>%s</h3><p>%s</p><ul><li>Rezumate și conspecte</li><li>Ghiduri de studiu</li>'
                 '<li>Idei de teme și structuri</li></ul></div>'
                 % ("linear-gradient(135deg,#6D28D9,#0EA5A4)", svg(ic, 22), n, txt))
    body = body.replace("__CATS__", cats).replace("__DOMS__", doms)
    return (head("Categorii de resurse educaționale — Caleidoscope Educational.ro",
                 "Categorii: cărți și materiale școlare, exerciții, povești, hărți, rezumate, eseuri, audiobookuri, licență și disertație.", "categorii")
            + body + footer())


# ------------------------------------------------------------------ DESPRE
def page_despre():
    vals = [("checkc", "Conținut original", "Toate resursele sunt redactate de autori profesori; verificăm sursele și actualizăm materialele periodic."),
            ("bolt", "Claritate", "Explicăm simplu: structură, pași, exemple, barem. Fiecare material are cuprins și extras gratuit."),
            ("heart", "Utilizare corectă", "Resursele sunt pentru studiu individual. Încurajăm citarea corectă și nu oferim lucrări gata de predat."),
            ("lock", "Siguranță", "Plăți securizate, factură fiscală, datele tale protejate conform GDPR.")]
    tiles = "".join('<div class="tile reveal"><span class="ico" style="background:linear-gradient(135deg,#6D28D9,#0EA5A4)">%s</span><h3>%s</h3><p>%s</p></div>' % (svg(i, 22), t, d) for i, t, d in vals)
    body = """
<div class="page-head"><div class="wrap">
  <div class="breadcrumb"><a href="index.html">Acasă</a> › <span>Despre noi</span></div>
  <h1>Despre Caleidoscope Educational</h1>
  <p>Un proiect construit pentru elevi, studenți, părinți și profesori care au nevoie de materiale clare, corecte și gata de folosit.</p>
</div></div>

<section><div class="wrap grid-2" style="align-items:center;gap:3rem">
  <div class="prose">
    <h2 style="margin-top:0">Povestea noastră</h2>
    <p>Caleidoscope Educational a pornit dintr-o nevoie foarte simplă: materialele bune sunt împrăștiate, greu de găsit și rareori adaptate nivelului celui care învață. Am adunat într-un singur loc exerciții, povești, rezumate, eseuri, hărți, conspecte, vocabular în limbi străine și audiobookuri – organizate pe materii, clase și niveluri.</p>
    <p>Lucrăm cu profesori și autori din învățământul preuniversitar și universitar, iar fiecare resursă trece printr-un proces de verificare: structură logică, acuratețea informațiilor, calitatea exemplului bun și a baremului de corectare.</p>
    <h3>Ce ne diferențiază</h3>
    <ul>
      <li>%s <b>Extras gratuit</b> pentru fiecare resursă, ca să știi exact ce cumperi.</li>
      <li>%s <b>Actualizări incluse</b> – versiunile noi le primești fără costuri suplimentare.</li>
      <li>%s <b>Organizare pe nivel</b>, nu doar pe materie: A1–B2, primar, gimnaziu, liceu, facultate.</li>
      <li>%s <b>Suport real</b> – răspundem la întrebări și adaptăm materialele la cerere.</li>
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
""".replace("__TILES__", tiles) % (svg("check", 18, 2.4), svg("check", 18, 2.4), svg("check", 18, 2.4), svg("check", 18, 2.4))
    return (head("Despre noi — Caleidoscope Educational.ro",
                 "Cine suntem, cum selectăm resursele educaționale și de ce materialele noastre sunt diferite.", "despre")
            + body + footer())


# ------------------------------------------------------------------ BLOG
POSTS = [
    ("Cum alegi tema de licență: 7 pași simpli", "Ghid", "ghid", "linear-gradient(135deg,#6D28D9,#4F46E5)",
     "Lista scurtă, criteriile de alegere, discuția cu coordonatorul și cum verifici dacă ai surse suficiente."),
    ("Vocabularul de bază în engleză: primele 300 de cuvinte", "Limbi străine", "engleza", "linear-gradient(135deg,#0EA5A4,#22C1A5)",
     "Cele mai frecvente cuvinte, grupate pe teme, cu exerciții rapide de fixare."),
    ("Structura unui eseu argumentativ (cu exemplu)", "Literatură", "eseu", "linear-gradient(135deg,#EC4899,#F472B6)",
     "Introducere, argumente, contraargument și încheiere – model de 800 de cuvinte."),
    ("5 tehnici de învățare care funcționează", "Studiu", "metode", "linear-gradient(135deg,#F59E0B,#FBBF24)",
     "Repetiția spațiată, recuperarea activă, intercalarea și altele – adaptate pentru elevi și studenți."),
    ("Cum citești corect o hartă istorică", "Hărți", "harta", "linear-gradient(135deg,#1D4ED8,#3B82F6)",
     "Legenda, scara, orientarea și greșelile frecvente la analiza hărților de examen."),
    ("Disertație în 30 de zile: plan de lucru pe zile", "Ghid", "plan", "linear-gradient(135deg,#0F766E,#14B8A6)",
     "Calendar realist, etape, livrabile și cum îți păstrezi ritmul fără nopți pierdute."),
]


def page_blog():
    posts = "".join(
        '<article class="post reveal"><div class="thumb" style="background:%s">%s</div>'
        '<div class="body"><span class="tag">%s</span><h3><a href="blog.html">%s</a></h3><p>%s</p>'
        '<div class="foot"><span>6 min de citit</span><span>12 martie 2026</span></div></div></article>'
        % (g, svg("book", 34, 1.6), cat, t, d) for t, cat, s, g, d in POSTS)
    body = """
<div class="page-head"><div class="wrap">
  <div class="breadcrumb"><a href="index.html">Acasă</a> › <span>Blog</span></div>
  <h1>Blog și ghiduri gratuite</h1>
  <p>Articole scurte, practice, scrise pentru elevi, studenți, părinți și profesori.</p>
</div></div>
<section><div class="wrap">
  <div class="grid-3">__POSTS__</div>
  <div class="cta-band" style="margin-top:3rem">
    <h2>Vrei resurse gratuite în fiecare săptămână?</h2>
    <p>Îți trimitem o fișă de lucru gratuită și un articol nou, direct în e-mail.</p>
    <a class="btn btn-white" href="contact.html">Abonează-te gratuit __ARROW__</a>
  </div>
</div></section>
""".replace("__POSTS__", posts).replace("__ARROW__", svg("arrow", 17, 2))
    return (head("Blog — ghiduri și resurse educaționale gratuite | Caleidoscope Educational.ro",
                 "Articole despre învățare, teme de licență, eseuri, vocabular în limbi străine și metode de studiu.", "blog")
            + body + footer())


# ------------------------------------------------------------------ CONTACT
def page_contact():
    faqs = [("Cum primesc resursa după plată?", "Imediat după confirmarea plății, linkul de descărcare apare pe ecran și în e-mailul tău. Îl găsești oricând și în contul de client."),
            ("Pot folosi materialele la clasă?", "Da, pentru uz personal și didactic direct, la o singură clasă. Pentru multiplicare la nivel de școală sau pentru platforme, scrie-ne pentru o licență extinsă."),
            ("Oferiți lucrări de licență gata făcute?", "Nu. Oferim ghiduri, structuri, bibliografii, metodologie și idei de teme – instrumente care te ajută să scrii tu lucrarea. Livrarea unei lucrări gata de predat contravine regulamentelor universitare."),
            ("Emiteti factură fiscală?", "Da, fiecare comandă primește factură fiscală emisă automat și trimisă pe e-mail, inclusiv pentru persoane fizice."),
            ("Pot returna un produs digital?", "Conform OUG 34/2014, produsele digitale descărcate nu pot fi returnate după descărcare. Dacă materialul nu corespunde descrierii, îl înlocuim sau returnăm contravaloarea integral.")]
    faq_html = "".join('<details><summary>%s</summary><p>%s</p></details>' % (q, a) for q, a in faqs)
    body = """
<div class="page-head"><div class="wrap">
  <div class="breadcrumb"><a href="index.html">Acasă</a> › <span>Contact</span></div>
  <h1>Contactează-ne</h1>
  <p>Întrebări despre o resursă, comenzi mai mari pentru școli sau o cerere personalizată? Îți răspundem în maximum 24 de ore lucrătoare.</p>
</div></div>

<section><div class="wrap contact-grid">
  <div class="form-card">
    <h2 style="font-size:1.2rem;font-weight:800;margin-bottom:.3rem">Trimite-ne un mesaj</h2>
    <p style="color:var(--muted);font-size:.9rem;margin-bottom:1.2rem">Completează formularul și revenim cu un răspuns personalizat.</p>
    <form onsubmit="event.preventDefault();var t=document.getElementById('toast');t.textContent='Mesaj trimis! Îți răspundem în max. 24h.';t.classList.add('show');setTimeout(function(){t.classList.remove('show')},3000);this.reset();">
      <div class="field"><label for="n">Nume și prenume</label><input id="n" required placeholder="Ana Popescu"></div>
      <div class="field"><label for="e">E-mail</label><input id="e" type="email" required placeholder="ana@exemplu.ro"></div>
      <div class="field"><label for="s">Subiect</label>
        <select id="s"><option>Întrebare despre o resursă</option><option>Comandă pentru școală / licență extinsă</option><option>Resursă personalizată</option><option>Problemă la descărcare</option><option>Altceva</option></select>
      </div>
      <div class="field"><label for="m">Mesaj</label><textarea id="m" required placeholder="Cum te putem ajuta?"></textarea></div>
      <label class="consent"><input type="checkbox" required> Sunt de acord cu prelucrarea datelor mele conform <a href="termeni.html" style="color:var(--violet);text-decoration:underline">politicii de confidențialitate</a>.</label>
      <button class="btn btn-primary" style="width:100%;justify-content:center" type="submit">Trimite mesajul __ARROW__</button>
    </form>
  </div>

  <div>
    <div class="tile"><h3>Date de contact</h3>
      <div class="info-list">
        <div class="info-item"><span class="ico">__MAIL__</span><div><b>E-mail</b><span>contact@caleidoscope-educational.ro</span></div></div>
        <div class="info-item"><span class="ico">__PHONE__</span><div><b>Telefon</b><span>+40 700 000 000 (L–V, 09:00–18:00)</span></div></div>
        <div class="info-item"><span class="ico">__PIN__</span><div><b>Sediu</b><span>București, România</span></div></div>
        <div class="info-item"><span class="ico">__CLOCK__</span><div><b>Timp de răspuns</b><span>sub 24 de ore în zilele lucrătoare</span></div></div>
      </div>
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
""".replace("__ARROW__", svg("arrow", 17, 2)).replace("__MAIL__", svg("mail", 20)).replace("__PHONE__", svg("phone", 20)).replace("__PIN__", svg("pin", 20)).replace("__CLOCK__", svg("clock", 20)).replace("__FAQ__", faq_html)
    return (head("Contact — Caleidoscope Educational.ro",
                 "Contactează echipa Caleidoscope Educational pentru întrebări, oferte pentru școli și resurse personalizate.", "contact")
            + body + footer())


# ------------------------------------------------------------------ TERMENI
def page_termeni():
    body = """
<div class="page-head"><div class="wrap">
  <div class="breadcrumb"><a href="index.html">Acasă</a> › <span>Informații legale</span></div>
  <h1>Termeni, confidențialitate și retur</h1>
  <p>Documente-cadru pe care le personalizezi cu datele firmei înainte de publicare.</p>
</div></div>

<section><div class="wrap prose">
  <div class="tile" style="border-color:#F59E0B;background:#FFFBEB;margin-bottom:2rem">
    <b>⚠️ Text demonstrativ.</b> Aceste pagini sunt un model de structură. Completează datele reale (denumire, CUI, sediu, e-mail, procesator de plăți) și, ideal, verifică-le cu un avocat sau consultant GDPR înainte de lansare.
  </div>

  <h2>1. Termeni și condiții</h2>
  <p>Prezentul document reglementează utilizarea site-ului caleidoscope-educational.ro și vânzarea resurselor educaționale în format digital, comercializate de [DENUMIRE OPERATOR], persoană juridică/persoană fizică autorizată cu sediul în [ADRESĂ], CUI [CUI], nr. Registrul Comerțului [J40/…/2026].</p>
  <h3>1.1 Comanda și plata</h3>
  <ul>
    <li>__C__ Prețurile sunt exprimate în RON și includ TVA.</li>
    <li>__C__ Plata se face online, prin procesatorul de plăți agreat (card, Apple Pay / Google Pay sau transfer bancar).</li>
    <li>__C__ Contractul se consideră încheiat la confirmarea plății; livrarea este electronică, prin link de descărcare.</li>
  </ul>
  <h3>1.2 Licență de utilizare</h3>
  <p>Resursele se vând cu licență <b>personală, netransmisibilă</b>, pentru uz educațional. Este interzisă redistribuirea, revânzarea, publicarea integrală sau parțială pe alte site-uri, grupuri sau platforme, precum și utilizarea în scop comercial fără o licență extinsă scrisă.</p>
  <h3>1.3 Exonerare privind utilizarea academică</h3>
  <p>Materialele destinate lucrărilor de licență/disertație (structuri, bibliografii, metodologie, idei de teme) sunt <b>instrumente de studiu</b>. Nu furnizăm lucrări redactate integral, gata de predat. Clientul răspunde de respectarea regulamentelor instituției de învățământ și a normelor de etică academică.</p>
  <h3>1.4 Proprietate intelectuală</h3>
  <p>Conținutul resurselor, grafica, textele și înregistrările audio sunt protejate de Legea nr. 8/1996 privind dreptul de autor. Orice încălcare atrage răspunderea civilă și penală.</p>

  <h2>2. Politica de confidențialitate (GDPR)</h2>
  <p>Operator: [DENUMIRE OPERATOR], contact: [E-MAIL], telefon: [TELEFON].</p>
  <ul>
    <li>__C__ <b>Date colectate:</b> nume, e-mail, telefon (opțional), adresa de facturare, istoricul comenzilor, date tehnice (IP, tip dispozitiv, cookie-uri).</li>
    <li>__C__ <b>Scopuri și temei:</b> executarea contractului (facturare, livrare), obligații legale fiscale, interes legitim (securitate, prevenirea fraudelor), consimțământ (newsletter, marketing).</li>
    <li>__C__ <b>Destinatari:</b> procesatorul de plăți, serviciul de facturare, furnizorul de e-mail marketing, servicii de hosting/analitică.</li>
    <li>__C__ <b>Durata:</b> datele de facturare se păstrează 10 ani (obligație legală), cele de marketing până la retragerea consimțământului.</li>
    <li>__C__ <b>Drepturi:</b> acces, rectificare, ștergere, restricționare, portabilitate, opoziție, retragerea consimțământului, plângere la ANSPDCP.</li>
  </ul>

  <h2>3. Politica de retur</h2>
  <p>Conform OUG 34/2014, dreptul de retragere nu se aplică conținutului digital livrat prin descărcare atunci când clientul și-a dat acordul expres pentru descărcare înainte de expirarea termenului de 14 zile. Dacă resursa nu corespunde descrierii sau este deteriorată tehnic, o înlocuim sau returnăm integral contravaloarea, la solicitarea trimisă la [E-MAIL].</p>

  <h2>4. Soluționarea litigiilor</h2>
  <p>Poți apela la <b>SAL</b> (Soluționarea Alternativă a Litigiilor – ANPC) sau la platforma europeană <b>SOL/ODR</b>. Ne poți scrie oricând la [E-MAIL].</p>

  <h2>5. Cookie-uri</h2>
  <p>Folosim cookie-uri strict necesare (funcționarea coșului, autentificare), de preferințe și, cu acordul tău, de analiză și marketing. Îți poți schimba opțiunea oricând din setările browserului sau din bannerul de cookie-uri.</p>
</div></section>
""".replace("__C__", svg("check", 17, 2.4))
    return (head("Termeni și condiții, confidențialitate și retur — Caleidoscope Educational.ro",
                 "Termeni și condiții, politică de confidențialitate, retur și cookies pentru Caleidoscope Educational.ro.", "termeni")
            + body + footer())


# ------------------------------------------------------------------ CONT
def page_cont():
    body = """
<div class="page-head"><div class="wrap">
  <div class="breadcrumb"><a href="index.html">Acasă</a> › <span>Contul meu</span></div>
  <h1>Contul meu</h1>
  <p>Zona de client: comenzi, facturi, linkuri de descărcare și resursele salvate.</p>
</div></div>
<section><div class="wrap grid-2">
  <div class="form-card">
    <h2 style="font-size:1.2rem;font-weight:800">Autentificare</h2>
    <p style="color:var(--muted);font-size:.9rem;margin:.4rem 0 1.2rem">Demo de interfață — se va conecta la sistemul de conturi al magazinului.</p>
    <div class="field"><label>E-mail</label><input placeholder="ana@exemplu.ro"></div>
    <div class="field"><label>Parolă</label><input type="password" placeholder="••••••••"></div>
    <button class="btn btn-primary" style="width:100%;justify-content:center" onclick="var t=document.getElementById('toast');t.textContent='Demo: autentificarea va fi conectată la sistemul magazinului.';t.classList.add('show');setTimeout(function(){t.classList.remove('show')},2800)">Intră în cont __ARROW__</button>
    <p style="font-size:.85rem;color:var(--muted);margin-top:1rem">Nu ai cont? Se creează automat la prima comandă.</p>
  </div>
  <div class="tile">
    <h3>Ce găsești în cont</h3>
    <ul>
      <li>Toate comenzile și facturile fiscale</li>
      <li>Linkuri de descărcare valabile 12 luni</li>
      <li>Versiunile actualizate ale resurselor cumpărate</li>
      <li>Lista de favorite și recomandări pe nivelul tău</li>
      <li>Istoric descărcări pentru re-descărcare rapidă</li>
    </ul>
    <p style="color:var(--muted);font-size:.9rem;margin-top:1rem">Ai o problemă cu o comandă? <a href="contact.html" style="color:var(--violet);font-weight:700;text-decoration:underline">Scrie-ne</a>.</p>
  </div>
</div></section>
""".replace("__ARROW__", svg("arrow", 17, 2))
    return (head("Contul meu — Caleidoscope Educational.ro", "Autentificare în contul de client Caleidoscope Educational.", "cont")
            + body + footer())


# ------------------------------------------------------------------ PRODUS (detaliu dinamic)
def page_produs():
    data = json.dumps([{k: p[k] for k in ("id", "title", "cat", "lang", "level", "fmt", "pages", "price", "old", "badge", "rating", "votes", "icon")} for p in PRODUCTS], ensure_ascii=False)
    body = """
<div class="page-head"><div class="wrap breadcrumb"><a href="index.html">Acasă</a> › <a href="produse.html">Produse</a> › <span id="crumb">Produs</span></div></div>
<section><div class="wrap" id="detail"></div></section>
<script>
var DATA=__DATA__;
var grads=%s;
function params(){ return new URLSearchParams(location.search) }
var id=parseInt(params().get('id')||'1',10);
var p=DATA.filter(function(x){return x.id===id})[0]||DATA[0];
var related=DATA.filter(function(x){return x.cat===p.cat && x.id!==p.id}).slice(0,4);
if(!related.length){ related=DATA.slice(0,4) }
document.getElementById('crumb').textContent=p.title.slice(0,40)+'…';
document.title=p.title+' — Caleidoscope Educational.ro';
function card(x){
  return '<a class="card" href="produs.html?id='+x.id+'" style="text-decoration:none">'
   +'<div class="cover" style="background:'+grads[x.icon]+'"><span class="fmt">'+x.fmt+'</span><span class="cico"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/></svg></span></div>'
   +'<div class="card-body"><h3>'+x.title+'</h3><div class="meta"><span>'+x.pages+'</span><span>'+x.lang+'</span></div></div>'
   +'<div class="card-foot"><div class="price">'+x.price+' LEI</div><span class="add">Vezi</span></div></a>';
}
document.getElementById('detail').innerHTML=
 '<div class="grid-2" style="align-items:start">'
 +'<div><div class="cover" style="height:320px;border-radius:22px;background:'+grads[p.icon]+'">'
 +'<span class="tag" style="top:1rem;left:1rem">'+(p.badge||'Resursă')+'</span>'
 +'<span class="cico" style="width:96px;height:96px"><svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></span></div>'
 +'<div class="tile" style="margin-top:1rem"><h3>Ce conține</h3><ul>'
 +'<li>Fișier '+p.fmt+' — '+p.pages+'</li><li>Nivel: '+p.level+'</li><li>Limbă: '+p.lang+'</li>'
 +'<li>Extras gratuit (3 pagini) înainte de cumpărare</li><li>Actualizări gratuite timp de 12 luni</li>'
 +'<li>Licență de utilizare personală</li></ul></div></div>'
 +'<div><span class="cat" style="color:var(--violet);font-weight:800;letter-spacing:.1em;text-transform:uppercase;font-size:.76rem">'+p.cat.replace(/-/g,' ')+'</span>'
 +'<h1 style="font-size:1.7rem;font-weight:800;margin:.5rem 0 .6rem;line-height:1.2">'+p.title+'</h1>'
 +'<div class="rating" style="font-size:.95rem">★ '+p.rating+' <small>('+p.votes+' recenzii)</small></div>'
 +'<div class="price" style="font-size:2rem;margin:1rem 0 .3rem">'+p.price+' LEI '+(p.old?'<small style="font-size:1rem">'+p.old+' LEI</small>':'')+'</div>'
 +'<div class="price-note">TVA inclus · descărcare instantă · factură fiscală automată</div>'
 +'<div style="display:flex;gap:.6rem;margin:1.4rem 0;flex-wrap:wrap">'
 +'<button class="btn btn-primary add" data-id="'+p.id+'" data-title="'+p.title.replace(/"/g,'')+'" data-price="'+p.price+'">Adaugă în coș</button>'
 +'<a class="btn btn-ghost" href="contact.html">Cere o mostră</a></div>'
 +'<div class="tile"><h3>Descriere</h3><p style="margin-top:.4rem">Material realizat de autori cu experiență didactică, structurat progresiv, cu explicații pas cu pas, exemple rezolvate și barem de corectare. Conținutul este verificat și actualizat periodic; primești gratuit orice versiune nouă apărută în 12 luni de la achiziție.</p>'
 +'<p style="margin-top:.7rem">După plată, primești pe e-mail factura și linkul de descărcare, valabil 12 luni, cu re-descărcări nelimitate.</p></div>'
 +'<div class="faq" style="margin-top:1.2rem"><details open><summary>Cum folosesc materialul?</summary><p>Îl descarci, îl poți tipări sau folosi pe tabletă/laptop. Este optimizat pentru print A4.</p></details>'
 +'<details><summary>Pot folosi materialul la clasă?</summary><p>Da, la nivelul unei clase. Pentru școli oferim licențe extinse — vezi pagina de contact.</p></details>'
 +'<details><summary>Lucrările sunt gata de predat?</summary><p>Nu. Oferim ghiduri, structuri și instrumente de lucru, nu lucrări redactate integral.</p></details></div>'
 +'</div></div>'
 +'<div style="margin-top:3rem"><h2 style="font-weight:800;margin-bottom:1rem">Resurse similare</h2><div class="prod-grid">'+related.map(card).join('')+'</div></div>';
</script>
""" % json.dumps(GRADS_JS, ensure_ascii=False) if False else """
<div class="page-head"><div class="wrap breadcrumb"><a href="index.html">Acasă</a> › <a href="produse.html">Produse</a> › <span id="crumb">Produs</span></div></div>
<section><div class="wrap" id="detail"></div></section>
<script>
var DATA=__DATA__;
var id=parseInt((new URLSearchParams(location.search)).get('id')||'1',10);
var p=DATA.filter(function(x){return x.id===id})[0]||DATA[0];
var related=DATA.filter(function(x){return x.cat===p.cat && x.id!==p.id}).slice(0,4);
if(!related.length){ related=DATA.slice(0,4) }
document.getElementById('crumb').textContent=p.title.slice(0,40)+'…';
document.title=p.title+' — Caleidoscope Educational.ro';
var G={"globe":"linear-gradient(135deg,#4F46E5,#0EA5A4)","file":"linear-gradient(135deg,#6D28D9,#A78BFA)","notes":"linear-gradient(135deg,#7C3AED,#EC4899)","edit":"linear-gradient(135deg,#0EA5A4,#84CC16)","story":"linear-gradient(135deg,#EC4899,#F59E0B)","map":"linear-gradient(135deg,#F59E0B,#EF4444)","audio":"linear-gradient(135deg,#8B5CF6,#EC4899)","cap":"linear-gradient(135deg,#1D4ED8,#0EA5A4)","science":"linear-gradient(135deg,#0F766E,#22C1A5)","brain":"linear-gradient(135deg,#DB2777,#7C3AED)","search":"linear-gradient(135deg,#334155,#0EA5A4)","lib":"linear-gradient(135deg,#B45309,#F59E0B)"};
function card(x){
  return '<a class="card" href="produs.html?id='+x.id+'">'
   +'<div class="cover" style="background:'+(G[x.icon]||G.file)+'"><span class="fmt">'+x.fmt+'</span></div>'
   +'<div class="card-body"><h3>'+x.title+'</h3><div class="meta"><span>'+x.pages+'</span><span>'+x.lang+'</span></div></div>'
   +'<div class="card-foot"><div class="price">'+x.price+' LEI</div><span class="add">Vezi</span></div></a>';
}
document.getElementById('detail').innerHTML=
 '<div class="grid-2" style="align-items:start">'
 +'<div><div class="cover" style="height:300px;border-radius:22px;background:'+(G[p.icon]||G.file)+'">'
 +'<span class="tag" style="top:1rem;left:1rem">'+(p.badge||'Resursă')+'</span>'
 +'<span class="cico" style="width:88px;height:88px"><svg width="42" height="42" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg></span></div>'
 +'<div class="tile" style="margin-top:1rem"><h3>Ce conține</h3><ul>'
 +'<li>Fișier '+p.fmt+' — '+p.pages+'</li><li>Nivel: '+p.level+'</li><li>Limbă: '+p.lang+'</li>'
 +'<li>Extras gratuit (3 pagini) înainte de cumpărare</li><li>Actualizări gratuite timp de 12 luni</li>'
 +'<li>Licență de utilizare personală</li></ul></div></div>'
 +'<div><span style="color:var(--violet);font-weight:800;letter-spacing:.1em;text-transform:uppercase;font-size:.76rem">'+p.cat.replace(/-/g,' ')+'</span>'
 +'<h1 style="font-size:1.7rem;font-weight:800;margin:.5rem 0 .6rem;line-height:1.2">'+p.title+'</h1>'
 +'<div class="rating" style="font-size:.95rem">★ '+p.rating+' <small>('+p.votes+' recenzii)</small></div>'
 +'<div class="price" style="font-size:2rem;margin:1rem 0 .3rem">'+p.price+' LEI '+(p.old?'<small style="font-size:1rem">'+p.old+' LEI</small>':'')+'</div>'
 +'<div class="price-note">TVA inclus · descărcare instantă · factură fiscală automată</div>'
 +'<div style="display:flex;gap:.6rem;margin:1.4rem 0;flex-wrap:wrap">'
 +'<button class="btn btn-primary add" data-id="'+p.id+'" data-title="'+p.title.replace(/"/g,'')+'" data-price="'+p.price+'">Adaugă în coș</button>'
 +'<a class="btn btn-ghost" href="contact.html">Cere o mostră</a></div>'
 +'<div class="tile"><h3>Descriere</h3><p style="margin-top:.4rem">Material realizat de autori cu experiență didactică, structurat progresiv, cu explicații pas cu pas, exemple rezolvate și barem de corectare. Conținutul este verificat și actualizat; primești gratuit orice versiune nouă apărută în 12 luni de la achiziție.</p>'
 +'<p style="margin-top:.7rem">După plată primești pe e-mail factura și linkul de descărcare, valabil 12 luni, cu re-descărcări nelimitate.</p></div>'
 +'<div class="faq" style="margin-top:1.2rem"><details open><summary>Cum folosesc materialul?</summary><p>Îl descarci, îl poți tipări sau folosi pe tabletă/laptop. Este optimizat pentru print A4.</p></details>'
 +'<details><summary>Pot folosi materialul la clasă?</summary><p>Da, la nivelul unei clase. Pentru școli oferim licențe extinse — vezi pagina de contact.</p></details>'
 +'<details><summary>Lucrările sunt gata de predat?</summary><p>Nu. Oferim ghiduri, structuri și instrumente de lucru, nu lucrări redactate integral.</p></details></div>'
 +'</div></div>'
 +'<div style="margin-top:3rem"><h2 style="font-weight:800;margin-bottom:1rem">Resurse similare</h2><div class="prod-grid">'+related.map(card).join('')+'</div></div>';
</script>
"""
    return (head("Produs — Caleidoscope Educational.ro", "Detalii resursă educațională, extras gratuit și descărcare instantă.", "produse")
            + body.replace("__DATA__", data) + footer())
