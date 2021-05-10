##### Make several dictionaries where each represents a different pet.
##### In each dictionary, include the kind of animal and the owners name. 
rex = {
    "name" : "rex",
    "owner" : "Alan",
    "type" : "iguana",
}

chonks = {
    "name" : "chonks",
    "owner" : "felicia",
    "type" : "cat",
}

harold = {
    "name" : "harold",
    "owner" : "marge",
    "type" : "parrot",
}

cooper = {
    "name" : "cooper",
    "owner" : "anna",
    "type" : "dog",
}

richter = {
    "name" : "richter",
    "owner" : "farjan",
    "type" : "cat",
}

##### Store these dictionaries in a list called pets.
##### Loop through the dictionary and print each persons name and pet.\
pets = [rex, chonks, harold, cooper, richter]

for animal in pets:
    print(f"Name: {animal['name'].title()}")
    print(f"Owner: {animal['owner'].title()}")
    print(f"Species: {animal['type'].title()}\n")