##### Add at least 3 pizzas to a list, and use a for loop to print the name of each pizza
pizzas = ["margherita", "pepperoni", "sausage", "bianca"]

for topping in pizzas:
    print(topping.title())

##### Modify your for loop to print a sentence using the pizza rather than just the name of the pizza
for topping in pizzas:
    print(f"I LOVE {topping.title()} pizza! Have you ever tried it?")

##### Add a line at the end of your program, outside the for loop, that states how much you love pizza
for topping in pizzas:
    print(f"I LOVE {topping.title()} pizza! Have you ever tried it?")

print("I guess I'm just a glutton for pizza, huh?")