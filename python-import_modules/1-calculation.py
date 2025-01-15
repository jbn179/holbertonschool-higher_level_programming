#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    """
    Perform basic arithmetic operations using functions from calculator_1.py
    and print the results.

    The operations include:
    - Addition
    - Subtraction
    - Multiplication
    - Division

    The values used for the operations are:
    a = 10
    b = 5
    """
    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    main()
