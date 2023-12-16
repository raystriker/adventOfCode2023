## Advent of Code 2023 - Day 3
## https://adventofcode.com/2023/day/3
## raystriker

import pprint as pp
import pandas as pd
from pandas import json_normalize

inputtxt = open("input", "r").read()
lines = inputtxt.split('\n')

full_list = []
for line in lines:
    for single_char in line:
        full_list.append(single_char)

usefulPositions = []

for i in range(0, len(full_list)):
    print("--------------")
    print(i, "-->", full_list[i])
    if full_list[i] != "." and not full_list[i].isdigit():
        try:
            north = full_list[i - 140]
            north_position = i - 140
        except:
            north = "."
            north_position = i
        try:
            south = full_list[i + 140]
            south_position = i + 140
        except:
            south = "."
            south_position = i
        try:
            east = full_list[i + 1]
            east_position = i + 1
        except:
            east = "."
            east_position = i
        try:
            west = full_list[i - 1]
            west_position = i - 1
        except:
            west = "."
            west_position = i
        try:
            ne = full_list[i - 140 + 1]
            ne_position = i - 140 + 1
        except:
            ne = "."
            ne_position = i
        try:
            nw = full_list[i - 140 - 1]
            nw_position = i - 140 - 1
        except:
            nw = "."
            nw_position = i
        try:
            se = full_list[i + 140 + 1]
            se_position = i + 140 + 1
        except:
            se = "."
            se_position = i
        try:
            sw = full_list[i + 140 - 1]
            sw_position = i + 140 - 1
        except:
            sw = "."
            sw_position = i

        print("north", north, north_position)
        print("south", south , south_position)
        print("east", east , east_position)
        print("west", west , west_position)
        print("ne", ne  , ne_position)
        print("nw", nw  , nw_position)
        print("se", se  , se_position)
        print("sw", sw  , sw_position)


        usefulPositions.append({
            "character": full_list[i],
            "position": i,
            "neighbours": {
                "north": {"value": north,
                          "position": north_position},
                "south": { "value": south,
                           "position": south_position},
                "east": { "value": east,
                          "position": east_position},
                "west": { "value": west,
                          "position": west_position},
                "ne": { "value": ne,
                        "position": ne_position},
                "nw": { "value": nw,
                        "position": nw_position},
                "se": { "value": se,
                        "position": se_position},
                "sw": { "value": sw,
                        "position": sw_position}
                }
            })





        print("--------------")

pp.pprint(usefulPositions)

usefulPositions_df = json_normalize(usefulPositions)

print(usefulPositions_df)


positions_to_look_into = []
for element in usefulPositions:
    # print(element['character'])
    for key in element['neighbours']:
        if element['neighbours'][key]['value'] != ".":
            positions_to_look_into.append({"spl_char":element['character'],
                                           "neighbour_position":element['neighbours'][key]['position'],
                                           "neighbour_value": element['neighbours'][key]['value'],
                                           "neighbour_direction":key})


pp.pprint(positions_to_look_into)

indexes_checked = []

valid_numbers = []

print("----------------------------------------------------------------------------------------------------------------")
for pos in positions_to_look_into:
    print("***********************",pos)

    if pos['neighbour_position'] not in indexes_checked:
        curr_number =""
        indexes_checked.append(pos['neighbour_position'])
        curr_number+=pos['neighbour_value']
        print(curr_number)

        next_char_index_supposedly = pos['neighbour_position'] + 1


        nex_char_is_number = True

        while nex_char_is_number:
            print("checking", pos['neighbour_position'] + 1)
            next_char = full_list[next_char_index_supposedly]
            if next_char.isdigit():
                curr_number += next_char
            else:
                nex_char_is_number = False
            indexes_checked.append(next_char_index_supposedly)

            next_char_index_supposedly += 1


        prev_char_index_supposedly = pos['neighbour_position'] - 1
        prev_char_is_number = True
        while prev_char_is_number:
            print("checking", pos['neighbour_position'] - 1)
            prev_char = full_list[prev_char_index_supposedly]
            if prev_char.isdigit():
                curr_number = prev_char + curr_number
            else:
                prev_char_is_number = False
            indexes_checked.append(prev_char_index_supposedly)

            prev_char_index_supposedly -= 1

        print(curr_number)
        valid_numbers.append(curr_number)



print(valid_numbers)


sum_of_valid_numbers = 0
for number in valid_numbers:
    sum_of_valid_numbers += int(number)

print(sum_of_valid_numbers)


# usefulPositions_df.to_csv('output.csv', index=False)

'''
W	n-1
E	n+1
N	n-(len Str)
S	n+(len Str)

NE	n-(len Str)+1
NW	n-(len Str) – 1
SE	n+(len Str) + 1
SW	n+(len Str) – 1

'''

