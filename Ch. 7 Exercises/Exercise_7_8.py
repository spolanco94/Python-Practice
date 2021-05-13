# Make a list named sandwich_orders and an empty list named finished_sandwiches.
# Simulate the completion of each sandwich, moving them from sandwich_orders to
# finished_sandwiches. Print a message with each iteration, and one final
# message with listing all sandwiches.
finished_sandwiches = []
sandwich_orders = ["ham and cheese melt", "grilled cheese", "tuna sandwich",
"philly cheesesteak", "blt", "grilled chicken club"]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == "blt":
        print(f"Now making {current_sandwich.upper()}... Done!")
    else:
        print(f"Now making {current_sandwich}... Done!")
    
    finished_sandwiches.append(current_sandwich)

print("\nHere are all the sandwiches that have been completed: ")
while finished_sandwiches:
    completed = finished_sandwiches.pop()
    if completed == "blt":
        print(f"\t{completed.upper()}")
    else:
        print(f"\t{completed.title()}")