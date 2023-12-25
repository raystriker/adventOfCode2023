## Advent of Code 2023 - Day 5
## https://adventofcode.com/2023/day/5
## raystriker

import time
import pprint

start_time = time.time()

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


# Main execution
lines = read_input_file("input")
seeds = extract_seeds(lines)  #got seeds

mappings = create_mappings(lines) # created mappings from seeds

all_finals = []

for seed in seeds:
    curr_seed = int(seed)
    mapnumber = 0

    for curr_map in mappings.values():

        print("Map length",len(curr_map))
        conditions_passed = 0
        for sub_range in curr_map:
            print("sub range: ",sub_range, " curr seed ",curr_seed)
            print(int(sub_range[1]) , curr_seed , int(sub_range[1])+int(sub_range[2]))

            if int(sub_range[1]) <= curr_seed <= int(sub_range[1])+int(sub_range[2]):
                conditions_passed += 1
                break

        if conditions_passed > 0 :
            if int(sub_range[1]) < int(sub_range[0]):
                curr_seed = curr_seed + abs(int(sub_range[1]) - int(sub_range[0]))
            else:
                curr_seed = curr_seed - abs(int(sub_range[1]) - int(sub_range[0]))
            print("New seed",curr_seed)
        else:
            curr_seed = int(curr_seed)

        print(mapnumber,curr_seed)
        mapnumber+=1

        print("-----------------------")
    all_finals.append(curr_seed)

    print("=================================================================================================")


print(min(all_finals))

end_time = time.time()

total_time = end_time - start_time
print(f"Total execution time: {total_time} seconds")
