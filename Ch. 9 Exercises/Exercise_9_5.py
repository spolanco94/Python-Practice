# Make an instance of the User class and call 'increment_login_attempts' several
# times and then print the value of 'login_attempts'.
# Call ' reset_login_attempts' and re-print the value of 'login_attempts' to 
# make sure the value is set to 0.
from User import User
import random

garfield = User("garfield", "cat", "09/12/1942", "fluildly male", "twin kitteh")
garfield.describe_user()

def login_tester():
    """Loop to help test login attempt count by simple number comparison."""
    key = random.randint(0, 5)
    guess = random.randint(0,5)
    login = False

    while not login:
        garfield.increment_login_attempts()
        if key == guess:
            garfield.reset_login_attempts()
            print(f"Success!\n# of login attempts: {garfield.login_attempts}")
            login = True
        elif key != guess:
            guess = random.randint(0,5)
            print(f"Error!\n# of login attempts: {garfield.login_attempts}")            

login_tester()