# Web Scanner

Una herramienta web construida con Flask para analizar sitios web de manera visual, con una estética cyberpunk.

## Objetivo

Permite ingresar una URL para:

* Obtener y analizar su contenido HTML
* Extraer títulos `<h1>`, correos, años y enlaces
* Simular navegación interna con `mechanize`
* Buscar la palabra clave “Python”
* Mostrar resultados en una interfaz colorida estilo cyberpunk

## Tecnologías utilizadas

* **Flask** — Framework web para Python
* **Requests** — Para obtener contenido web
* **BeautifulSoup** — Para analizar el HTML
* **Mechanize** — Para simular navegación
* **Expresiones Regulares (`re`)** — Para buscar patrones como correos y años

## Capturas de pantalla

![Interfaz principal](img/Screenshot%202025-06-04%20095720.png)
![Análisis de resultados](img/Screenshot%202025-06-04%20100823.png)
![Resultados de extracción](img/Screenshot%202025-06-04%20102851.png)
![Detalle de resultados](img/Screenshot%202025-06-04%20103031.png)

## Estructura del proyecto

cyberpunk_scraper/
│

├── app.py # Servidor principal Flask

├── scraper.py # Lógica del análisis web

├── requirements.txt # Requisitos para ejecutar el proyecto

├── README.md

├── templates/

│         └── index.html # Interfaz HTML (estilo cyberpunk)

├── static/

|         └── style.css # Estilos CSS (colores brillantes, neón)

└── img/ # Capturas de pantalla

## Instalación y uso

### 1. Clonar o descargar el proyecto

    git clone https://github.com/usuario/scraper.git
    cd scraper

2. Crear entorno virtual (opcional pero recomendado)

   python -m venv venv
   venv\Scripts\activate  # En Windows

   source venv/bin/activate  # En Linux/macOS

3. Instalar dependencias

    pip install -r requirements.txt

4. Ejecutar el servidor

    python app.py

5. Usar la aplicación

    Abrir el navegador en: http://localhost:5000

    Ingresar una URL (por ejemplo: https://www.python.org)

    Revisar los resultados

## Ejemplo de URLs válidas para pruebas

https://www.python.org
https://httpbin.org
https://flask.palletsprojects.com

Autor

Nombre: orami

Carrera: Ingeniería en Seguridad Informática

Curso: Programación Avanzada
