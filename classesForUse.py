class Employee:
    def __init__(self, name, position, salary, dept):
        self.name = name
        self.position = position
        self.salary = salary
        self.setDept(dept)

    # def display_info(self):
    #     print(f"Name: {self.name}, Position: {self.position}, Salary: ${self.salary}")
    
    def displayInfo(self):
        return f"Name : {self.name}, Positon : {self.position}, Salary : {self.salary}, Dept : {self.department.deptname}"
    
    def setDept(self, deptObj):
        """
        Purpose: self
        """
        self.department = deptObj
    # end def

# class Vendor(Employee):
#     def __init__(self, name, service_type, rating):
#         self.name = name
#         self.service_type = service_type
#         self.rating = rating
#         super().__init__(name, "Vendor", 0)  # Vendors don't have a salary in this context 

#     def display_info(self):
#         print(f"Vendor Name: {self.name}, Service Type: {self.service_type}, Rating: {self.rating}/5")


# create manager class that inherits from employee and has a method to give a raise to the employee
# class Manager(Employee):
#     def __init__(self, name, department, salary):
#         super().__init__(name, "Manager", salary)
#         self.department = department

#     def give_raise(self, employee, amount):
#         employee.salary += amount
#         print(f"{employee.name} has been given a raise of ${amount}. New salary: ${employee.salary}")

#     def display_info(self):
#         print(f"Manager Name: {self.name}, Department: {self.department}, Salary: ${self.salary}") 


# creating a clerk class that inherits from employee and has a method to calculate the total salary of all employees under the clerk
# class Clerk(Employee):
#     def __init__(self, name, department, salary):
#         super().__init__(name, "Clerk", salary)
#         self.department = department
#         self.employees = []

#     def add_employee(self, employee):
#         self.employees.append(employee)

#     def calculate_total_salary(self):
#         total_salary = sum(employee.salary for employee in self.employees)
#         return total_salary

#     def display_info(self):
#         print(f"Clerk Name: {self.name}, Department: {self.department}, Salary: ${self.salary}")
#         print(f"Total Salary of Employees under {self.name}: ${self.calculate_total_salary()}")


