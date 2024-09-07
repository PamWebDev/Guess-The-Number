""" Opción para volver a jugar """
def play_again(gameFunction):
    """ Preguntando si quiere volver a jugar """
    answerPlayAgain = input("\n☆ Do you want play again? (Yes/No): ")

    while answerPlayAgain != "Yes" and answerPlayAgain != "No":
        print("\nPlease enter a valid answer (Yes/No)")
        answerPlayAgain = input("\n☆ Do you want play again? (Yes/No): ")

    if answerPlayAgain == "Yes":
        gameFunction()
    else:
        print("Thanks for playing!")
