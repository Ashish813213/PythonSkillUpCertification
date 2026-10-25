# Method overriding: SalesEmployee.get_info adds the sales field to the output.
class Employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary

    def get_info(self):
        return "EmployeeID:{} Salary:{}".format(self.id, self.salary)


class SalesEmployee(Employee):
    def __init__(self, id, salary, sales=0):
        super().__init__(id, salary)
        self.sales = sales

    def get_info(self):
        return "EmployeeID:{} Salary:{} Sales:{}".format(
            self.id, self.salary, self.sales
        )
