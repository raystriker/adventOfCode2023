## Advent of Code 2023 - Day 1
## https://adventofcode.com/2023/day/1
## raystriker


## Part 1
inputtxt = open("input", "r").read()
lines = inputtxt.split('\n')


def return2digitNumber(someString):
    firstDigit = None
    lastDigit = None
    for someChar in someString:
        if someChar.isdigit():
            if firstDigit is None:
                firstDigit = someChar
            lastDigit = someChar
    return int(firstDigit + lastDigit)


superSum = 0
for line in lines:
    superSum += return2digitNumber(line)
print(superSum)
