from art import logo,vs
from game_data import data 
import random
import os

score = 0


while True:
    os.system("cls")

    print(f"Your current score is: {score}")

    print(logo)

    first_name = random.choice(data)
    second_name = random.choice(data)

    first_name_values = list(first_name.values())
    second_name_values = list(second_name.values())

    #comparing values 

    print(f"{first_name_values[0]}, a {first_name_values[2]}, from, {first_name_values[3]}.")

    print(vs)

    print(f"{second_name_values[0]}, a {second_name_values[2]}, from, {second_name_values[3]}.")
    print("")

    #comparing followers from values


    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()



    if user_choice == "A":
        if first_name_values[1] > second_name_values[1]:
            score += 1
            print(f"You're right! Current score: {score}.")
            
        else:
            print(f"Wrong answer. You lose. Your final score is: {score}.")
            exit()

    if user_choice == "B":
        if second_name_values[1] > first_name_values[1]:
            score +=1
            print(f"You're right! Current score: {score}.")
            
        else:
            print(f"Wrong answer. You lose. Your final score is: {score}.")
            exit()

    

