import unittest
from KarmaChophel_02240122_A3 import BankAccount, PersonalAccount, BusinessAccount, BankingSystem, InvalidInputError, TransferError


class TestBankingApplication(unittest.TestCase):

    def setUp(self):
        """Set up test accounts and a bank system instance."""
        self.bank = BankingSystem(filename="test_accounts.txt")  # use test file to avoid overwriting main data
        self.account1 = PersonalAccount("12345", "1111", 1000.0)
        self.account2 = BusinessAccount("54321", "2222", 500.0)
        self.bank.accounts["12345"] = self.account1
        self.bank.accounts["54321"] = self.account2

    # 1. Test Deposit
    def test_deposit_positive_amount(self):
        result = self.account1.deposit(100)
        self.assertEqual(self.account1.funds, 1100.0)
        self.assertEqual(result, "Deposit completed.")

    def test_deposit_negative_amount(self):
        with self.assertRaises(InvalidInputError):
            self.account1.deposit(-50)

    # 2. Test Withdrawal
    def test_withdraw_valid_amount(self):
        result = self.account1.withdraw(500)
        self.assertEqual(self.account1.funds, 500.0)
        self.assertEqual(result, "Withdrawal completed.")

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(InvalidInputError):
            self.account1.withdraw(2000)

    def test_withdraw_negative_amount(self):
        with self.assertRaises(InvalidInputError):
            self.account1.withdraw(-100)

    # 3. Test Transfer
    def test_valid_transfer(self):
        result = self.account1.transfer(200, self.account2)
        self.assertEqual(self.account1.funds, 800.0)
        self.assertEqual(self.account2.funds, 700.0)
        self.assertEqual(result, "Transfer completed.")

    def test_invalid_transfer_recipient(self):
        with self.assertRaises(TransferError):
            self.account1.transfer(100, "not_an_account")

    def test_transfer_insufficient_funds(self):
        with self.assertRaises(InvalidInputError):
            self.account1.transfer(2000, self.account2)

    # 4. Test Mobile Top-Up
    def test_valid_mobile_top_up(self):
        result = self.account1.mobile_top_up(100, "77445566")
        self.assertEqual(self.account1.funds, 900.0)
        self.assertIn("Top-up of Nu. 100 to 77445566", result)

    def test_invalid_phone_number(self):
        with self.assertRaises(InvalidInputError):
            self.account1.mobile_top_up(100, "abc123")

    def test_mobile_top_up_insufficient_funds(self):
        with self.assertRaises(InvalidInputError):
            self.account1.mobile_top_up(2000, "77445566")

    # 5. Test Account Deletion
    def test_delete_existing_account(self):
        self.bank.delete_account("12345")
        self.assertNotIn("12345", self.bank.accounts)

    def test_delete_nonexistent_account(self):
        with self.assertRaises(InvalidInputError):
            self.bank.delete_account("99999")

    # 6. Login Function
    def test_login_successful(self):
        account = self.bank.login("12345", "1111")
        self.assertEqual(account.account_id, "12345")

    def test_login_failure_wrong_passcode(self):
        with self.assertRaises(InvalidInputError):
            self.bank.login("12345", "wrong")

    def test_login_failure_nonexistent_account(self):
        with self.assertRaises(InvalidInputError):
            self.bank.login("99999", "1234")

    def tearDown(self):
        """Clean up by removing test accounts."""
        try:
            import os
            os.remove("test_accounts.txt")
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
