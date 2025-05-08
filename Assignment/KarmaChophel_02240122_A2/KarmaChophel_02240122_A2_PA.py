import random

class GuessNumberGame:
    """Guess a number between 1 and 10 without using try-except."""
    def __init__(self):
        self.score = 0

    def play(self):
        number = random.randint(1, 10)
        attempts = 0
        print("Guess a number between 1 and 10.")
        while True:
            guess = input("Your guess: ")
            if not guess.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            guess = int(guess)
            attempts += 1
            if guess == number:
                print("Correct!")
                self.score += max(0, 10 - attempts)
                break
            elif guess < number:
                print("Too low!")
            else:
                print("Too high!")

class RockPaperScissorsGame:
    """Play rock paper scissors against the computer"""
    def __init__(self):
        self.score = 0

    def play(self):
        choices = ['rock', 'paper', 'scissors']
        user = input("Pick one from rock, paper and scissors: ").lower()
        if user not in choices:
            print("Invalid choice.")
            return
        comp = random.choice(choices)
        print(f"You have picked: {user}")
        print(f"Computer have picked: {comp}")
        if user == comp:
            print("It's a tie.")
        elif user == 'rock' and comp == 'scissors':
             print("You win!")
        elif user == 'scissors' and comp == 'paper':
             print("You win!")
        elif (user == 'paper' and comp == 'rock'):
            print("You win!")
            self.score += 1
        else:
            print("You lose!")

class TriviaGame:
    """Answer Bhutanese Kings trivia questions"""
    def __init__(self):
        self.score = 0

    def play(self):
        questions = [
            {
                "q": "Who was the first King of Bhutan?",
                "A": "A", "options": {
                    "A": "Ugyen Wangchuck",
                    "B": "Jigme Wangchuck",
                    "C": "Jigme Dorji Wangchuck",
                    "D": "Jigme Singye Wangchuck"
                }
            },
            {
                "q": "Which King introduced modern reforms in Bhutan?",
                "A": "C", "options": {
                    "A": "Jigme Khesar Namgyel Wangchuck",
                    "B": "Jigme Singye Wangchuck",
                    "C": "Jigme Dorji Wangchuck",
                    "D": "Ugyen Wangchuck"
                }
            },
            {
                "q": "Who is the current King of Bhutan?",
                "A": "D", "options": {
                    "A": "Jigme Dorji Wangchuck",
                    "B": "Jigme Singye Wangchuck",
                    "C": "Ugyen Wangchuck",
                    "D": "Jigme Khesar Namgyel Wangchuck"
                }
            }
        ]

        for i, q in enumerate(questions, 1):
            print(f"\nQ{i}: {q['q']}")
            for k, v in q['options'].items():
                print(f"{k}) {v}")
            ans = input("Enter your option: ")
            if ans == q["A"]:
                print("Correct!")
                self.score += 1
            else:
                print(f"Incorrect! Correct answer: {q['A']}) {q['options'][q['A']]}")

class ScoreSystem:
    """Show total scores"""
    def __init__(self, g1, g2, g3):
        self.g1 = g1
        self.g2 = g2
        self.g3 = g3

    def show(self):
        print("\n--- Score Summary ---")
        print(f"Guess Number: {self.g1.score}")
        print(f"Rock Paper Scissors: {self.g2.score}")
        print(f"Trivia Game: {self.g3.score}")
        print(f"Total Score: {self.g1.score + self.g2.score + self.g3.score}")

class GameMenu:
    """Game menu to choose functions"""
    def __init__(self):
        self.g1 = GuessNumberGame()
        self.g2 = RockPaperScissorsGame()
        self.g3 = TriviaGame()
        self.score = ScoreSystem(self.g1, self.g2, self.g3)

    def run(self):
        while True:
            print("\nSelect a function (0-5):")
            print("1. Guess Number Game")
            print("2. Rock Paper Scissors")
            print("3. Trivia Game")
            print("4. Pokemon Card Binder Manager (Part B)")
            print("5. Show Score")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.g1.play()
            elif choice == '2':
                self.g2.play()
            elif choice == '3':
                self.g3.play()
            elif choice == '4':
                print("Launching Pokemon Binder Manager... (see Part B file)")
            elif choice == '5':
                self.score.show()
            elif choice == '0':
                print("Goodbye! Had a good time")
                break
            else:
                print("Invalid input.")
                continue

            again = input("Would you like to try another game (y/n): ").lower()
            if again != 'y':
                print("Thank you for your time")
                break

if __name__ == "__main__":
    GameMenu().run()
