#Ejemplo 1
# def suma(n1,n2):
#     return n1+n2
# print (suma(4,2))

suma=lambda n1,n2: n1+n2
print(suma(4,3))

#Ejemplo 2
elevar=lambda num:num*num
print(elevar(4))

# Ejemplo 3
# def mensaje():
#     nombre = input("Ingrese su numbre ")
#     return f"Hola, {nombre}! Eres increible"
# print(mensaje())


mensaje=lambda: f"Hola, {input("Ingresa tu nombre")}! Eres increible"
print (mensaje())