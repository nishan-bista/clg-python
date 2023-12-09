#8 Wap  to accept the cost of a bike and display the road tax to be paid.


bike_price = int(input("Enter the Price of bike : "))

if bike_price>1000000:
    a =int(15)
elif bike_price>500000 and bike_price<100000:
    a = int(10)
elif bike_price<=50000:
    a = int(5)

tax_money= (a/100) * bike_price

def bike_tax(tax):
    if tax>15:
        return (f"You need to pay road tax of Rs {tax}")
    elif tax>10 and tax <15:
        return (f"You need to pay tax of Rs {tax}")
    elif tax<=5:
        return(f"You need to pay tax of Rs {tax}")
    else:
        return("The value you entered is not able to be calculated")
print(bike_tax(tax_money))