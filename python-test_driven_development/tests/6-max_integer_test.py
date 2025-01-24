#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    TestCase subclass to test the max_integer function.
    """

    def test_regular_list(self):
        """Test with a normal list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([10, 9, 11, 7]), 11)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """Test with a single-element list."""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_integers(self):
        """Test with a list of negative integers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test with a mixture of positive and negative integers."""
        self.assertEqual(max_integer([-10, 0, 1, -1, 100, -50]), 100)

    def test_floats(self):
        """Test with a list of floats."""
        self.assertEqual(max_integer([1.5, 2.8, 2.5, 2.9]), 2.9)

    def test_duplicate_values(self):
        """Test with repeated values in the list."""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

if __name__ == '__main__':
    unittest.main()
    