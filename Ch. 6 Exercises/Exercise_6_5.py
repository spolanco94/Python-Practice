##### Make a dictionary containing 3 majors rivers and their countries
rivers = {
    "indus" : "china, india, pakistan",
    "yellowstone" : "usa",
    "yangtze" : "china",
}

#####    1. loop through and print a sentence about each river
for key in rivers:
    if rivers[key] == "usa":
        print(f"The {key.title()} River runs through {rivers[key].upper()}.")
    else:
        print(f"The {key.title()} River runs through {rivers[key].title()}.")

#####    2. use a loop to print the name of each river
print("\nRivers:")
for river in rivers:
    print(river.title())

#####    3. use a loop to print the name of each country
print("\nCountries")
for country in rivers.values():
    print(country.title())
