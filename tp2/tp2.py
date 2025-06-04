import soporte

o = open("ordenes.txt", "rt")

monedas_posibles = ("ARS", "USD", "EUR", "GBP", "JYP")

moneda_inv = 0
destinatario_mal_ident = 0
orden_incorrecta = 0
cant_oper_validas = 0


for linea in o:
    linea = o.readline()
    print(linea)

    nom_desti = linea[0:20]
    id_desti = linea[20:30]
    cod_orden_pago = linea[30:40]
    monto_nominal = linea[40:50]
    id_alg_calc_com = linea[50:52]
    id_alg_calc_mon_final = linea[52:54]

    # validez de una orden de pago

    # r1_

    monedas_encontradas = [
        moneda for moneda in monedas_posibles if moneda in cod_orden_pago
    ]

    if len(monedas_encontradas) >= 2:
        moneda_inv += 1

    # el codigo de indentificacion del destinatario debe contener letras mayusculas digitos guiones.
    # r2_
    if not soporte.identificador_destinatario(id_desti):
        destinatario_mal_ident += 1
        dest_mal_ident = True
    else:
        dest_mal_ident = False

    # r3
    if soporte.operaciones_validas(moneda_inv, dest_mal_ident):
        cant_oper_validas += 1
    # r4

print(" (r1) - Cantidad de ordenes invalidas - moneda no autorizada:", moneda_inv)
print(
    " (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:",
    destinatario_mal_ident,
)
print(" (r3) - Cantidad de operaciones validas:", cant_oper_validas)
