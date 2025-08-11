# calculate area and circumference of circle using class

import math
radius = 5

class circle():
    def getArea(self):
        return math.pi*radius*radius

    def getcircumference(self):
        return radius*2*math.pi


c = circle()
print("radius = ",radius)
print("area = ",c.getArea())
print("circumference = ",c.getcircumference())
