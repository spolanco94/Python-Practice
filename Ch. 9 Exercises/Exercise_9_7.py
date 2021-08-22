# Add an Admin class to the User.py file, Add a 'privileges' attribute that
# stores in a list of string directives such as "can post", "can delete". Write
# a method called show_privileges() that lists the Administrators privileges
from User import Admin

hal = Admin("hal", "9000", "1/12/1992", "ai", "urbana, illinois",
            ["can delete posts", "can create posts", "can speak", "can pilot",
            "can play chess"])
hal.greet_user()
hal.privileges.show_privileges()
