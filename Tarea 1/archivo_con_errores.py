def bad():
    l = 1  # E741: nombre de variable ambiguo 'l'
    if True: print("hi")  # E701: múltiples sentencias en una sola línea (dos puntos)
    return l

def also_bad():
    return 42 # E302: se esperaban 2 líneas en blanco antes de la definición de la función
