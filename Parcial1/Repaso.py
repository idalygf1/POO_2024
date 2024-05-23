#Pide al usuario que ingrese 5 números y ordénalos de menor a mayor 

numeros = [int(input("Ingresa el número {}: ".format(i+1))) for i in range(1,6)]

numeros.sort() #.sort sirve para ordenar 

print("Los números ordenados de menor a mayor son:", numeros)

