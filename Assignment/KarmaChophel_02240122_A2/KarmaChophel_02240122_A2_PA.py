import random

class GuessNumberGame:
#Guess a number
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
                print("Perfect! You nailed it")
                self.score += max(0, 10 - attempts)
                break
            else:
                print("Try your luck again")
        return self.score


class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.score = 0

    def play(self):
        print("Rock, Paper, Scissors Game!")
        print("Let's play a best-of-three game")
        for _ in range(3):
            user = input("Choose one from rock, paper and scissors: ").lower()
            if user not in self.choices:
                print("Invalid input.")
                continue
            comp = random.choice(self.choices)
            print(f"Computer chose: {comp}")
            if user == comp:
                print("Draw")
            elif (user == "rock" and comp == "scissors"):
                print("You win!")
            elif (user == "paper" and comp == "rock"):
                print("You win!")
            elif (user == "scissors" and comp == "paper"):
                print("You win!")
                self.score += 1
            else:
                print("You lose!")
        print(f"Total wins: {self.score}")
        return self.score


class TriviaGame:
#Trivia game with multiple categories and multiple choice questions.
    def __init__(self):
        self.score = 0

    def play(self):
        categories = {
            "1": ("Bhutanese Kings", [
                {"question": "Who was the first King of Bhutan?", "options": {"A": "Ugyen Wangchuck",
         "B": "Jigme Wangchuck", "C": "Jigme Dorji Wangchuck", "D": "Jigme Singye Wangchuck"}, "answer": "A"},
                {"question": "Which King introduced modern education and infrastructure in Bhutan?", "options": {"A": 
                 "Jigme Khesar Namgyel Wangchuck", "B": "Jigme Singye Wangchuck", "C": "Jigme Dorji Wangchuck",
                "D": "Ugyen Wangchuck"}, "answer": "C"},
                {"question": "Who is the current King of Bhutan?", "options": {"A": "Jigme Dorji Wangchuck", 
                "B": "Jigme Singye Wangchuck", "C": "Ugyen Wangchuck", "D": "Jigme Khesar Namgyel Wangchuck"}, "answer": "D"}
            ]),
            "2": ("Science", [
                {"question": "What planet is known as the Red Planet?", "options": {"A": "Earth", "B": "Mars", "C": "Venus",
                 "D": "Jupiter"}, "answer": "B"},
                {"question": "What gas do plants absorb from the atmosphere?", "options": {"A": "Oxygen", "B": "Hydrogen", 
                "C": "Carbon Dioxide", "D": "Nitrogen"}, "answer": "C"},
                {"question": "Which organ pumps blood through the body?", "options": {"A": "Lungs", "B": "Brain", 
                "C": "Heart", "D": "Kidneys"}, "answer": "C"}
            ]),
            "3": ("Sports", [
                {"question": "How many players are on a soccer team?", "options": {"A": "9", "B": "10", "C": "11", "D": "12"},
                "answer": "C"},
                {"question": "Which sport uses a bat, ball, and bases?", "options": {"A": "Cricket", "B": "Baseball",
                 "C": "Golf", "D": "Hockey"}, "answer": "B"},
                {"question": "Who is known as the fastest man in the world?", "options": {"A": "Usain Bolt", 
                "B": "Cristiano Ronaldo", "C": "Michael Phelps", "D": "LeBron James"}, "answer": "A"}
            ])
        }

        print("Select a Trivia Category:")
        for key, (name, _) in categories.items():
            print(f"{key}. {name}")

        choice = input("Enter your choice (1/2/3): ")
        if choice not in categories:
            print("Invalid category choice.")
            return 0

        category_name, questions = categories[choice]
        print(f"\nCategory Selected: {category_name}")

        for i, q in enumerate(questions, 1):
            print(f"\nQ{i}: {q['question']}")
            for key, value in q['options'].items():
                print(f"{key}) {value}")
            user_ans = input("Enter your option(A/B/C/D): ").upper()
            if user_ans == q['answer']:
                print("Correct!")
                self.score += 1
            else:
                correct_option = q['options'][q['answer']]
                print(f"Incorrect! Correct answer: {q['answer']}) {correct_option}")

        return self.score


class PokemonManagerMini:
    def play(self):
        print("Welcome to Pokemon Card Binder Manager.")
        return 0


class ScoreTracker:
    def __init__(self):
        self.total_score = 0
        self.guess_score = 0
        self.rps_score = 0
        self.trivia_score = 0

    def add_score(self, game_name, score):
        self.total_score += score
        if game_name == "guess":
            self.guess_score += score
        elif game_name == "rps":
            self.rps_score += score
        elif game_name == "trivia":
            self.trivia_score += score

    def show_score(self):
        print("\n--- Current Scores ---")
        print(f"Guess Number Game Score: {self.guess_score}")
        print(f"Rock Paper Scissors Score: {self.rps_score}")
        print(f"Trivia Game Score: {self.trivia_score}")
        print(f"Total Overall Score: {self.total_score}")


class GameMenu:
    def __init__(self):
        self.score_tracker = ScoreTracker()

    def run(self):
        while True:
            print("\nSelect a function (0-5):")
            print("1. Guess Number game")
            print("2. Rock paper scissors game")
            print("3. Trivia Pursuit Game")
            print("4. Pokemon Card Binder Manager")
            print("5. Check Current Overall score")
            print("0. Exit program")

            choice = input("Enter your choice: ")
            if choice == "1":
                game = GuessNumberGame()
                score = game.play()
                self.score_tracker.add_score("guess", score)
            elif choice == "2":
                game = RockPaperScissors()
                score = game.play()
                self.score_tracker.add_score("rps", score)
            elif choice == "3":
                game = TriviaGame()
                score = game.play()
                self.score_tracker.add_score("trivia", score)
            elif choice == "4":
                # Importing and running Part B app only when needed
                from KarmaChophel_02240122_A2_PB import PokemonBinderApp
                app = PokemonBinderApp()
                app.run()
            elif choice == "5":
                self.score_tracker.show_score()
                continue
            elif choice == "0":
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")
                continue

            while True:
                print("\nWould you like to return to the menu or exit the program?")
                print("1. Return to Menu")
                print("2. Exit Program")
                user_choice = input("Enter your choice (1 or 2): ")
                if user_choice == "1":
                    break  # return to menu
                elif user_choice == "2":
                    print("Exiting the program.")
                    return
                else:
                    print("Invalid input. Please enter 1 or 2.")


if __name__ == "__main__":
    menu = GameMenu()
    menu.run()