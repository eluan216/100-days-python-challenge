import random

choices = ["rock", "paper", "scissors"]

print("=== ROCK, PAPER, SCISSORS ===")

player = input("Choose rock, paper, or scissors: ").lower().strip()
score = {"player": 0, "computer": 0}

if player not in choices:
    print("Invalid choice! Please try again.")
else:
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or  \
         (player == "scissors" and computer == "paper"):
        print("You win! 🎉")
    else:
        print("Computer wins! 🤖") 

    if player != computer:
        if (player == "rock" and computer == "scissors") or \
           (player == "paper" and computer == "rock") or  \
           (player == "scissors" and computer == "paper"):
            score["player"] += 1
        else:
            score["computer"] += 1

print(f"Score - Player: {score['player']}, Computer: {score['computer']}")