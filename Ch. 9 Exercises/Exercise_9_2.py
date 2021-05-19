# Using the class from 9-1, create 3 different instances and call 
# 'describe_restaurant' for each instance
from Restaurant import Restaurant

hyaku_ryouri = Restaurant("hyaku ryouri", "japanese")
hyaku_ryouri.describe_restaurant()

le_pain = Restaurant("le pain", "french")
le_pain.describe_restaurant()

classic_diner = Restaurant("classic diner", "american")
classic_diner.describe_restaurant()