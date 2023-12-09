#program to accept two number and mathematical operator and perform operation

first_number = int(input("Enter first number : "))
math_op = input("Enter operator you want to perform : ")
second_number = int(input("Enter second number : "))



def addition(a,b):
    return a+ b
def minus(a,b):
    return a-b
def mult(a,b):
    return a*b
def division(a,b):
    return a/b

if math_op == "+":
    print(addition(first_number,second_number))
elif math_op =="-":
    print(minus(first_number,second_number))
elif math_op =="*":
    print(mult(first_number,second_number))
elif math_op =="/":
    print(division(first_number,second_number))
else:
    print("Invalid mathematial operator!")


