class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        combined_salary = self.salary + other.salary
        return f"Combined salary: {combined_salary}"

    def __sub__(self, other):
        salary_difference = abs(self.salary - other.salary)
        return f"Salary difference: {salary_difference}"

# User Input
name1 = input("Enter the name of first employee: ")
salary1 = float(input("Enter the salary of first employee: "))
emp1 = Employee(name1, salary1)

name2 = input("Enter the name of second employee: ")
salary2 = float(input("Enter the salary of second employee: "))
emp2 = Employee(name2, salary2)

print(emp1 + emp2)  # Combine salaries
print(emp1 - emp2)  # Compare salary differences
