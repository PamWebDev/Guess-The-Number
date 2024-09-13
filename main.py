""" importando módulo random para tener acceso a la función radint """
import random
from src.username import user_name
from src.usernumber import user_number
from src.systemnumber import system_number
from src.playagain import play_again
from src.intelligencesystem import system_intelligence

#? JUEGO:
def game():
    """ Reproduciendo juego """
    #? OBTENIENDO NÚMERO GANADOR:
    winningNumber = random.randint(1, 10)
    # print(winningNumber)

    #? DESCRIPCIÓN DE BIENVENIDA:
    print("\nWelcome to 'Guess The Number'\nIn this game you will take turns with the system to guess a random number between 1 and 100.")

    #? INGRESANDO NOMBRE DE USUARIA (y dandole primera indicación):
    userName = input("\nBefore we begin, what's your name?\n--> ")
    validUserName = user_name(userName)
    #? ALMACENANDO INTENTOS DE USUARIA:
    userNumberList = []
    #? ALMACENANDO INTENTOS DE COMPUTADORA:
    systemNumberList = []
    #? ALMACENANDO PISTAS
    # Almacenando número de computadora
    systemNumber = system_number()
    hintUser = ''
    hintSystem = ''

    while winningNumber:
        #? ESTRUCTURA DE USUARIA:
        print(f"\n<--- {validUserName}'s turn --->")
        # Pidiendole a la usuaria que ingrese un número:
        userNumber = input("Enter your guess: ")
        # Validando el número ingresado por la usuaria:
        validUserNumber = user_number(userNumber)
        # Almacenando los intentos de la usuaria:
        userNumberList.append(validUserNumber)
        # Brindando pistas a la usuaria:
        if validUserNumber < winningNumber:
            hintUser = "Tip: Try a higher number!"
            print(hintUser)
        elif validUserNumber > winningNumber:
            hintUser = "Tip: Try a lower number!"
            print(hintUser)
        # Verificando si la usuaria es la ganadora
        if validUserNumber == winningNumber:
            print(f"\nCongratulations {validUserName}! You guessed the number")
            print(f"\nThese were your attempts: {userNumberList}")
            break

        #? ESTRUCTURA DE COMPUTADORA:
        print("\n<--- Computer turn --->")
        # Pidiendole a la computadora que ingrese un número:
        print(f"Enter your guess: {systemNumber}")
        # Almacenando los intentos del ordenador:
        systemNumberList.append(systemNumber)
        # Verificando si el ordenador es el ganador:
        if systemNumber == winningNumber:
            print("\nCongratulations Computer! You guessed the number")
            print(f"These were your attempts: {systemNumberList}")
            break
        # Brindando pistas a la computadora:
        if systemNumber < winningNumber:
            hintSystem = "Tip: Try a higher number!"
            print(hintSystem)
            systemNumber = system_intelligence(systemNumber, hintSystem, hintUser, 1, 10)
        elif systemNumber > winningNumber:
            hintSystem = "Tip: Try a lower number!"
            print(hintSystem)
            systemNumber = system_intelligence(systemNumber, hintSystem, hintUser, 1, 10)

    play_again(game)

game()
