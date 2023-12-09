#To display 7 days of week.

week_no = int(input("Enter a number to find day in week : "))
match week_no:
    case 1: print("Sunday")
    case 2: print("Monday")
    case 3: print("Tuesday")
    case 4: print("Wednesday")
    case 5: print("Thursday")
    case 6: print("Friday")
    case 7: print("Saturday")
    case _: print("Invalid number of day in week")
    