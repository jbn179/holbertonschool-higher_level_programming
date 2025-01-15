#!/usr/bin/python3
import sys


def main():
    """
    Calculate and print the sum of all command-line arguments.

    The output should be the result of the addition of all arguments, followed by a new line.
    You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers).
    """
    total = 0

    for arg in sys.argv[1:]:
        total += int(arg)

    print(total)


if __name__ == "__main__":
    main()
