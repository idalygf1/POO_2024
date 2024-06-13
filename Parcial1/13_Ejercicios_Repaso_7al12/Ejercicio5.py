# Crear una lista y un diccionario con el contenido de esta tabla: 

#   ACCION              TERROR        DEPORTES
#   MAXIMA VELOCIDAD    LA MONJA       ESPN
#   ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#   RAPIDO Y FURIOSO I  LA MALDICION   ACCION

contenido={
    "Acción":"MÁXIMA VELOCIDAD"" ARMA MORTAL 4"" RAPIDO Y FURIOSO I",
    "Terror":"LA MOJA "" ELCONJURO"" LA MALDICIÓN",
    "Deportes":"ESPN ""MAS DEPORTE "" ACCION",
}

print("Contenido de Diccionario: ")

print(contenido["Acción"])
("\n")
print(contenido["Terror"])
("\n")
print(contenido["Deportes"])


for i in contenido:
    print(f"\n{i} : {contenido[i]}")
