# 34. Accept input from user
# if given number is a multiple of both 3 and 5 prints "FizzBuzz" instead of number

# if  given number is a multiple of 3 but not 5 prints "Fizz" instead of number

# if given number is a multiple of 5 but not 3 prints "Buzz" instead of number

# if given number is not multiple of 3 or 5 prints value as usual. 

user_input_1 = int(input("Enter first number : "))
user_input_2 = int(input("Enter second number : "))

def div3(x):
    if x%3==0:
        return True
    else:
        return False
    
def div5(z):
    if z%5==0:
        return True
    else:
        return False
    
if div3(user_input_1) and div5(user_input_2) is True:
    print("FizzBuzz")
elif div3 is True and div5 is  not True:
    print("Fizz")
elif div5 is True and div3 is not True:
    print("Buzz")
else:
    print(f"{user_input_1}, {user_input_2} Both is not divisble by both")
    
