import random

def system_intelligence(actualSystemNumber, hintSystem, hintUser, minNum, maxNum):
    minNumber = minNum
    maxNumber = maxNum

    while hintUser == hintSystem:
        if hintSystem == 'Tip: Try a higher number!':
            minNumber = actualSystemNumber + 1
            break
        if hintSystem == 'Tip: Try a lower number!':
            maxNumber = actualSystemNumber - 1
            break

    resultNumber = random.randint(minNumber, maxNumber)

    return resultNumber
