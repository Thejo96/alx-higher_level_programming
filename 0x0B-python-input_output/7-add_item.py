#!/usr/bin/python3
import sys
import os.path
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Filename for the JSON file
filename = 'add_item.json'

# Initialize an empty list or load the existing list from the JSON file
if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
            my_list = []

            # Add command-line arguments to the list
            my_list.extend(sys.argv[1:])

            # Save the updated list to the JSON file
            save_to_json_file(my_list, filename)
