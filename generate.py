# -*- coding: utf-8 -*-
"""Script principal de generare a paginilor pentru Caleidoscope Educational.ro"""

from kit import head, footer, category_card, CATEGORIES, DOMAINS, LANGS, PRODUCTS, svg, GRADIENTS
import json

def build_index():
    cats = "".join(category_card(*c) for c in CATEGORIES)
    doms = "".join(
        '<a href="produse.html?cat=%s">%s<span>%s</span></a>' % (
            "limbi-straine-vocabular" if d == "Limbi străine" else
            "rezumate-si-eseuri" if d == "Literatură" else
            "literatura-de-specialitate",
            n, "→")
        for n, s, i in DOMAINS)
    langs = "".join('<a href="produse.html?lang=%s">%s</a>' % (l, l) for l in LANGS[:5])
    best = "".join(product_card(p) for p in sorted(PRODUCTS, key=lambda x: -x["votes"])[:8])

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
    </div>

    <div class="dom-list">
      <h3>Domenii</h3>
      __DOMS__
    </div>

    <div class="promo-card">
      <h2>Mai multă cunoaștere,<br>mai multe posibilități!</h2>
      <p>Învățăm azi, construim mâine! Alege resursa potrivită nivelului tău și transformă învățarea într-un proces simplu.</p>
      <a class="btn btn-primary" style="width:100%;justify-content:center;margin-top:1.1rem" href="produse.html">Explorează catalogul →</a>
    </div>

    <div class="lang-col">
      <h3>Limbi</h3>
      __LANGS__
    </div>
  </div>
</section>

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
  </div>
</section>
""".replace("__DOMS__", doms).replace("__LANGS__", langs).replace("__CATS__", cats).replace("__BEST__", best)

    html = head("Caleidoscope Educational.ro — Resurse educaționale", "Materiale educaționale, cărți, exerciții, rezumate, eseuri.", "home") + body + footer()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: index.html")

def build_produse():
    cards = "".join(product_card(p) for p in PRODUCTS)
    body = """
<div class="page-head"><div class="wrap">
  <div class="breadcrumb"><a href="index.html">Acasă</a> › <span>Catalog produse</span></div>
  <h1>Toate resursele educaționale</h1>
  <p>Filtrează după categorie, limbă, nivel, format sau buget. Descărcare instantă după plată.</p>
</div></div>
<section><div class="wrap shop">
  <aside class="filters">
    <h3>Filtrează</h3>
    <div class="fgroup"><h4>Căutare</h4>
      <input type="search" id="q" placeholder="Caută după titlu..." style="width:100%;border:1.5px solid var(--line);border-radius:12px;padding:.6rem .8rem;outline:0">
    </div>
  </aside>
  <div>
    <div class="prod-grid" id="grid">__CARDS__</div>
  </div>
</div></section>
""".replace("__CARDS__", cards)
    html = head("Catalog resurse educaționale — Caleidoscope Educational.ro", "Catalog complet.", "produse") + body + footer()
    with open("produse.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: produse.html")

def build_categorii():
    cats = "".join(category_card(*c) for c in CATEGORIES)
    body = """
<div class="page-head"><div class="wrap">
  <div class="breadcrumb"><a href="index.html">Acasă</a> › <span>Categorii</span></div>
  <h1>Toate categoriile de resurse</h1>
</div></div>
<section><div class="wrap"><div class="cat-grid" style="grid-template-columns:repeat(4,1fr)">__CATS__</div></div></section>
""".replace("__CATS__", cats)
    html = head("Categorii de resurse educaționale — Caleidoscope Educational.ro", "Categorii.", "categorii") + body + footer()
    with open("categorii.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: categorii.html")

def build_despre():
    body = """
<div class="page-head"><div class="wrap">
  <div class="breadcrumb"><a href="index.html">Acasă</a> › <span>Despre noi</span></div>
  <h1>Despre Caleidoscope Educational</h1>
  <p>Un proiect construit pentru elevi, studenți, părinți și profesori.</p>
</div></div>
<section><div class="wrap prose">
  <h2>Povestea noastră</h2>
  <p>Caleidoscope Educational a pornit dintr-o nevoie simplă: materialele bune sunt împrăștiate și greu de găsit. Am adunat totul într-un singur loc.</p>
</div></section>
"""
    html = head("Despre noi — Caleidoscope Educational.ro", "Despre noi.", "despre") + body + footer()
    with open("despre.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: desre.html")

def build_contact():
    body = """
<div class="page-head"><div class="wrap">
  <div class="breadcrumb"><a href="index.html">Acasă</a> › <span>Contact</span></div>
  <h1>Contactează-ne</h1>
  <p>Întrebări sau comenzi pentru școli? Răspundem în maximum 24 de ore.</p>
