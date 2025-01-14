def uppercase(str):
    """
    Print a string in uppercase followed by a new line.

    Parameters:
    str (str): The string to convert to uppercase.
    """
    result = ""
    for char in str:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
