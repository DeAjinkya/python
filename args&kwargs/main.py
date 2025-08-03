# *args

def sum(*args):
    total = 0
    for item in args:
        total += item
    return total

print(sum(1,2,3,4,5))