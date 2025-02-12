#!/usr/bin/python3
'''Module for XML serialization.'''

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename of the output XML file.

    This function creates an XML tree with a root element named 'data'.
    Each key-value pair in the dictionary is added as a child element
    of the root, where the key is the tag name and the value is the text
    content of the child element. The resulting XML tree is then written
    to the specified file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Args:
        filename (str): The filename of the input XML file.

    Returns:
        dict: The deserialized dictionary.

    This function reads an XML file and parses it into an XML tree.
    It then iterates over the child elements of the root element,
    adding each tag and its text content as a key-value pair in a
    dictionary. The resulting dictionary is returned.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
