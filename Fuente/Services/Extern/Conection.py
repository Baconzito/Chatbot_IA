import pyodbc

# Configuración de la conexión
server = 'localhost\\SQLEXPRESS'
database = 'Ai_Chan'
connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;TrustServerCertificate=yes;'

# Conexión a la base de datos
try:
    connection = pyodbc.connect(connection_string)
    print("Conexión exitosa a la base de datos")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

# Cerrar la conexión
finally:
    if 'connection' in locals():
        connection.close()
        print("Conexión cerrada")