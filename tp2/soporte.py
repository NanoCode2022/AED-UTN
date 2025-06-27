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
    if algoritmo == 2:
        if monto_nominal < 50000:
            comision = 0
        elif monto_nominal >= 50000 and monto_nominal < 80000:
            comision = (5 * monto_nominal) // 100
        elif monto_nominal >= 80000:
            comision = (7.8 * monto_nominal) // 100
    if algoritmo == 3:
        comision = 100
        if monto_nominal > 25000:
            comision += (6 * monto_nominal) // 100
    if algoritmo == 4:
        if monto_nominal <= 100000:
            comision = 500
        if monto_nominal > 100000:
            comision = 100
    if algoritmo == 5:
        if monto_nominal < 500000:
            comision = 0
        if monto_nominal >= 500000:
            comision += (7 * monto_nominal) // 100
        if comision > 50000:
            comision = 50000
    monto_base = monto_nominal - comision
    return monto_base


def calculo_monto_final(algoritmo,monto_base):
    algoritmo = int(algoritmo)
    impuesto = 0
    if algoritmo == 1:
        if monto_base <= 300000:
            impuesto = 0
        if monto_base > 300000:
            excedente = monto_base - 300000
            impuesto = (25 * excedente) // 100
    if algoritmo == 2:
        if monto_base < 50000:
            impuesto = 50
        if monto_base >= 50000:
            impuesto = 1000
    if algoritmo == 3:
        impuesto = (3 * monto_base) // 100
    if algoritmo == 4:
        impuesto = 0
    monto_final = monto_base - impuesto
    return monto_final