def black_jack(mano_uno, mano_dos):
    """
    Esta función evalúa el puntaje de cada tupla representando las manos
    del jugador y la casa. Retorna un string con un mensaje que señala
    si ganó la casa o el jugador.
    """

    suma_uno = suma_mano(mano_uno)
    suma_dos = suma_mano(mano_dos)

    # Si el jugador tiene Black Jack o suma 21, no importa lo que tenga la
    # casa, el jugador gana.
    if suma_uno[0] == 21:
        return "El jugador gana"

    # Si el jugador tiene al menos un As y la suma sobrepasa 21, se resta
    # hasta tener 21 o menos.
    if suma_uno[0] > 21 and suma_uno[1] > 0:
        for i in range(suma_uno[1]):
            suma_uno[0] -= 10
            if suma_uno[0] <= 21:
                break

    # Lo mismo para la casa.
    if suma_dos[0] > 21 and suma_dos[1] > 0:
        for i in range(suma_dos[1]):
            suma_dos [0] -= 10
            if suma_dos[0] <= 21:
                break

    # NOTA: esto último podría haberse mejorado con una función extra que
    # hiciera los descuentos correspondientes, de ser necesario, para am-
    # bas manos.

    # En este punto de la función, la mano de la casa y del jugador tie-
    # nen el valor más bajo posible, contando los As como 1, si se sobre-
    # pasa 21. Por lo tanto, la comparación se vuelve mucho más sencilla.
    if suma_uno[0] <= 21 and suma_dos[0] <= 21:
        if suma_uno[0] == suma_dos[0]:
            return "El jugador gana"
        elif suma_uno[0] > suma_dos[0]:
            return "El jugador gana"
        else:
            return "La casa gana"

    if suma_uno[0] > 21 and suma_dos[0] <= 21:
        return "La casa gana"

    if suma_uno[0] <= 21 and suma_dos[0] > 21:
        return "El jugador gana"

    if suma_uno[0] > 21 and suma_dos[0] > 21:
        return "Ambos pierden"

def suma_mano(mano):
    """
    Esta función retorna una lista de dos elementos, donde el primer
    elemento corresponde a la suma total de la mano (contando los As
    como 11), y donde el segundo elemento tiene la cantidad total de
    As que tiene la mano, para así hacer la resta correspondiente en
    el caso que sea necesario.
    """
    suma = 0
    count_as = 0
    for carta in mano:
        if carta in {"J", "Q", "K"}:
            suma += 10
        elif carta == "A":
            suma += 11
            count_as += 1
        else:
            suma += int(carta) # Se fuerza el valor numérico a int.
    return [suma, count_as]
