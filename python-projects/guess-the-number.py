# This game tells the computer to generate a random number between 1 and x
# and x is defined with a parameter supplied to the function. 
# Using a while loop keeps the game going unless x is correctly guessed and 
# if, elif statements are used to provide feedback if our guess is too high
# or too low.

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess > random_number:
            print("Sorry, guess again. Too high...")
        elif guess < random_number:
            print("Sorry, guess again. Too low...")
    
    print(f"Well done! You have correctly guessed the number {random_number}!")

guess(100)