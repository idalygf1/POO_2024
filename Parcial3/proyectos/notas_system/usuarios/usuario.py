
from conexionBD import *
import hashlib
import datetime


class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.contrasena = self.hash_password(password) #para encriptar osea que no se vea
    def hash_password(self,contrasena):
        return hashlib.sha256(contrasena.encode()).hexdigest()# para encriptar el mas seguro 

    def registrar(self):

        try:
            fecha=datetime.datetime.now()
            cursor.execute(
                "insert into usuarios values(null,%s,%s,%s,%s,%s)", #Valor dinamico %s
                (self.nombre,self.apellidos,self.email,self.contrasena,fecha)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod #para que sepa que es abstracto y no pida self
    def iniciarSesion(email, contrasena):
        contrasena=hashlib.sha256(contrasena.encode()).hexdigest()
        try:
            cursor.execute(
                "select * from usuarios where email =%s and password=%s",
                (email,contrasena)
            )
            usuario=cursor.fetchone()
            if usuario:
                return usuario
            else:
                return []
        except:
            return []