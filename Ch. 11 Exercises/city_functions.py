# Write a function that takes in the name of a city and country and formats them
# as "Santiago, Chile". (Taken from Exercise 8-6)

def format_city(city, country):
    """Formats a city and country as 'City', 'Country'"""
    formatted = f"{city.title()}, {country.title()}"

    return formatted
