import os
from dotenv import load_dotenv
import pyodbc

# Obtener la ruta absoluta del archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__), 'configs.env')
load_dotenv(dotenv_path=dotenv_path)

try:
    connection_string = os.getenv('CONNECTION_STRING')
    print(f"CONNECTION_STRING: {connection_string}")  # Para depuración
    connection = pyodbc.connect(connection_string)
    print("Conexión exitosa a la base de datos")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
finally:
    if 'connection' in locals():
        connection.close()
        print("Conexión cerrada")