##### Make a dictionary and add 3 names to it with their favorite places as 
##### values. Loop through and print each name with their favorite place
favorite_places = {
    "anna" : ["aruba", "paris", "japan"],
    "jackson" : ["florida", "arizona", "california"], 
    "yuuki" : ["new york", "arizona", "japan"],
}
for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")