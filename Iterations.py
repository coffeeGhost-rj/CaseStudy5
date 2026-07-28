Nostart = int(input("Enter the starting number: "))
Nend = int(input("Enter the ending number: "))
multiplier = int(input("Enter the multiplier: "))   

# do-while loop to print the multiples of the multiplier from Nostart to Nend
# while True:
#     for i in range(Nostart, Nend + 1):
#         if i % multiplier == 0:
#             print(i)
#     choice = input("Do you want to continue? (y/n): ")
#     if choice.lower() != 'y':
#         break

for i in range(Nostart, Nend + 1):
    if i % multiplier == 0:
        print(i)