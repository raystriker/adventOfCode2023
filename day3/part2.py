## Advent of Code 2023 - Day 3
## https://adventofcode.com/2023/day/3
## raystriker
#Part 2

import pprint as pp

# Reading input
inputtxt = open("input", "r").read()
lines = inputtxt.split('\n')

# Processing each character in the lines
full_list = [char for line in lines for char in line]

# Identifying positions of interest
usefulPositions = []
for index, char in enumerate(full_list):
    if char != "." and not char.isdigit() and char == "*":
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
print("Useful positions:")
pp.pprint(usefulPositions)

# Finding neighboring characters for analysis
positions_to_look_into = []
for element in usefulPositions:
    for direction, neighbor_info in element['neighbours'].items():
        if neighbor_info['value'] != ".":
            positions_to_look_into.append({
                "spl_char": element['character'],
                "spl_char_position": element['position'],
                "neighbour_position": neighbor_info['position'],
                "neighbour_value": neighbor_info['value'],
                "neighbour_direction": direction
            })

print("Positions to look into:")
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

        valid_numbers.append({"number": curr_number, "position": pos['spl_char_position']})

print(valid_numbers)

pp.pprint(valid_numbers)

print("---------------------------------------------")

# Counting the occurrences of each position
position_counts = {}
for item in valid_numbers:
    position = item['position']
    if position in position_counts:
        position_counts[position] += 1
    else:
        position_counts[position] = 1

# Filtering items where the position occurs exactly twice
filtered_list = [item for item in valid_numbers if position_counts[item['position']] == 2]

pp.pprint(filtered_list)

print(len(filtered_list), len(valid_numbers))

product_dict = {}

for item in filtered_list:
    position = item['position']
    number = int(item['number'])

    if position in product_dict:
        product_dict[position] *= number
    else:
        product_dict[position] = number

# Summing all the products
sum_of_products = sum(product_dict.values())

print(sum_of_products)