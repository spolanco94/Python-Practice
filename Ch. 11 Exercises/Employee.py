# Write a class, Employee, that takes in a first name, last name, and an annual 
# salary and stores each of these attributes. Write a method called give_raise() 
# that adds 5,000 to the annual salary by default, but also accepts a different 
# amount. 

class Employee:
    """
    Creates an employee file storing first and last name, and salary 
    information.
    """

    def __init__(self, f_name, l_name, salary) -> None:
        """
        Initialize employee profile with first name, last name, and salary.
        """
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary

    def give_raise(self, salary_raise=5000):
        """Increases salary by a given amount, by default 5000."""
        self.salary += int(salary_raise)