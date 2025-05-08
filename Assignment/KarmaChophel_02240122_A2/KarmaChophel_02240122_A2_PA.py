# YourName_YourStudentNumber_A2_PA.py

import random

class GuessNumberGame:
    """Guess a number between 1 and 10"""
    def __init__(self):
        self.score = 0

    def play(self):
        number = random.randint(1, 10)
        attempts = 0
        print("Guess a number between 1 and 10.")
        while True:
            try:
                guess = int(input("Your guess: "))
                attempts += 1
                if guess == number:
                    print("Correct!")
                    self.score += max(0, 10 - attempts)
                    break
                elif guess < number:
                    print("Too low!")
                else:
                    print("Too high!")
            except ValueError:
                print("Invalid input. Please enter a number.")

