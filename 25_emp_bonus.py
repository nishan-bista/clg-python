# 12. A company decided to give bonus to employee according to following criteria:
# Time period of service     Bonus
# More than 10 years            10%
# >=6 and <=10                     8%
# Less than 6 years               5%

emp_salary = int(input("Enter Employee Salary : "))
emp_y = int(input("Enter Employee year at work : "))

def emp_a(x,y):
    if x>10:
        return (10/100)*y
    elif x>=6 and x<=10:
        return (8/100)*y
    elif x<6:
        return (5/100)*y
    else:
        return ("Invalid Input!")
    
final = emp_a(emp_y,emp_salary)
bonus_salary = final + emp_salary


print(f"The bonus is Rs {final},\nThe Salary with bonus is Rs {bonus_salary}")

