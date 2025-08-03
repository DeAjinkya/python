# walrus operator

def very_slow():
    print("something....")
    print("something....")
    print("something....")
    return 17

# a = very_slow()
# if (a>10):
#     print(a)
# else:
#     print("not")

#or
if ((a:=very_slow())>10):
    print(a)
else:
    print("not")