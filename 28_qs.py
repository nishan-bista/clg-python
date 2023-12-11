# 14. Accept the number of days from the user and calculate the charge for library according to following:
# Till five days: Rs 2/day
# Six to ten days: Rs 3/day
# 11 to 15 days: Rs 4/day
# After 15 days: Rs 5/day


days = int(input("Enter Days : "))

def lib(x):
    if x<=5:
        return x* 2
    elif x>6 and x<=10:
        return x * 3
    elif x>=11 and x<15:
        return x * 4
    elif x>15:
        return x*5
    else:
        return("Invalid Input! ")  
    
tt = lib(days)
print(f"Your charge for {days} days is Rs {tt}")
