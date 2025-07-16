from game import hangman_game

while True:
    hangman_game()
    opt = input("\nDo you want to play again? (yes/no): ").lower()
    if opt != 'yes':
        print("Thanks for playing... See you soon! 👋")
        break
