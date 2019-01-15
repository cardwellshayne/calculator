#! /usr/bin/env python3
"""
    Title: calculator_use_case.py

    Author: Shayne Cardwell

    Description: A commandline use case for the calculator module
"""
import argparse

from app.calculator import add
from app.calculator import divide
from app.calculator import modulus
from app.calculator import multiply
from app.calculator import subtract


def check_type(num):
    """Checks if the value is a float or int"""
    try:
        test = int(num)
    except ValueError:
        if '.' in num:
            try:
                test = float(num)
            except ValueError:
                return num
            else:
                return test
    else:
        return test


def main():
    """
        This function is used to execute the module as a standalone
        module.
    """
    parser = argparse.ArgumentParser()
    group1 = parser.add_argument_group()
    group2 = parser.add_mutually_exclusive_group(required=True)

    group1.add_argument('x', help='The first value in the equation', type=check_type)
    group1.add_argument('y', help='The second value in the equation', type=check_type)
    group2.add_argument('--add', action='store_true')
    group2.add_argument('--subtract', action='store_true')
    group2.add_argument('--multiply', action='store_true')
    group2.add_argument('--divide', action='store_true')
    group2.add_argument('--modulus', action='store_true')

    args = parser.parse_args()

    if args.add:
        print(add(args.x, args.y))
    if args.subtract:
        print(subtract(args.x, args.y))
    if args.multiply:
        print(multiply(args.x, args.y))
    if args.divide:
        print(divide(args.x, args.y))
    if args.modulus:
        print(modulus(args.x, args.y))


if __name__ == '__main__':
    main()
