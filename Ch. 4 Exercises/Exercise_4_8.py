##### Create an empty list and append to it the first 10 cubed values (from 1 to 10), and then print it out
cubed = []

for num in range(1, 11):
    cubed.append(num**3)

for val in cubed:
    print(val)