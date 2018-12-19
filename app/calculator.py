#! /usr/bin/python3
"""
    Title: calculator.py

    Author: Shayne Cardwell

    Description: A class focused on performing calculations
"""


def add(augend, addend):
    """Adds the augend and addend together

    This function add augend and addend together only when they are either
    integers or floats

    Args:
        augend(int/float): The number to which an addend is added
        addend(int/float): The number that is added to another

    >>> add(2, 3)
    5

    Returns:
        The sum of augend added by the addend
    Raises:
        TypeError if augend or addend is neither an integer or float
    """
    if not isinstance(augend, (int, float)):
        raise TypeError(f"{augend} is not an integer or float")
    if not isinstance(addend, (int, float)):
        raise TypeError(f"{addend} is not an integer or float")

    return augend + addend


def subtract(subtrahend, minuend):
    """Subtracts minuend from subtrahend

    This function subtracts minuend from subtrahend only when they are
    either integers or floats

    Args:
        subtrahend(int/float): The quantity or number to be subtracted
            from another
        minuend(int/float): The quantity or number from which another
            is to be subtracted

    >>> subtract(10, 6)
    4

    Returns:
        The difference of subtrahend subtracted by the minuend
    Raises:
        TypeError if subtrahend or minuend is neither an integer or
            float
    """
    if not isinstance(subtrahend, (int, float)):
        raise TypeError(f"{subtrahend} is not an integer or float")
    if not isinstance(minuend, (int, float)):
        raise TypeError(f"{minuend} is not an integer or float")

    return subtrahend - minuend


def multiply(multiplicand, multiplier):
    """Multiplies the multiplicand by the multiplier

    This function multiplies the multiplicand by the multiplier only
    when they are either integers or floats

    Args:
        multiplicand(int/float): The quantity that is to be multiplied
            by another
        multiplier(int/float): The quantity by which a given number is
            to be multiplied

    >>> multiply(6, 3)
    18

    Returns:
        The product of the multiplicand multiplied by the multiplier
    Raises:
        TypeError if the multiplicand or multiplier is neither an
            integer or float
    """
    if not isinstance(multiplicand, (int, float)):
        raise TypeError(f"{multiplicand} is not an integer or float")
    if not isinstance(multiplier, (int, float)):
        raise TypeError(f"{multiplier} is not an integer or float")

    product = 0
    list_multiplier = []
    for num in range(multiplier):
        list_multiplier.append(multiplicand)

    while list_multiplier:
        product = add(product, list_multiplier.pop())
    return product


def divide(dividend, divisor):
    """Divides the dividend by the divisor

    This function divides the dividend by the divisor only when they
        are either integers or floats

    Args:
        dividend(int/float): The number to be divided by another number
        divisor(int/float): The number by which another number is to be
            divided

    >>>divide(8, 2)
    4

    Returns:
        The quotient of the dividend divided by the divisor
    Raises:
        TypeError if the dividend or divisor is neither an
            integer or float
        ZeroDivisionError if the divisor is equal to 0
    """
    if not isinstance(dividend, (int, float)):
        raise TypeError(f"{dividend} is not an integer or float")
    if not isinstance(divisor, (int, float)):
        raise TypeError(f"{divisor} is not an integer or float")
    if divisor == 0 or divisor == 0.0:
        raise ZeroDivisionError(f"Trying to divide by {divisor}")

    quotient = 0
    remainder = dividend
    while remainder > 1:
        remainder = subtract(remainder, divisor)
        quotient += 1

    return quotient


def modulus(dividend, divisor):
    """Divides the dividend by the divisor

    This function divides the dividend by the divisor only when they
        are either integers or floats and then returns the remainder

    Args:
        dividend(int/float): The number to be divided by another number
        divisor(int/float): The number by which another number is to be
            divided

    >>>modulus(5, 2)
    1

    Returns:
        The remainder of the dividend divided by the divisor
    Raises:
        TypeError if the dividend or divisor is neither an
            integer or float
        ZeroDivisionError if the divisor is equal to 0
    """
    if not isinstance(dividend, (int, float)):
        raise TypeError(f"{dividend} is not an integer or float")
    if not isinstance(divisor, (int, float)):
        raise TypeError(f"{divisor} is not an integer or float")
    if divisor == 0 or divisor == 0.0:
        raise ZeroDivisionError(f"Trying to divide by {divisor}")

    quotient = 0
    remainder = dividend
    while remainder > 1:
        remainder = subtract(remainder, divisor)
        quotient += 1

    return remainder
