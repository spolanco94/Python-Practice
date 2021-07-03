# Create a 'Restaurant' class, including a 'restaurant_name' and 'cuisine_type'
# attribute as well as two methods, 'describe_restaurant' to print the name and
# cuisine type, and 'open_restaurant' to print that the restaurant is open.
import string

class Restaurant:
    """A simple restaurant class."""

    def __init__(self, name, cuisine) -> None:
        """Initialize name, cuisine and customers served attributes."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Print out the name and cuisine of the restaurant."""
        print(f"Welcome to {self.name.title()}!")
        print(f"Here we serve authentic {self.cuisine.title()} cuisine.\n")

    def open_restaurant(self):
        print(f"{self.name.title()} is now open!")

    def set_number_served(self, customers):
        """Change the value of number_served."""
        self.number_served = customers

    def increment_number_served(self, number_served):
        """Increment the value of number_served."""
        self.number_served += number_served

class IceCreamStand(Restaurant):
    """A subset of the Restaurant class representing an Ice Cream Stand."""

    def __init__(self, name, cuisine, flavors) -> None:
        """
        Initialize the attributes of the parent Restaurant class.
        Initialize flavors attribute for Ice Cream Stand class.
        """
        super().__init__(name, cuisine)
        self.flavors = flavors

    def display_flavors(self):
        """Displays the list of available ice cream flavors."""
        read = []
        curr = ""
        finished = False
        self.flavors.reverse()

        print(f"Welcome to {string.capwords(self.name)}.\nCurrently, the "
               "flavors we have available are:")

        while not finished:
            curr = self.flavors.pop()
            print(f"\t> {curr.title()}")
            read.append(curr)
            if(self.flavors == []):
                finished = True
