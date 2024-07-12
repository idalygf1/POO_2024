
from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, 'Juan Polainas', 'Col. del valle', '6181234567');"

    micursor.execute(sql)
    #Es necesario ejecutar el commit para que finalice el SQL con éxito
    conexion.commit()
except:
    print(f"Ocurrió un error por favor vuelva inentar más tarde")
else:
    print("Registro insertado con éxito")