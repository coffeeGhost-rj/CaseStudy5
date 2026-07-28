from bankingSector import Account, BankAccount, SavingsAccount, CurrentAccount


def demo():
    print("Demo: banking account behaviors")

    acc = BankAccount("001", "Alice", 1000, 2.5)
    print(acc.show_account_details())
    interest = acc.calculate_interest()
    print(f"Calculated interest: ${interest:.2f}")
    applied = acc.apply_interest()
    print(f"Applied interest: ${applied:.2f} -> New balance: ${acc.balance:.2f}")

    sav = SavingsAccount("002", "Bob", 500, 3.0)
    print(sav.show_account_details())
    print(f"Savings interest (preview): ${sav.calculate_interest():.2f}")
    sav.apply_interest()
    print(f"Savings balance after applying interest: ${sav.balance:.2f}")

    cur = CurrentAccount("003", "Carol", 100, 0.5, overdraft_limit=200)
    print(cur.show_account_details())
    print(cur.withdraw(250))
    print(cur.withdraw(60))


if __name__ == "__main__":
    demo()
