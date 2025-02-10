#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file"""

import sys
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

'''Load existing items from the file if it exists'''
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

'''Add new arguments to the list'''
items.extend(sys.argv[1:])

'''Save the updated list to the file'''
save_to_json_file(items, filename)
