print("Advent Of Code - Day 1")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
data = [int(i) for i in PUZZLEINPUT]
dataset = set(data)
## Part 1

#Ugly solution
# for number1 in data:
#     for number2 in data:
#         if number1+number2 == 2020:
#             print(f'Part 1: {number1*number2} {number1} {number2}')
#             break;

for number in data:
    diff = 2020-number
    if diff in dataset:
        print(f'Part 1: {diff*(2020-diff)}')
        break;

#Part 2 - ugly solution continued
for number1 in data:
    for number2 in data:
        for number3 in data:
            if number1+number2+number3 == 2020:
                print(f'Part 2: {number1*number2*number3}')
                exit()
