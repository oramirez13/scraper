from flask import Flask, render_template, request
from scraper import analizar_pagina

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        url = request.form["url"]
        resultado = analizar_pagina(url)
    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
