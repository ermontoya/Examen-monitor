## Monitor del Sistema con Django y Psutil

Este proyecto es una aplicación web desarrollada en Django que permite visualizar en tiempo real el estado del sistema, incluyendo el uso del CPU, memoria RAM, almacenamiento en disco y otros recursos relevantes, utilizando la librería externa `psutil`.

---

## Tecnologías usadas

- Python 3
- Django
- Psutil

---

## Instalación paso a paso

1. Crear el entorno virtual y activarlo:
python3 -m venv venv
source venv/bin/activate


2. Instalar dependencias:

pip install -r requirements.txt

3. Ejecutar el servidor:
python manage.py runserver

4. Abrir en el navegador:
http://127.0.0.1:8000/

## Estructura del Proyecto

monitor/: proyecto principal
sistema/: aplicación interna
sistema/views.py: lógica para obtener datos del sistema
sistema/templates/sistema/index.html: interfaz web con tarjetas
requirements.txt: dependencias del proyecto
README.md: este archivo

## Autores
Jose Enrique Montoya 201820110033

## Video de explicación
