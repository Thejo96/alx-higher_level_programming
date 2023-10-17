# Define the dictionary
my_dict = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}

# Print the dictionary and its type
print(my_dict)
print(type(my_dict))

# Convert the dictionary to a list with a single element and print it
my_list = [my_dict]
print(my_list)
print(type(my_list))

# Convert the list to a JSON string
import json
my_json = json.dumps(my_list)

# Write the JSON string to a file
with open('14-main.py', 'w') as file:
    file.write(my_json)
