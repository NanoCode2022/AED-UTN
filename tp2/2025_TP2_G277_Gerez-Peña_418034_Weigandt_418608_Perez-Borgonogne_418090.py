def identificador_destinatario(codigo):
    codigo = codigo.strip()
    tiene_dig_may_gui = True
    digitos_validos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-"
    contador = 0

    for c in codigo:
        if c in "_-":
            contador += 1 
        if c not in digitos_validos:
            tiene_dig_may_gui = False
    if len(codigo) == contador:
        tiene_dig_may_gui = False
    return tiene_dig_may_gui


def operaciones_validas(mon_inv, desti_mal_iden):
    if mon_inv < 2 and desti_mal_iden == False:
        return True
    else:
        return False


def calculo_monto_base(algoritmo,monto_nominal):
    comision = 0
    if algoritmo == 1:
        comision = (9 * monto_nominal) // 100
    elif algoritmo == 2:
        if monto_nominal < 50000:
            comision = 0
        elif monto_nominal >= 50000 and monto_nominal < 80000:
            comision = (5 * monto_nominal) // 100
        elif monto_nominal >= 80000:
            comision = (7.8 * monto_nominal) // 100
    elif algoritmo == 3:
        comision = 100
        if monto_nominal > 25000:
            comision += (6 * monto_nominal) // 100
    elif algoritmo == 4:
        if monto_nominal <= 100000:
            comision = 500
        if monto_nominal > 100000:
            comision = 1000
    elif algoritmo == 5:
        if monto_nominal < 500000:
            comision = 0
        if monto_nominal >= 500000:
            comision += (7 * monto_nominal) // 100
        if comision > 50000:
            comision = 50000
    elif algoritmo == 6 or algoritmo == 7 or algoritmo == 8:
        comision = 0
    monto_base = monto_nominal - comision
    return monto_base


def calculo_monto_final(algoritmo, monto_base, monto_nominal, moneda):
    algoritmo = int(algoritmo)
    impuesto = 0
    if algoritmo == 1:
        if monto_base <= 300000:
            impuesto = 0
        if monto_base > 300000:
            excedente = monto_base - 300000
            impuesto = (25 * excedente) // 100
    elif algoritmo == 2:
        if monto_base < 50000:
            impuesto = 50
        if monto_base >= 50000:
            impuesto = 100
    elif algoritmo == 3:
        impuesto = (3 * monto_base) // 100
    elif algoritmo == 4:
       impuesto = 0
    elif algoritmo == 5:
       if moneda == "USD" or moneda == "GBP":
           impuesto = 100
       else:
           if monto_nominal <= 20000 and monto_base <= 20000:
               impuesto = (1 * monto_base) // 100
           elif monto_base > 20000:
               impuesto = (2 * monto_base) // 100
    monto_final = monto_base - impuesto
    return monto_final

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
    dest_mal_ident = False
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

        # r2_
        if not identificador_destinatario(id_desti) and moneda_valida:
            dest_mal_ident = True
            cont_dest_mal_iden += 1
            cont_op_inv += 1
        # r3
        if moneda_valida and not dest_mal_ident:
            cant_oper_validas += 1
            # r4
            monto_base = calculo_monto_base(int(id_alg_calc_com),monto_nominal)
            monto_final = calculo_monto_final(int(id_alg_calc_mon_final), monto_base, monto_nominal, monedas_encontradas)
            suma_montos_finales += monto_final
            if monedas_encontradas[0] == 'ARS':
                sum_monto_final_ARS += monto_final
                cant_monto_ARS += 1

        diferencia = monto_nominal - calculo_monto_final(int(id_alg_calc_mon_final), calculo_monto_base(int(id_alg_calc_com),monto_nominal),monto_nominal, monedas_encontradas)

        if diferencia > calculo_diferencial:
            calculo_diferencial = diferencia 
            r10 = cod_orden_pago
            r11 = monto_nominal
            monto_base = calculo_monto_base(int(id_alg_calc_com),monto_nominal)
            r12 = calculo_monto_final(int(id_alg_calc_mon_final), monto_base, monto_nominal, monedas_encontradas)
        
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
    print(' (r4) - Suma de montos finales de operaciones validas:', round(suma_montos_finales, 2))
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


if __name__ == "__main__":
    main()