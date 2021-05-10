##### Using the program from 6-2, add more than 1 favorite number to each person
##### Print each person's name and favorite numbers
favorite_numbers = {
    "anna" : [22, 14, 17, 28],
    "jasmine" : [12, 39, 31, 199, 16],
    "olivia" : [5, 5, 2, 1, 10], 
    "farjan" : [67, 1_000, 199, 29],
    "tareen" : [102, 54, 230],
}

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are:")
    for num in numbers:
        print(f"\t{num}")