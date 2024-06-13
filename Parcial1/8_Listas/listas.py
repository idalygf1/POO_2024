# List(Array)
# son coleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores
# se hace con un índice numérico

# Nota: sus valores si son modificables 

# La lista es una coleción ordenada y modificable. Permite miembros duplicados.

#Ejemplo 1 Crear una lista con valores numéricos enteros e impriir la lista 

# numeros=[23,34]
# print(numeros).

#Recorrer las listas con un FOR salto de linea
# for i in numeros:
#     print(i)

# #Recorrer la lista con un WHILE
# i=0
# while i<len(numeros):
#     print(numeros[i])
#     i+=1

#Ejemplo 2 Crear una lista de palabras, posteriormente ingresar una palabra 
#para buscar la coincidencia en la lista, e indicar si aparece la palabra y en que posicion en caso contrario indicar una sola vez si no lo encontro 

# palabras=["hola","2024","13.23","True"]
# print(palabras)

# palabra_buscar=input("Ingresa la palabra a buscar: ")

# noencontro=True
# # for i in palabras:
# #     if palabra_buscar == i:
# #         print(f"Encontre la palabra {palabra_buscar}, en la posición : {palabras.index(i)}")
#     #noencontrio=False

# i=0
# while i<len(palabras):
#         if palabra_buscar==palabras[i]:
#                 print(f"Encontre la palabra {palabra_buscar}, en la posición: {i}")
#                 noencontro=False
#         i+=1

# if noencontro:

#         print(f"No se encontro la palabra dentro de la lista")

#Ejemplo 3 Crear una lista multilinea o multidimensional (matriz) para crear una agenda telefónica

# agenda=[
#    ["Carlos", 6188158665],
#    ["Fernando", 6189859560],
#    ["Matias", 6186109045],
#    ["Idaly", 6741115227],
# ]

# print(agenda)

# for i in agenda:
#     print(f"{agenda.index(i)+1}.-{i}")

#Ejemplo 4 Crear un programa que permita Gestionar (Administrar) peliculas, colocar un menu de opciones para agregar,
#remover, consultar, peliculas
#Notas
#1.- Utilizar funciones y mandar llamar desde otro archivo
#2.- Utilizar listas para almacenar los nombres de peliculas 

# consultarpeliculas()
# system.cl
# buscarpelicula()
# delete
# se ha eliminado correctamente
# matrices
# cambiar nombre
# listas
# cineplis clon
# sistema de gestion de peliculas
# agregar
# eliminar
# actualizar
# consultar
# buscar
# salir
# elige una opcion 
# metodo de actualizar
# mandar archivo e importamos funciones
# 
peliculas = []

def esperar_confirmacion():
    input("Presione Enter para continuar...")

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Salir")

def agregar_pelicula(nombre):
    peliculas.append(nombre)
    print(f'Película "{nombre}" agregada.')

def remover_pelicula(nombre):
    if nombre in peliculas:
        peliculas.remove(nombre)
        print(f'Película "{nombre}" removida.')
    else:
        print(f'La película "{nombre}" no se encuentra en la lista.')

def consultar_peliculas():
    if peliculas:
        print("Lista de películas:")
        for pelicula in peliculas:
            print(f'- {pelicula}')
    else:
        print("No hay películas en la lista.")