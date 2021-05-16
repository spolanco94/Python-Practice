# Refactor one of the codes I've written with functions to be in a separate file
# Call the function using all the different import methods learned
# Code from Exercise 8-12
#       Write a function that accepts a list of items a person wants on their 
#       sandwich. Take in one arbitrary param, and call it 3 times with 3 
#       different param's

# import make_sandwich
# pastrami = make_sandwich.make_sandwich("pastrami", "pastrami", "munster cheese", "spinach", 
# "mayo", "tomatoes", "onions", "dijon mustard")
# blt = make_sandwich.make_sandwich("blt", "thick cut maple bacon", "romaine lettuce", 
# "roma tomatoes", "cheddar cheese")
# ham_and_cheese = make_sandwich.make_sandwich("ham and cheese", "black forest ham", 
# "american cheese", "mayo")

# from make_sandwich import make_sandwich
# pastrami = make_sandwich("pastrami", "pastrami", "munster cheese", "spinach", 
# "mayo", "tomatoes", "onions", "dijon mustard")
# blt = make_sandwich("blt", "thick cut maple bacon", "romaine lettuce", 
# "roma tomatoes", "cheddar cheese")
# ham_and_cheese = make_sandwich("ham and cheese", "black forest ham", 
# "american cheese", "mayo")

# from make_sandwich import make_sandwich as s
# pastrami = s("pastrami", "pastrami", "munster cheese", "spinach", 
# "mayo", "tomatoes", "onions", "dijon mustard")
# blt = s("blt", "thick cut maple bacon", "romaine lettuce", 
# "roma tomatoes", "cheddar cheese")
# ham_and_cheese = s("ham and cheese", "black forest ham", 
# "american cheese", "mayo")

# import make_sandwich as ms
# pastrami = ms.make_sandwich("pastrami", "pastrami", "munster cheese", "spinach", 
# "mayo", "tomatoes", "onions", "dijon mustard")
# blt = ms.make_sandwich("blt", "thick cut maple bacon", "romaine lettuce", 
# "roma tomatoes", "cheddar cheese")
# ham_and_cheese = ms.make_sandwich("ham and cheese", "black forest ham", 
# "american cheese", "mayo")

from make_sandwich import *
pastrami = make_sandwich("pastrami", "pastrami", "munster cheese", "spinach", 
"mayo", "tomatoes", "onions", "dijon mustard")
blt = make_sandwich("blt", "thick cut maple bacon", "romaine lettuce", 
"roma tomatoes", "cheddar cheese")
ham_and_cheese = make_sandwich("ham and cheese", "black forest ham", 
"american cheese", "mayo")