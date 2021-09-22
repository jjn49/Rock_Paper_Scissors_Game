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

# Code used from Fenny on slack

if user_choice == computer_choice:
    print("Tie. There is no winner.")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("The computer wins.")
    else:
        print("The user wins.")
elif user_choice == "paper":
    if computer_choice == "scissors":
        print("The computer wins.")
    else:
        print("The user wins.")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("The computer wins.")
    else:
        print("The user wins.")
