import unittest
from city_functions import format_city

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Does it return a location like 'Paris, France'?"""
        formatted_location = format_city('paris', 'france')
        self.assertEqual(formatted_location, 'Paris, France')

    def test_city_country_population(self):
        """ Does it return a location like
            'Fukuoka, Japan - population 1539000'?"""
        formatted_location = format_city('fukuoka', 'japan', '1539000')
        self.assertEqual(formatted_location,
            'Fukuoka, Japan - population 1539000')

if __name__ == '__main__':
    unittest.main()
