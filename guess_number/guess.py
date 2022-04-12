import random
from logo import logo 

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("")


random_number = random.randint(1,101)

my_choice = input("Choose a difficulty. Type 'easy' or 'hard': ")

#counter 
counter_easy = 9
counter_hard = 4


#easy function with 10 tries
def easy():
      
  while True:
    global counter_easy
    my_guess = int(input("Enter your number: "))

    if random_number != my_guess:
          print(f"You have {counter_easy} attempts remaining to guess the number.")
          counter_easy = counter_easy - 1

          if random_number < my_guess:
              print("Too high.")
          elif random_number > my_guess:
                print("Too low.")

    elif random_number == my_guess:
          print("Correct! You won!")
          exit()

    elif counter_easy == -1:
          print("You lose.")
          exit()

#hard function with 5 tries 

def hard():
      
  while True:
    global counter_hard
    my_guess = int(input("Enter your number: "))

    if random_number != my_guess:
          print(f"You have {counter_hard} attempts remaining to guess the number.")
          counter_hard = counter_hard - 1

          if random_number < my_guess:
              print("Too high.")
          elif random_number > my_guess:
                print("Too low.")

    elif random_number == my_guess:
          print("Correct! You won!")
          exit()

    elif counter_easy == -1:
          print("You lose.")
          exit()

    

while True: 

  if my_choice == "easy":
      print("You have 10 attempts remaining to guess the number.")
      easy()

  elif my_choice == "hard":
    print("You have 5 attempts remaining to gues the number.")
    hard()
  else:
      print("Invalid input, please choose between 'easy' or 'hard' ")
      break
