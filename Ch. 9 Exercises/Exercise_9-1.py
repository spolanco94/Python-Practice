# Create an instance of the Restaraunt class. Print the two attributes, then
# call each method
from Restaurant import Restaurant

my_restaurant = Restaurant("El Amor", "Latin")
print(f"{my_restaurant.name.title()}, {my_restaurant.cuisine.title()}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
