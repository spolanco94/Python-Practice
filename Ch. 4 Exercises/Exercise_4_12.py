##### Take a version of 'foods.py' from chapter 4 and use two for loops to print
##### each element instead of the lists
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
for val in my_foods:
    print(val.title())

print("\nMy friend's favorite foods are:")
for val in friend_foods:
    print(val.title())
