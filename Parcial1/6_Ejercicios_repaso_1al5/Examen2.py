#Examen 2.
basico= 0.987
Intermedido=1.203
IVA= .16
impuesto= 12.56

kWh=float(input("Ingrese la cantidad de kWh"))

if kWh <=150:
    tarifa= kWh - 150 
    tarifa2= tarifa * basico
    tarifa3= tarifa + 150
    tarifa4 = tarifa * Intermedido


iva = tarifa4 * IVA 
Total_pagar = iva + impuesto


print("Su total a pagar de recibo de luz es: {}".format(Total_pagar))