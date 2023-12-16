## Advent of Code 2023 - Day 4
## https://adventofcode.com/2023/day/4
## raystriker

import pprint as pp

## get input
inputtxt = open("input", "r").read()
lines = inputtxt.split('\n')


sum_of_points = 0

for l in lines:

    card_no = l.split(":")[0]

    card_data_winners = l.split(":")[1].split("|")[0]

    card_data_my_number = l.split(":")[1].split("|")[1]

    card_data_winners_list = [int(x) for x in card_data_winners.split(" ") if x.isdigit()]

    card_data_my_number_list = [int(x) for x in card_data_my_number.split(" ") if x.isdigit()]

    # card_no = [x for x in card_no if x.isdigit()]
    print(card_no)
    print(card_data_winners_list)
    print(card_data_my_number_list)

    card_point = 0

    first_time = True

    for curr_no in card_data_my_number_list:

        if curr_no in card_data_winners_list:
            if first_time:
                card_point = card_point + 1
                first_time = False
            else:
                card_point = card_point * 2


    sum_of_points += card_point

    print("---------------------")

print(sum_of_points)













