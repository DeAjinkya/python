# variable scope
def sum(a,b):
    # a and b are local variables
    c = a+b
    print(z)
    return c

def greet():
    z = 44 # local variable
    print("hello")

z = 8 # global variable
print(sum(2,2))
# print(c)
greet()