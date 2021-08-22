# Write a program that takes in 2 numbers and adds them together. Catch a
# potential ValueError exception that may be thrown in the case of text being
# inputted instead of a number.

print("Feed me 2 numbers and I will add them together for you.\n"
        "Enter 'q' at any time to quit.")

while True:

    number_1 = input("Give me the first number: ")
    if(number_1.lower() == 'q'):
        break

    number_2 = input("Give me the second number: ")
    if(number_2.lower() == 'q'):
        break

    try:
        number_1 = int(number_1)
        number_2 = int(number_2)
    except ValueError:
        print("Sorry, one of the values you entered is not a number.")
    else:
        print(number_1 + number_2)
