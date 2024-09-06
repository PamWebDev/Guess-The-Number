"""Obteniendo el número por parte de la usuaria"""

def user_number(userNumber):

    """Verificar que el numero sea válido:"""
    def number_is_number(validNumber):
        while not validNumber.isdigit():
            print("\nPlease, enter a number")
            validNumber = input("\nEnter your guess: ")

        return int(validNumber)

    userNumber = number_is_number(userNumber)

    while int(userNumber) <= 0 or int(userNumber) > 100:
        print("\nPlease, enter a number between 1 and 100")
        userNumber = input("\nEnter your guess: ")
        userNumber = number_is_number(userNumber)


    return int(userNumber)
