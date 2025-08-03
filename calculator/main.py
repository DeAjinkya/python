try:
    a = int(input("enter the first number: "))

    b = int(input("enter the second number: "))

    print("what kind of operation do u want to perform. press + for  addition\n press - for  subtraction\n press / for  division\n press * for  multiplication")

    O = input("enter operation: ")

    match O:
        case "+":
            print(f"the result is: {a+b}")
        case "-":
            print(f"the result is: {a-b}")
        case "/":
            print(f"the result is: {a/b}")
        case "*":
            print(f"the result is: {a*b}")
        case _:
            print("error in operation")



except:
    print("error")
