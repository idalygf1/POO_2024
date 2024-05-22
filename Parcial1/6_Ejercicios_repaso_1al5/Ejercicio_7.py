#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

N1=min(num1,num2)
N2=max(num1,num2)

num=1

for num in range(N1 + 1 if N2 % 2 == 0 else N1, N2, 2):
    print(num)