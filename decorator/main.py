# Decortor 
# is a function that takes a function.
# it creates a new function inside its body(wrapper)
# the it returns that new function

def decorator(func):
    def wrapper():
        print("going too ....")
        func()
        print("done..")
    return wrapper

@decorator
def say_hii():
    print("hiii")

"""
def d():
    print("going too ....")
    print("hiii")
    print("done..")

"""

# d = decorator(say_hii)
# d()

say_hii()