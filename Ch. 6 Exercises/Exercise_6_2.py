##### Use a dictionary to store at least 5 people's names and favorite numbers
favorite_numbers = {
    "anna" : 22,
    "jasmine" : 12,
    "olivia" : 5, 
    "farjan" : 67,
    "tareen" : 102,
}

for val in favorite_numbers.keys():
    print(f"{val.title()}: {favorite_numbers[val]}")