#Crear un programa que permita calcular e imprimir el precio a pagar por un articulo.
#En el precio a pagar se incluye el IVA. El programa debera de funcionar n veces como el usuario desee 

IVA=0.16

precio=input("Ingrese el precio a pagar: ")
precio_neto=(precio * IVA)

precio_pagar=precio + precio_neto

print=("El precio a pagar es de: ")