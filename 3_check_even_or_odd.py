#to check the number is even or odd 

number = int(input("Enter Number to check even or odd : "))
check  = number/2 
if check == 0:
    print(f"{number} is an even Number!")
else:
    print(f"{number} is an odd Number!")