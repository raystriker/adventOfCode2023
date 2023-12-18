import pprint as pp
from pandas import json_normalize

# Reading input
inputtxt = open("input", "r").read()
lines = inputtxt.split('\n')

# Processing each character in the lines
full_list = [char for line in lines for char in line]

# Identifying positions of interest
usefulPositions = []
for index, char in enumerate(full_list):
    if char != "." and not char.isdigit():
        # Defining directions and their relative positions
        directions = {
            "north": -140,
            "south": 140,
            "east": 1,
            "west": -1,
            "ne": -139,
            "nw": -141,
            "se": 141,
            "sw": 139
        }

        # Analyzing neighboring characters
        neighbors = {}
        for direction, offset in directions.items():
            try:
                neighbor_char = full_list[index + offset]
                neighbors[direction] = {"value": neighbor_char, "position": index + offset}
            except IndexError:
                neighbors[direction] = {"value": ".", "position": index}

        usefulPositions.append({
            "character": char,
            "position": index,
            "neighbours": neighbors
        })

# Displaying useful positions
pp.pprint(usefulPositions)

# Converting to DataFrame for analysis
usefulPositions_df = json_normalize(usefulPositions)
print(usefulPositions_df)

# Finding neighboring characters for analysis
positions_to_look_into = []
for element in usefulPositions:
    for direction, neighbor_info in element['neighbours'].items():
        if neighbor_info['value'] != ".":
            positions_to_look_into.append({
                "spl_char": element['character'],
                "neighbour_position": neighbor_info['position'],
                "neighbour_value": neighbor_info['value'],
                "neighbour_direction": direction
            })

pp.pprint(positions_to_look_into)

# Checking for valid numbers
indexes_checked = []
valid_numbers = []

for pos in positions_to_look_into:
    if pos['neighbour_position'] not in indexes_checked:
        curr_number = pos['neighbour_value']
        indexes_checked.append(pos['neighbour_position'])

        # Extending number to the right
        next_char_index = pos['neighbour_position'] + 1
        while full_list[next_char_index].isdigit():
            curr_number += full_list[next_char_index]
            indexes_checked.append(next_char_index)
            next_char_index += 1

        # Extending number to the left
        prev_char_index = pos['neighbour_position'] - 1
        while full_list[prev_char_index].isdigit():
            curr_number = full_list[prev_char_index] + curr_number
            indexes_checked.append(prev_char_index)
            prev_char_index -= 1

        valid_numbers.append(curr_number)

# Summing valid numbers
sum_of_valid_numbers = sum([int(number) for number in valid_numbers])
print(valid_numbers)
print(sum_of_valid_numbers)
