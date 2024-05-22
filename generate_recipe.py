#!/usr/bin/env python3

import cgi
import html

def generate_recipe(zutat1, zutat2, zutat3):
    # Beispiel für ein einfaches Rezept auf Basis der Zutaten
    return f"""
    <h2>Rezept Vorschlag</h2>
    <p>Mit den Zutaten {zutat1}, {zutat2} und {zutat3} können Sie folgendes Rezept zubereiten:</p>
    <ul>
        <li>1. Mischen Sie {zutat1} und {zutat2} in einer Schüssel.</li>
        <li>2. Fügen Sie {zutat3} hinzu und gut umrühren.</li>
        <li>3. Bei 180 Grad für 20 Minuten im Ofen backen.</li>
    </ul>
    """

print("Content-Type: text/html")
print()
print("<html><head>")
print("<title>Rezept Vorschlag</title>")
print('<link rel="stylesheet" href="/styles.css">')
print("</head><body>")

form = cgi.FieldStorage()
zutat1 = html.escape(form.getvalue("zutat1", ""))
zutat2 = html.escape(form.getvalue("zutat2", ""))
zutat3 = html.escape(form.getvalue("zutat3", ""))

if zutat1 and zutat2 and zutat3:
    print(generate_recipe(zutat1, zutat2, zutat3))
else:
    print("<h2>Fehler: Bitte geben Sie alle drei Zutaten ein!</h2>")

print("</body></html>")