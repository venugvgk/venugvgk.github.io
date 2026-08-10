import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
round_number = 1

print("Rock Paper Scissors")
print("Type rock, paper, or scissors. Type quit to stop.")

while True:
    print()
    print(f"Round {round_number}")
    user_choice = input("Your choice: ").strip().lower()

    if user_choice == "quit":
        break

    if user_choice not in choices:
        print("Invalid choice. Please type rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie.")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round.")
        user_score += 1
    else:
        print("Computer wins this round.")
        computer_score += 1

    print("Score:", user_score, "-", computer_score)
    round_number += 1

print()
print("Final score:", user_score, "-", computer_score)
if user_score > computer_score:
    print("You won the game.")
elif computer_score > user_score:
    print("Computer won the game.")
else:
    print("The game ended in a tie.")