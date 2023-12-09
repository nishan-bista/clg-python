#11 Accept the percentage from user and display the grade.


user_input = int(input("Enter your percentage : "))

def func_grade(x):
    if x>80 and x<100:
        return(f"Your Grade is A+ with {x}%")
    elif x>60 and x<80:
        return (f"Your Grade is A with {x}%")
    elif x>50 and x<60:
        return (f"Your Grade is B+ with {x}%")
    elif x>45 and x<50:
        return (f"Your Grade is B with {x}%")
    elif x>25 and x<45:
        return (f"Your Grade is C with {x}%")
    elif x<25:
        return ("You have failed  ")
    else:
        return("Enter valid Percentage!")
    
print(func_grade(user_input))