# command line utilities
# argparse module

import argparse

parser = argparse.ArgumentParser(description="simple calculator")

parser.add_argument("num1", type=float, help="first number")
parser.add_argument("num2", type=float, help="second number")
parser.add_argument("operation", choices=["add","mul","div","sub"], help="operation to perform")

args = parser.parse_args()

print(args)

if (args.operation == "add"):
    print(args.num1 + args.num2)
elif (args.operation == "sub"):
    print(args.num1 - args.num2)
elif (args.operation == "mul"):
    print(args.num1 * args.num2)
elif (args.operation == "div"):
    print(args.num1 / args.num2)
else:
    print("error")