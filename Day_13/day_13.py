PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
# PUZZLEINPUT = open('test_input.txt', 'r').read().split("\n")

print("Advent Of Code - Day 13")

BUS_ID = int(PUZZLEINPUT[0])

#Could probably swap this for a list comprehension
BUS_LINES = PUZZLEINPUT[1].split(',')
BUS_LINES = [int(line) for line in BUS_LINES if line !=  "x" and line != ',']


all_bus_line_times = {}
for line in BUS_LINES:
    temp = 0
    while temp < BUS_ID:
        temp += line
    print(f'Bus line {line} is checked time is {temp}')
    
    all_bus_line_times.update({line:temp})
    
fastest_bus_line = min(all_bus_line_times, key=all_bus_line_times.get)
depart_time = all_bus_line_times[fastest_bus_line] - BUS_ID
print(f'Part 1: Fastest line is {fastest_bus_line*depart_time}')
