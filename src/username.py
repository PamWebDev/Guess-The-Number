"""Obteniendo el nombre de la usuaria"""

def user_name(username):
    """Verificar que el username sea válido:"""

    while not username.isalpha():
        print("\nPlease enter a valid name (letters only)")
        username = input("\nBefore we begin, what's your name?\n--> ")

    print(f"\nHi {username}! Now, please enter a number between 1 and 100 to start:\n")
    return username
