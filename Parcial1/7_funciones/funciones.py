#Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular
#como un programa más pequeño que cumple una función específica. La función se puede rautlizar 
#con el simple hecho de invocarla es decir mandarla llamar. 

#Sintaxis
#def nombredeMifuncion(parametros):
# bloque o conjunto de instrucciones

# # # nombreMifuncion(parametros)

# Las funciones pueden ser de 4 tipos 
# 1.- Función que no recibe parametros y no regresa valor 
# 2.- Función que no recibe paramatros y regresa valor 
# 3.- funcion que no recibe parametros y no regresa valor 
# 4.- Función que recibe parametros y regresa valor 

#1.- Función que no recibe parametros y no regresa valor

# def sumaNumeros1():
#     n1=int(input("Número #1:"))
#     n2=int(input("Número #2:"))

#     suma=n1+n2
#     print(f"{n1}+{n2}")

#     sumaNumeros1()

# 2.- Función que no recibe paramatros y regresa valor

# def sumaNumeros2():
#     n1=int(input("Número #1:"))
#     n2=int(input("Número #2:"))

#     suma=n1+n2
#     return(f"{n1}+{n2}={suma}") #return se regresa a la línea 29

#     print(sumaNumeros2())

# 3.- funcion que no recibe parametros y no regresa valor 

def sumaNumeros3(n1,n2):

    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

sumaNumeros3(34,23)