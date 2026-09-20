# app.py
# Servidor principal de la aplicacion Web Scanner usando Flask.

import os  # Para leer variables de entorno (control del modo debug)

from flask import Flask, render_template, request
from scraper import analizar_pagina

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Pagina principal: muestra el formulario y procesa los escaneos."""
    resultado = None
    if request.method == "POST":
        # .get devuelve None si el campo no llega (evita un error de tipo
        # KeyError cuando alguien envia el formulario sin la clave "url")
        url = request.form.get("url", "").strip()
        if url:
            resultado = analizar_pagina(url)
        else:
            resultado = {"error": "Debes escribir una URL para escanear"}
    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    # El modo debug la activa una variable de entorno (off por defecto).
    # Activar debug en produccion expone una consola interactiva peligrosa.
    modo_debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    # host="127.0.0.1" limita el servidor a la propia maquina
    app.run(host="127.0.0.1", debug=modo_debug)