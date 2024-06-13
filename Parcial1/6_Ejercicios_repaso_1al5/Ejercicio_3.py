# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for.
"""

for numero in range(1, 61):

    cuadrado = numero ** 2
    

    print("{} cuadrado -> {}".format(numero,cuadrado))

"""

contador = 1


while contador <= 60:
    cuadrado = contador ** 2
    
    print("{} cuadrado -> {}".format(contador,cuadrado))
    
    contador += 1