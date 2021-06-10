# Write a function that takes in the name of a city, its country and its 
# population, and formats them as "Santiago, Chile - population 5000000"

def format_city(city, country, population=''):
    """Formats a city and country as 'City', 'Country - population xxx'"""
    if population != '':
        formatted = (f"{city.title()}, {country.title()} - population "
            f"{population}")
    else: 
        formatted = f"{city.title()}, {country.title()}"

    return formatted