## Advent of Code 2023 - Day 6
## https://adventofcode.com/2023/day/6
## raystriker

#Part 2


# Reading input
inputtxt = open("input", "r").read()
lines = inputtxt.split('\n')

print(lines)

time_list = ["".join(list(filter(None, lines[0].split(":")[-1].split(" "))))]
distance_list = ["".join(list(filter(None, lines[1].split(":")[-1].split(" "))))]

print(time_list, distance_list)

ans = 1

for i in range(len(time_list)):

    total_time = int(time_list[i])

    curr_record = int(distance_list[i])

    ways_to_beat_record = 0

    for i in range(total_time):

        time_left = total_time - i

        distance_traveled = time_left * i

        if distance_traveled > curr_record:

            ways_to_beat_record += 1

    print(ways_to_beat_record)

    ans *= ways_to_beat_record

print("final ans",ans)


