# methods of list
l2 = [10,11,12,13,14]
l1 = [1,2,3,4,5,6,7,8]
print("before",l1)

l1.append(9)
print(l1)

l1.extend(l2)
print(l1)

l1.pop()
print(l1)

l1.remove(10)
print(l1)

#         index 
#         |  value
l1.insert(10,10)
print(l1)

l1.sort()
print(l1)

l1.reverse()
print(l1)
