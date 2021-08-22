##### Add at least 3 different animals into a list and print the names of each using a for loop
mischievous_animals = ["fox", "shiba", "raccoon", "cat"]

for animal in mischievous_animals:
    print(animal.title())

##### Modify your program to print a statement about each animal
for animal in mischievous_animals:
    if animal[-1] == "x":
        print(f"{animal.title()}es are pretty mishievous aren't they?")
    else:
        print(f"{animal.title()}'s are pretty mishievous aren't they?")
