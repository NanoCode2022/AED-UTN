def identificador_destinatario(codigo):
    codigo = codigo.strip()
    tiene_dig_may_gui = True
    digitos_validos = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_"
    for c in codigo:
        if c not in digitos_validos:
            tiene_dig_may_gui = False

    return tiene_dig_may_gui


def operaciones_validas(mon_inv, desti_mal_iden):
    if mon_inv < 2 and desti_mal_iden == False:
        return True
    else:
        return False
