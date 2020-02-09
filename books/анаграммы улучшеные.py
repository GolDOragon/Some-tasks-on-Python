# урок 4 задание 2
# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# Resault of game
rez = 11

# start the game
print(
"""
           Welcome to Word Jumble!
        
   Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print("The jumble is:", jumble)

guess = 'spawn'

while guess != correct:

    rez -= 1
    guess = input("\nYour guess: ")

    if guess == "":                         #Help
        print('Can I help you? Yes/No')
        ans = input('')
        if ans.upper() == 'YES':
            print('How many letters open? (max ', len(correct),')')
            letter = int(input())
            print(correct[:letter])
            rez -= letter
        elif ans.upper() == 'NO':
            ex = input('Exit from game? ')
            if ex.upper() == 'YES':
                break


  
        
    
if guess == correct:
    print("That's it!  You guessed it!\nAnd gets ", rez,"point(s)")

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")


