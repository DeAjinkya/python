# map() function

n = [1,2,3,4,5,6]

def square(x):
    return x*x

new = list(map(square,n))
print(new)