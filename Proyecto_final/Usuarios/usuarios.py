from conexionBD import *

class Usuarios:
    def __init__(self, id, nombres, apellido_paterno, apellido_materno, rfc, pin):
        self.id = id
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.rfc = rfc
        self.pin = pin


class Clientes(Usuarios):
    def __init__(self, id, pin, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, rfc, regimen, calle, numero, colonia, id_debito, id_credito, saldo_aprobado):
        super().__init__(id, nombres, apellido_paterno, apellido_materno, rfc, pin)
        self.fecha_nacimiento = fecha_nacimiento
        self.regimen = regimen
        self.calle = calle
        self.numero = numero
        self.colonia = colonia
        self.id_debito = id_debito
        self.id_credito = id_credito
        self.saldo_aprobado = saldo_aprobado

        
    
    @staticmethod
    def iniciarSesion(id,pin):
        try:
            cursor.execute(
                "SELECT * FROM clientes WHERE id_clientes=%s AND pin=%s",
                (id, pin)
                )
            correcto = cursor.fetchone()
            if correcto:
                return True
            else: 
                return False
        except Exception as e:
            print("Error de inicio de sesión")
            return False
                

    def crearCliente(self):
        try:
            cursor.execute(
                "INSERT INTO clientes VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (self.id, self.pin, self.nombres, self.apellido_paterno, self.apellido_materno, self.fecha_nacimiento, self.rfc, self.regimen, self.calle, self.numero, self.colonia)
                 )
            cursor.execute(

                "INSERT INTO debito VALUES (%s, %s, %s)",
                (self.id_debito, 0, self.id )
            )
            cursor.execute(
                "INSERT INTO credito VALUES (%s, %s, %s, %s)",
                (self.id_credito, self.saldo_aprobado, 0, self.id )  
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear cliente: {e}")
            return False

    @staticmethod
    def mostrarClientes():
        try:
            cursor.execute("SELECT * FROM clientes")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar clientes: {e}")
            return []
            
    @staticmethod
    def actualizarCliente(id, pin, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, rfc, regimen, calle, numero, colonia):
        try:
            cursor.execute(
                "UPDATE clientes SET pin=%s, nombres=%s, apellido_paterno=%s, apellido_materno=%s, fecha_nacimiento=%s, rfc=%s, regimen=%s, calle=%s, numero=%s, colonia=%s WHERE id_clientes=%s", 
                (pin, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, rfc, regimen, calle, numero, colonia, id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return False
            
    def eliminarCliente(id):
        try:

            cursor.execute(
                "DELETE FROM debito WHERE id_cuenta=%s",
                (id,)
            )
            cursor.execute(
                "DELETE FROM credito WHERE id_cuenta=%s",
                (id,)
            )
            cursor.execute(
                "DELETE FROM clientes WHERE id_clientes=%s ",
                (id,)
                )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            return False
    
    @staticmethod
    def obtenerClientePorNumeroCuenta(id):
        try:
            query = """
            SELECT c.id_clientes, cr.id_credito, db.id_debito
            FROM clientes c
            LEFT JOIN credito cr ON c.id_clientes = cr.id_cuenta
            LEFT JOIN debito db ON c.id_clientes = db.id_cuenta
            WHERE c.id_clientes=%s
            """
            cursor.execute(query, (id,))
            cliente = cursor.fetchone()
            if cliente:
                return {
                    "id_clientes": cliente[0],
                    "id_credito": cliente[1],
                    "id_debito": cliente[2],
                }
            else:
                return None
        except Exception as e:
            print(f"Error al obtener cliente por número de cuenta: {e}")
            return None


    

class Adminsitradores(Usuarios):
    def __init__(self, id, nombres, apellido_paterno, apellido_materno, rfc, pin, salario, puesto):
        super().__init__(id, nombres, apellido_paterno, apellido_materno, rfc, pin)
        self.salario = salario
        self.puesto = puesto


    @staticmethod
    def iniciarSesion(id, pin):
        try:
            cursor.execute(
                "SELECT * FROM administradores WHERE id=%s AND pin=%s",
                (id, pin)
                )
            correcto = cursor.fetchone()
            if correcto:
                return True
            else: 
                return False
        except Exception as e:
            print("Error de inicio de sesión")
            return False

    def crearAdministrador(self):
        try:
            cursor.execute(
                "INSERT INTO administradores VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (self.id, self.nombres, self.apellido_paterno, self.apellido_materno, self.rfc, self.pin, self.salario, self.puesto)
                )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear administrador : {e}")
            return False

    @staticmethod
    def mostrarAdministrador():
        try:
            cursor.execute("SELECT * FROM administradores")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar administrador: {e}")
            return []
            
    @staticmethod
    def actualizarAdministrador(id, nombres, apellido_paterno, apellido_materno, rfc, pin, salario, puesto):
        try:
            cursor.execute(
                "UPDATE administradores SET nombres=%s, apellido_paterno=%s, apellido_materno=%s, rfc=%s, pin=%s, salario=%s, puesto=%s WHERE id=%s",
                (nombres, apellido_paterno, apellido_materno, rfc, pin, salario, puesto, id)
                )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar administrador: {e}")
            return False
            
    def eliminarAdministrador(id):
        try:
            cursor.execute(
                "DELETE FROM administradores WHERE id=%s ",
                (id,)
                )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar administrador: {e}")
            return False


        


