# Write a test case for Employee. Write two test methods,
# test_give_default_raise() and test_give_custom_raise(). Use the setUp() method
# so you don't have to create a new employee instance in each method.
import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class named Employee."""

    def setUp(self) -> None:
        """
        Create a complete Employee profile with a full name and salary
        information.
        """
        self.new_employee = Employee("rick", "sanchez", 500000)

    def test_give_default_raise(self):
        """Test to see if a default value of 5000 is added to salary."""
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.salary, 505000)

    def test_give_custom_raise(self):
        """Test to check if a custom value of 14000 is added to the salary."""
        self.new_employee.give_raise(14000)
        self.assertEqual(self.new_employee.salary, 514000)

if __name__ == '__main__':
    unittest.main()
