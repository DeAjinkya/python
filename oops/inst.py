# instance and class attribute

class Employee:
    company = "Asus" #this is class attribute
    age = 34

    def __init__(self,name,company):
        self.name = name
        self.company = company

e = Employee("raj","tesla")
print(e.company) # will always print instance attribute whenever present

print(e.age)

# object introspection
print(dir(e))

print(Employee.company) # this will always print class attribute