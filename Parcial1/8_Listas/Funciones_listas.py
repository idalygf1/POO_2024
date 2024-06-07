paises=["Mexico", "USA", "BRASIL","CHINA"]
numero=[100,80,3.1416,75]
varios=["UTD",True,100,0.100]

#Ordernar las listas
print(paises)
paises.sort()
print(paises)

print(numero)
numero.sort()
print(numero)

#Agregar elementos a la lista
print(numero)
numero.append(100)
print(numero)
numero.insert(len(numero),200)
print(numero)

#Remover elementos
print(numero)
numero.remove(100)
print(numero)
numero.pop(2)
print(numero)
