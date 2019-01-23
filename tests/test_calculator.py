#! /usr/bin/python3
"""
    Title: test_calculator.py

    Author: Shayne Cardwell

    Description: A Testing module to test the Calculator class
"""
import unittest

from app import calculator


class MyCalculatorTest(unittest.TestCase):
    def test_add_non_int_non_float_exception(self):
        """Validates that an exception raises when adding strings"""
        data_sets = [[], '', {}]
        for data_set in data_sets:
            with self.assertRaises(TypeError):
                calculator.add(data_set, data_set)

    def test_add_integer_addition(self):
        """Validates that add yields the expected integer results"""
        self.assertEqual(calculator.add(2, 3), 5)

    def test_add_float_addtion(self):
        """Validates that add yields the expected flotation results"""
        self.assertEqual(calculator.add(2.0, 3.0), 5.0)

    def test_add_float_and_integer_addtion(self):
        """Validates that add yields the expected flotation results"""
        self.assertEqual(calculator.add(2.0, 3), 5.0)

    def test_subtract_non_int_non_float_exception(self):
        """
        Validates that an exception raises when subtracting a non float
            or int
        """
        data_sets = [[], '', {}]
        for data_set in data_sets:
            with self.assertRaises(TypeError):
                calculator.subtract(data_set, data_set)

    def test_subtract_integer_subtraction(self):
        """Validates that subtract yields the expected integer results"""
        self.assertEqual(calculator.subtract(10, 6), 4)

    def test_subtract_float_subtraction(self):
        """Validates that subtract yields the expected flotation results"""
        self.assertEqual(calculator.subtract(10.0, 6.0), 4.0)

    def test_subtract_float_and_integer_subtraction(self):
        """Validates that subtract yields the expected flotation results"""
        self.assertEqual(calculator.subtract(10.0, 6), 4.0)

    def test_multiply_non_int_non_float_exception(self):
        """Validates that an exception raises when adding strings"""
        data_sets = [[], '', {}]
        for data_set in data_sets:
            with self.assertRaises(TypeError):
                calculator.multiply(data_set, data_set)

    def test_multiply_integer_multiplication(self):
        """Validates that add yields the expected results"""
        self.assertEqual(calculator.multiply(6, 3), 18)

    def test_multiply_float_multiplication(self):
        """Validates that add yields the expected results"""
        self.assertEqual(calculator.multiply(6.0, 3), 18.0)

    def test_multiply_integer_zero_mulitplicand(self):
        """Validates that add yields the expected results"""
        self.assertEqual(calculator.multiply(0, 3), 0)

    def test_multiply_integer_zero_muliplier(self):
        """Validates that add yields the expected results"""
        self.assertEqual(calculator.multiply(6, 0), 0)

    def test_multiply_float_zero_mulitplicand(self):
        """Validates that add yields the expected results"""
        print(calculator.multiply(0.0, 3))
        self.assertEqual(calculator.multiply(0.0, 3), 0.0)

    def test_divide_non_int_non_float_exception(self):
        """Validates that an exception raises when adding strings"""
        data_sets = [[], '', {}]
        for data_set in data_sets:
            with self.assertRaises(TypeError):
                calculator.divide(data_set, data_set)

    def test_divide_integer_by_zero_integer(self):
        """Validates that an exception raises when dividing by 0"""
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(4, 0)

    def test_divide_integer_by_zero_float(self):
        """Validates that an exception raises when dividing by 0"""
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(4, 0.0)

    def test_divide_integer(self):
        """Validates that add yields the expected results"""
        self.assertEqual(calculator.divide(8, 2), 4)

    def test_divide_remainder_integer(self):
        """Validates that add yields the expected results"""
        self.assertEqual(calculator.divide(5, 2), 2)

    def test_divide_float(self):
        """Validates that add yields the expected results"""
        self.assertEqual(calculator.divide(8.0, 2.0), 4.0)

    def test_divide_remainder_float(self):
        """Validates that add yields the expected results"""
        self.assertEqual(calculator.divide(5.0, 2.0), 2.0)

    def test_modulus_non_int_non_float_exception(self):
        """Validates that an exception raises when adding strings"""
        data_sets = [[], '', {}]
        for data_set in data_sets:
            with self.assertRaises(TypeError):
                calculator.modulus(data_set, data_set)

    def test_modulus_integer_by_zero(self):
        """Validates that an exception raises when dividing by 0"""
        with self.assertRaises(ZeroDivisionError):
            calculator.modulus(4, 0)

    def test_modulus_integer(self):
        """Validates that add yields the expected results"""
        self.assertEqual(calculator.modulus(8, 2), 0)

    def test_modulus_integer_remainder(self):
        """Validates that add yields the expected results"""
        self.assertEqual(calculator.modulus(5, 2), 1)

    def test_modulus_float_by_zero(self):
        """Validates that an exception raises when dividing by 0"""
        with self.assertRaises(ZeroDivisionError):
            calculator.modulus(4, 0.0)

    def test_modulus_float(self):
        """Validates that add yields the expected results"""
        self.assertEqual(calculator.modulus(8.0, 2.0), 0.0)

    def test_modulus_float_remainder(self):
        """Validates that add yields the expected results"""
        self.assertEqual(calculator.modulus(5.0, 2.0), 1.0)


if __name__ == '__main__':
    unittest.main()
