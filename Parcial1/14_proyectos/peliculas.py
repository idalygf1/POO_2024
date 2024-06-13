import os
from funciones_compartir import agregar_pelicula, eliminar_pelicula, actualizar_pelicula, consultar_peliculas, buscar_pelicula, vaciar_peliculas, mostrar_menu

peliculas = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre de la película: ")
        agregar_pelicula(peliculas, nombre)
    elif opcion == "2":
        nombre = input("Ingrese el nombre de la película a eliminar: ")
        eliminar_pelicula(peliculas, nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre de la película a actualizar: ")
        nuevo_nombre = input("Ingrese el nuevo nombre de la película: ")
        actualizar_pelicula(peliculas, nombre, nuevo_nombre)
    elif opcion == "4":
        consultar_peliculas(peliculas)
    elif opcion == "5":
        nombre = input("Ingrese el nombre de la película a buscar: ")
        buscar_pelicula(peliculas, nombre)
    elif opcion == "6":
        vaciar_peliculas(peliculas)
    elif opcion == "7":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, intente nuevamente.")