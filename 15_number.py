#accept city and display monument

user_input = str(input("Enter city name : "))
user_input = user_input.lower()
cities = {
    "city":"monument",
    "delhi":"red fort",
    "agra":"taj mahal",
    "jaipur":"jal mahal"

}
if user_input == "city":
    print(cities["city"])
elif user_input == "delhi":
    print(cities["delhi"])
elif user_input == "agra":
    print(cities["agra"])
elif user_input == "jaipur":
    print(cities["jaipur"])
else:
    print("City not found, Enter valid city! ")

