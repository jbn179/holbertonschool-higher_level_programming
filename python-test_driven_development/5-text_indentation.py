#!/usr/bin/python3

def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: '.', '?', and ':'.

    Parameters:
    text (str): The text to be printed.

    Raises:
    TypeError: If text is not a string.

    Note:
    There should be no space at the beginning or end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = {'.', '?', ':'}
    buffer = ""

    for char in text:
        buffer += char
        if char in delimiters:
            print(buffer.strip())
            print()
            buffer = ""

    if buffer.strip():
        print(buffer.strip())
