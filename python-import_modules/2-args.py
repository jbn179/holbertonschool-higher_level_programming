#!/usr/bin/python3
import sys


def main():
    """
    Print the number of and the list of its arguments.

    The output format is:
    - Number of argument(s) followed by "argument"
    (if one) or "arguments" (otherwise)
    - Followed by ":" (or "." if no arguments were passed)
    - Followed by a new line
    - Followed by one line per argument (if at least one argument):
      - The position of the argument (starting at 1) followed by ":"
      - Followed by the argument value and a new line
    """
    argv = sys.argv[1:]  # Get all arguments except the script name
    argc = len(argv)  # Count the number of arguments

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argc))

    for i, arg in enumerate(argv, start=1):
        print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
