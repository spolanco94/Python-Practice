def make_sandwich(type, *ingredients):
    """Takes in any number of ingredients and prints out the sandwich built"""
    sandwich = []
    print(f"Now making your {type} sandwich...")
    
    for ingredient in ingredients:
        print(f"\tAdding {ingredient} to your sandwich... Done!")
        sandwich.append(ingredient)

    print(f"Your {type} sandwich is complete! Enjoy!\n")

    return sandwich