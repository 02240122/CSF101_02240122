"""
KarmaChophel_02240122_A3.py

Part A: CSF101 Banking Application
Implements CLI and GUI banking system with exception handling, docstrings, and phone top-up functionality.
"""

import random
import tkinter as tk
from tkinter import messagebox

# ---------------------- Custom Exception Classes ----------------------

class InvalidInputError(Exception):
    """Raised when invalid input is provided."""
    pass

class TransferError(Exception):
    """Raised when a transfer operation fails."""
    pass



# ---------------------- Account Classes ----------------------

class BankAccount:
    """
    Base class for a bank account.
    """

    def __init__(self, account_id, passcode, account_category, funds=0):
        self.account_id = account_id
        self.passcode = passcode
        self.account_category = account_category
        self.funds = funds

    def deposit(self, amount):
        """Deposits amount if positive."""
        if amount > 0:
            self.funds += amount
            return "Deposit completed."
        raise InvalidInputError("Invalid amount for deposit.")

    def withdraw(self, amount):
        """Withdraws amount if valid and funds are sufficient."""
        if amount > 0 and amount <= self.funds:
            self.funds -= amount
            return "Withdrawal completed."
        raise InvalidInputError("Insufficient funds or invalid withdrawal amount.")

    def transfer(self, amount, recipient_account):
        """Transfers amount to another account."""
        if not isinstance(recipient_account, BankAccount):
            raise TransferError("Recipient account is invalid.")
        withdrawal_message = self.withdraw(amount)
        recipient_account.deposit(amount)
        return "Transfer completed."

    def mobile_top_up(self, amount, phone_number):
        """Deducts amount for mobile phone top-up."""
        if len(phone_number) < 7 or not phone_number.isdigit():
            raise InvalidInputError("Invalid phone number.")
        self.withdraw(amount)
        return f"Top-up of Nu. {amount} to {phone_number} completed."

class PersonalAccount(BankAccount):
    def __init__(self, account_id, passcode, funds=0):
        super().__init__(account_id, passcode, "Personal", funds)

class BusinessAccount(BankAccount):
    def __init__(self, account_id, passcode, funds=0):
        super().__init__(account_id, passcode, "Business", funds)

# ---------------------- Banking System ----------------------

class BankingSystem:
    """
    Handles account creation, login, file storage and retrieval.
    """

    def __init__(self, filename="accounts.txt"):
        self.filename = filename
        self.accounts = self.load_accounts()

    def load_accounts(self):
        """Loads accounts from a text file."""
        accounts = {}
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    account_id, passcode, account_category, funds = line.strip().split(",")
                    funds = float(funds)
                    if account_category == "Personal":
                        account = PersonalAccount(account_id, passcode, funds)
                    else:
                        account = BusinessAccount(account_id, passcode, funds)
                    accounts[account_id] = account
        except FileNotFoundError:
            pass
        return accounts

    def save_accounts(self):
        """Saves accounts to file."""
        with open(self.filename, "w") as file:
            for account in self.accounts.values():
                file.write(f"{account.account_id},{account.passcode},{account.account_category},{account.funds}\n")

    def create_account(self, account_type):
        """Creates new account."""
        account_id = str(random.randint(10000, 99999))
        passcode = str(random.randint(1000, 9999))
        if account_type == "Personal":
            account = PersonalAccount(account_id, passcode)
        else:
            account = BusinessAccount(account_id, passcode)
        self.accounts[account_id] = account
        self.save_accounts()
        return account

    def login(self, account_id, passcode):
        """Authenticates user."""
        account = self.accounts.get(account_id)
        if account and account.passcode == passcode:
            return account
        raise InvalidInputError("Account number or password is not recognized")

    def delete_account(self, account_id):
        """Deletes account by ID."""
        if account_id in self.accounts:
            del self.accounts[account_id]
            self.save_accounts()
        else:
            raise InvalidInputError("Account does not exist")

# ---------------------- CLI Input Processor ----------------------

def process_user_input(choice, account, bank, account_id):
    """
    Processes a menu choice.
    """
    try:
        if choice == "1":
            print(f"Your funds: Nu. {account.funds}")

        elif choice == "2":
            amount = float(input("Deposit amount: "))
            print(account.deposit(amount))
            bank.save_accounts()

        elif choice == "3":
            amount = float(input("Withdrawal amount: "))
            print(account.withdraw(amount))
            bank.save_accounts()

        elif choice == "4":
            recipient_id = input("Recipient account ID: ")
            amount = float(input("Amount to transfer: "))
            recipient_account = bank.accounts[recipient_id]
            print(account.transfer(amount, recipient_account))
            bank.save_accounts()

        elif choice == "5":
            number = input("Phone number: ")
            amount = float(input("Amount to top-up: "))
            print(account.mobile_top_up(amount, number))
            bank.save_accounts()

        elif choice == "6":
            bank.delete_account(account_id)
            print("Account deleted.")
            return False  # Logout

        elif choice == "7":
            return False  # Logout

        else:
            print("Invalid menu option.")

        return True

    except (InvalidInputError, TransferError, KeyError, ValueError) as e:
        print("Error:", e)
        return True

# ---------------------- GUI (Using Tkinter) ----------------------

class BankingAppGUI:
    """
    Basic tkinter GUI for banking system.
    """
    def __init__(self, bank: BankingSystem):
        self.bank = bank
        self.window = tk.Tk()
        self.window.title("Banking System")
        self.window.geometry("400x300")

        self.label = tk.Label(self.window, text="Enter Account ID and Passcode:")
        self.label.pack()

        self.entry_id = tk.Entry(self.window)
        self.entry_id.pack()

        self.entry_pass = tk.Entry(self.window, show="*")
        self.entry_pass.pack()

        self.login_button = tk.Button(self.window, text="Login", command=self.login)
        self.login_button.pack()

        self.result = tk.Label(self.window, text="")
        self.result.pack()

        self.window.mainloop()

    def login(self):
        aid = self.entry_id.get()
        pw = self.entry_pass.get()
        try:
            acc = self.bank.login(aid, pw)
            messagebox.showinfo("Login", f"Welcome {aid}. Balance: Nu. {acc.funds}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# ---------------------- Main CLI Loop ----------------------

def main():
    bank = BankingSystem()

    while True:
        print("\nHello. How can I assist you?")
        print("1. Open Account\n2. Login\n3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            atype = input("1 for Personal, 2 for Business: ")
            if atype == "1":
                account = bank.create_account("Personal")
            elif atype == "2":
                account = bank.create_account("Business")
            else:
                print("Invalid type.")
                continue
            print(f"Account created: ID={account.account_id}, Passcode={account.passcode}")

        elif choice == "2":
            print("Login options:")
            print("1. CLI Login")
            print("2. GUI Login")
            login_mode = input("Choose login method (1 or 2): ")
            if login_mode == "2":
                BankingAppGUI(bank)
                # After GUI closes, return to main menu
            else:
                account_id = input("Account ID: ")
                passcode = input("Passcode: ")
                try:
                    account = bank.login(account_id, passcode)
                    while True:
                        print("\n1. Check Funds\n2. Deposit\n3. Withdraw\n4. Transfer\n5. Mobile Top-up\n6. Delete Account\n7. Logout")
                        action = input("Enter action: ")
                        if not process_user_input(action, account, bank, account_id):
                            break
                except Exception as e:
                    print("Login failed:", e)

        elif choice == "3":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
