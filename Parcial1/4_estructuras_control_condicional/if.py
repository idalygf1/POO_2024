"""

Existe una estructura de condición llamada "if"
la cual evalua una condición para encontrar el valor "True" y si se cumple 
la condición se ejecuta la linea o lineas código

Tienes 4 variantes del if 

1.- if simple 
2.- if compuesto 
3.- if anidado 
4.- if y elif 
"""

#ejemplo 1 if siemple 
color =input("Ingresa un color: ")

if color=="rojo":
    print("Soy el color rojo")

#ejemplo 2 if compuesto

color =input("Ingresa un color: ")

if color=="rojo":
    print("Soy el color rojo")
else:
    print("No soy el color rojo soy otra cosa")

#ejemplo 3 if anidado

color =input("Ingresa un color: ")

if color=="rojo":
    print("Soy el color rojo")
    if color!="rojo":
        print("No soy el color rojo")
else:
    print("No soy el color rojo soy otra cosa")
    

    #ejemplo 4 if y elif opciones, else=de otro modo

color =input("Ingresa un color: ")

if color=="rojo":
    print("Soy el color rojo")
elif color=="amarillo":
    print("Soy el color amarillo")
elif color=="azul":
    print("Soy el color azul")
elif color=="morado":
    print("Soy el color morado")
else: 
    print("No soy ningun de los anteriores")


#Elemplo 4 Crear un programa que solicite el numero de la semana 
# e imprima en pantalla el dia que le corresponda 

dia=input("Ingresa el Dia: ")

if dia=="1":
    print("Su dia seleccionado es Lunes")
elif dia=="2":
    print("Su dia seleccionado es Martes")
elif dia=="3":
    print("Su dia seleccionado es Miércoles")
elif dia=="4":
    print("Su dia seleccionado es Jueves")
elif dia=="5":
    print("Su dia seleccionado es Viernes")
elif dia=="6":
    print("Su dia seleccionado es Sábado")
elif dia=="7":
    print("Su dia seleccionado es Domingo")
else:
    print("No soy ningun dia de la semana")