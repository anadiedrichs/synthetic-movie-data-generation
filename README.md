# synthetic-movie-data-generation

* Generate a synthetic dataset to ingest to mongoDB. 
* This is an academic / teaching project.
* Below, the instructions in Spanish for the team.

# Generación de datos sintéticos.

## Requisitos

* Debe ya contar con Python 3.12 instalado en su sistema operativo.
* Conocimientos de Git y Python.

## Instrucciones de configuración

### 1) Clonar este repositorio

### 2) Virtual environment de Python

Crea el entorno virtual: esto aísla las dependencias de tu proyecto.

En tu terminal, dentro de la carpeta del proyecto:

```
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3) Instalación de librerías

En tu terminal, dentro de la carpeta del proyecto:

```
pip install -r requirements.txt
```

### 4) Variables de entorno

Copia el archivo .env.example para renombrarlo a .env.

```
cp .env.example .env
```
Dentro del mismo debes agregar tus claves para cada API.

**NO agregues a Git tu archivo .env**

**NO agregues a Git tu archivo .env**

### 5) API key

Para el servicio TMDB, debes tener una API KEY , como se menciona en el archivo .env.
Completalo antes de ejecutar el proyecto si deseas utilizar esta API. 
De lo contrario se usará el catálogo por defecto de películas argentinas.
