import random
from datetime import datetime, timedelta


def generar_pool_clientes(cantidad_minima=60, locale='es_AR'):
    """
    Genera una lista de nombres de clientes únicos.
    Si se dispone de Faker, usa nombres argentinos aleatorios.
    """
    # Intentamos importar Faker para generar nombres realistas.
    try:
        from faker import Faker
        usa_faker = True
        fake = Faker(locale)
    except ImportError:
        usa_faker = False
        print("Nota: La librería 'faker' no está instalada. Usando lista de nombres simple.")

    clientes = set()
    
    if usa_faker:
        while len(clientes) < cantidad_minima:
            clientes.add(fake.name())
    else:
        nombres = ["Juan", "María", "Carlos", "Ana", "Pedro", "Sofía", "Miguel", "Lucía", "Diego", "Valentina"]
        apellidos = ["García", "Rodríguez", "González", "Fernández", "López", "Martínez", "Pérez", "Gómez"]
        while len(clientes) < cantidad_minima:
            clientes.add(f"{random.choice(nombres)} {random.choice(apellidos)}")
            
    return list(clientes)

def generar_fecha_acceso():
    """Genera una fecha aleatoria dentro del último año."""
    fin = datetime.now()
    inicio = fin - timedelta(days=365)
    fecha_random = inicio + (fin - inicio) * random.random()
    return fecha_random.isoformat(timespec='seconds')

