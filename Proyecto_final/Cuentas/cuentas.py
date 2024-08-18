from conexionBD import *

class Cuentas:
    def __init__(self, id_cuenta):
        self.id_cuenta = id_cuenta

class Cuenta_Debito:
    def __init__(self, id_cuenta):
        super().__init__(id_cuenta)


    @staticmethod
    def consultar_saldo(id_cuenta):
        try:
            cursor.execute("SELECT saldo_debito FROM debito WHERE id_cuenta=%s", (id_cuenta,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error al obtener el saldo: {e}")
            return []
        
    @staticmethod
    def depositar(id_cuenta, nuevo_saldo):
        try:
            cursor.execute(
                "UPDATE debito SET saldo_debito=%s WHERE id_cuenta=%s",
            (nuevo_saldo, id_cuenta)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al depositar {e}")
            return False

    @staticmethod
    def retirar(id_cuenta, nuevo_saldo):
        try:
            cursor.execute(
                "UPDATE debito SET saldo_debito=%s WHERE id_cuenta=%s",
            (nuevo_saldo, id_cuenta)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al retirar {e}")
            return False
        

    @staticmethod
    def transferir(id_cuenta_origen, nuevo_saldo_origen, id_cuenta_destino, nuevo_saldo_destino):
        try:
            cursor.execute(
                "UPDATE debito SET saldo_debito=%s WHERE id_cuenta=%s",
            (nuevo_saldo_origen, id_cuenta_origen)
            )
            conexion.commit()
            cursor.execute(
                "UPDATE debito SET saldo_debito=%s WHERE id_cuenta=%s",
            (nuevo_saldo_destino, id_cuenta_destino)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al retirar {e}")
            return False
        

class Cuenta_Credito:
    def __init__(self, id_cuenta):
        super().__init__(id_cuenta)


    @staticmethod
    def consultar_saldo(id_cuenta):
        try:
            cursor.execute("SELECT * FROM credito WHERE id_cuenta=%s", (id_cuenta,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al obtener el saldo: {e}")
            return []
        
    @staticmethod
    def pagarTarjeta(id_cuenta, nuevo_saldo):
        try:
            cursor.execute(
                "UPDATE credito SET saldo_pendientes=%s WHERE id_cuenta=%s",
            (nuevo_saldo, id_cuenta)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al deposita {e}")
            return False

    @staticmethod
    def retirar(id_cuenta, nuevo_saldo):
        try:
            cursor.execute(
                "UPDATE credito SET saldo_pendientes=%s WHERE id_cuenta=%s",
            (nuevo_saldo, id_cuenta)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al retirar {e}")
            return False
        

    
        

    

