# YourName_YourStudentNumber_A2_PB.py

class PokemonCard:
    def __init__(self, pokedex_number):
        self.pokedex_number = pokedex_number
        self.page, self.row, self.col = self.calculate_position()

    def calculate_position(self):
        index = self.pokedex_number - 1
        page = index // 64 + 1
        pos = index % 64
        row = pos // 8 + 1
        col = pos % 8 + 1
        return page, row, col

class Binder:
    def __init__(self):
        self.cards = {}
        self.MAX = 1025

    def add_card(self, number):
        if number < 1 or number > self.MAX:
            print("Invalid Pokedex number.")
            return
        if number in self.cards:
            print("Status: Already exists.")
        else:
            card = PokemonCard(number)
            self.cards[number] = card
            print(f"Page: {card.page}")
            print(f"Position: Row {card.row}, Column {card.col}")
            print(f"Status: Added Pokedex #{number}")

    def reset(self):
        confirm = input("Type 'CONFIRM' to reset or 'EXIT' to cancel: ").upper()
        if confirm == "CONFIRM":
            self.cards.clear()
            print("Binder reset successful.")
        else:
            print("Reset cancelled.")

    def view(self):
        if not self.cards:
            print("Binder is empty.")
        else:
            print("Current Binder Contents:")
            for num in sorted(self.cards):
                card = self.cards[num]
                print(f"Pokedex #{num}: Page {card.page}, Row {card.row}, Col {card.col}")
        total = len(self.cards)
        percent = round((total / self.MAX) * 100, 1)
        print(f"Total cards: {total}")
        print(f"Completion: {percent}%")
        if total == self.MAX:
            print("You have caught them all!!")

class BinderManager:
    def __init__(self):
        self.binder = Binder()

    def main_menu(self):
        while True:
            print("\nPokemon Card Binder Manager")
            print("1. Add Pokemon card")
            print("2. Reset binder")
            print("3. View binder")
            print("4. Exit")
            choice = input("Select option: ")
            if choice == '1':
                try:
                    num = int(input("Enter Pokedex number: "))
                    self.binder.add_card(num)
                except ValueError:
                    print("Please enter a valid integer.")
            elif choice == '2':
                self.binder.reset()
            elif choice == '3':
                self.binder.view()
            elif choice == '4':
                print("Thanks for using the Pokemon Card Binder Manager!")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    BinderManager().main_menu()
