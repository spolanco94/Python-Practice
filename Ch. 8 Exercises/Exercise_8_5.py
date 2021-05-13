# Write a function called 'describe_city' that accepts the name of a city and 
# country. Have it print a simple sentence. Give it a default parameter for 
# the country, and call it for 3 different cities. Choose one city from a 
# different country.

def describe_city(city, country="japan"):
    """Display's a statement about a city and where it is located."""
    print(f"{city.title()} is in {country.title()}.")

describe_city(city= "kyoto")
describe_city(city= "tokyo")
describe_city(city= "barcelona", country= "spain")