print("Advent Of Code - Day 1")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
## Part 1
data = [int(i) for i in PUZZLEINPUT]
all_diffs = []

for number1 in data:
    for number2 in data:
        if number1+number2 == 2020:
            print(f'Part 1: {number1*number2}')
            exit()
