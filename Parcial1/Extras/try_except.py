    #Try | Except | Finally 

#Programa para operaciones basicas 
n1 = int(input("Ingresa un numero: "))
n2 = int(input("Ingresa un numero: "))
res = n1 + n2
print(res)

#Try | Except
try: #Intenta ejecutar un bloque de codigo
    n1 = int(input("Ingresa un numero: "))
    n2 = int(input("Ingresa un numero: "))
    res = n1 + n2 
    print(res)
except: #Si da algun error al ejecutar el bloque de codigo imprime la siguiente linea
    print("Error: Ingresa valores validos")


#try | Except
try: 
    n1 = int(input("ingresa un numero: "))
    n2 = int(input("Ingresa un numero: "))
    res = n1 + n2
    print(res)
except: 
    print("Error: Ingresa valores validos")
finally: #Siempre se ejecuta
    print("SIEMPRE SE EJECUTA")

#While con try-except
while(True):
    try: 
        n1 = int(input("Ingresa un numero: "))
        n2 = int(input("Ingresa un numero: "))
        res = n1 + n2
        print(res)
        opcion = input("Desea capturar otra operacion (si/no)").lower()
        if opcion == "no":
            break
    except Exception as e:
        print(f" Ha ocurrido un error: {e}")