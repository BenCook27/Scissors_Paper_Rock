# Computer needs to select either scissors, paper or rock
# Player needs to select either scissors, paper or rock
# Evaluate the two inputs to determine if the game is a tie or who the winner is 
# Use a while loop to allow the player to choose to play again or quit playing
# Extension - use a loop counter to keep track of how many games have been won or lost

import random

computer_score = 0
user_score = 0
game_number = 0

while True:
    SPR = ["Scissors", "Paper", "Rock"]
    computer_choice = random.choice(SPR)
    user_choice = input("Please type Scissors, Paper or Rock: ").title()

    if computer_choice == user_choice:
        print(F"You both picked {computer_choice} the game is a tie")
    elif user_choice == "Scissors":
        if computer_choice == "Rock":
            computer_score += 1 
            print("Bad luck the computer picked Rock, you lose!")
        else:
            user_score += 1
            print("The computer picked Paper, you win!")
    elif user_choice == "Paper":
        if computer_choice == "Scissors":
            computer_score += 1
            print("Bad luck the computer picked Scissors, you lose!")
        else:
            user_score += 1
            print("The computer picked Rock, you win!")
    elif user_choice == "Rock":
        if computer_choice == "Paper":
            computer_score += 1
            print("Bad luck the computer picked Paper, you lose!")
        else:
            user_score += 1
            print("The computer picked Scissors, you win!")
    game_number += 1

    if user_score == computer_score:
        print(f"Out of {game_number} games you have only won 50% of the time!")
    elif user_score > computer_score:
        percentage = user_score/game_number*100
        print(f"You have won {user_score} out of {game_number} games. Thats a {percentage}% win rate!")
    elif user_score < computer_score:
        percentage = computer_score/game_number*100
        print(f"The computer has won {computer_score} out of {game_number} games. You have lost {percentage}% of the time!")
    
    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again != "y":
        break
