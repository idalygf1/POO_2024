#Examen.

presion1=int(input("Ingrese la presion 1: "))
presion2=int(input("Ingrese la presion 2: "))
presion3=int(input("Ingrese la presion 3: "))



Diastolica= presion1 + presion2 + presion3 / 3

sistolica= presion1 + presion2 + presion3 / 3

presion_final= presion1 + presion2 + presion3 / 3

if Diastolica <=120:
    print("Presenta una presión Diastolica {} es normal".format(Diastolica))
else:
    print("Su presión Diastólica es anormal")

    if sistolica <=80:
        print("Presenta una presión Sistolica {} es normal".format(sistolica))
    else:
        print("Su presión de Sistolica es anormal".format(sistolica))

pacientes=0
respuesta ="SI"

print("Desea capturar otro paciente?")
if respuesta == "SI": 
    
    pacientes=+1
else:
    print("El número de pacientes es de: {}".format(pacientes+1))



