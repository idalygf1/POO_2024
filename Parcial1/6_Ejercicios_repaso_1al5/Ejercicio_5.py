#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))


menor = min(num1, num2)
mayor = max(num1, num2)


print(f"Los números entre {menor} y {mayor} son:")
for numero in range(menor, mayor+1):
    print(numero)