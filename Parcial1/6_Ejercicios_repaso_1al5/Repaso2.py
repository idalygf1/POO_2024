"""
Solicitar al usuario que ingrese el total de la cuenta.
Solicitar al usuario que ingrese el porcentaje de propina deseado.
Calcular el monto de la propina multiplicando el total de la cuenta por el porcentaje de propina.
Calcular el total a pagar sumando el total de la cuenta y la propina..
Mostrar el total de la cuenta, el monto de la propina y el total a pagar.
"""

total_cuenta=float(input("Ingreese el total de la cuenta: "))

porcentaje=float(input("Ingrese el porcentaje de propina deseado (sin %): "))

propina_total= total_cuenta * porcentaje / 100

total_pagar= total_cuenta + propina_total

print("EL TOTAL A PAGAR ES DE: {} EL PORCENTAJE DE LA PROPINA ES DE: {} LA PROPINA ES DE: {} Y EL TOTAL A PAGAR ES DE: {}"
      .format(total_cuenta,porcentaje,propina_total,total_pagar))
