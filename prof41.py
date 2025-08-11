from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/status/<nom>")
def status(nom):
    # Vérifie si l'image existe dans static/
    image_path = os.path.join("static", f"{nom}.jpg")
    if os.path.exists(image_path):
        image = f"{nom}.jpg"
    else:
        image = None  # Pas d'image trouvée

    return render_template("chapitre.html", image=image, nom=nom)

if __name__ == "__main__":
    # app.run(port=10000, debug=True)

app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))







