#Ciclo wuile es Estructura iterativa que se ejecuta x veces, siempre y cuando la condición se cumpla y se seguirá ejecutando tantas veces
#como sea True la condición 

#Sintaxis
#while condición:
#   bloque de instrucciones 

#Ejemplo 1 Crear un programa que imprima en pantalla 5 veces el @.
"""

contador=10
while contador<=5:
    print("@")
    contador+=1


#Ejemplo 2 Crear un programa que imprima los numeros del 1 al 5 y los sume y al final imprima la suma 

contador=1
suma=0

while contador<=5:
    print(contador)
    suma+=contador
    contador+=1

print(f"La suma es: {suma}")
"""

#Ejemplo 3 Crear un programa que imprima la tabla de multiplicar que el usuario desee

tabla=int(input("Ingresa un numero para calcular su tabla de multiplicar: "))

i=1
multi=0

while i<=10:
    multi=i*tabla
    print(f"{tabla} X {i} = {multi}")
    i+=1