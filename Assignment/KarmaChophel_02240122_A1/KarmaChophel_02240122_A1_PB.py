import random

def guess_number_game():
    
    rand_num = random.randint(1, 5)

    guess_num = int(input("Guess a number between 1 and 5: "))

    if guess_num < 1 or guess_num > 5:
        print("Error: Guess a number between 1 - 5")
    elif guess_num == rand_num:
        print("Hooray, You guessed it right!")
    else:
        print("Oops! Better luck next time.")

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice!")
        return

    print(f"Computer's choice: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")

def main():
    while True:
        print("\n1. Guess Number game")
        print("2. Rock Paper Scissors game")
        print("3. Exit Program")

        choose = input("Enter your choice (1-3): ")

        if choose == "1":
            guess_number_game()
        elif choose == "2":
            rock_paper_scissors()
        elif choose == "3":
            print("Exit Successful")
            break
        else:
            print("Invalid choice! Try again.")

main()