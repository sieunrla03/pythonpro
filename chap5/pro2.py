import random
word = ('difficult', 'banana', 'apple', 'python', 'daegu', 'catholic', 'university')
a = random.choice(word)
print('Welcome to word Jumble!\nUnscramble the latters to make a word.')
b = list(a)
random.shuffle(b)
b = ''.join(b) 
print('Jumbled word : ', b)
guess = input('your guess : ')
if a == guess:
    print('>>clear!!<<')
else:
    print("sorry, that's not correct. The word was : ", a)
