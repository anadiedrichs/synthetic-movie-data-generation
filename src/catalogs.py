
from time import time


# Intentamos importar requests para la API de TMDB

try:
    import requests
except ImportError:
    requests = None
    print("Nota: La librería 'requests' no está instalada. La función de TMDB no estará disponible.")

def obtener_catalogo_argentino():
    """
    Retorna una lista manual con 100 películas y series argentinas reales
    con sus respectivos años y actores principales. (Método Offline/Rápido)
    """
    return [
        # Clásicos y Siglo XX
        {"nombre": "Esperando la carroza", "anio": 1985, "actores": ["China Zorrilla", "Luis Brandoni", "Antonio Gasalla"]},
        {"nombre": "La historia oficial", "anio": 1985, "actores": ["Norma Aleandro", "Héctor Alterio"]},
        {"nombre": "La tregua", "anio": 1974, "actores": ["Héctor Alterio", "Ana María Picchio"]},
        {"nombre": "Camila", "anio": 1984, "actores": ["Susú Pecoraro", "Imanol Arias"]},
        {"nombre": "Plata dulce", "anio": 1982, "actores": ["Federico Luppi", "Julio De Grazia"]},
        {"nombre": "Nueve reinas", "anio": 2000, "actores": ["Ricardo Darín", "Gastón Pauls", "Leticia Brédice"]},
        {"nombre": "Pizza, birra, faso", "anio": 1998, "actores": ["Héctor Anglada", "Jorge Sesán"]},
        {"nombre": "Mundo grúa", "anio": 1999, "actores": ["Luis Margani", "Adriana Bizotti"]},
        {"nombre": "El lado oscuro del corazón", "anio": 1992, "actores": ["Darío Grandinetti", "Sandra Ballesteros"]},
        {"nombre": "Caballos salvajes", "anio": 1995, "actores": ["Héctor Alterio", "Leonardo Sbaraglia"]},
        {"nombre": "Cenizas del paraíso", "anio": 1997, "actores": ["Héctor Alterio", "Cecilia Roth"]},
        {"nombre": "El bonaerense", "anio": 2002, "actores": ["Jorge Román", "Mimí Ardú"]},
        {"nombre": "Historias mínimas", "anio": 2002, "actores": ["Javier Lombardo", "Antonio Benedictis"]},
        {"nombre": "Valentín", "anio": 2002, "actores": ["Rodrigo Noya", "Carmen Maura"]},
        {"nombre": "El hijo de la novia", "anio": 2001, "actores": ["Ricardo Darín", "Héctor Alterio", "Norma Aleandro"]},
        {"nombre": "Luna de Avellaneda", "anio": 2004, "actores": ["Ricardo Darín", "Mercedes Morán"]},
        {"nombre": "Tiempo de valientes", "anio": 2005, "actores": ["Diego Peretti", "Luis Luque"]},
        {"nombre": "Un oso rojo", "anio": 2002, "actores": ["Julio Chávez", "Soledad Villamil"]},
        {"nombre": "El aura", "anio": 2005, "actores": ["Ricardo Darín", "Dolores Fonzi"]},
        {"nombre": "Crónica de una fuga", "anio": 2006, "actores": ["Rodrigo de la Serna", "Pablo Echarri"]},

        # Éxitos Modernos (2009 - Presente)
        {"nombre": "El secreto de sus ojos", "anio": 2009, "actores": ["Ricardo Darín", "Soledad Villamil", "Guillermo Francella"]},
        {"nombre": "Relatos salvajes", "anio": 2014, "actores": ["Ricardo Darín", "Érica Rivas", "Leonardo Sbaraglia"]},
        {"nombre": "Carancho", "anio": 2010, "actores": ["Ricardo Darín", "Martina Gusmán"]},
        {"nombre": "Un cuento chino", "anio": 2011, "actores": ["Ricardo Darín", "Muriel Santa Ana"]},
        {"nombre": "Elefante blanco", "anio": 2012, "actores": ["Ricardo Darín", "Jérémie Renier"]},
        {"nombre": "Metegol", "anio": 2013, "actores": ["Pablo Rago", "Diego Ramos"]},
        {"nombre": "Wakolda", "anio": 2013, "actores": ["Natalia Oreiro", "Diego Peretti"]},
        {"nombre": "El clan", "anio": 2015, "actores": ["Guillermo Francella", "Peter Lanzani"]},
        {"nombre": "El ciudadano ilustre", "anio": 2016, "actores": ["Oscar Martínez", "Dady Brieva"]},
        {"nombre": "Gilda, no me arrepiento de este amor", "anio": 2016, "actores": ["Natalia Oreiro", "Lautaro Delgado"]},
        {"nombre": "Nieve negra", "anio": 2017, "actores": ["Ricardo Darín", "Leonardo Sbaraglia"]},
        {"nombre": "Zama", "anio": 2017, "actores": ["Daniel Giménez Cacho", "Lola Dueñas"]},
        {"nombre": "El ángel", "anio": 2018, "actores": ["Lorenzo Ferro", "Chino Darín"]},
        {"nombre": "Acusada", "anio": 2018, "actores": ["Lali Espósito", "Leonardo Sbaraglia"]},
        {"nombre": "La odisea de los giles", "anio": 2019, "actores": ["Ricardo Darín", "Luis Brandoni"]},
        {"nombre": "El robo del siglo", "anio": 2020, "actores": ["Guillermo Francella", "Diego Peretti"]},
        {"nombre": "Argentina, 1985", "anio": 2022, "actores": ["Ricardo Darín", "Peter Lanzani"]},
        {"nombre": "Granizo", "anio": 2022, "actores": ["Guillermo Francella", "Peto Menahem"]},
        {"nombre": "30 noches con mi ex", "anio": 2022, "actores": ["Adrián Suar", "Pilar Gamboa"]},
        {"nombre": "La extorsión", "anio": 2023, "actores": ["Guillermo Francella", "Pablo Rago"]},
        {"nombre": "Puan", "anio": 2023, "actores": ["Marcelo Subiotto", "Leonardo Sbaraglia"]},
        {"nombre": "Cuando acecha la maldad", "anio": 2023, "actores": ["Ezequiel Rodríguez", "Demián Salomón"]},
        {"nombre": "Los delincuentes", "anio": 2023, "actores": ["Esteban Bigliardi", "Daniel Elías"]},
        {"nombre": "Blondi", "anio": 2023, "actores": ["Dolores Fonzi", "Carla Peterson"]},
        {"nombre": "Casi muerta", "anio": 2023, "actores": ["Natalia Oreiro", "Diego Velázquez"]},
        {"nombre": "Norma", "anio": 2023, "actores": ["Mercedes Morán", "Alejandro Awada"]},
        {"nombre": "El rapto", "anio": 2023, "actores": ["Rodrigo de la Serna", "Julieta Zylberberg"]},
        {"nombre": "Elena sabe", "anio": 2023, "actores": ["Mercedes Morán", "Érica Rivas"]},
        {"nombre": "No me rompan", "anio": 2023, "actores": ["Carla Peterson", "Julieta Díaz"]},
        {"nombre": "Descansar en paz", "anio": 2024, "actores": ["Joaquín Furriel", "Griselda Siciliani"]},
        {"nombre": "Goyo", "anio": 2024, "actores": ["Nicolás Furtado", "Nancy Dupláa"]},

        # Series Argentinas Icónicas y Nuevas
        {"nombre": "Los simuladores", "anio": 2002, "actores": ["Federico D'Elía", "Diego Peretti", "Martín Seefeld", "Alejandro Fiore"]},
        {"nombre": "Okupas", "anio": 2000, "actores": ["Rodrigo de la Serna", "Ariel Staltari"]},
        {"nombre": "Hermanos y detectives", "anio": 2006, "actores": ["Rodrigo Noya", "Rodrigo de la Serna"]},
        {"nombre": "Vientos de agua", "anio": 2006, "actores": ["Héctor Alterio", "Eduardo Blanco"]},
        {"nombre": "Epitafios", "anio": 2004, "actores": ["Julio Chávez", "Cecilia Roth"]},
        {"nombre": "El marginal", "anio": 2016, "actores": ["Nicolás Furtado", "Claudio Rissi", "Juan Minujín"]},
        {"nombre": "Historia de un clan", "anio": 2015, "actores": ["Alejandro Awada", "Chino Darín"]},
        {"nombre": "Un gallo para Esculapio", "anio": 2017, "actores": ["Peter Lanzani", "Luis Brandoni"]},
        {"nombre": "Monzón", "anio": 2019, "actores": ["Jorge Román", "Mauricio Paniagua"]},
        {"nombre": "El reino", "anio": 2021, "actores": ["Diego Peretti", "Chino Darín", "Mercedes Morán"]},
        {"nombre": "Santa Evita", "anio": 2022, "actores": ["Natalia Oreiro", "Darío Grandinetti"]},
        {"nombre": "Iosi, el espía arrepentido", "anio": 2022, "actores": ["Natalia Oreiro", "Gustavo Bassani"]},
        {"nombre": "El encargado", "anio": 2022, "actores": ["Guillermo Francella", "Gabriel Goity"]},
        {"nombre": "División Palermo", "anio": 2023, "actores": ["Santiago Korovsky", "Pilar Gamboa"]},
        {"nombre": "El amor después del amor", "anio": 2023, "actores": ["Iván Hochman", "Micaela Riera"]},
        {"nombre": "Diciembre 2001", "anio": 2023, "actores": ["Jean Pierre Noher", "Diego Cremonesi"]},
        {"nombre": "Barrabrava", "anio": 2023, "actores": ["Gastón Pauls", "Matías Mayer"]},
        {"nombre": "Nada", "anio": 2023, "actores": ["Luis Brandoni", "Robert De Niro"]},
        {"nombre": "Coppola, el representante", "anio": 2024, "actores": ["Juan Minujín", "Mónica Antonópulos"]},
        {"nombre": "El eternauta", "anio": 2025, "actores": ["Ricardo Darín", "Carla Peterson"]},

        # Rellenando hasta llegar a 100 con más títulos variados
        {"nombre": "Tango feroz", "anio": 1993, "actores": ["Fernán Mirás", "Cecilia Dopazo"]},
        {"nombre": "Martín (Hache)", "anio": 1997, "actores": ["Federico Luppi", "Juan Diego Botto"]},
        {"nombre": "Comodines", "anio": 1997, "actores": ["Adrián Suar", "Carlos Calvo"]},
        {"nombre": "El mismo amor, la misma lluvia", "anio": 1999, "actores": ["Ricardo Darín", "Soledad Villamil"]},
        {"nombre": "La ciénaga", "anio": 2001, "actores": ["Graciela Borges", "Mercedes Morán"]},
        {"nombre": "La niña santa", "anio": 2004, "actores": ["Mercedes Morán", "María Alche"]},
        {"nombre": "Derecho de familia", "anio": 2006, "actores": ["Daniel Hendler", "Julieta Díaz"]},
        {"nombre": "XXY", "anio": 2007, "actores": ["Ricardo Darín", "Inés Efron"]},
        {"nombre": "Leonera", "anio": 2008, "actores": ["Martina Gusmán", "Elli Medeiros"]},
        {"nombre": "El hombre de al lado", "anio": 2009, "actores": ["Rafael Spregelburd", "Daniel Aráoz"]},
        {"nombre": "Viudas", "anio": 2011, "actores": ["Graciela Borges", "Valeria Bertuccelli"]},
        {"nombre": "Dos más dos", "anio": 2012, "actores": ["Adrián Suar", "Julieta Díaz"]},
        {"nombre": "Tesis sobre un homicidio", "anio": 2013, "actores": ["Ricardo Darín", "Calu Rivero"]},
        {"nombre": "Corazón de león", "anio": 2013, "actores": ["Guillermo Francella", "Julieta Díaz"]},
        {"nombre": "Séptimo", "anio": 2013, "actores": ["Ricardo Darín", "Belén Rueda"]},
        {"nombre": "Betibú", "anio": 2014, "actores": ["Mercedes Morán", "Daniel Fanego"]},
        {"nombre": "Voley", "anio": 2014, "actores": ["Martín Piroyansky", "Violeta Urtizberea"]},
        {"nombre": "Abzurdah", "anio": 2015, "actores": ["China Suárez", "Esteban Lamothe"]},
        {"nombre": "Kóblic", "anio": 2016, "actores": ["Ricardo Darín", "Oscar Martínez"]},
        {"nombre": "Permitidos", "anio": 2016, "actores": ["Lali Espósito", "Martín Piroyansky"]},
        {"nombre": "Mamá se fue de viaje", "anio": 2017, "actores": ["Diego Peretti", "Carla Peterson"]},
        {"nombre": "El fútbol o yo", "anio": 2017, "actores": ["Adrián Suar", "Julieta Díaz"]},
        {"nombre": "Perdida", "anio": 2018, "actores": ["Luisana Lopilato", "Amaia Salamanca"]},
        {"nombre": "El potro", "anio": 2018, "actores": ["Rodrigo Romero", "Jimena Barón"]},
        {"nombre": "Re loca", "anio": 2018, "actores": ["Natalia Oreiro", "Diego Torres"]},
        {"nombre": "Mi obra maestra", "anio": 2018, "actores": ["Guillermo Francella", "Luis Brandoni"]},
        {"nombre": "4x4", "anio": 2019, "actores": ["Peter Lanzani", "Dady Brieva"]},
        {"nombre": "El cuaderno de Tomy", "anio": 2020, "actores": ["Valeria Bertuccelli", "Esteban Lamothe"]},
        {"nombre": "Corazón loco", "anio": 2020, "actores": ["Adrián Suar", "Soledad Villamil"]},
        {"nombre": "Causalidad", "anio": 2021, "actores": ["Juana Viale", "Laura Novoa"]},
        {"nombre": "Distancia de rescate", "anio": 2021, "actores": ["Dolores Fonzi", "María Valverde"]},
        {"nombre": "Ecos de un crimen", "anio": 2022, "actores": ["Diego Peretti", "Julieta Cardinali"]},
        {"nombre": "Pipa", "anio": 2022, "actores": ["Luisana Lopilato", "Mauricio Paniagua"]},
        {"nombre": "Más respeto que soy tu madre", "anio": 2022, "actores": ["Florencia Peña", "Diego Peretti"]},
        {"nombre": "El gerente", "anio": 2022, "actores": ["Leonardo Sbaraglia", "Carla Peterson"]},
        {"nombre": "Matrimillas", "anio": 2022, "actores": ["Luisana Lopilato", "Juan Minujín"]},
        {"nombre": "La ira de Dios", "anio": 2022, "actores": ["Diego Peretti", "Juan Minujín"]},
        {"nombre": "Objetos", "anio": 2023, "actores": ["China Suárez", "Álvaro Morte"]},
        {"nombre": "Asfixiados", "anio": 2023, "actores": ["Leonardo Sbaraglia", "Julieta Díaz"]}
    ]

