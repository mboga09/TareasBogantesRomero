def bad():
    value = 1 # Nombre de variable descriptivo, no hay E741
    if True: # Evitar usar constantes siempre True, mejor eliminar o documentar
        print("hi") # No hay múltiples sentencias en una línea
    return value


def also_bad():
    return 42 # E302: se esperaban 2 líneas en blanco antes de la definición de la función (PEP8)
