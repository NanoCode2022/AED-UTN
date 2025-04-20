# ingreso de datos
destinatario = input("ingrese nombre y apellido del destinatario: ")
tipo_moneda = ("ARS", "USD", "EUR", "GBP", "JPY")
moneda_pagar = input("ingrese la moneda a pagar (ARS, USD, EUR, GBP, JPY): ")
monto_nominal = float(input("ingrese el monto a enviar: "))

# validacion de la moneda
if tipo_moneda[0] in moneda_pagar:
    monto_base = round((95 * monto_nominal) / 100, 2)

elif tipo_moneda[1] in moneda_pagar:
    monto_base = round((93 * monto_nominal) / 100, 2)

elif tipo_moneda[2] in moneda_pagar:
    monto_base = round((93 * monto_nominal) / 100, 2)

elif tipo_moneda[3] in moneda_pagar:
    monto_base = round((91 * monto_nominal) / 100, 2)

elif tipo_moneda[4] in moneda_pagar:
    monto_base = round((91 * monto_nominal) / 100, 2)

else:
    moneda_pagar = "Moneda no autorizada"
    monto_base = 0

if monto_base > 500000:
    monto_final = round(monto_base * 79 / 100, 2)
else:
    monto_final = monto_base

# muestra de datos
print("Beneficiario:", destinatario)
print("Moneda:", moneda_pagar)
print("Monto base (descontadas las comisiones):", monto_base)
print("Monto final (descontados los impuestos):", monto_final)
