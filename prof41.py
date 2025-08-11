from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def accueil():
    return "<h1>Bienvenue !</h1><p><a href='/chapitre1'>Lire le chapitre 1</a></p>"

@app.route("/chapitre1")
def chapitre1():
    try:
        with open("chapitre1.txt", "r", encoding="utf-8") as f:
            contenu = f.read()
    except FileNotFoundError:
        contenu = "Chapitre introuvable."

    image = "chapitre1.jpg"
    return render_template("chapitre.html", contenu=contenu, image=image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))





