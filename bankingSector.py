class Account:
    def __init__(self, account_number, account_holder, initial_balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = float(initial_balance)

    def show_account_details(self):
        return (f"Account Number: {self.account_number}\n"
            f"Account Holder: {self.account_holder}\n"
            f"Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            return f"Deposit amount must be positive."
        self.balance = round(self.balance + float(amount), 2)
        return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance:
            return f"Insufficient funds. Current balance: ${self.balance:.2f}"
        self.balance = round(self.balance - float(amount), 2)
        return f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}"

class BankAccount(Account):
    def __init__(self, account_number, account_holder, initial_balance, interest_rate):
        super().__init__(account_number, account_holder, initial_balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        """Return the interest amount (not applied) rounded to 2 decimals."""
        interest = round(self.balance * (float(self.interest_rate) / 100), 2)
        return interest

    def apply_interest(self):
        """Apply interest to balance and return the interest amount."""
        interest = self.calculate_interest()
        self.balance = round(self.balance + interest, 2)
        return interest

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, initial_balance, interest_rate):
        super().__init__(account_number, account_holder, initial_balance, interest_rate)
    # Inherits calculate_interest and apply_interest from BankAccount


class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder, initial_balance, interest_rate, overdraft_limit):
        super().__init__(account_number, account_holder, initial_balance, interest_rate)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.balance + float(self.overdraft_limit):
            return (f"Insufficient funds. Current balance: ${self.balance:.2f}, "
                    f"Overdraft limit: ${float(self.overdraft_limit):.2f}")
        self.balance = round(self.balance - float(amount), 2)
        return f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}"

    def calculate_interest(self):
        return super().calculate_interest()


account1 = BankAccount("001", "Alice", 1000, 2.5)
savings1 = SavingsAccount("002", "Bob", 500, 3.0)
current1 = CurrentAccount("003", "Carol", 100, 0.5, overdraft_limit=200)
print(account1.show_account_details())
print(f"interest calculated: ${account1.calculate_interest():.2f}")
print("-------------")
print(savings1.show_account_details())
print(f"interest calculated: ${savings1.calculate_interest():.2f}")
print("-------------")
print(current1.show_account_details())