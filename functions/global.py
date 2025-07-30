# global keyword
def sum(a,b):
    print("hiii")
    c = a+b
    global z # modify the global z
    z = 0 # now this global variable
    return c

z = 3
print(sum(3,4))
print(z)
