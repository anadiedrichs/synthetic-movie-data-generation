import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# --- CONFIGURACIÓN ---
CANTIDAD_A_GENERAR = 10 
NOMBRE_ARCHIVO_SALIDA = "../data/dataset_mongo_argentina.json"

# ¡ATENCIÓN! Si tienes una API Key de TMDB, pégala en el archivo .env (TMDB_API_KEY="tu_clave_aqui")
# Si lo dejas vacío en .env, o el archivo .env no existe, el script usará la lista manual rápida.
TMDB_API_KEY = os.getenv("TMDB_API_KEY", "")
