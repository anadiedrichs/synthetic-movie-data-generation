import json
from catalogs import *
from generators import *
from config import *
import uuid


def generar_dataset(tamano_dataset, catalogo_origen=None):
    """
    Función principal para generar el dataset.
    Permite pasar un catalogo_origen personalizado (ej: desde API).
    """
    
    # 1. Obtener recursos base (si no hay catalogo externo, usa el manual)
    if catalogo_origen:
        catalogo = catalogo_origen
    else:
        catalogo = obtener_catalogo_argentino()
        
    if not catalogo:
        print("Error: El catálogo de películas está vacío.")
        return []

    clientes = generar_pool_clientes(cantidad_minima=60)
    
    dataset = []
    
    for _ in range(tamano_dataset):
        contenido = random.choice(catalogo)
        cliente = random.choice(clientes)
        
        documento = {
            "clientId": str(uuid.uuid4()),
            "nombre_contenido": contenido["nombre"],
            "anio_estreno": contenido["anio"],
            "actores": contenido["actores"],
            "nombre_cliente": cliente,
            "fecha_acceso": generar_fecha_acceso()
        }
        dataset.append(documento)
        
    return dataset

def guardar_dataset_en_json(dataset, nombre_archivo):
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            json.dump(dataset, f, indent=4, ensure_ascii=False)
        print(f"\n[Éxito] Archivo guardado correctamente como: {nombre_archivo}")
    except Exception as e:
        print(f"\n[Error] No se pudo guardar el archivo: {e}")

# Bloque de ejecución principal
if __name__ == "__main__":
    
    # --- LOGICA ---
    catalogo_a_usar = None
    
    if TMDB_API_KEY:
        # Si hay clave, intentamos traer datos frescos de la API
        print("API Key detectada. Intentando obtener datos desde TMDB...")
        catalogo_api = obtener_catalogo_tmdb(TMDB_API_KEY, cantidad=100)
        if catalogo_api:
            catalogo_a_usar = catalogo_api
            print("¡Catálogo descargado con éxito!")
        else:
            print("Falló la descarga de API. Usando catálogo manual de respaldo.")
    else:
        print("No se detectó API Key. Usando catálogo manual interno (Modo Rápido).")

    print(f"--- Generando dataset de {CANTIDAD_A_GENERAR} registros ---")
    
    # Generamos usando el catálogo seleccionado (o None para que use el default)
    datos_generados = generar_dataset(CANTIDAD_A_GENERAR, catalogo_origen=catalogo_a_usar)
    
    if datos_generados:
        print("\n--- Documento de Ejemplo (Captura) ---")
        print(json.dumps(datos_generados[0], indent=4, ensure_ascii=False))
        guardar_dataset_en_json(datos_generados, NOMBRE_ARCHIVO_SALIDA)