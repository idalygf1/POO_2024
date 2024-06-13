# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas

lista = []

if not lista:
    print("La lista está vacía. Ingrese palabras o frases para llenarla :")
    while True:
        entrada = input("> ")
        if entrada=="salir": 
            lista.append(entrada)
    

print("\nContenido de la lista en mayúsculas:")
for elemento in lista:
    print(elemento.upper())#convierte a mayusculas los caracteres