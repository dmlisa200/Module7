"""
these aren't going to work till I get the basic_list to work
"""

import unittest
from basic_list_exception import make_list


class TestList(unittest.TestCase):
    @patch('fun_with_collections.basic_list_exception.get_input', return_value='ab')
    def test_make_list_non_numeric(self, input):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list()


class MyTestCase(unittest.TestCase):
    def test_make_list_below_range(self):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list(-1)


class MyTestCase(unittest.TestCase):
    def test_make_list_above_range(self):
        with self.assertRaises(ValueError):
            basic_list_exception.make_list(51)


if __name__ == '__main__':
    unittest.main()
