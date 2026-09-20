# Web Scanner

Una herramienta web construida con Flask para analizar sitios web de manera visual, con una estética cyberpunk.

## Objetivo

Permite ingresar una URL para:

* Obtener y analizar su contenido HTML
* Extraer títulos `<h1>`, correos, años y enlaces (internos y externos)
* Buscar la palabra clave "Python"
* Mostrar resultados en una interfaz colorida estilo cyberpunk

## Tecnologías utilizadas

* **Flask** — Framework web para Python
* **Requests** — Para obtener contenido web (con timeout y verificación de estado HTTP)
* **BeautifulSoup** — Para analizar el HTML y extraer títulos y enlaces
* **`ipaddress` y `urllib.parse`** — Para validar URLs y bloquear direcciones internas (protección SSRF)
* **Expresiones Regulares (`re`)** — Para buscar patrones como correos y años

## Seguridad incluida

* **Validación de URL**: solo se aceptan direcciones que comiencen con `http://` o `https://`
* **Protección SSRF**: se bloquean IPs privadas, de bucle local (`127.0.0.1`), de enlace local y el nombre `localhost`
* **Timeout de 10 segundos** en cada descarga y límite de tamaño de respuesta (2 MB)
* **Verificación de estado HTTP**: las respuestas con error (404, 500, etc.) se muestran como error y no se analizan
* **Modo debug controlado por entorno**: se activa con `FLASK_DEBUG=1 python app.py`; por defecto está apagado y el servidor solo escucha en `127.0.0.1`
* **Mensajes de error amigables**: si algo falla, la página muestra el motivo en lugar de un error 500

## Capturas de pantalla

![Interfaz principal](img/Screenshot%202025-06-04%20095720.png)
![Análisis de resultados](img/Screenshot%202025-06-04%20100823.png)
![Resultados de extracción](img/Screenshot%202025-06-04%20102851.png)
![Detalle de resultados](img/Screenshot%202025-06-04%20103031.png)

## Estructura del proyecto

```
cyberpunk_scraper/
├── app.py              # Servidor principal Flask
├── scraper.py          # Lógica del análisis web
├── requirements.txt    # Dependencias para ejecutar el proyecto
├── .gitignore          # Archivos temporales excluidos del repositorio
├── README.md
├── templates/
│   └── index.html      # Interfaz HTML (estilo cyberpunk)
├── static/
│   └── style.css       # Estilos CSS (colores brillantes, neón)
└── img/                # Capturas de pantalla
```

## Instalación y uso

### 1. Clonar el proyecto

    git clone https://github.com/oramirez13/scraper.git
    cd scraper

### 2. Crear un entorno virtual (recomendado en Arch Linux, que bloquea pip global)

    python -m venv venv
    source venv/bin/activate   # En Linux/macOS
    venv\Scripts\activate      # En Windows

### 3. Instalar dependencias

    pip install -r requirements.txt

### 4. Ejecutar el servidor

    python app.py

### 5. Usar la aplicación

Abrir el navegador en: http://localhost:5000

Ingresar una URL (por ejemplo: https://www.python.org) y revisar los resultados.

## Ejemplo de URLs válidas para pruebas

https://www.python.org
https://httpbin.org
https://example.com

Autor

Nombre: orami

Carrera: Ingeniería en Seguridad Informática

Curso: Programación Avanzada