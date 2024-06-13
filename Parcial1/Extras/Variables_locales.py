#Ejercicio1.
def calcular_area_perimetro(base,altura):

    area=0
    perimetro=0

    area= base * altura
    perimetro= base*2 + altura*2

    print(f"Un rectangulo con base {base} y altura {altura}, tiene un area de: {area} y su perimetro es de: {perimetro}")

base=int(input("Ingrese la base del rectangulo: "))
altura=int(input("Ingrese la altura del rectangulo: "))

calcular_area_perimetro(base,altura)