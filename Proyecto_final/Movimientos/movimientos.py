from conexionBD import *
class Movimiento:
    def __init__(self, n_movimiento, fecha, tipo, monto_depositado, descripcion, saldo_final):
        self.n_movimiento = n_movimiento
        self.fecha = fecha
        self.tipo = tipo
        self.monto_depositado = monto_depositado
        self.descripcion = descripcion
        self.saldo_final = saldo_final

class Movimiento_debito(Movimiento):
    def __init__(self, id_movimiento_debito, n_movimiento, fecha, tipo, monto_depositado, descripcion, saldo_final, id_debito):
        super().__init__(n_movimiento, fecha, tipo, monto_depositado, descripcion, saldo_final)
        self.id_movimiento_debito = id_movimiento_debito
        self.id_debito = id_debito

    def agregarMovimiento(self):
        try:
            cursor.execute(
                "INSERT INTO movimiento_debito VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (self.id_movimiento_debito, self.n_movimiento, self.fecha, self.tipo, self.monto_depositado, self.descripcion, self.saldo_final, self.id_debito)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar movimiento: {e}")
            return False
        
    @staticmethod
    def mostrarMovimientos(id_debito):
        try:
            cursor.execute("SELECT * FROM movimiento_debito WHERE id_debito=%s", (id_debito,))
            return cursor.fetchall()
        
        except Exception as e:
            print(F"Error al mostrar estados de cuenta: {e}")


class Movimiento_credito(Movimiento):
    def __init__(self, id_movimiento_credito, n_movimiento, fecha, tipo, monto_depositado, descripcion, saldo_final, id_credito):
        super().__init__(n_movimiento, fecha, tipo, monto_depositado, descripcion, saldo_final)
        self.id_movimiento_credito = id_movimiento_credito
        self.id_credito = id_credito

    def agregarMovimiento(self):
        try:
            cursor.execute(
                "INSERT INTO movimiento_credito VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (self.id_movimiento_credito, self.n_movimiento, self.fecha, self.tipo, self.monto_depositado, self.descripcion, self.saldo_final, self.id_credito)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al registrar movimiento: {e}")
            return False
        
    @staticmethod
    def mostrarMovimientos(id_credito):
        try:
            cursor.execute("SELECT * FROM movimiento_credito WHERE id_credito=%s", (id_credito,))
            return cursor.fetchall()
        
        except Exception as e:
            print(F"Error al mostrar estados de cuenta: {e}")

    