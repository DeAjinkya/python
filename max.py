a = 10
b = 20

print(max(a,b))

#or

print(a if a>b else b)

#or

if a>b:
    print(a)
else:
    print(b)

#or

num = [a,b]
num.sort()
print(num[-1])