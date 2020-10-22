import unittest
from city_function import city_country

class PopulationTestCase(unittest.TestCase):

    def test_ll(self):
        double = city_country('beijing', 'china')
        self.assertEqual(double, 'Beijing,China')

    def test_population(self):
        double = city_country('beijing', 'china', '50000000')
        self.assertEqual(double, 'Beijing,China-50000000')

unittest.main()