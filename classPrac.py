# Classes in Python
# A class is a blueprint for creating objects.
# Objects are instances of a class, and they can store data (attributes)
# and perform actions (methods).

class Dog:
    # The __init__ method runs when a new Dog object is created.
    # It sets up the object's initial state.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # A method is a function inside a class.
    # It describes what the object can do.
    def bark(self):
        return f"{self.name} says woof!"

    def birthday(self):
        self.age += 1
        return self.age


# Creating an object from the class:
my_dog = Dog("Buddy", 3)

# Accessing attributes:
print(my_dog.name)
print(my_dog.age)

# Calling methods:
print(my_dog.bark())
print(my_dog.birthday())

# Why use classes?
# 1. They organize related data and behaviors together.
# 2. They let you reuse the same blueprint for many objects.
# 3. They make code easier to read and maintain.
# 4. They help model real-world things in a program.

# Example: You can make many Dog objects without rewriting the code.
dog2 = Dog("Max", 5)
print(dog2.bark())


class BankAccount:
    def __init__(self, accid, holdername, balance):
        self.accid = accid
        self.holdername = holdername
        self.balance = balance

    def show_acc_details(self):
        return f"Account ID: {self.accid}\nHolder Name: {self.holdername}\nBalance: ${self.balance}"

    def deposit_amount(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw_amount(self, amount):
        if amount > self.balance:
            return f"Insufficient balance. Current balance: ${self.balance}"
        self.balance -= amount
        return f"Withdrew ${amount}. Remaining balance: ${self.balance}"


# Example usage
account1 = BankAccount(101, "Alice", 500)
print(account1.show_acc_details())
print(account1.deposit_amount(200))
print(account1.withdraw_amount(100))


