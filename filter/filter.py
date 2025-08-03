# filter

def is_greater(x):
    if x>9:
        return True
    else:
        return False
    
a = [1,2,3,4,9,12,32]

new = list(filter(is_greater,a))
print(new)