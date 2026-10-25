# Inheritance: Employee (id, salary) and SalesEmployee subclass that adds sales.
class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary


class SalesEmployee(Employee):
    def __init__(self, id, salary, sales):
        super().__init__(id, salary)
        self.sales = sales
