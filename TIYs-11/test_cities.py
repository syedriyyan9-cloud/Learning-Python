import unittest
from city_functions import get_city_country_names

class CityCountryTestCase(unittest.TestCase):
    '''a class that will test the functions in city_functions.py'''

    def test_city_country(self):
        '''method to test get_city_country function'''
        expected_result = get_city_country_names('santiago','chile')
        self.assertEqual(expected_result, 'Santiago, Chile')

    def test_city_country_population(self):
        '''method to test get_city_country_population function'''
        expected_result = get_city_country_names('santiago','chile',5000000)
        self.assertEqual(expected_result,'Santiago, Chile - Population 5000000')

if __name__ == "__main__":
    unittest.main()