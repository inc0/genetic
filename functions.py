import math

def add(a, b):
    return a+b
add.num_args = 2
add.symbol = "+"

def subtract(a, b):
    return a-b
subtract.num_args = 2
subtract.symbol = "-"

def multiply(a, b):
    return a*b
multiply.num_args = 2
multiply.symbol = "*"

def divide(a, b):
    return a / b
divide.num_args = 2
divide.symbol = "/"

def square_root(a):
    return math.sqrt(abs(a))
square_root.num_args = 1
square_root.symbol = "sqrt"

def power(a, b):
    return math.pow(a, round(b))
power.num_args = 2
power.symbol = "^"

def greater_than(a, b, yes, no):
    if a > b:
        return yes
    else:
        return no
greater_than.num_args = 4
greater_than.symbol = ">"

def lesser_than(a, b, yes, no):
    if a < b:
        return yes
    else:
        return no
lesser_than.num_args = 4
lesser_than.symbol = "<"

func_list = [add, subtract, multiply, divide, square_root, power, greater_than, lesser_than]
