import random

word_list = ["difficult", "banana", "apple", "python", "daegu", "catholic", "university"]
selected_word = random.choice(word_list)
word_len = len(selected_word)
chance = 6
guess_word = ['_'] * word_len
print('Guess the word!!!')
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n\n")
print('Length of the selected word : ', word_len)
print('Remaining attempts : ', chance)

while chance > 0:
    print('Current guess word : ', " ".join(guess_word))
    guess = input('Guess a letter : ').lower()
    
    if guess in selected_word:
        for i in range(word_len):
            if selected_word[i] == guess:
                guess_word[i] = guess  
        if ''.join(guess_word) == selected_word:
            print('Congratulations! You guessed the word : ', selected_word)
            break
        print('Remaining attempts', chance)
    else:
        print('Incorrect guess.')
        chance -= 1
        if chance == 0:
            break
        print('Remaining attempts : ', chance)

if chance == 0:
    print("You've used up all your attempts. The correct word was : ", selected_word)

