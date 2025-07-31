# decorator with arguments

def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(5)
def say_hii(a):
    print(f"hiii {a}")

say_hii("Ajinkya")

"""
def decorator(say_hii):
        def wrapper(a):
            for i in range(n):
                say_hii(a)
        return wrapper
"""

"""
for i in range(5):
      say_hii("Ajinkya")
"""
