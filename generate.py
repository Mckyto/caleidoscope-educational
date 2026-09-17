# -*- coding: utf-8 -*-
"""Script principal de generare a paginilor pentru Caleidoscope Educational.ro"""

from kit import head, footer, category_card, PRODUCTS, CATEGORIES, DOMAINS, LANGS, svg

def build_index():
    # Generăm toate cele 12 categorii pentru grilă
    cat_html = "".join(category_card(slug, title, desc, icon, grad) for slug, title, desc, icon, grad in CATEGORIES)
    
    # Domeniile populare din hero
    domains_html = "".join(f'<a href="produse.html?dom={slug}">{name} {svg(icon, 16, 2)}</a>' for name, slug, icon in DOMAINS)
    
    # Limbile străine
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
    <div class="trust-item">
      {svg("search", 24, 2)}
      <div><b>Acces rapid</b><small>Găsești ușor ce ai nevoie</small></div>
    </div>
    <div class="trust-item">
      {svg("shield", 24, 2)}
      <div><b>Plată sigură</b><small>Tranzacții 100% securizate</small></div>
    </div>
    <div class="trust-item">
      {svg("truck", 24, 2)}
      <div><b>Livrare instant</b><small>Acces imediat după comandă</small></div>
    </div>
    <div class="trust-item">
      {svg("headset", 24, 2)}
      <div><b>Suport clienți</b><small>Suntem aici pentru tine</small></div>
    </div>
    <div class="trust-item">
      {svg("check", 24, 2)}
      <div><b>Resurse verificate</b><small>Calitate și acuratețe garantate</small></div>
    </div>
  </div>
</section>

<section class="wrap">
  <div class="sec-head">
    <span class="eyebrow">Categorii principale</span>
    <h2>Explorează categoriile noastre</h2>
    <p>Descoperă o lume întreagă de resurse educaționale, într-un singur loc!</p>
  </div>
  <div class="cat-grid">
    {cat_html}
  </div>
</section>

{footer()}
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Generat: index.html cu designul complet!")

if __name__ == "__main__":
    build_index()
    for page_name in ["produse", "categorii", "despre", "blog", "contact", "termeni", "cont", "produs"]:
        with open(f"{page_name}.html", "w", encoding="utf-8") as f:
            f.write(head(page_name.capitalize(), "Caleidoscope Educational", page_name) + f"<div class='wrap' style='padding:4rem 0'><h1>{page_name.capitalize()}</h1><p>Pagină în curs de actualizare.</p></div>" + footer())
        print(f"Generat: {page_name}.html")
    print("Gata toate paginile!")