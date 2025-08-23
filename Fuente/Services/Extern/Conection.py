import os
from dotenv import load_dotenv
import pyodbc

# Configuración de la conexión
load_dotenv()

try:
    connection = pyodbc.connect(os.getenv('connection_string'))
    print("Conexión exitosa a la base de datos")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

# Cerrar la conexión
finally:
    if 'connection' in locals():
        connection.close()
        print("Conexión cerrada")