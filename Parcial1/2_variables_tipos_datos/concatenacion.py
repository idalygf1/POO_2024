#concatenar cadenas de caracteres con contenido de variables 

nombre="Idaly Guadalupe Garcia Flores "
especialidad="Area de Desarrollo de SW Multiplataforma"
carrera="Ingeniero en Gestion y Desarrollo de SW"

#1er forma de concatenación
print("Mi nombre es: "+nombre+ "estoy en la especialidad de: " +especialidad+ "en la carrera de: "+carrera)

print("\n")


#2da forma de concatenar
print("Mi nombre es: ",nombre, "estoy en la especialidad de: " ,especialidad, ",en la carrera de: ",carrera)

print("\n")
#3er forma de concatenar MAS COMÚN
print(f"Mi nombre es:{nombre} estoy en la especialidad de: {especialidad}, en la carrera de: {carrera}")

      
print("\n")

#4ta forma de concatenar 
print("Mi nombre es:{} estoy en la especialidad de:{} ,en la carrera de: {}".format(nombre,especialidad,carrera))
print("\n")

#5ta forma de concatenar 
print('Mi nombre es: '+nombre+' estoy en la especialidad de: ' +especialidad+ 'en la carrera de: '+carrera)