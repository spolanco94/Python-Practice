# Refactor the User class so that the Privileges and Admin classes are in a
# separate module. Check to see that they still work properly.
from admin import Admin

grizzly = Admin("grizzly", "bear", "1/1/1900", "male", "the forest",
                ["can eat berries", "can roar", "can hibernate", "can fish"])

grizzly.privileges.show_privileges()
