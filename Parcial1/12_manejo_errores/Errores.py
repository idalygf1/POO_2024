#Manejo de errores es la forma en la que tienen los lenguajes de programación para evitar
#que sucedan errores en tiempo de ejecución

#Ejemplo 1 Error cuando una variable no se genera 

# try:
#     nombre=input("Dame el nombre: ")

#     if len(nombre)>1:
#         nombre_usuario="El nombre es: "+nombre

#     print(nombre_usuario)
# except:
#     print("Es necesario introducir un nombre de usuario...")

#Ejemplo cuando se solicita un numero y se introduce una letra.

# try:
#     numero=int(input("Dame un numero: "))

#     if numero>="0":
#         print("Soy un numero entero positivo")
#     else:
#         print("Soy un número entero negativo")
    

# except:
#         print("No se puede convertir una carcter no numérico a número...")
# else:
#         print("Todo se ejecuto sin errores")

#Ejemplo 3 cuando se generan multples excepciones 

try:
    numero=int(input("Dame un número: "))

    print("El cuadrado es "+str(numero*numero))

except ValueError:
    print("Debes de introducir un número, no se puede convertir un caracter que no sea numérico")

except TypeError:
    print("No es posible convertir el número entero")
else:
    print("Finalizó correctamente")

finally:
    print("Listo se termino")

    #listo 