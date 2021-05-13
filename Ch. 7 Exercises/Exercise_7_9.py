# Use the list from 7-8 and add pastrami to it 3 times. Make a message stating
# that there is no pastrami and iterate through sandwich_orders to remove them
finished_sandwiches = []
sandwich_orders = ["ham and cheese melt", "pastrami", "pastrami", "grilled "
"cheese", "tuna sandwich", "philly cheesesteak", "pastrami", "blt", "grilled "
"chicken club"]

print("Apologies for the inconvenience, but the deli has run out of pastrami.\n")
print(sandwich_orders)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == "blt":
        print(f"Now making {current_sandwich.upper()}... Done!")
    else:
        print(f"Now making {current_sandwich}... Done!")
    
    finished_sandwiches.append(current_sandwich)

print(finished_sandwiches)
print("\nHere are all the sandwiches that have been completed: ")
while finished_sandwiches:
    completed = finished_sandwiches.pop()
    if completed == "blt":
        print(f"\t{completed.upper()}")
    else:
        print(f"\t{completed.title()}")