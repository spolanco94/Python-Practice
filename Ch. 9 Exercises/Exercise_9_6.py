# Add an IceCeamStand class to the Restaurant.py file. Initialize it with an
# attribute called 'flavors' to take in a list of ice cream flavors and write a
# function to display these flavors
from Restaurant import IceCreamStand

shakeys = IceCreamStand("shakey's", "italian gelato", ["vanilla", "chocolate",
                        "strawberry", "mango", "coffee", "cookies n cream"])
shakeys.display_flavors()
