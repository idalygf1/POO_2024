paises=["Mexico", "USA", "BRASIL","CHINA"]
numero=[100,80,3.1416,75]
varios=["UTD",True,100,0.100]

#Ordernar las listas
print(paises)
paises.sort()#ordenar
print(paises)

print(numero)
numero.sort()
print(numero)

#Agregar elementos a la lista.
print(numero)
numero.append(100)#agregar
print(numero)
numero.insert(len(numero),200)
print(numero)

#Remover elementos
print(numero)
numero.remove(100)#remover
print(numero)
numero.pop(2)#lo recorre
print(numero)

#Dar la vuelta a los elementos de una lista 
print(varios)
varios.reverse()
print(varios)

#Buscar un valor dentro de una lista
encontro="BRASIL" in paises
print(encontro)

#Vaciar una lista 
print(paises)
paises.clear()
print(paises)

#Unir o concatenar listas
print(varios)
varios.extend(numero)
print(varios)