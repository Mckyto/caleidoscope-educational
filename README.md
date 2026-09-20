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
- **Fișiere reale blurate până la cumpărare** (schițele ilustrate, produsele cu `img=`): în catalog, pe pagina de produs, la favorite și în „similare” se încarcă doar o previzualizare blurată (`uploads/preview/…`) cu lacăt. După plasarea comenzii (demo, `caleido_orders` în `localStorage`) produsul se deblochează automat: imagine clară, zoom în mărime completă și butoane **Descarcă** — pe confirmarea comenzii, pe card („Descarcă” în locul lui „Adaugă”), pe pagina produsului și în `cont.html` („Fișele tale”). Logica este în JS-ul comun din `kit.py` (`Caleido.getOwned / isOwned / fileFor / applyLocks`).
- SEO: canonical, Open Graph, JSON-LD (`WebSite`, `FAQPage`), `sitemap.xml`, `robots.txt`, pagină `404.html`.

## Adăugarea unui produs

Adaugă un `dict(...)` în `PRODUCTS` din `kit.py` (id unic), opțional o descriere în `DESCRIPTIONS`, apoi rulează `python3 generate.py`.

### Produs cu fișier real (blurat până la cumpărare)

1. Pune fișierul în `uploads/` (ex. `uploads/schita-x.jpg`).
2. Generează previzualizarea blurată (mică, ilizibilă) în `uploads/preview/` — necesită ImageMagick, doar local, o singură dată:
   ```bash
   convert uploads/schita-x.jpg -strip -resize 200x300 -gaussian-blur 0x3.5 -quality 60 -interlace Plane uploads/preview/schita-x.jpg
   ```
3. În `PRODUCTS` setează `img="uploads/schita-x.jpg"` și `preview="uploads/preview/schita-x.jpg"` (dacă lipsește `preview`, se folosește implicit `uploads/preview/<același nume>`), apoi rulează `python3 generate.py`.

> Site-ul este static (GitHub Pages), deci deblocarea se face în browser, pe baza comenzilor salvate local. Fișierul complet rămâne accesibil public prin URL-ul lui direct; pentru protecție reală, livrarea trebuie făcută de un backend / procesator de plăți (link semnat sau e-mail după plată).

## Panou de administrare (admin.html)

Adresă: **https://mckyto.github.io/caleidoscope-educational/admin.html** (nu figurează în meniul public; `noindex` + `Disallow` în `robots.txt`).

- **Prima dată — „Resetează contul”**: introdu un token GitHub fine-grained (repo *Mckyto/caleidoscope-educational*, Permissions → Contents: **Read and write**), un nume și o parolă de minim 12 caractere. Contul este salvat în `admin/cont-admin.json`: tokenul este criptat AES-GCM cu o cheie PBKDF2-SHA256 (310.000 iterații) derivată din parolă; numele și parola sunt stocate doar ca hash.
- **Login**: cu nume + parolă, de pe orice dispozitiv (tokenul este decriptat local, în browser).
- **„Încarcă produs nou”**: formularul creează produsul în `admin/produse-admin.json` și încarcă opțional coperta (`uploads/preview/…`, blurată cu lacăt până la cumpărare) și fișierul complet (`uploads/…`, livrat după comandă). Commit-ul declanșează workflow-ul **Build site**, care regenerează paginile — produsul apare pe site în **~1–2 minute**.

`kit.py` încarcă automat `admin/produse-admin.json` (dacă există) și adaugă produsele în `PRODUCTS` cu ID-uri care continuă de la cel mai mare id din catalog. Fișierul este opțional — dacă lipsește, catalogul rămâne neschimbat.

