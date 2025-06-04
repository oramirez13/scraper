import requests
import mechanize
import re
from bs4 import BeautifulSoup

def analizar_pagina(url):
    reporte = {}

    # Obtener HTML
    try:
        response = requests.get(url)
        html = response.text
    except Exception as e:
        return {"error": f"No se pudo obtener la página: {e}"}

    # Mechanize - Navegación
    try:
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.open(url)
        enlaces = [link.url for link in br.links()]
        reporte["enlaces"] = enlaces
    except Exception as e:
        reporte["enlaces"] = [f"Error al usar Mechanize: {e}"]

    # BeautifulSoup - Títulos h1
    soup = BeautifulSoup(html, 'html.parser')
    reporte["titulos_h1"] = [h.text.strip() for h in soup.find_all('h1')]

    # Expresiones regulares
    reporte["correos"] = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', html)
    reporte["anios"] = re.findall(r'\b\d{4}\b', html)
    reporte["enlaces_externos"] = re.findall(r'https?://[^\s"\']+', html)
    reporte["clave"] = "Python"
    reporte["ocurrencias_clave"] = len(re.findall("Python", html, re.IGNORECASE))

    return reporte
