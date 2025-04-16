# ingreso de datos
destinatario = input("ingrese nombre y apellido del destinatario: ")
tipo_moneda = ('ARS', 'USD', 'EUR', 'GBP', 'JPY')
moneda_pagar = input("ingrese la moneda a pagar (ARS, USD, EUR, GBP, JPY): ")
monto = float(input("ingrese el monto a enviar: "))
monto_base = 0
# validacion de la moneda
if tipo_moneda[0] in moneda_pagar:
    comision = monto * 0.05
    monto_base = monto + comision
else:
    if tipo_moneda[1] in moneda_pagar:
        comision = monto * 0.07
        monto_base = monto - comision
    else:
        if tipo_moneda[2] in moneda_pagar:
            comision = monto * 0.07
            monto_base = monto - comision
        else:
            if tipo_moneda[3] in moneda_pagar:
                comision = monto * 0.09
                monto_base = monto - comision
            else:
                if tipo_moneda[4] in moneda_pagar:
                    comision = monto * 0.09
                    monto_base = monto - comision
                else:
                    print("moneda no autorizada")
                    exit()

if monto_base > 500000:
    impuesto = monto_base * 0.21
    monto_final = monto_base - impuesto
else:
    monto_final = monto_base

# muestra de datos
print("Beneficiario: ", destinatario)
print("Moneda: ", moneda_pagar)
print("Monto base: ", monto_base)
print("Monto final: ", monto_final)
