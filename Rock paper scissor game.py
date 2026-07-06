import random

user_score = 0
computer_score = 0

while True:

    print("\n*** Welcome to Rock Paper Scissor Game ***")
    print("Choose one:")
    print("rock")
    print("paper")
    print("scissor")

    user_choice = input("Enter your choice: ").lower()

    if user_choice not in ["rock", "paper", "scissor"]:
        print("Invalid choice! Please choose rock, paper, or scissor.")
        continue

    choices = ["rock", "paper", "scissor"]
    computer_choice = random.choice(choices)

    print("\nYou chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):

        print("Congratulations! You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("\nScoreboard")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nFinal Scores")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)
        print("Thank you for playing!")
        break
