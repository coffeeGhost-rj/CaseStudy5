fruits = {"apple", "banana", "cherry"}
fruits.add("mango")
print("After add:", fruits)

fruits.remove("banana")
print("After remove:", fruits)

fruits.discard("grape")
print("After discard (element not present):", fruits)

fruits.clear()
print(fruits)
print(len(fruits))

if not fruits:
    print("empty")
else:
    print("not empty")
    
fruits.add("element")    
set_b = {3, 4, 5, 6}

print(fruits | set_b)


list1 = [1, 2, 3, 4, 5, 3, 2]
list2 = [3, 4, 5, 6, 7, 4, 5]

print(set(list1) & set(list2))

text = "the cat sat on the mat the cat"

words = text.lower().split()
unique_words = set(words)

print("Unique word count:", len(unique_words), "\n", unique_words)

tags = {"python", "set", "programming", "tutorial"}

result = " ".join(sorted(tags))

print(result)

sqNo = {x**2 for x in range(1, 21) if x%2==0}
print(sorted(sqNo))


student = {"name": "Alice", "age": 20, "grade": "B"}
student["city"]="Pune"
student["age"]=21
print("Details: ", student)

car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}

# Remove a key
car.pop("color")
print(car)

# Get all key-value pairs
print(car.items())

# Check key existence
print("'brand' exists:", "brand" in car)
print("'color' exists:", "color" in car)

keys = ["name", "age", "city"] 
values = ["Bob", 25, "London"]

dict1213 = dict(zip(keys, values))
print(dict1213)

person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}

print(person["address"]["city"])


keys = ["math", "science", "english", "history"]
default = 0

scores = dict.fromkeys(keys, default)
print(scores)

employee = {"fname": "John", "age": 30, "dept": "Engineering"}

employee["first_name"] = employee.pop("fname")
print(employee)

user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}
keys_to_keep = ["id", "username", "email"]

subset = {k: user[k] for k in keys_to_keep}
print(subset)

text = "hello world"

# collections.Counter(text)

freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

print(freq)

