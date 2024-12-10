import random

def hangman_game():
    chances=5
    words = ["adventure", "mysterious", "universe", "journey", "chocolate", 
    "paradise", "horizon", "quarantine", "puzzle", "spectrum",
    "harmony", "whisper", "ocean", "guitar", "pyramid",
    "wilderness", "labyrinth", "starlight", "treasure", "reflection" ] 

    word=random.choice(words)
    display=['_']*len(word)
    
    print('Welcome To Our Hangman Game\n')
    print(f"Guess the word: {' '.join(display)}")
    
    while(chances > 0 and '_' in display):
        guess=input("Enter a letter: ").lower()
        if(not guess.isalpha() or len(guess) != 1 or guess in display):
            print("Invalid input (not a single letter or already guessed)")
            continue
    
        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    display[index] = guess
            print(f"Correct Guess!\nUpdated Word: {' '.join(display)}\n")
        else:
            chances -= 1
            print(f"Incorrect Guess! \nRemaining chances: {chances}\n")
    
    if chances==0:
        print(f"Oops! Your chances are over....Better luck next time...\nThe actual word was {word}")
    else:
        print("Congratulation!!! You won")
        
while True:
    hangman_game()
    opt=input("\nDo you want to play again (yes/no)").lower()
    if (opt!='yes'):
        print("Thanks for playing.....See you soon...GoodBye!")
        break
    
