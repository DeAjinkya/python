name = "Ajinkya"

# string is immutable

# name[0] = "R" #TypeError: 'str' object does not support item assignment

# returns the length of the string
a = len(name)
print(a)

b = "hello world!"
print(b)

print(b.upper()) # HELLO WORLD!
print(b.lower())
print(b.title()) # Hello World!
print(b.capitalize()) # Hello world!

# removing whitespace
n = " bro code "
print(n.strip()) #bro code
print(n.lstrip())#"bro code "
print(n.rstrip()) #" bro code"

# finding and replacing
n1 = "bro hiii"
print(n1.find("bro")) # 0 
print(n1.replace("bro","hello")) #hello code

# splitting and joining
text = "Apples,Bananas,Pineapples"
print(text.split(","))
print(",".join(['Apples', 'Bananas', 'Pineapples']))

# checking string properties
age = "hiii"
print(age.isalpha()) # true 
print(age.isdigit()) # false
print(age.isalnum()) # true
print(age.isspace()) # false