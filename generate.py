# -*- coding: utf-8 -*-
"""Script de generare a paginilor pentru Caleidoscope Educational.ro și publicare automată."""

import os
import subprocess
from kit import head, footer, product_card, category_card, PRODUCTS, CATEGORIES, DOMAINS, LANGS

def build_all():
    # Asigură-te că directorul de ieșire există
    os.makedirs(".", exist_ok=True)
    
    # Generăm pagina principală
    html_index = head("Caleidoscope Educational — Resurse Școlare", "Resurse educaționale", "home") + footer()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_index)
    print("Generat: index.html")

    # Generăm restul paginilor de bază
    pages = ["produse", "categorii", "despre", "blog", "contact", "termeni", "cont", "produs"]
    for p in pages:
        filename = f"{p}.html"
        content = head(f"{p.capitalize()} — Caleidoscope Educational", "Resurse educaționale", p) + footer()
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generat: {filename}")

if __name__ == "__main__":
    build_all()
    print("Gata paginile!")

    # Încercare de publicare automată pe GitHub via Git cu verificare inteligentă
    try:
        print("Se verifică modificările pentru GitHub...")
        subprocess.run(['git', 'add', '.'], check=True)
        
        # Verificăm dacă sunt fișiere noi sau modificate de comis
        result = subprocess.run(['git', 'diff', '--cached', '--quiet'])
        if result.returncode != 0:
            subprocess.run(['git', 'commit', '-m', 'Actualizare automata site și coș către checkout'], check=True)
            subprocess.run(['git', 'push'], check=True)
            print("Succes! Modificările au fost urcate pe GitHub!")
        else:
            print("Totul este la zi! Nu există modificări noi de urcat pe GitHub.")
    except Exception as e:
        print("Notă Git:", e)