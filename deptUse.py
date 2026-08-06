from dept import *
from classesForUse import *

# dpname = input("Enter the dpet name : ")
# dpFloor = input("Enter the dpet location : ")
# try: 
#     deptObj = Department(dpname, dpFloor)
#     empObj = Employee("BOB", "Compliance", "2000", deptObj)
 
#     # deptObj2 = Department("Legal", "3rd Floor")

#     print(empObj.displayInfo())
#     # print(deptObj2.showDeptDetails())
#     print(deptObj.showDeptDetails())
# except ValueError as e:
#     print(e)

# --- Execution Script ---
dpname = input("Enter the dept name: ")
dpFloor = input("Enter the dept location: ")
street = input("Enter the street: ")
city = input("Enter the city: ")
pincode = input("Enter the pincode: ")

try: 
    empAddr = Address(street, city, pincode)
    # 1. Instantiate the Department object
    deptObj = Department(dpname, dpFloor)
    
    # 2. Pass the Department object inside the Employee constructor
    empObj = Employee("BOB", "Compliance", "2000", deptObj)
    
    print(empAddr.showAdd())
 
    # 3. Print outputs
    print("\n--- Employee Info ---")
    print(empObj.displayInfo())
    
    print("\n--- Department Info ---")
    print(deptObj.showDeptDetails())

except ValueError as e:
    print(f"Validation Error: {e}")