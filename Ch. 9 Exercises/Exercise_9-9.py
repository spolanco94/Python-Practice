# Using the final version of electric_car.py, add a method to the Battery class
# called upgrade_battery(). This method should check the battery size and set
# the capacity to 100 if it isn't already. Make an electric car with a default
# battery size, call get_range() before and after upgrading the battery.
from electric_car import ElectricCar

my_mustang = ElectricCar("ford", "mustang mach-e", 2021)

my_mustang.get_descriptive_name()
my_mustang.battery.describe_battery()
my_mustang.battery.get_range()
my_mustang.battery.upgrade_battery()
my_mustang.battery.describe_battery()
my_mustang.battery.get_range()
