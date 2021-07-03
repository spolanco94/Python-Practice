# Write a loop that ask users for their age and informs them of theater ticket
# costs. < 3 = free, 3 - 12 = $10, 12 and over = $15
age = None

while age == None:
    print(f"Welcome to Awesome Movie Theaters. Tickets are free for anyone"
    ", $10 for anyone ages 3 to 12 and $15 for anyone over 12. ")
    age = input("What is your age? ")
    age = int(age)

    if age >= 12:
        print("That will be $15 for your ticket.")
    elif age >= 3:
        print("That will be $10 for your ticket.")
    else:
        print("There will be no fee for your ticket.")

print("Please enjoy your film!")
