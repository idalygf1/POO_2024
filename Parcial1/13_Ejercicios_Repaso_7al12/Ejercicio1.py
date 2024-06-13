# 1.- Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado
numeros=[2,5,12,9,1,10,3,4]
print(numeros)
numeros.sort() #Funcion ordenar
print("\n")
for num in numeros:
    print(num)

def recorrer(lista):
    recorrer_lista = ""
    for num in lista:
        recorrer_lista_lista += str(num) + ","
    return recorrer_lista()
print("\n")

longitud = len(numeros)
print(f"Longitud de la lista: {longitud}")

elemento_buscar = int(input("Ingrese un número entero a buscar en la lista: "))


if elemento_buscar in numeros:
    print(f"El elemento {elemento_buscar} se encuentra en la lista.")
else:
    print(f"El elemento {elemento_buscar} no se encuentra en la lista.")

