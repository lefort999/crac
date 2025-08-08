from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route("/")  # ← Route pour afficher l'accueil
def accueil():
    return render_template("index.html")  # ← Ton fichier HTML doit être placé dans /templates/

# 🔹 Exécution de l’application Flask
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
