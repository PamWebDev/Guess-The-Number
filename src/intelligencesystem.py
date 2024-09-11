import random

def system_intelligence(numberSystem, hint):
    # deberia leer la pista ingresada
    if hint == 'Tip: Try a higher number!':
        lowSystemNumber = random.randint(numberSystem, 5)
        return lowSystemNumber

    if hint == 'Tip: Try a lower number!':
        highSystemNumber = random.randint(1, numberSystem)
        return highSystemNumber
