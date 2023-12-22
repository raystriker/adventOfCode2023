## Advent of Code 2023 - Day 4
## https://adventofcode.com/2023/day/4
## raystriker
import pprint as pp

# get input
inputtxt = open("input", "r").read()
lines = inputtxt.split('\n')


multiplier_dict = {i: 1 for i in range(1, len(lines) + 1)}

for l in lines:

    parts = l.split(":")

    card_no = int(parts[0].split()[1])

    numbers = parts[1].split("|")

    winning_numbers = set(map(int, numbers[0].split()))

    my_numbers = set(map(int, numbers[1].split()))

    print("card no ",card_no," winning numbers ",winning_numbers," my numbers ",my_numbers)


    matches = len(winning_numbers.intersection(my_numbers))

    print("card no ",card_no," matches ",matches)
    print("---")

    for next_card in range(card_no + 1, card_no + 1 + matches):

        if next_card in multiplier_dict:

            multiplier_dict[next_card] += multiplier_dict[card_no]

            print("card no ",card_no," next card ",next_card," multiplier ",multiplier_dict[next_card])

    print("==========================================================================================================")

total_cards = sum(multiplier_dict.values())

print(total_cards)

# multiplier_dict = {}
#
#
# super_sum = 0
#
# for l in lines:
#     card_no = int(l.split(":")[0].split(" ")[-1])
#     card_data_winners_list = [int(x) for x in l.split(":")[1].split("|")[0].split(" ") if x.isdigit()]
#     card_data_my_number_list = [int(x) for x in l.split(":")[1].split("|")[1].split(" ") if x.isdigit()]
#
#     print("card no :", card_no)
#     print("Card winner numbers: ",card_data_winners_list)
#     print("Card my numbers: ",card_data_my_number_list)
#
#     matching_cards = []
#
#     for curr_card in card_data_my_number_list:
#         if curr_card in card_data_winners_list:
#             matching_cards.append(curr_card)
#
#
#
#     if len(matching_cards) > 0:
#         for i in range(int(card_no)+1, int(card_no)+len(matching_cards)+1):
#             print(i)
#             try:
#                 multiplier_dict[i] += 1
#             except:
#                 multiplier_dict[i] = 1
#
#         pp.pprint(multiplier_dict)
#
#         try:
#             super_sum += len(matching_cards) * multiplier_dict[int(card_no)]
#         except:
#             super_sum += len(matching_cards) * 1
#
#         print("card no ",card_no," len matching cards ",len(matching_cards)," supersum",super_sum)
#
#
#
#     print("-------------------")
#
#
# print(super_sum+len(lines))
#
#     locallist = []
#
#
#     if len(matching_cards) > 0:
#         for i in range(int(card_no)+1, int(card_no)+len(matching_cards)+1):
#             print(i)
#             locallist.append(i)
#
#             try:
#                 alt_dict[i] += 1
#             except:
#                 alt_dict[i] = 1
#
#         cards_dict[card_no] = locallist
#
#     print("-------------------")
#
# pp.pprint(cards_dict)
# pp.pprint(alt_dict)
#
#
# supersum = 0
#
# print("=========================================================================================")
# for item, value in cards_dict.items():
#     try:
#         mods = alt_dict[int(item)]
#     except:
#         mods = 1
#
#     print(item, len(value), mods)
#     supersum += (len(value) ** mods)
#
# print(supersum)
# '''
# {1: [2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
#  2: [3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
#  3: [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
#  4: [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
#  6: [7, 8, 9, 10, 11, 12, 13],
#  7: [8, 9, 10, 11, 12],
#  8: [9, 10, 11, 12, 13, 14],
#  10: [11],
#  11: [12, 13, 14, 15],
#  12: [13, 14],
#  13: [14, 15],
#  14: [15],
#
#  2: 1,
#  3: 2,
#  4: 3,
#  5: 4,
#  6: 4,
#  7: 5,
#  8: 6,
#  9: 7,
#  10: 7,
#  11: 8,
#  12: 7,
#  13: 6,
#  14: 5,
# '''