</div></div>
<section><div class="wrap contact-grid">
  <div class="form-card">
    <h2>Trimite-ne un mesaj</h2>
    <form onsubmit="event.preventDefault();var t=document.getElementById('toast');t.textContent='Mesaj trimis!';t.classList.add('show');setTimeout(function(){t.classList.remove('show')},3000);">
      <div class="field"><label>Nume</label><input required placeholder="Ana Popescu"></div>
      <div class="field"><label>E-mail</label><input type="email" required placeholder="ana@exemplu.ro"></div>
      <div class="field"><label>Mesaj</label><textarea required placeholder="Cum te putem ajuta?"></textarea></div>
      <button class="btn btn-primary" type="submit">Trimite</button>
    </form>
  </div>
</div></section>
"""
    html = head("Contact — Caleidoscope Educational.ro", "Contact.", "contact") + body + footer()
    with open("contact.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: contact.html")

def build_checkout():
    body = """
<div class="page-head"><div class="wrap">
  <div class="breadcrumb"><a href="index.html">Acasă</a> › <span>Checkout</span></div>
  <h1>Coș de cumpărături</h1>
</div></div>
<section><div class="wrap grid-2">
  <div class="tile">
    <h3>Produsele din coș</h3>
    <div id="cartItems"><p style="color:var(--muted)">Coșul tău este gol.</p></div>
  </div>
  <div class="tile">
    <h3>Sumar comandă</h3>
    <p style="margin:1rem 0;font-weight:700">Total: <span id="cartTotal" style="color:var(--violet)">0 LEI</span></p>
    <button class="btn btn-primary" style="width:100%;justify-content:center" onclick="alert('Comandă plasată cu succes!')">Plasează comanda</button>
  </div>
</div></section>
<script>
(function(){
  var key='caleido_cart';
  function getCart(){ try{ return JSON.parse(localStorage.getItem(key))||[] }catch(e){ return [] } }
  var cart=getCart(), box=document.getElementById('cartItems'), tot=document.getElementById('cartTotal');
  if(cart.length){
    var sum=0;
    box.innerHTML=cart.map(function(item){ sum+=parseFloat(item.price||0); return '<div style="display:flex;justify-content:space-between;padding:.5rem 0;border-bottom:1px solid var(--line)"><span>'+item.title+'</span><b>'+item.price+' LEI</b></div>'; }).join('');
    tot.textContent=sum+' LEI';
  }
})();
</script>
"""
    html = head("Checkout — Caleidoscope Educational.ro", "Finalizare comandă.", "produse") + body + footer()
    with open("checkout.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: checkout.html")

def build_produs():
    body = """
<div class="page-head"><div class="wrap breadcrumb"><a href="index.html">Acasă</a> › <a href="produse.html">Produse</a> › <span id="crumb">Produs</span></div></div>
<section><div class="wrap" id="detail"></div></section>
<script>
var DATA=%s;
var id=parseInt((new URLSearchParams(location.search)).get('id')||'1',10);
var p=DATA.filter(function(x){return x.id===id})[0]||DATA[0];
document.getElementById('crumb').textContent=p.title;
document.title=p.title+' — Caleidoscope Educational.ro';
var G=%s;
document.getElementById('detail').innerHTML='<div class="grid-2"><div><div class="cover" style="height:300px;border-radius:22px;background:'+(G[p.icon]||G.file)+'"></div></div><div><h1>'+p.title+'</h1><div class="price" style="font-size:2rem;margin:1rem 0">'+p.price+' LEI</div><button class="btn btn-primary add" data-id="'+p.id+'" data-title="'+p.title.replace(/"/g,'')+'" data-price="'+p.price+'">Adaugă în coș</button></div></div>';
</script>
""" % (json.dumps([{k: p[k] for k in ("id", "title", "cat", "lang", "level", "fmt", "pages", "price", "old", "badge", "rating", "votes", "icon")} for p in PRODUCTS], ensure_ascii=False), json.dumps(GRADIENTS))
    html = head("Produs — Caleidoscope Educational.ro", "Detalii resursă.", "produse") + body + footer()
    with open("produs.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: produs.html")

if __name__ == "__main__":
    build_index()
    build_produse()
    build_categorii()
    build_despre()
    build_contact()
    build_checkout()
    build_produs()
    for p in ["blog", "termeni", "cont"]:
        html = head(p.capitalize() + " — Caleidoscope Educational", "Informații.", p) + f'<div class="wrap" style="padding:4rem 0"><h1>{p.capitalize()}</h1><p>Conținut actualizat.</p></div>' + footer()
        with open(f"{p}.html", "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Generat: {p}.html")
    print("Toate paginile au fost generate complet!")