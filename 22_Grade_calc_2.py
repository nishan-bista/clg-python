#6 program which accepts marks for four subjects and display total , marks , percentage andf grade.


first_sub = int(input("Enter Marks of first subject : "))
second_sub = int(input("Enter Marks of second subject : "))
third_sub = int(input("Enter Marks of third subject : "))
fourth_sub = int(input("Enter Marks of fourth subject : "))

total_marks = first_sub + second_sub + third_sub + fourth_sub
percentage = (total_marks * 100)/ 400

def func_grade(x):
    if x>70:
        return("distinction")
    elif x>40 and x<70:
        return ("pass")
    else:
        return ("fail")
    
grade_output= func_grade(percentage)
    
print(f"Your Total marks is {total_marks}\nYour Percentage is {percentage}\nYour Grade is {grade_output}% ! ")