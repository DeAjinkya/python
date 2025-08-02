# errors
while True:
    try:
        a = int(input("enter a number: "))
        b = int(input("enter a number: "))

        print(f"the sum is {a+b}")
    
    except ValueError:
        print("value error")

    except ZeroDivisionError:
        print("zero error")
        
    except Exception as e:
        print("error",e)