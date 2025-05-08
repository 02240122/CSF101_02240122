class PokemonBinder:
    def __init__(self):
        self.cards = {}

    def add_card(self, pokedex_num):
        if not (1 <= pokedex_num <= 1025):
            return "Invalid Pokedex number. Please enter a number between 1 and 1025."

        if pokedex_num in self.cards:
            page, row, col = self.cards[pokedex_num]
            return f"Pokedex #{pokedex_num} already exists at Page {page}, Row {row}, Column {col}."

        index = pokedex_num - 1
        page = index // 64 + 1
        position = index % 64
        row = position // 8 + 1
        col = position % 8 + 1
        self.cards[pokedex_num] = (page, row, col)
        return f"Page: {page}\nPosition: Row {row}, Column {col}\nStatus: Added Pokedex #{pokedex_num} to binder"

    def reset_binder(self):
        self.cards.clear()

    def view_binder(self):
        if not self.cards:
            return "The binder is empty."

        result = ["Current Binder Contents:\n------------------------"]
        for num in sorted(self.cards):
            page, row, col = self.cards[num]
            result.append(f"Pokedex #{num}:\n  Page: {page}\n  Position: Row {row}, Column {col}")
        result.append("------------------------")
        total = len(self.cards)
        percent = round((total / 1025) * 100, 1)
        result.append(f"Total cards in binder: {total}\n% completion: {percent}%")
        if total == 1025:
            result.append("You have caught them all!!")
        return "\n".join(result)

    def get_total(self):
        return len(self.cards)


class PokemonBinderApp:
    def __init__(self):
        self.binder = PokemonBinder()

    def run(self):
        print("Welcome to Pokemon Card Binder Manager!")
        while True:
            print("\nMain Menu:")
            print("1. Add Pokemon card")
            print("2. Reset binder")
            print("3. View current placements")
            print("4. Exit")

            choice = input("Select option: ")
            if choice == "1":
                try:
                    pokedex_number = int(input("Enter Pokedex number: "))
                    print(self.binder.add_card(pokedex_number))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            elif choice == "2":
                print("WARNING: This will delete ALL Pokemon cards from the binder.")
                print("This action cannot be undone.")
                confirm = input("Type 'CONFIRM' to reset or 'EXIT' to return to the Main Menu: ").upper()
                if confirm == "CONFIRM":
                    self.binder.reset_binder()
                    print("The binder reset was successful! All cards have been removed.")
                else:
                    print("Binder reset cancelled.")
            elif choice == "3":
                print(self.binder.view_binder())
            elif choice == "4":
                print("Thank you for using Pokemon Card Binder Manager!")
                print(f"Total cards collected: {self.binder.get_total()}")
                break
            else:
                print("Invalid selection. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    app = PokemonBinderApp()
    app.run()
