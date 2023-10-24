import random

word_list = ["difficult", "banana", "apple", "python", "daegu", "catholic", "university"]

select_word = random.choice(word_list)

display_word = ["_"] * len(select_word)

use_chance = 6

def draw_hangman(chance):
    Hangman = [
        """ 
           --------
           |      |
                  |
                  |
                  |
                  |
                  |
        """,
        """ 
           --------
           |      |
           O      |
                  |
                  |
                  |
                  |
        """,
        """ 
           --------
           |      |
           O      |
           |      |
                  |
                  |
                  |
        """,
        """ 
           --------
           |      |
           O      |
          /|      |
                  |
                  |
                  |
        """,
        """ 
           --------
           |      |
           O      |
          /|\\     |
                  |
                  |
                  |
        """,
        """ 
           --------
           |      |
           O      |
          /|\\     |
          /       |
                  |
        """,
        """ 
           --------
           |      |
           O      |
          /|\\     |
          / \\     |
                  |
        """    
    ]
    print(Hangman[6 - chance])

print("Welcome to Hangman!")
print("You have 6 attempts to guess the word.")

correct_guesses = []  

while use_chance > 0:
    
    draw_hangman(use_chance)
    print(" ".join(display_word))

    guess = input("Enter your guess: ").lower()

    if guess in select_word and guess not in correct_guesses:  
        correct_guesses.append(guess)  
        for i in range(len(select_word)):
            if select_word[i] == guess:
                display_word[i] = guess
        print('Yes!', guess, 'is in the word!')
        if "".join(display_word) == select_word:
            print("Congratulations! You guessed the word:", select_word)
            break
    elif guess in correct_guesses:
        print('You already guessed', guess)
    else:
        print("Incorrect guess.")
        use_chance -= 1
        print("Remaining attempts:", use_chance)

if use_chance == 0:
    draw_hangman(use_chance)
    print("You ran out of attempts. The word was:", select_word)
