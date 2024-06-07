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