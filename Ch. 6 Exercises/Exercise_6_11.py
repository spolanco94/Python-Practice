##### Make a dictionary called cities, and store info about the county,
##### population, and one fun fact. Loop through and print all info about each
##### city
cities = {
    "fukuoka" : {
        "country" : "japan",
        "population" : "1.539 million",
        "fact" : "there is a shopping mall with a river running through "
        "named Canal City.",
    },
    "new york city" : {
        "country" : "united states of america",
        "population" : "8.419 million",
        "fact" : "Times Square was originally called Longacre Square before "
        "the Times moved there.",
    },
    "paris" : {
        "country" : "france",
        "population" : "2.161 million",
        "fact" : "the eiffel tower was orignally built to show of France's "
        "technical and construction skills, meant to be torn down after.",
    },
}

for city, city_info in cities.items():
    print(f"City: {city.title()}")
    print(f"\t{city_info['country'].title()}")
    print(f"\t{city_info['population'].title()}")
    print(f"\t{city_info['fact'].capitalize()}")
