#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random


options = ["rock", "paper", "scissors"]
score = {"player": 0, "computer": 0}

while True:
    computer_choice = random.choice(options)
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if player_choice not in options:
        print("Invalid option. Please try again.")
        continue

    print(f"Computer chose {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        score["player"] += 1
    else:
        print("You lose!")
        score["computer"] += 1

    print(f"Score: Player {score['player']}, Computer {score['computer']}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break




