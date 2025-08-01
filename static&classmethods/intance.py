# intance method(default method)
class Employee:
    company = "hp"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    #intance method
    def print_info(self):
        info = f"the name is {self.name} and the salary is {self.salary}"
        print(info)

e = Employee("lily",10000)
e.print_info()