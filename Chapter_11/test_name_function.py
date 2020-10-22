import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
        
    def test_first_last_name(self):
        formatted_name = get_formatted_name('jj', 'gg')
        self.assertEqual(formatted_name, 'Jj Gg')
    
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('jj', 'gg', 'pp')
        self.assertEqual(formatted_name, 'Jj Pp Gg')

unittest.main()