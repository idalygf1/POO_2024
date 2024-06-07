import os
from funciones_cinepolis import agregar_pelicula, remover_pelicula, consultar_peliculas, esperar_confirmacion, mostrar_menu




while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar pantalla
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Ingrese el nombre de la película: ")
            agregar_pelicula(nombre)
            esperar_confirmacion()
        elif opcion == "2":
            nombre = input("Ingrese el nombre de la película a remover: ")
            remover_pelicula(nombre)
            esperar_confirmacion()
        elif opcion == "3":
            consultar_peliculas()
            esperar_confirmacion()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")
            esperar_confirmacion()