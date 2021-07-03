# Expand the Restaurant class with an attribute called 'number_served' with a
# default value of 0. Print the number of customers served, then change the
# number and reprint.
from Restaurant import Restaurant
railway_diner = Restaurant("raleway diner", "american")
print(f"Opening service number: {railway_diner.number_served}")
railway_diner.number_served = 12
print(f"Customers served for breakfast: {railway_diner.number_served}")

# Add a method to the class called 'set_number_served' that lets you set the
# number of customers that have been served.
railway_diner.set_number_served(59)
print(f"Customers served by lunch: {railway_diner.number_served}")

# Add a second method called 'increment_number_served' that lets you increment
# the number of customers who've been served.
railway_diner.increment_number_served(33)
print(f"Customers served by closing: {railway_diner.number_served}")
