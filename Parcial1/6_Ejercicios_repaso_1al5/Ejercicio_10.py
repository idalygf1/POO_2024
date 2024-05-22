#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron



aprobados=1
reprobados=1

cal=str(input("Ingrese la calificación de los 15 alumnos: "))
for i in range(1,16):

    cal=float(input("Ingrese la calificación del alumno".format(i)))

    if cal <= 80:
        aprobados +=1

    else:
        reprobados +=1

print("Alumnos aprobados: {}".format(aprobados))

print("Reprobados: {}".format(reprobados))


