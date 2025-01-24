#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divide two numbers and print the result safely.

    Parameters:
    a (int or float): The numerator.
    b (int or float): The denominator.

    Returns:
    float or None: The result of the division. If division by zero occurs, returns None.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
