# string formatting

template = "Dear {}, u are awesome. take this {}$ dollers."

a = "john"
a1 = 1000
b = "jack"
b1 = 2000
c = "marie"
c1 = 1500

s1 = template.format(a,a1)
print(s1)

#fstring
print(f"{b} u are awesome and take this {b1}$ money")