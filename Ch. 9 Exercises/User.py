# Create a User class that takes in first_name, last_name, and several other
# attributes commonly found in a user profile. Create a method, 'describe_user'
# to print a summary of the attributes. Then create a second method,
# 'greet_user' to print a personalized greeting to the user.

class User:
    """Creates a user profile class."""

    def __init__(self, f_name, l_name, birthday, gender, city) -> None:
        """Initialize first and last name, birthday, gender, and city."""
        self.f_name = f_name
        self.l_name = l_name
        self.birthday = birthday
        self.gender = gender
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user's name, birthday, gender, and city."""
        print(f"Name: {self.f_name.title()} {self.l_name.title()}")
        print(f"Birthday: {self.birthday}")
        print(f"Gender: {self.gender.title()}")
        print(f"City: {self.city.title()}")

    def greet_user(self):
        """Prints a personalized greeting to the user."""
        print(f"Welcome, {self.f_name.title()} {self.l_name.title()}. Glad to "
               "see you here!")

    def increment_login_attempts(self):
        """Increment the number of times a user has tried to login by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the login attempt count back to 0 upon successful login."""
        self.login_attempts = 0
