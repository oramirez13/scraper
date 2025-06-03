# Cyberpunk Web Scanner

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

## Estructura del proyecto

cyberpunk_scraper/
│
├── app.py # Servidor principal Flask
├── scraper.py # Lógica del análisis web
├── requirements.txt # Requisitos para ejecutar el proyecto
├── README.md
├── templates/
│ └── index.html # Interfaz HTML (estilo cyberpunk)
└── static/
└── style.css # Estilos CSS (colores brillantes, neón)


## ⚙️ Instalación y uso

### 1. Clonar o descargar el proyecto

```bash
git clone https://github.com/usuario/cyberpunk_scraper.git
cd cyberpunk_scraper

2. Crear entorno virtual (opcional pero recomendado)

python -m venv venv
venv\Scripts\activate  # En Windows
# o
source venv/bin/activate  # En Linux/macOS

3. Instalar dependencias

pip install -r requirements.txt

4. Ejecutar el servidor

python app.py

