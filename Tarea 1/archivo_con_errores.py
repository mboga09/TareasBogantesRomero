def bad():
    l = 1  # E741: ambiguous variable name 'l'
    if True: print("hi")  # E701: multiple statements on one line (colon)
    return l

def also_bad():
    return 42
