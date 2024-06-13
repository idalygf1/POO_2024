def solicitarNumero():
    global n1,n2
    n1=int(input("Número #1."))
    n2=int(input("Número #2"))

def calculadora(n1,n2,opcion):
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        return f"{n1}+{n2}={n1+n2}"
    
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        return f"{n1}-{n2}={n1-n2}"
    
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
        return f"{n1}*{n2}={n1*n2}"
    
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        return f"{n1}/{n2}={n1/n2}"
    
    else:
        opcion=False
        return "Gracias por utilizar el sistema ..."

def espereTecla():
    print("Oprima una tecla para continuar...")
    input()

