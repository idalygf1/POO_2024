import os

def solicitarNumeros():
    n1 = int(input("Numero # 1: "))
    n2 = int(input("Numero # 2: "))
    return n1, n2

def calculadora(n1, n2, opcion):
    if opcion == "1" or opcion == "+" or opcion == "SUMA":
        return f"{n1} + {n2} = {n1 + n2}"
    elif opcion == "2" or opcion == "-" or opcion == "RESTA":
        return f"{n1} - {n2} = {n1 - n2}"
    elif opcion == "3" or opcion == "*" or opcion == "MULTIPLICACION":
        return f"{n1} * {n2} = {n1 * n2}"
    elif opcion == "4" or opcion == "/" or opcion == "DIVISION":
        if n2 != 0:
            return f"{n1} / {n2} = {n1 / n2}"
        else:
            return "Error: División por cero no permitida"
    elif opcion == "5" or opcion == "^" or opcion == "POTENCIA":
        return f"{n1} ^ 2  = {n1 ** n1}"
    elif opcion == "6" or opcion == "RAIZ":
        if n2 > 0:
            return f"Raíz {n1} de {n2} = {n2 ** (1 / n1)}"
        else:
            return "Error: No se pueden calcular raíces de números negativos"

def esperaTecla():
    input("Oprima cualquier tecla para continuar...")

def menu():
    os.system("clear")
    print("\n\t..::: CALCULADORA BÁSICA :::...")
    print(" 1.- Suma")
    print(" 2.- Resta")
    print(" 3.- Multiplicación")
    print(" 4.- División")
    print(" 5.- Potencia")
    print(" 6.- Raíz")
    print(" 7.- SALIR")

opcion = True
while opcion:
    menu()
    opcion = input("\t Elige una opción: ").upper()

    if opcion in ["1", "+", "SUMA", "2", "-", "RESTA", "3", "*", "MULTIPLICACION", "4", "/", "DIVISION", "5", "^", "POTENCIA", "6", "RAIZ" ,"67", "SALIR"]:
        n1, n2 = solicitarNumeros()
        resultado = calculadora(n1, n2, opcion)
        print(resultado)
        esperaTecla()
    elif opcion == "7" or opcion == "SALIR":
        print("Gracias por utilizar el sistema...")
        opcion = False
    else:
        print("Opción inválida. Intente nuevamente.")
        esperaTecla()