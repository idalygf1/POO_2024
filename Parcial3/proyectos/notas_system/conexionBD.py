import mysql.connector

#Conexion con la BD de MySQL
try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_notas'  
    )
except Exception as e:
    print(f"Ocurrió un error por favor vuelva inentar más tarde")