PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
# PUZZLEINPUT = open('test_input.txt', 'r').read().split("\n")

print("Advent Of Code - Day 13")

BUS_ID = int(PUZZLEINPUT[0])
BUS_LINES = [int(line) for line in PUZZLEINPUT[1].split(',') if line != 'x']

all_bus_line_times = {}
for line in BUS_LINES:
    temp = 0
    while temp < BUS_ID:
        temp += line
    # print(f'Bus line {line} is checked time is {temp}')
    
    all_bus_line_times.update({line:temp})
    
fastest_bus_line = min(all_bus_line_times, key=all_bus_line_times.get)
depart_time = all_bus_line_times[fastest_bus_line] - BUS_ID
print(f'Part 1: Fastest line is line {fastest_bus_line} with depart wait time {depart_time}, answer {fastest_bus_line*depart_time}')

#Rearrange data structure for part 2
BUSES = PUZZLEINPUT[1].split(',')
BUS_LINES = [(int(BUSES[line]), line) for line in range(len(BUSES)) if BUSES[line] != 'x']

least_commen_multiplier = 1
time = 0    
for i in range(len(BUS_LINES)-1):
    bus_id = BUS_LINES[i+1][0]
    idx = BUS_LINES[i+1][1]
    least_commen_multiplier *= BUS_LINES[i][0]
    while (time + idx) % bus_id != 0:
        time += least_commen_multiplier

print(f'Part 2: Fastest time is {time}')