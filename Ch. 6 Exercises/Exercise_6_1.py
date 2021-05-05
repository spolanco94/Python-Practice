##### Use a dictionary to store information about a person 

farjan_profile = {
    "first_name" : "farjan",
    "last_name" : "khan",
    "age" : 26,
    "city" : "queens",
}
for val in farjan_profile.keys():
    if isinstance(farjan_profile[val], int):
        print(f"{val} : {farjan_profile[val]}")
    else:
        print(f"{val} : {farjan_profile[val].title()}")