# 31. Accept the age, sex('M', 'F'), number of days and display the wages accordingly.
# Age                    Sex    Wage/day
# >=18 and <30             M      700
#                          F      750
# >=30 and <=40            M      800
#                          F      850

age = int(input("Enter Age : "))
sex = input("Enter sex, 'm' for Male 'f' for female : ")
days = int(input("Enter the days worked : "))


def male(a):
    if a>=18 and a<30:
        return 700
    elif a >=30 and a <=40:
        return 800
    else:
        return "Eror Input"
    
def female(b):
    if b>=18 and b<30:
        return 750
    elif b >=30 and b <=40:
        return 850
    else:
        return "Eror Input"
    

final_m = male(age) * days
final_f = female(age)* days

if sex =="m":
    print(f"The wage of {age , sex} is {final_m}")
elif sex =="f":
    print(f"The wage of {age , sex} is {final_f}")
else:
    print("ERROR! You must have enter something Wrong!")