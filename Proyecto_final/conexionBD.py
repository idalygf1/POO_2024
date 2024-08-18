import mysql.connector

try:
    conexion=mysql.connector.connect(
        host='localhost',
        user = 'root',
        password = '',
        database = 'banfuturo'
    )
    cursor = conexion.cursor(buffered=True)
    print("Conexión exitosa a la base de datos")

except Exception as e:
    print(f"Ocurrió un error al conectar con la base de datos: {e}")