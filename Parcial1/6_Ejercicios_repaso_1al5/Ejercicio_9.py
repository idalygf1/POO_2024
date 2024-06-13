#Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa.

numero = None

while numero != 111:
    numero = int(input("Ingresa un número del 1 al 200 "))

    if numero != 111:
        print(f"El número ingresado es: {numero}")

print("El programa se cerrará")