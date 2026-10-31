#01 guess the number

import random

def guess(x):

    number = random.randint(1, x)
    guess = 0
    
    while guess != number:
        guess = int(input(f"guess a number between 1 and {x}: "))
        if guess < number:
            print("number is too low.")
            
        elif guess > number:
            print("number is too high.")
    print(f"Congratulations! You guessed the number {number} correctly.")

guess(10)
