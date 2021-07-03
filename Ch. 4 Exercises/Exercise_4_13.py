##### Add 5 foods to a tuple, use a for loop to print out each item
buffet = ("hot dogs", "fried chicken", "pasta", "roasted vegetables",
"creme caramel")
print("For the winter menu, we have:")
for val in buffet:
    print(val.title())

##### Try to modify one item to ensure Python catches and rejects the change
# buffet[3] = "mac and cheese"

##### The restaraunt changed its menu, replacing 2 items in the orignal list.
##### Rewrite the tuple and print each item
buffet = ("grilled salmon", "fried chicken", "mashed potatoes",
"roasted vegetables", "creme caramel")
print("\nFor the summer menu, we have:")
for val in buffet:
    print(val.title())
