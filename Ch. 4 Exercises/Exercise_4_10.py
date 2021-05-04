##### Using a program from a previous exercise, complete the following:
#####       1. Print the message 'The first three items are: ' and use a slice to print the first three items
#####       2. Print the message 'Three items from the middle are: ' and use a slice again to print 3 items from the middle
#####       3. Print the message 'The last three items are: ' and use a slice again to print 3 items from the end of the list

cubed = [num**3 for num in range(1, 11)]

print("The first three items are:")
for num in cubed[:3]:
    print(num)

print("\nThree items from the middle are:")
for num in cubed[4:7]:
    print(num)

print("\nThe last three items are:")
for num in cubed[-3:]:
    print(num)