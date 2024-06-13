# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for

lista = []


print("Ingrese valores para añadir a la lista: ")
while len(lista) < 120:
    valor = input("Valor: ")
    lista.append(valor)#función agregar valores a la lista

print("La lista final es:")
for elemento in lista:
    print(elemento)