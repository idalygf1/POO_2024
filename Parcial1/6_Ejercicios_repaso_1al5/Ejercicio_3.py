# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

tabla=int(input("Ingresa un numero para calcular su tabla de multiplicar: "))

for contador in range(0,60):
    



    i=0
    multi=0
while i<=60:
    multi=i*i
    print(f"{i} ^ {i} = {multi}")
    