# function arguments

# positional arguments
def add(a,b):
    return a+b

c = add(2,2)
print(c)

# default arguments

def sub(x,y,plus=2):
    return x-y-plus

o2 = sub(2,3)
print(o2)

# plus can be overwriten
print(sub(5,2,1))

# keyword arguments
print(add(b=10,a=20))