from User import User

class Privileges:
    """A class representing a list of user privileges."""

    def __init__(self, privileges=["can monitor", "can pilot"]) -> None:
        self.privileges = privileges

    def show_privileges(self):
        """Displays Administrators full privileges."""
        read = []
        curr = ""
        finished = False
        self.privileges.reverse()

        print(f"Your full administrator privileges are as follows:")

        while not finished:
            curr = self.privileges.pop()
            print(f"\t> {curr.title()}")
            read.append(curr)
            if(self.privileges == []):
                finished = True

class Admin(User):
    """A subset of the User class that represents an Administrator user."""

    def __init__(self, f_name, l_name, birthday,
                 gender, city, privileges) -> None:
        super().__init__(f_name, l_name, birthday, gender, city)
        self.privileges = Privileges(privileges)
