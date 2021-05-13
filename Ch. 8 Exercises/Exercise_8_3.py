# Write a function called 'make_shirt' that accepts a size and text of a message
# to be printed on. Print a message that includes the parameter. Use positional
# arguments first, and repeat again with keyword arguments

def make_shirt(size, message):
    """Display information about a printed t-shirt."""
    print(f'The shirt you have requested will be size {size} and will have the '
    f'message "{message.capitalize()}" printed on it.')

size = input("What size shirt would you like? ")
message = input("What message would you like printed? ")

make_shirt(size, message)
make_shirt(size= "medium", message= "This is an orange.")