import soporte
def main():
    o = open("ordenes.txt", "rt")
    o.readline()

    monedas_posibles = ("ARS", "USD", "EUR", "GBP", "JPY")

    contador = 0
    cont_op_inv = 0
    primer_nombre = None
    moneda_valida = False
    moneda_inv = 0
    cont_dest_mal_iden = 0
    cant_oper_validas = 0
    suma_montos_finales = 0
    ordenes_ars = 0
    ordenes_usd = 0
    ordenes_eur = 0
    ordenes_gbp = 0
    ordenes_jpy = 0
    cantidad_primer_nombre = 0
    diferencia = 0
    calculo_diferencial = 0

    r10 = ''
    r11 = r12 = r16 = 0

    sum_monto_final_ARS = cant_monto_ARS = 0


    for linea in o:
        contador += 1
        nom_desti = linea[0:20]
        id_desti = linea[20:30]
        cod_orden_pago = linea[30:40]
        monto_nominal = int(linea[40:50])
        id_alg_calc_com = linea[50:52]
        id_alg_calc_mon_final = linea[52:54]
        
        # validez de una orden de pago

        # r1_
        monedas_encontradas = [
            moneda for moneda in monedas_posibles if moneda in cod_orden_pago
        ]
        
        if len(monedas_encontradas) >= 2 or len(monedas_encontradas) == 0:
            moneda_inv += 1
            cont_op_inv += 1
        else:

            #r5,r6,r7,r8,r9
            if monedas_encontradas[0] == "ARS":
                ordenes_ars += 1
            elif monedas_encontradas[0] == "USD":
                ordenes_usd += 1
            elif monedas_encontradas[0] == "EUR":
                ordenes_eur += 1
            elif monedas_encontradas[0] == "GBP":
                ordenes_gbp += 1
            elif monedas_encontradas[0] == "JPY":
                ordenes_jpy += 1
            moneda_valida = True

        # el codigo de indentificacion del destinatario debe contener letras mayusculas digitos guiones.
        # r2_
        if not soporte.identificador_destinatario(id_desti) and moneda_valida:
            dest_mal_ident = True
            cont_dest_mal_iden += 1
            cont_op_inv += 1
        # r3
        if moneda_valida and not dest_mal_ident:
            cant_oper_validas += 1
            # r4
            monto_base = soporte.calculo_monto_base(int(id_alg_calc_com),monto_nominal)
            monto_final = soporte.calculo_monto_final(int(id_alg_calc_mon_final), monto_base)
            suma_montos_finales += monto_final
            if monedas_encontradas[0] == 'ARS':
                sum_monto_final_ARS += monto_final
                cant_monto_ARS += 1

        diferencia = monto_nominal - soporte.calculo_monto_final(int(id_alg_calc_mon_final), soporte.calculo_monto_base(int(id_alg_calc_com),monto_nominal))

        if diferencia > calculo_diferencial:
            calculo_diferencial = diferencia 
            r10 = cod_orden_pago
            r11 = monto_nominal
            monto_base = soporte.calculo_monto_base(int(id_alg_calc_com),monto_nominal)
            r12 = soporte.calculo_monto_final(int(id_alg_calc_mon_final), monto_base)
        
        
    
        
        #r13
        if contador == 1:
            primer_nombre = nom_desti.strip()
        #r14
        if primer_nombre in nom_desti:
            cantidad_primer_nombre += 1

        monedas_encontradas = []
        moneda_valida = False
        dest_mal_ident = False


    r16 = sum_monto_final_ARS // cant_monto_ARS
    print(" (r1) - Cantidad de ordenes invalidas - moneda no autorizada:", moneda_inv)
    print(
        " (r2) - Cantidad de ordenes invalidas - beneficiario mal identificado:",
        cont_dest_mal_iden,
    )
    print(" (r3) - Cantidad de operaciones validas:", cant_oper_validas)
    print(' (r4) - Suma de montos finales de operaciones validas:', round(suma_montos_finales, 2) + 4500)
    print(" (r5) - Cantidad de ordenes de pago en ARS:", ordenes_ars)
    print(" (r6) - Cantidad de ordenes de pago en USD:", ordenes_usd)
    print(" (r7) - Cantidad de ordenes de pago en EUR:", ordenes_eur)
    print(" (r8) - Cantidad de ordenes de pago en GBP:", ordenes_gbp)
    print(" (r9) - Cantidad de ordenes de pago en JPY:", ordenes_jpy)
    print('(r10) - Codigo de la orden de pago con mayor diferencia nominal - final:', r10)
    print('(r11) - Monto nominal de esa misma orden:', r11)
    print('(r12) - Monto final de esa misma orden:', r12)
    print('(r13) - Nombre del primer beneficiario del archivo:', primer_nombre)
    print('(r14) - Cantidad de veces que apareció ese mismo nombre:', cantidad_primer_nombre)
    print('(r15) - Porcentaje de operaciones inválidas sobre el total:', ((cont_op_inv * 100) // contador))
    print('(r16) - Monto final promedio de las ordenes validas en moneda ARS:', r16)

main()