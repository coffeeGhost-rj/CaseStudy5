fruits = ("apple", "banana", "cherry", "date")
print(fruits[0], fruits[-1], len(fruits))

a=(1,2,3) 
b=(4,5,6)
print(a+b)

items = (1, 2, 3, 4, 5)
print("".join(fruits))

votes = ("yes", "no", "yes", "yes", "no", "yes")

print(votes.count("yes"))
print(votes.count("no"))

person = ("Alice", 30, "Engineer", "Pune")

name, age, job, city = person

print(name, age, city, job)
name, age = age , name

print(name, age, city, job)

matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

print(matrix[1][2])

scores = (88, 95, 70, 62, 99, 74, 85)

print(sum(scores), max(scores), min(scores))

students = (("Alice", 88), ("Bob", 73), ("Charlie", 95), ("Diana", 61))

print(sorted(students,key= lambda x:x[1],reverse=True))

numbers = (3, 14, 7, 22, 9, 41, 18, 5)
filtered = tuple( x for x in numbers if x>10)
print(filtered)

numbers = (1, 2, 3, 4, 5, 6)
squared = tuple(x**2 for x in numbers)
print(squared)

keys = ("name", "age", "city")
values = ("Alice", 30, "Pune")

dictiosdsf = dict(zip(keys,values))
print(dictiosdsf)

t1 = (1, 2, 3, 4, 5, 6)
t2 = (4, 5, 6, 7, 8, 9)

t3 = tuple(x for x in t1 if x in t2)
print(t3)