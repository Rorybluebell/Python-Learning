#rock-paper-scissors game

import random

def is_win(user, opponent):
    return (user == 'r' and opponent == 's' or
            user == 's' and opponent == 'p' or
            user == 'p' and opponent == 'r')

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie!"

    if is_win(user, computer):
        return "You won!"

    return "You lost!"
play(user, computer)
    
    

    