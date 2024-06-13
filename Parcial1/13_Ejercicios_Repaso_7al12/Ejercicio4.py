#  Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones



cadena = "Hola, mundo"
entero = 42
booleano = True

def imprimir_mensaje_lista(lista):
    print(f"La variable '{lista}' es una lista.")

def imprimir_mensaje_cadena(cadena):
    print(f"La variable '{cadena}' es una cadena.")

def imprimir_mensaje_entero(entero):
    print(f"La variable '{entero}' es un entero.")

def imprimir_mensaje_booleano(booleano):
    print(f"La variable '{booleano}' es un booleano.")



imprimir_mensaje_cadena(cadena)
imprimir_mensaje_entero(entero)
imprimir_mensaje_booleano(booleano)