##### Write a program asking user for their selection of a rental car
car = input("What car would you like to rent today? ")

if car[-1] == "s":
    print(f"Let me see if we have any {car.title()}' in stock today. One moment"
    "please.")
elif car == "bmw":
    print(f"Let me see if we have any {car.upper()}'s in stock today. One moment"
    "please.")
else:
    print(f"Let me see if we have any {car.title()}'s in stock today. One moment"
        "please.")
