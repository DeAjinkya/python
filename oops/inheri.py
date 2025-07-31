# inheritance
#super class
class Animal:
    location = "india"
    def __init__(self,name):
        self.name = name

    def speak(self):
        print("animal sound")

#sub class
class Dog(Animal):
    def speak(self):
        super().speak() # calling parent class method
        print("woof!")

d = Dog("bruno")
d.speak()
print(d.location)