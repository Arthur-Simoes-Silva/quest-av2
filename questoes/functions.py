def carga_horaria (hrs):
    if hrs >= 40:
        print("Carga completa")
    else:
        print("Carga incompleta")


def depositar(qtd, sld):
    if qtd <= 0:
        raise ValueError

    sld += qtd
    return sld

def sacar (vlr,sld):
    if vlr <= 0:
        raise ValueError

    sld -= vlr
    return sld


