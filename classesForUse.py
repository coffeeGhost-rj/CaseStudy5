class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: ${self.salary}")

class Vendor(Employee):
    def __init__(self, name, service_type, rating):
        self.name = name
        self.service_type = service_type
        self.rating = rating
        super().__init__(name, "Vendor", 0)  # Vendors don't have a salary in this context 

    def display_info(self):
        print(f"Vendor Name: {self.name}, Service Type: {self.service_type}, Rating: {self.rating}/5")

# Creating an Employee object
emp_name = input("Enter employee name: ")
emp_position = input("Enter employee position: ")
emp_salary = float(input("Enter employee salary: "))
employee1 = Employee(emp_name, emp_position, emp_salary)

vendor_name = input("Enter vendor name: ")
vendor_service_type = input("Enter vendor service type: ")
vendor_rating = float(input("Enter vendor rating (out of 5): "))
vendor1 = Vendor(vendor_name, vendor_service_type, vendor_rating)


# Displaying employee information
employee1.display_info()
# Displaying vendor information
vendor1.display_info()


# create manager class that inherits from employee and has a method to give a raise to the employee
class Manager(Employee):
    def __init__(self, name, department, salary):
        super().__init__(name, "Manager", salary)
        self.department = department

    def give_raise(self, employee, amount):
        employee.salary += amount
        print(f"{employee.name} has been given a raise of ${amount}. New salary: ${employee.salary}")

    def display_info(self):
        print(f"Manager Name: {self.name}, Department: {self.department}, Salary: ${self.salary}") 

# Creating a Manager object
manager_name = input("Enter manager name: ")
manager_department = input("Enter manager department: ")
manager_salary = float(input("Enter manager salary: "))
manager1 = Manager(manager_name, manager_department, manager_salary)

# Displaying manager information
manager1.display_info() 

# Giving a raise to the employee
raise_amount = float(input(f"Enter raise amount for {employee1.name}: "))
manager1.give_raise(employee1, raise_amount)

# creating a clerk class that inherits from employee and has a method to calculate the total salary of all employees under the clerk
class Clerk(Employee):
    def __init__(self, name, department, salary):
        super().__init__(name, "Clerk", salary)
        self.department = department
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_salary(self):
        total_salary = sum(employee.salary for employee in self.employees)
        return total_salary

    def display_info(self):
        print(f"Clerk Name: {self.name}, Department: {self.department}, Salary: ${self.salary}")
        print(f"Total Salary of Employees under {self.name}: ${self.calculate_total_salary()}")

# Creating a Clerk object
clerk_name = input("Enter clerk name: ")
clerk_department = input("Enter clerk department: ")
clerk_salary = float(input("Enter clerk salary: "))
clerk1 = Clerk(clerk_name, clerk_department, clerk_salary)
clerk1.display_info()

# Adding employees to the clerk's list
clerk1.add_employee(employee1)

# shown polymorphism by creating a list of employees and calling the display_info method on each one
employees = [employee1, vendor1, manager1, clerk1]
for emp in employees:
    emp.display_info()


# loop through the employees list and check if the employee is a manager or a clerk and print their department
for emp in employees:
    if isinstance(emp, Manager):
        print(f"{emp.name} is a Manager in the {emp.department} department.")
    elif isinstance(emp, Clerk):
        print(f"{emp.name} is a Clerk in the {emp.department} department.")
    else:
        print(f"{emp.name} is an Employee with position: {emp.position}.")



