import mysql.connector

#Conexion con la BD de MySQL
try:
    conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='bd_notas'  
    )
    #Se crea un cursor un objeto de tipo cursor con un parametro 
    # que permite reutilizar el mismo objeto
    cursor=conexion.cursor(buffered=True)
except:
    print(f"Ocurrió un error por favor vuelva inentar más tarde")