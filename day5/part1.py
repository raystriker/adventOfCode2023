## Advent of Code 2023 - Day 5
## https://adventofcode.com/2023/day/5
## raystriker


import pprint

def read_input_file(file_path):
    """Reads input from file and returns lines as a list."""
    try:
        with open(file_path, "r") as file:
            return file.read().strip().split('\n')
    except IOError:
        print("Error: File not found or unable to read.")
        return []

def extract_seeds(lines):
    """Extracts seeds from the first line of the input."""
    return lines[0].split(" ")[1:]

def create_mappings(lines):
    """Creates a mapping dictionary from the given lines."""
    mappings = {}
    current_map_key = None

    for line in lines:
        if line.endswith('map:'):
            current_map_key = line
            mappings[current_map_key] = []
        elif current_map_key and line:
            mappings[current_map_key].append(line.split(" "))

    return mappings

def generate_range_mappings(mappings):
    """Generates range mappings from the given mappings."""
    range_mappings = {}

    for map_name, map_data in mappings.items():
        print(map_name)
        range_list = []
        for (destination, source, num_range) in map_data:
            destination, source, num_range = int(destination), int(source), int(num_range)
            range_list.extend([(i, destination + i - source) for i in range(source, source + num_range)])
        range_mappings[map_name] = range_list

    return range_mappings

def print_mappings(mappings):
    """Prints the mappings in a formatted way."""
    for map_name, mapping in mappings.items():
        print(map_name)
        # pprint.pprint(mapping)
        print("--------------------------------------------")

# Main execution
lines = read_input_file("input2")
seeds = extract_seeds(lines)

mappings = create_mappings(lines)
range_mappings = generate_range_mappings(mappings)
# print_mappings(range_mappings)

all_finals = []

for seed in seeds:
    final_seed = int(seed)
    for map_list in range_mappings.values():
        for src, dst in map_list:
            if final_seed == src:
                final_seed = dst
                break

    print(final_seed)
    all_finals.append(final_seed)
    print("-----------------------")

print("=======================================")
print(min(all_finals))
