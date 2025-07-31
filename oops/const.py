# constructor

class Employee:
    
    def __init__(self,salary,name,bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"the name {self.name}, salary is {self.salary}, the bond is for {self.bond} years")

e = Employee(34000,"raj",4)
print(e.get_salary())
e.get_info()
