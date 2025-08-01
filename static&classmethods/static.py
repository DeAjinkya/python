# static method
class Employee:
    company = "hp"

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    #instance method
    def print_info(self):
        info = f"the name is {self.name} and the salary is {self.salary}"
        print(info)

    @staticmethod
    def sum(a,b):
        return a+b

e = Employee("lily",10000)
e.print_info()

print(e.sum(2,3))