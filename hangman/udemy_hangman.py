import random
from word_list import word_list
from stages import stages
from stages import logo
import os


print(logo)

chosen_word = random.choice(word_list)



display = []

for i in chosen_word:

    display.append("_")

lives = 6

while True: 

    guess = input("Guess a letter: ").lower()

    os.system("cls")

    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter


    print(display)



    if guess not in chosen_word:
        lives = lives - 1
        print(stages[lives])
        if lives == 0: 
            print("You lose!")
            exit()
        

    if "_" not in display:
            print("You won! Congratulations!") 
            break



    