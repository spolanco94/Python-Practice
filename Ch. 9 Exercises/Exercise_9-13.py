# Make a class Die with one attribute called 'sides' which has a default value
# 6. Write a method called roll_die() that prints a random number between 1 and
# the number of sides the die has. Make a 6 sided, 10 sided and 20 sided die and
# roll each 10 times.
from die import Die

die = Die()
ten_die = Die(10)
twenty_die = Die(20)

count = 0
print("Normal:")
while count < 10:
    die.roll_die()
    count += 1

count = 0
print("Ten sided:")
while count < 10:
    ten_die.roll_die()
    count += 1

count = 0
print("Twenty sided:")
while count < 10:
    twenty_die.roll_die()
    count += 1
