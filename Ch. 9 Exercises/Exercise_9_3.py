# Create several instances and call both methods for each user.
from User import User

alvin = User("alvin", "chipmunk", "01/22/2004", "male", "chiptopia")
alvin.describe_user()
alvin.greet_user()

joseph = User("joseph", "roots", "04/02/1983", "male", "chicago")
joseph.describe_user()
joseph.greet_user()

jessica = User("jessica", "rigatoni", "11/19/1991", "female", "tuscany")
jessica.describe_user()
jessica.greet_user()

ras = User("ra's", "al ghul", "01/01/1900", "non-binary", "unknown")
ras.describe_user()
ras.greet_user()

pierce = User("pierce", "larue", "07/04/1990", "female", "paris")
pierce.describe_user()
pierce.greet_user()

rain = User("rain", "chaliah", "3/25/2001", "non-binary", "atlantis")
rain.describe_user()
rain.greet_user()

farjan = User("farjan", "khan", "06/28/1994", "male", "new york")
farjan.describe_user()
farjan.greet_user()