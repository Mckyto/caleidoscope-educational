# Caleidoscope Educational.ro

Site static pentru platforma educațională **Caleidoscope Educational.ro**, generat din Python și publicat pe GitHub Pages:
https://mckyto.github.io/caleidoscope-educational/

## Structură

| Fișier | Rol |
|---|---|
| `kit.py` | CSS global, iconițe SVG, date (categorii, domenii, limbi, catalog produse, descrieri), `head()`, `footer()`, `product_card()`, `category_card()` și JS-ul comun (coș, favorite, cookie banner, reveal). |
| `generate.py` | Construiește toate paginile: `index`, `produse`, `categorii`, `despre`, `blog`, `contact`, `checkout`, `produs`, `favorite`, `termeni`, `cont`, `404`, plus `sitemap.xml` și `robots.txt`. |
| `*.html` | Fișierele generate (comise, pentru GitHub Pages). **Nu se editează manual.** |

## Rulare

```bash
python3 generate.py
```

Nu există dependențe externe. Workflow-ul `.github/workflows/build.yml` regenerează paginile automat la push pe `main` și verifică pe PR-uri că HTML-ul este sincronizat cu sursa.

## Funcționalități

- Catalog cu filtre (categorie, limbă, nivel, format, preț), sortare, căutare fără diacritice și filtre sincronizate în URL (partajabile).
- Coș în `localStorage` cu cantități, cupoane (`BUNVENIT10`, `SCOALA15`, `STUDENT20`), validare formular și confirmare comandă (demo, fără plată reală).
- Favorite (♥) + „vizualizate recent”.
- Pagină de produs randată pe client din `?id=`, cu descriere, specificații, produse similare, JSON-LD `Product`.
- SEO: canonical, Open Graph, JSON-LD (`WebSite`, `FAQPage`), `sitemap.xml`, `robots.txt`, pagină `404.html`.

## Adăugarea unui produs

Adaugă un `dict(...)` în `PRODUCTS` din `kit.py` (id unic), opțional o descriere în `DESCRIPTIONS`, apoi rulează `python3 generate.py`.
