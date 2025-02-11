#!/usr/bin/python3
'''Module for CSV to JSON conversion.'''

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file.

    Args:
        csv_filename (str): The filename of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False otherwise.

    This function reads data from a CSV file,
    converts each row into a dictionary,
    and then serializes the list of dictionaries
    to a JSON file named 'data.json'.
    If the CSV file is not found or any other error occurs during the process,
    the function returns False.
    """
    try:
        data = []

        # Open the CSV file for reading
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            # Read each row in the CSV file and append it to the data list
            for row in csv_reader:
                data.append(row)

        # Open the JSON file for writing
        with open('data.json', 'w') as json_file:
            # Serialize the list of dictionaries to the JSON file
            json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        # Handle the case where the CSV file is not found
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"An error occurred: {e}")
        return False
