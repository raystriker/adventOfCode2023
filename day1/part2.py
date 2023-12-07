## Advent of Code 2023 - Day 1
## https://adventofcode.com/2023/day/1
## raystriker


## Part 2
inputtxt = open("input", "r").read()
lines = inputtxt.split('\n')

digit_lookup = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}

actual_final_sum = 0

for line in lines:
    print(line)
    final_number = []
    for someIndex in range(0, len(line)):
        if line[someIndex].isdigit():
            final_number.append(line[someIndex])
        else:
            for aNumber in digit_lookup.keys():
                len_of_aNumber = len(aNumber)
                if line[someIndex:someIndex + len_of_aNumber] == aNumber:
                    final_number.append(str(digit_lookup[line[someIndex:someIndex + len_of_aNumber]]))

    actual_final_sum += int(str(final_number[0]) + str(final_number[-1]))

print(actual_final_sum)
