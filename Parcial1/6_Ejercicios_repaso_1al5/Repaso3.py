#Escribir un programa que tome una cadena de texto como entrada y cuente el número de vocales (a, e, i, o, u) 
#que contiene, tanto en mayúsculas como en minúsculas..

def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

texto = input("Ingrese una cadena de texto: ")
total_vocales = contar_vocales(texto)
print(f"El número total de vocales es: {total_vocales}")