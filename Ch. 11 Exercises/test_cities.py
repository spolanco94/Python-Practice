import unittest
from city_functions import format_city

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country_format(self):
        """Does it return a location like 'Paris, France'?"""
        formatted_location = format_city('paris', 'france')
        self.assertEqual(formatted_location, 'Paris, France')

if __name__ == '__main__':
    unittest.main()