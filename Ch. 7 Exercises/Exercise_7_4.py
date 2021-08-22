# Write a while loop that prompts the user to enter a series of pizza toppings
# until they enter a 'quit' value. Print a message verifying that the topping
# will be added.

# Initialize empty list to track requested toppings, order total to track cost
# of toppings, and a dictionary of available toppings with their prices.
pizza_toppings = []
order_total = 0.00
available_toppings = {
    "pepperoni" : 2.00,
    "mushrooms" : 1.00,
    "olives" : 1.00,
    "bacon" : 1.50,
    "extra cheese" : 2.00,
    "anchovies" : 1.50,
    "spinach" : 1.00,
    "peppers" : 1.00,
    "tomatoes" : 1.00,
    "sausage" : 2.00,
    "chicken" : 2.00,
}
# Print welcome message.
print("Welcome to pizza world! What kind of pizza can I help you make today?")

# Loop goes on until user enters 'done', other wise they will continually be
#### prompted for more toppings. --- refactor as a separate function
while True:
    requested_topping = input("Please let me know what toppings you would like. "
    "When you're done, please let me know by entering 'done'. ")
    requested_topping = requested_topping.lower()

    # Check if user has input 'done' and break out of loop if true
    if requested_topping == 'done':
        break
    else:
        # Check if the requested topping is in the dictionary of available
        # toppings and feedback outcome to user
        print(f"Adding {requested_topping} to your pizza now...")

        for available, price in available_toppings.items():
            if requested_topping not in  available_toppings.keys():
                print(f"Sorry, we do not have any {requested_topping}. Can I "
                "get you anything else?")
                break
            elif requested_topping == available:
                # if topping is found, add its value to order total.
                pizza_toppings.append(requested_topping)
                order_total = order_total + available_toppings[available]
                print("Done!")
                break

print("So the pizza you ordered will have the following toppings:")
for topping in pizza_toppings:
    print(f"\t{topping.title()}")

# Confirm with user if the order is correct
verification = input("Is this correct? (y/n) ")
if verification.lower() == "y":
    final_total = order_total + 9.00
    format_final = "{:.2f}".format(final_total)
    print(f"Okay! So your final total will be ${format_final}.\nThank you for "
    "coming to Pizza World. We hope to serve you again soon!")
else:
    #### Rewrite to call either add_toppings or remove_toppings functions
    print("We're sorry to hear that! Please start over again.")
