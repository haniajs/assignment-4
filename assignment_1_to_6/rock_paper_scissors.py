import random

choices = ["rock", "paper", "scissors"]
player_choice = input("Enter rock, paper or scissors: ").lower()
computer_choice = random.choice(choices)

if player_choice == computer_choice:
    print(f"dono ka choice {player_choice} tha. Its a tie!")
elif player_choice == "rock" and computer_choice  == "scissors":
    print(f"Players win! {player_choice} beats {computer_choice}.")

elif player_choice == "paper" and computer_choice == "rock":
    print(f"Players win! {player_choice} beats {computer_choice}.")
elif player_choice == "scissors" and computer_choice == "paper":
    print(f"Players win! {player_choice} beats {computer_choice}.")
else:
    print(f"Computer win! {computer_choice} beats {player_choice}.")    