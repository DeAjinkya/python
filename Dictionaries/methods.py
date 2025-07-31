# methods

marks = {"bro":90,"lily":89,"raj":78}

print(marks.keys()) #dict_keys(['bro', 'lily', 'raj'])

print(marks.values()) #dict_values([90, 89, 78])

print(marks.items()) #dict_items([('bro', 90), ('lily', 89), ('raj', 78)])

marks.pop("bro")
print(marks) # {'lily': 89, 'raj': 78}

marks.clear()
print(marks) # {}