import math

x = int(input("enter number"))
y = int(input("enter number"))

a = input("enter what you want to do to the numbers")

def calc(x, y, a):
    if a == "+":
        return(x + y)
    elif a == "-":
        return(x - y)
    elif a == "/":
        return(x / y)
    elif a =="*":
        return(x * y)

print(calc(x, y, a))
