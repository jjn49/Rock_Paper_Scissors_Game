# game.py

import random

print("Rock, Paper, Scissors, Shoot!")

# Prompt User for Input

#x = input("Choose 'rock' or 'paper' or 'scissors'")
user_choice = input("Choose 'rock' or 'paper' or 'scissors':")
print("User chose:")
print(user_choice)

# Computer Choice (At Random)

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
print("Computer chose:")
print(computer_choice)
