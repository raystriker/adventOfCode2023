## Advent of Code 2023 - Day 6
## https://adventofcode.com/2023/day/6
## raystriker

#Part 1

import pprint as pp

# Reading input
inputtxt = open("input", "r").read()
lines = inputtxt.split('\n')

print(lines)

time_list = list(filter(None, lines[0].split(":")[-1].split(" ")))
distance_list = list(filter(None, lines[1].split(":")[-1].split(" ")))
print(time_list)
print(distance_list)

ans = 1

for i in range(len(time_list)):

    total_time = int(time_list[i])

    curr_record = int(distance_list[i])

    ways_to_beat_record = 0

    for i in range(total_time):

        time_left = total_time - i

        distance_traveled = time_left * i

        print(f"this is i->{i}", f" time left->{time_left}", f" ditance traveled->{distance_traveled}")

        if distance_traveled > curr_record:

            ways_to_beat_record += 1

    print(ways_to_beat_record)

    ans *= ways_to_beat_record

print(ans)


