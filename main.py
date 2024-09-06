""" importando módulo random para tener acceso a la función radint """
import random
from src.username import user_name
from src.usernumber import user_number
from src.systemnumber import system_number

#? OBTENIENDO NÚMERO GANADOR:
winningNumber = random.randint(1,5)
print(winningNumber)

#? DESCRIPCIÓN DE BIENVENIDA:
print("Welcome to 'Guess The Number'\nIn this game you will take turns with the system to guess a random number between 1 and 100.")

#? INGRESANDO NOMBRE DE USUARIA (y dandole primera indicación):
userName = input("\nBefore we begin, what's your name?\n--> ")
validUserName = user_name(userName)
#? ALMACENANDO INTENTOS DE USUARIA:
userNumberList = []
#? ALMACENANDO INTENTOS DE COMPUTADORA:
systemNumberList = []
#? JUEGO:
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
        print("Tip: Try a higher number!")
    else:
        if validUserNumber > winningNumber:
            print("Tip: Try a lower number!")
    # Verificando si la usuaria es la ganadora
    if validUserNumber == winningNumber:
        print(f"\nCongratulations {validUserName}! You guessed the number")
        print(f"\nThese were your attempts: {userNumberList}")
        break

    #? ESTRUCTURA DE COMPUTADORA:
    print("\n<--- Computer turn --->")
    # Pidiendole a la computadora que ingrese un número:
    print(f"Enter your guess: {system_number()}")
    # Almacenando los intentos del ordenador:
    systemNumberList.append(system_number())
    # Brindando pistas a la computadora:
    if system_number() < winningNumber:
        print("Tip: Try a higher number!")
    else:
        if system_number() > winningNumber:
            print("Tip: Try a lower number!")
    # Verificando si el ordenador es el ganador:
    if system_number() == winningNumber:
        print("\nCongratulations Computer! You guessed the number")
        print(f"\nThese were your attempts: {systemNumberList}")
        break
