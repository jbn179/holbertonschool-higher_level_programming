def print_last_digit(number):
    """
    Print the last digit of a number and return its value.

    Parameters:
    number (int): The number to extract the last digit from.

    Returns:
    int: The value of the last digit.
    """
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
