"""
Una función es un conjunto de instrucciones
agrupadas bajo un nombre en particular como un 
programa más pequeño que cumple una función
específica . La función se puede reutilizar con 
el simple hecho de invocarla es decir mandarla 
llamar 

  Sintaxis:

   def nombredeMifuncion(parámetros):
     bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
   1°- Función que no recibe parámetros y no regresa valor
   2°- Función que no recibe parámetros y regresa valor
   3°- Función que recibe parámetros y no regresa valor
   4°- Función que recibe parámetros y regresa valor
   

  """

#1.  Función que no recibe parámetros y no regresa valor

def sumaNumeros1():
    n1= int(input("Numero 1:"))
    n2= int(input("Numero 2:"))
    suma = n1+n2
    print(f"{n1} + {n2} = {suma}")

sumaNumeros1()

#2.  Función que no recibe parámetros y regresa valor

def sumaNumeros2():
    n1= int(input("Numero 1:"))
    n2= int(input("Numero 2:"))
    suma = n1+n2
    return f"{n1} + {n2} = {suma}"

print(sumaNumeros2())

#3.  Función que recibe parámetros y no regresa valor

def sumaNumeros3(n1,n2):
    suma = n1+n2
    print(f"{n1} + {n2} = {suma}")

n1= int(input("Numero 1:"))
n2= int(input("Numero 2:"))
sumaNumeros3(n1,n2)

#4.  Función que recibe parámetros y regresa valor

def sumaNumeros4(n1,n2):
    suma = n1+n2
    return f"{n1} + {n2} = {suma}"

n1= int(input("Numero 1:"))
n2= int(input("Numero 2:"))
print(sumaNumeros4(n1,n2))


#Ejemplo 6 Crear un programa que solicite a través de una función la siguiente 
#información: Nombre del paciente, Edad, Estatura, Tipo de Sangre Utilizar los
#4 tipos de funciones

def informacionPaciente1():
    nombre_paciente = input("Ingrese el nombre del paciente")
    edad = int(input("Ingrese la edad del paciente"))
    estatura = float(input("Ingrese la estatura del paciente"))
    tipo_sangre = input("Ingrese el tipo de sangre")
    print(f"Paciente: {nombre_paciente} tiene {edad} años, mide {estatura} y tiene sangre{tipo_sangre} ")

informacionPaciente1()



def informacionPaciente2():
    nombre_paciente = input("Ingrese el nombre del paciente")
    edad = int(input("Ingrese la edad del paciente"))
    estatura = float(input("Ingrese la estatura del paciente"))
    tipo_sangre = input("Ingrese el tipo de sangre")
    return f"Paciente: {nombre_paciente} tiene {edad} años, mide {estatura} y tiene sangre{tipo_sangre} "

print(informacionPaciente2())
    


def informacionPaciente3(nombre_paciente, edad, estatura, tipo_sangre):
    
    print(f"Paciente: {nombre_paciente} tiene {edad} años, mide {estatura} y tiene sangre{tipo_sangre} ")


nombre_paciente = input("Ingrese el nombre del paciente")
edad = int(input("Ingrese la edad del paciente"))
estatura = float(input("Ingrese la estatura del paciente"))
tipo_sangre = input("Ingrese el tipo de sangre")
informacionPaciente3(nombre_paciente, edad, estatura, tipo_sangre)



def informacionPaciente4(nombre_paciente, edad, estatura, tipo_sangre):
    
    return f"Paciente: {nombre_paciente} tiene {edad} años, mide {estatura} y tiene sangre{tipo_sangre} "


nombre_paciente = input("Ingrese el nombre del paciente")
edad = int(input("Ingrese la edad del paciente"))
estatura = float(input("Ingrese la estatura del paciente"))
tipo_sangre = input("Ingrese el tipo de sangre")
print(informacionPaciente4(nombre_paciente, edad, estatura, tipo_sangre))