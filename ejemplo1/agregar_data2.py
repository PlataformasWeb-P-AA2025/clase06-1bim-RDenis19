from sqlalchemy.orm import sessionmaker
from crear_base import Saludo2
from configuracion import engine
import csv 

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# Abrir el csv y leerlo 
with open('data/saludos_mundo.csv', newline='', encoding='utf-8') as archivo:
    lector = csv.DictReader(archivo, delimiter='|')
    for fila in lector:
        saludo = Saludo2(
            mensaje=fila['saludo'],
            tipo=fila['tipo'],
            origen=fila['origen']
        )
        session.add(saludo)

# Confirmar transacción
session.commit()