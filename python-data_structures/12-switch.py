#!/usr/bin/python3
"""
This script switches the values of two variables and prints the result.
"""
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
