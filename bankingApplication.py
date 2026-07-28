from bankingSector import BankAccount, CurrentAccount
try:
    account1 = BankAccount("001", "Alice", 1000, 2.5)
    # savings1 = SavingsAccount("002", "Bob", 500, 3.0)
    current1 = CurrentAccount("003", "Carol", 100, 0.5, overdraft_limit=200)
except ValueError:
    print("Invalid value.")

print(account1.show_account_details())
print(f"interest calculated: ${account1.calculate_interest():.2f}")

print("-------------")

# print(savings1.show_account_details())
# print(f"interest calculated: ${savings1.calculate_interest():.2f}")

print("-------------")

print(current1.show_account_details())