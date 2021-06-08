# Write a program prompting users for their favorite number, and save it to a 
# JSON file. Then print a message reading back the stored value.
import json

def save_favorite_num():
    """Stores a user's favorite number into a JSON file."""

    favorite_num = input("Tell me your favorite number to keep it safe! ")

    filename = "favorite_number.json"
    with open(filename, 'w') as f:
        json.dump(favorite_num, f)
        
    return favorite_num

def recall_favorite_num():
    """Reads a JSON file that holds the user's favorite number."""

    try:
        filename = "favorite_number.json"
        with open(filename) as f:
            favorite_num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favorite_num

def print_favorite_num():
    """Prints out the user's favorite number."""
    favorite_num = recall_favorite_num()
    if favorite_num:
        print(f"Your favorite number is {favorite_num}!")
    else:
        favorite_num = save_favorite_num()
        print(f"Got it! Your number {favorite_num} will be saved!")

print_favorite_num()