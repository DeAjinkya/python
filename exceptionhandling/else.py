# else 

try:
    a = 34/0

except Exception as e:
    print(e)

# else part will run when no error in try code
else:
    print("hiii")