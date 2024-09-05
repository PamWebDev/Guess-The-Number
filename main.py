""" importando módulo random para tener acceso a la función radint """
import random

#? PSEUDOCÓDIGO BASE:
#* 1. Generar número random (respuesta ganadora) ✅
winningNumber = random.randint(1,5)
print(winningNumber)

#* 2. Usuaria ingrese un número (número de usuaria) ✅
#* 3. Computadora generé un número random (número de sistema) ✅
#* 3. Evaluar ambas respuestas (n. sistema y n. usuaria) ✅
#* 4. Verificiar cual de las dos coincide con la respuesta ganadora ✅

#? OPCIÓN 1 (USANDO WHILE):
print("Welcome to 'Guess The Number'\nIn this game you will take turns with the system to guess a random number between 1 and 100.")
userName = input("\nBefore we begin, what's your name?\n--> ")
print(f"\nHi {userName}! Now, please enter a number between 1 and 100 to start:\n")

while winningNumber:
    print(f"<--- {userName}'s turn --->")
    userNumber = int(input("Enter your guess: "))
    if userNumber < winningNumber:
        print("Tip: Try a higher number!")
    else:
        if userNumber > winningNumber:
            print("Tip: Try a lower number!")

    print("\n<--- Computer turn --->")
    systemNumber = random.randint(1,5)
    print(f"Enter your guess: {systemNumber}")

    if userNumber == winningNumber:
        print(f"Enter your guess: {userNumber}")
        print(f"\nCongratulations {userName}! You guessed the number")
        break
    if systemNumber == winningNumber:
        print("\nCongratulations Computer! You guessed the number")
        break

#* 5. Si el número de la usuaria coincide con la respuesta ganadora, terminar la partida ✅
#* 6. Si el número del sistema coincide con la respuesta ganadora, terminar la partida ✅

#? ERRORES IDENTIFICADOS:
#* El juego termina cuando el sistema arroja un último número, pero no cuando la usuaria lo adivina ✅
