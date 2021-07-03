# Modify 'make_shirt()' so that it defaults to a size Large shirt with a message
# that reads 'I love python'. Print a large and medium shirt with the default
# message, and then a shirt of any size with any message

def make_shirt(size="large", message="i love python."):
    """Display information about a printed t-shirt."""
    print(f'The shirt you have requested will be size {size.capitalize()} and '
    f'will have the message "{message.capitalize()}" printed on it.')

make_shirt()
make_shirt(size="medium")

size = input("What size shirt would you like? ")
message = input("What message would you like printed? ")

make_shirt(size, message)
