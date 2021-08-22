# Write a function that takes in the name of a city and country and formats them
# as "Santiago, Chile".

def format_city(city, country):
    """Formats a city and country as 'City', 'Country'"""
    formatted = f"{city.title()}, {country.title()}"

    return formatted

location = format_city(city= "paris", country= "france")
print(location)
