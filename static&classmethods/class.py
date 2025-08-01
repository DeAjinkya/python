# class method
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
    
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company


e = Employee("jack",20000)
print(Employee.company)
e.change_company("google")
print(Employee.company)
