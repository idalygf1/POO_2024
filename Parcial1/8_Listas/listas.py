# List(Array)
# son coleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores
# se hace con un índice numérico

# Nota: sus valores si son modificables 

# La lista es una coleción ordenada y modificable. Permite miembros duplicados.

#Ejemplo 1 Crear una lista con valores numéricos enteros e impriir la lista 

numeros=[23,34]
print(numeros)

#Recorrer las listas con un FOR salto de linea
for i in numeros:
    print(i)

#Recorrer la lista con un WHILE
i=0
while i<len(numeros):
    print(numeros[i])
    i+=1

#Ejemplo 2 Crear una lista de palabras, posteriormente ingresar una palabra para buscar la coincidencia en la lista, e indicar si aparece la palabra y en que posicion en caso contrario indicar una sola vez si no lo encontro 

palabras=["hola","2024","13.23","True"]

palabra_buscar=input("Ingresa la palabra a buscar: ")

palab=["hola","2024","13.23","True"]
print(palab)

