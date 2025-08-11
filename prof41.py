from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def accueil():
    chapitres = ["chapitre1", "chapitre2", "chapitre3", "chapitre4"]
    return render_template("index.html", chapitres=chapitres)

@app.route("/chapitre/<nom>")
def afficher_chapitre(nom):
    chemin = os.path.join(os.getcwd(), f"{nom}.txt")
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            contenu = f.read()
    except FileNotFoundError:
        contenu = "Chapitre introuvable."
    return render_template("chapitre.html", nom=nom, contenu=contenu)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)







