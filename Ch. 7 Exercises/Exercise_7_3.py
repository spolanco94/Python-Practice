##### Ask the user for a number, then report if it is a multiple of 10.
multiple_of_ten = input("Give me a number and I'll tell you if it is a multiple"
" of ten! ")
multiple_of_ten = int(multiple_of_ten)
if multiple_of_ten % 10 == 0:
    print(f"The number {multiple_of_ten} is a multiple of ten!")
else:
    print(f"Sorry, {multiple_of_ten} is not a multiple of ten.")
