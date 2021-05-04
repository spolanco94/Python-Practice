##### Using the program from exercise 4-1, make a copy of the list of pizzas and
##### call it friend_pizzas.
#####       1. Add a new pizza to the ORIGNAL list
#####       2. Add a different pizza to the list friend_pizzas
#####       3. Print both lists with a message to show they are different

pizzas = ["margherita", "pepperoni", "sausage", "bianca"]
friend_pizzas = pizzas[:]

pizzas.append("chicken and bacon")
friend_pizzas.append("veggie")

print("My favorite pizza's are:")
for val in pizzas:
    print(val.title())

print("\nMy friend's favorite pizza's are:")
for val in friend_pizzas:
    print(val.title())