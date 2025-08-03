# custome error
# raising error

a = int(input("enter a number: "))
b = int(input("enter a number: "))

if b == 0:
    raise ValueError("do not divide 0")

print(f"the sum is {a/b}")
