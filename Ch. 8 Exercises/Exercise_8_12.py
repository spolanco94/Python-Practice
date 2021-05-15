# Write a function that accepts a list of items a person wants on their sandwich
# Take in one arbitrary param, and call it 3 times with 3 different param's

def make_sandwich(type, *ingredients):
    """Takes in any number of ingredients and prints out the sandwich built"""
    sandwich = []
    print(f"Now making your {type} sandwich...")
    
    for ingredient in ingredients:
        print(f"\tAdding {ingredient} to your sandwich... Done!")
        sandwich.append(ingredient)

    print(f"Your {type} sandwich is complete! Enjoy!\n")

    return sandwich

pastrami = make_sandwich("pastrami", "pastrami", "munster cheese", "spinach", 
"mayo", "tomatoes", "onions", "dijon mustard")
blt = make_sandwich("blt", "thick cut maple bacon", "romaine lettuce", 
"roma tomatoes", "cheddar cheese")
ham_and_cheese = make_sandwich("ham and cheese", "black forest ham", 
"american cheese", "mayo")