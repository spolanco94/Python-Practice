# Write a function called 'favorite_book' that accepts 1 parameter. Use it to
# display a message stating what someone's favorite book is.

def favorite_book(title):
    """Takes a user input and returns a statement that says what their favorite
    book is."""
    print(f"Your favorite book is {title.title()}? Wow, I will check it out myself!")

title = input("What is your favorite book? ")
favorite_book(title)
