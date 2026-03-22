a = int(input("Enter a bigger number "))
b = int(input("Enter a smaller number "))
def add(a,b):
    print(a+b)
def subtract(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def division(a,b):
    print(a/b)
p = input("Which operation do you want to perform? add, subtract, multiply, division KINDLY NOTE - plz enter the correct spelling and the name of the operation")
if p == 'add' or p == 'Add':
    add(a,b)
elif p == 'subtract' or p == 'Subtract':
    subtract(a,b)
elif p == 'multiply' or p == 'Multiply':
    multiply(a,b)
elif p == 'division ' or p == 'Division':
    division(a,b)
else:
    print("invalid input") 