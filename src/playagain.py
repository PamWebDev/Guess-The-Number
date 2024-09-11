""" Opción para volver a jugar """
def play_again(gameFunction):
    """ Preguntando si quiere volver a jugar """
    answerPlayAgain = input("\n☆ Do you want play again? (Yes/No): ")

    while answerPlayAgain not in ('Yes', 'No', 'yes', 'no'):
        print("\nPlease enter a valid answer (Yes/No)")
        answerPlayAgain = input("\n☆ Do you want play again? (Yes/No): ")

    if answerPlayAgain in ('Yes', 'yes'):
        gameFunction()
    else:
        print("Thanks for playing!")
