#! /usr/bin/python3
"""
    Title: test_calculator.py

    Author: Shayne Cardwell

    Description: A Testing module to test the Calculator class
"""
import unittest
from app.calculator import add
from app.calculator import subtract
from app.calculator import multiply
from app.calculator import divide
from app.calculator import modulus


class MyCalculatorTest(unittest.TestCase):
    def test_add_non_int_non_float_exception(self):
        """Validates that an exception raises when adding strings"""
        data_sets = [[], '', {}]
        for data_set in data_sets:
            with self.assertRaises(TypeError):
                add(data_set, data_set)

    def test_add(self):
        """Validates that add yields the expected results"""
        self.assertEqual(add(2, 3), 5)

    def test_subtract_non_int_non_float_exception(self):
        """
        Validates that an exception raises when subtracting a non float
            or int
        """
        data_sets = [[], '', {}]
        for data_set in data_sets:
            with self.assertRaises(TypeError):
                subtract(data_set, data_set)

    def test_subtract(self):
        """Validates that subtract yields the expected results"""
        self.assertEqual(subtract(10, 6), 4)

    def test_multiply_non_int_non_float_exception(self):
        """Validates that an exception raises when adding strings"""
        data_sets = [[], '', {}]
        for data_set in data_sets:
            with self.assertRaises(TypeError):
                multiply(data_set, data_set)

    def test_multiply(self):
        """Validates that add yields the expected results"""
        self.assertEqual(multiply(6, 3), 18)

    def test_multiply_zero_mulitplicand(self):
        """Validates that add yields the expected results"""
        self.assertEqual(multiply(0, 3), 0)

    def test_multiply_zero_muliplier(self):
        """Validates that add yields the expected results"""
        self.assertEqual(multiply(6, 0), 0)

    def test_divide_non_int_non_float_exception(self):
        """Validates that an exception raises when adding strings"""
        data_sets = [[], '', {}]
        for data_set in data_sets:
            with self.assertRaises(TypeError):
                divide(data_set, data_set)

    def test_divide_by_zero(self):
        """Validates that an exception raises when dividing by 0"""
        with self.assertRaises(ZeroDivisionError):
            divide(4, 0)

    def test_divide(self):
        """Validates that add yields the expected results"""
        self.assertEqual(divide(8, 2), 4)

    def test_divide_remainder(self):
        """Validates that add yields the expected results"""
        self.assertEqual(divide(5, 2), 2)

    def test_modulus_non_int_non_float_exception(self):
        """Validates that an exception raises when adding strings"""
        data_sets = [[], '', {}]
        for data_set in data_sets:
            with self.assertRaises(TypeError):
                modulus(data_set, data_set)

    def test_modulus_by_zero(self):
        """Validates that an exception raises when dividing by 0"""
        with self.assertRaises(ZeroDivisionError):
            modulus(4, 0)

    def test_modulus(self):
        """Validates that add yields the expected results"""
        self.assertEqual(modulus(8, 2), 0)

    def test_modulus_remainder(self):
        """Validates that add yields the expected results"""
        self.assertEqual(modulus(5, 2), 1)


if __name__ == '__main__':
    # unittest.main()
    import doctest
    doctest.testfile('calculator.py')
