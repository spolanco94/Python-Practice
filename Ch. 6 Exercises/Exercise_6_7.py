##### Beginning with the program from 6-1, add 2 more people with 2 more 
##### dictionaries. Store all in a list called 'people' and loop through 
##### printing everything you know about each person
people = []

farjan_profile = {
    "first_name" : "farjan",
    "last_name" : "khan",
    "age" : 26,
    "city" : "queens",
}
anna_profile = {
    "first_name" : "anna",
    "last_name" : "madrigal",
    "age" : 27,
    "city" : "bronx",
}
yuuki_profile = {
    "first_name" : "yuuki",
    "last_name" : "takahashi",
    "age" : 23,
    "city" : "kyuushu",
}

people = [farjan_profile, anna_profile, yuuki_profile]

for friend in people:
    print(f"Name: {friend['first_name'].title()} {friend['last_name'].title()}")
    print(f"Age: {friend['age']}")
    print(f"Location: {friend['city'].title()}\n")