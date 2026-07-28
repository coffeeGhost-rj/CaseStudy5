# Nostart = int(input("Enter the starting number: "))
# Nend = int(input("Enter the ending number: "))
# multiplier = int(input("Enter the multiplier: "))   

# do-while loop to print the multiples of the multiplier from Nostart to Nend
# while True:
#     for i in range(Nostart, Nend + 1):
#         if i % multiplier == 0:
#             print(i)
#     choice = input("Do you want to continue? (y/n): ")
#     if choice.lower() != 'y':
#         break

# for i in range(Nostart, Nend + 1):
#     if i % multiplier == 0:
#         print(i)

# -----------------------------------------------------------------

#  check if a number is positive, negative, or zero

# number = int(input("Enter a number to check:"))

# if number < 0:
#     print("Negative numbers.")
# elif number == 0:
#     print("Zero.")
# elif number > 0:
#     print("Positive numbers.")

# if number == 0:
#     print("Zero.")
# elif number % 2 == 0 and number != 0:
#     print("Even number.")
# else:
#     print("Odd number.")

# ----------------------------------------------------------------
#  check if the user is eligible to vote based on their age


# try:
#     name = input("Enter your name: ")
#     if name is None or name.strip() == "" or name.isdigit():
#         raise ValueError("Please enter a valid name.")
#     age = input("Enter your age: ")
#     if age is None or age.strip() == "" or not age.isdigit():
#         raise ValueError("Please enter a valid age.")
#     elif age.isdigit():
#         age = int(age)
#         if age < 18:
#             print("Underage.")
#         elif age >= 18:
#             print("You are an adult and eligible to vote.")
# except ValueError as e:
#     print(f"Error: {e}")


# ---------------------------------------------------------------------   

#  check if a number is prime

# number = int(input("Enter a number to check if it is prime: "))
# is_prime = True
# for i in range(2, int(number ** 0.5) + 1):
#     if number % i == 0:
#         is_prime = False
#         break

# if is_prime:
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

# ---------------------------------------------------------------------

# count = 0
# list = []
# while count<10:
#     for i in range(count):
#         # print(count*2)
#         list.append(count)
#     count += 1

# print(list)


# for i in range(10):
#     for j in range(5):
#         print("i=",i+1," j=",j+1)

# ------------------------------------------------------------------

from funcFile import add, multiply, substract, divide

number1 = input("enter the number: ")
number2 = input("enter the number: ")


try:
    print(add(number1, number2))
except ValueError as e:
    print(f"Error: {e}")