def obtener_catalogo_tmdb(api_key, cantidad=100, lang='es_AR', country = "AR"):
    """
    Obtiene un catálogo de películas argentinas conectándose a la API de TMDB.
    Requiere una API KEY válida y la librería 'requests'.
    Devuelve lista de diccionarios con formato: {'nombre', 'anio', 'actores'}
    """
    if not requests:
        print("Error: No se puede usar TMDB sin la librería 'requests'.")
        return []
        
    print(f"\n--- Conectando a TMDB para descargar {cantidad} películas argentinas ---")
    url_descubrimiento = "https://api.themoviedb.org/3/discover/movie"
    catalogo_api = []
    pagina = 1
    
    while len(catalogo_api) < cantidad:
        try:
            # 1. Buscar películas argentinas populares
            params = {
                "api_key": api_key,
                "language": lang,
                "with_origin_country": country, # Filtrar por Argentina
                "sort_by": "popularity.desc",
                "page": pagina
            }
            
            resp = requests.get(url_descubrimiento, params=params)
            if resp.status_code != 200:
                print(f"Error API: {resp.status_code} - {resp.text}")
                break
                
            resultados = resp.json().get("results", [])
            if not resultados:
                break # No hay más resultados
                
            for p in resultados:
                if len(catalogo_api) >= cantidad:
                    break
                    
                # 2. Para cada película, obtener actores (requiere llamada extra)
                # Nota: Esto hace que el proceso sea más lento, pero los datos son reales.
                id_pelicula = p["id"]
                url_creditos = f"https://api.themoviedb.org/3/movie/{id_pelicula}/credits"
                resp_creditos = requests.get(url_creditos, params={"api_key": api_key})
                
                actores_lista = []
                if resp_creditos.status_code == 200:
                    cast = resp_creditos.json().get("cast", [])
                    # Tomamos los top 3 o 4 actores
                    actores_lista = [actor['name'] for actor in cast[:4]]
                
                # Procesar fecha de estreno
                fecha_str = p.get("release_date", "")
                anio = int(fecha_str[:4]) if fecha_str and len(fecha_str) >= 4 else 2000
                
                catalogo_api.append({
                    "nombre": p["title"],
                    "anio": anio,
                    "actores": actores_lista
                })
                
                # Pequeña pausa para ser amables con la API
                time.sleep(0.1) 
            
            pagina += 1
            print(f"Procesada página {pagina-1}... (Total: {len(catalogo_api)})")
            
        except Exception as e:
            print(f"Error conectando a TMDB: {e}")
            break
            
    return catalogo_api
