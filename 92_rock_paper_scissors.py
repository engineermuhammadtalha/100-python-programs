# Rock Paper Scissors
import random

choices = ["rock", "paper", "scissors"]

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    wins = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
    if wins[user] == computer:
        return "You win! 🎉"
    return "Computer wins! 🤖"

score_user = 0
score_computer = 0

print("=== Rock Paper Scissors ===")
print("Type 'quit' to exit.\n")

while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice == "quit":
        break
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)

    if "You win" in result:
        score_user += 1
    elif "Computer wins" in result:
        score_computer += 1

    print(f"Score → You: {score_user} | Computer: {score_computer}\n")

print("Thanks for playing!")
