# class : class is a blueprint or a template. eg. form for an exam that contains name,age,electives,father'name etc

# object : specific instance created from the template (class). eg. form which contains the data for Raj

class Employee:
    company = "HP"

    def get_salary(self): # self is important here because self is a way to reference the object of class which is being created
        return 34000

e = Employee() # an object of class employee is created here
print(e.get_salary()) # employee get salary method is called
print(e.company)
