""" Unittest for max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """"Run this test with python3 -m unittest tests.6-max_integer_test"""

    def test_module_docstring(self):
        moduleDoc = __import__('6-max_integer').__doc__
        self.assertTrue(len(moduleDoc) > 1)

    def test_function_docstring(self):
        functionDoc = __import__('6-max_integer').max_integer.__doc__
        self.assertTrue(len(functionDoc) > 1)

    def test_signed_unsigned_and_float(self):
        self.assertEqual(max_integer([1, 3, 4, 6]), 6)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([2, 0, -1]), 2)
        self.assertEqual(max_integer([0.5, 1.5, 2.5]), 2.5)
        self.assertEqual(max_integer([1, 2, 0.5, -1]), 2)

    def test_list(self):
        self.assertEqual(max_integer([[1, 2], [3, 8]]), [3, 8])

    def test_string(self):
        self.assertEqual(max_integer("abcd"), 'd')
        self.assertEqual(max_integer(['a', 'j', 'l', 'q']), 'q')
        self.assertEqual(max_integer("gbdf9"), 'g')

    def test_other_data_type(self):
        with self.assertRaises(TypeError):
            max_integer({1, 2, 4})
        with self.assertRaises(TypeError):
            max_integer({1, 3, 5}, {1, 4, 6})
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer(True)
        with self.assertRaises(TypeError):
            max_integer([1, "sdf", {1, 4, 5}])

if __name__ == "__main__":
    unittest.main()
