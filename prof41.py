from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/")
def accueil():
    noms = ["Jacques", "Paul", "Pierre"]
    return render_template("index.html", noms=noms)

@app.route("/bonjour/<prenom>")
def bonjour(prenom):
    return render_template("bonjour.html", prenom=prenom)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
