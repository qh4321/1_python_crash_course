import unittest

from city_function import city_country

class CityTestCase(unittest.TestCase):
    def test_ll(self):
        double = city_country('beijing', 'china')
        self.assertEqual(double, 'Beijing,China')

unittest.main()
