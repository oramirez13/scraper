# scraper.py
# Modulo de analisis web: recibe una URL, descarga su contenido y extrae
# informacion (titulos, correos, anios y enlaces) con herramientas de Python.

import re  # Expresiones regulares, para buscar patrones en el texto
import ipaddress  # Para detectar IPs privadas o de bucle local (proteccion SSRF)
from urllib.parse import urlparse  # Para analizar la estructura de una URL

import requests  # Libreria para descargar paginas web
from bs4 import BeautifulSoup  # Libreria para analizar el HTML


def es_ip_privada(url):
    """Devuelve True si la URL apunta a una IP privada o local.

    Esta funcion protege contra el ataque SSRF: no dejar que la aplicacion
    consulte servicios internos (como 127.0.0.1 o 192.168.x.x). Si el host
    es un dominio normal, se permite el acceso.
    """
    # Extraer solo el nombre del host de la URL (ej: "192.168.1.5" o "python.org")
    host = urlparse(url).hostname

    # Si la URL no tiene host, no es valida
    if host is None:
        return True

    # Bloquear tambien el nombre localhost (no es una IP pero si es local)
    if host.lower() == "localhost":
        return True

    # Intentar interpretar el host como una direccion IP
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        # No era una IP, es un dominio; se permite el acceso
        return False

    # Verificar si la IP es privada, de bucle local o de enlace local
    return ip.is_private or ip.is_loopback or ip.is_link_local


def analizar_pagina(url):
    """Descarga una URL y devuelve un reporte con la informacion extraida."""
    reporte = {}

    # 1. Validar que la URL comience con http:// o https://
    if not url.startswith(("http://", "https://")):
        return {"error": "La URL debe comenzar con http:// o https://"}

    # 2. Bloquear IPs internas y locales para evitar el ataque SSRF
    if es_ip_privada(url):
        return {"error": "No se permiten direcciones internas o locales (SSRF)"}

    # 3. Descargar el HTML con timeout y verificando el estado HTTP
    try:
        # El timeout evita que la peticion se cuelgue con sitios lentos
        response = requests.get(url, timeout=10)
        # raise_for_status lanza un error si la respuesta es 404, 500, etc.
        response.raise_for_status()

        # Limitar el tamano de la descarga (evita consumir mucha memoria)
        tamano = response.headers.get("Content-Length")
        if tamano and int(tamano) > 2000000:
            return {"error": "La pagina es demasiado grande (mas de 2 MB)"}

        html = response.text
    except Exception as e:
        # Si algo falla, devolver un reporte con la clave "error"
        return {"error": f"No se pudo obtener la pagina: {e}"}

    # 4. Analizar el contenido con BeautifulSoup
    sopa = BeautifulSoup(html, "html.parser")

    # 4a. Extraer todos los titulos <h1> (se eliminan espacios sobrantes)
    reporte["titulos_h1"] = [h.text.strip() for h in sopa.find_all("h1")]

    # 4b. Separar los enlaces en internos y externos
    dominio = urlparse(url).netloc  # Dominio de la URL analizada
    enlaces_internos = []
    enlaces_externos = []
    for enlace in sopa.find_all("a"):
        destino = enlace.get("href")  # Valor del atributo href
        if not destino:
            continue  # Saltar enlaces sin destino
        # Si el enlace es absoluto (empieza con http), comparar sus dominios
        if destino.startswith(("http://", "https://")):
            if urlparse(destino).netloc == dominio:
                enlaces_internos.append(destino)
            else:
                enlaces_externos.append(destino)
        else:
            # Los enlaces relativos (sin http) pertenecen al mismo sitio
            enlaces_internos.append(destino)
    reporte["enlaces_internos"] = enlaces_internos
    reporte["enlaces_externos"] = enlaces_externos

    # 5. Buscar patrones con expresiones regulares

    # Correos: letras, numeros y algunos simbolos antes y despues de la @
    reporte["correos"] = re.findall(
        r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", html
    )

    # Anios: solo numeros de 4 digitos entre 1900 y 2099 (menos falsos positivos)
    reporte["anios"] = re.findall(r"\b(19[0-9]{2}|20[0-9]{2})\b", html)

    # Ocurrencias de la palabra "Python" (sin distinguir mayusculas y minusculas)
    reporte["ocurrencias_clave"] = len(re.findall("Python", html, re.IGNORECASE))

    return reporte