class office:
    no_of_employees = 0
    def __init__(self, name):
        self.name = name
        self.employees = []
    def add_employee(self, emp):
        self.no_of_employees += 1
        self.employees.append(emp)
        print(f"Employee {emp.name} added to office {self.name}. Total employees: {self.no_of_employees}")
    def get_all_employees(self):
        return self.employees
    def __str__(self):
        return f"Office Name: {self.name}, Number of Employees: {self.no_of_employees} \n\n"