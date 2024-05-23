#Examen
pacientes=0
respuesta ="SI"

print("Desea capturar otro paciente?")
if respuesta == "SI": 
    while pacientes <=0:

   
        presion1=int(input("Ingrese la presion 1: "))
        presion2=int(input("Ingrese la presion 2: "))
        presion3=int(input("Ingrese la presion 3: "))

    medicion_final= presion1 + presion2 + presion3 / 3

if medicion_final <=120:
    print("Presenta una presión de {} normal".format(medicion_final))
else:
    print("Su presión es {} es anormal".format(medicion_final))

    if medicion_final <=80:
        print("Presenta una presión de {} normal".format(medicion_final))
    else:
        print("Su presión de {} es anormal".format(medicion_final))

print("El número de pacientes es de: {}".format(pacientes+1))



