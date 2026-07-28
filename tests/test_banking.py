import unittest
from bankingSector import BankAccount, SavingsAccount, CurrentAccount


class TestBanking(unittest.TestCase):
    def test_calculate_and_apply_interest(self):
        acc = BankAccount("100", "Test", 1000, 5)
        interest = acc.calculate_interest()
        self.assertEqual(interest, 50.00)
        applied = acc.apply_interest()
        self.assertEqual(applied, 50.00)
        self.assertEqual(acc.balance, 1050.00)

    def test_savings_inherits_interest(self):
        sav = SavingsAccount("101", "Saver", 200, 2.5)
        self.assertEqual(sav.calculate_interest(), 5.00)
        sav.apply_interest()
        self.assertEqual(sav.balance, 205.00)

    def test_current_withdraw_overdraft(self):
        cur = CurrentAccount("102", "Current", 100, 1, overdraft_limit=50)
        # can withdraw within overdraft
        res = cur.withdraw(140)
        self.assertIn("Remaining balance", res)
        self.assertEqual(cur.balance, -40.00)
        # cannot withdraw beyond overdraft
        res2 = cur.withdraw(200)
        self.assertIn("Insufficient funds", res2)

    def test_deposit_and_validation(self):
        acc = BankAccount("103", "D", 10, 1)
        self.assertIn("Deposit amount must be positive", acc.deposit(0))
        self.assertIn("Deposited", acc.deposit(50))
        self.assertEqual(acc.balance, 60.00)

    def test_withdraw_validation(self):
        acc = BankAccount("104", "W", 100, 1)
        self.assertIn("Withdrawal amount must be positive", acc.withdraw(0))


if __name__ == '__main__':
    unittest.main()
