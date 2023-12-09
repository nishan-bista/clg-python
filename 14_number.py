#display months

week_no = int(input("Enter a number to number of month : "))
match week_no:
    case 1: print("January")
    case 2: print("February")
    case 3: print("March")
    case 4: print("April")
    case 5: print("June")
    case 6: print("July")
    case 7: print("August")
    case _: print("Invalid number of day in week")
    