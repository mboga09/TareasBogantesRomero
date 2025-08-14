import re


def count_char(cadena, caracter):
    # -100: cadena no es string
    if not isinstance(cadena, str):
        return -100, None

    # -200: cadena contiene algo fuera de [A-Za-z0-9]
    if not re.fullmatch(r"[A-Za-z0-9]+", cadena):
        return -200, None

    # -300: caracter no es string de longitud 1 alfanumérico
    if not isinstance(caracter, str) or len(caracter) != 1:
        return -300, None
    if not re.fullmatch(r"[A-Za-z0-9]", caracter):
        return -300, None

    # Éxito (0): contar ocurrencias (sensible a mayúsculas/minúsculas)
    cantidad = cadena.count(caracter)
    return 0, cantidad


def multiplo_2(base, multiplo):
    # -400: parámetros no son enteros (o base/multiplo < 0)
    if not isinstance(base, int) or not isinstance(multiplo, int):
        return -400, None
    if base < 0 or multiplo < 0:
        return -400, None

    # -500: multiplo no está en [1, 2, 4, 8, 16]
    if multiplo not in [1, 2, 4, 8, 16]:
        return -500, None

    # Éxito (0): multiplicar por potencias de 2 usando desplazamientos de bits
    shifts = {1: 0, 2: 1, 4: 2, 8: 3, 16: 4}
    resultado = base << shifts[multiplo]
    return 0, resultado
