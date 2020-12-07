import time
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

N = 8
M = 128

plane = [[']'] for i in range(N)]
for i in range(N):
    for j in range(M):
        plane[i].append(']')

def printArray(args):
    print ("\t".join(args))

def print_plane():
    print(chr(27) + "[2J")
    print('                                                                                                                 --------------------')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 | / / / / / / / /  |')
    print('                                                                                                                 | \ \ \ \ \ \ \ \  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                               <=|                  |')
    print('                                                                                                               <=|                  |')
    print('                                                                                                               <=|                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                               <=|                  |')
    print('                                                                                                               <=|                  |')
    print('                                                                                                               <=|                  |')
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in plane]))
    print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('                                                                                                               <=|                  |')
    print('                                                                                                               <=|                  |')
    print('                                                                                                               <=|                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                               <=|                  |')
    print('                                                                                                               <=|                  |')
    print('                                                                                                               <=|                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 | / / / / / / / /  |')
    print('                                                                                                                 | \ \ \ \ \ \ \ \  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 |                  |')
    print('                                                                                                                 --------------------')

def set_plane(x,y):
    plane[x][y] = bcolors.OKGREEN+"#]"+bcolors.ENDC

import math

print("Advent Of Code - Day 5")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")

boarding_passes = []
seat_ids = []

def get_middle(range):
    x,y = range
    length = y-x
    return math.ceil(y-length/2)

def get_seat(boarding_pass_number):
    row_position = (0,127)
    col_position = (0,7)

    for direction in boarding_pass_number:
        if(direction == 'B'):
            row_x,row_y = row_position
            row_position = (get_middle(row_position),row_y)
        elif(direction == 'F'):
            row_x,row_y = row_position
            row_position = (row_x,get_middle(row_position)-1)
        elif(direction == 'R'):
            row_x,row_y = col_position
            col_position = (get_middle(col_position),row_y)
        elif(direction == 'L'):
            row_x,row_y = col_position
            col_position = (row_x,get_middle(col_position)-1)
        else:
           print(f'Direction {direction} doenst exist')
    
    seat = (row_position[0],col_position[0])
    return seat

for boarding_pass in PUZZLEINPUT:
    time.sleep(0.01)
    print_plane()
    seat = get_seat(boarding_pass)
    seat_ids.append(seat[0]*8+seat[1])
    print(f'Boarding Pass {boarding_pass} is row {seat[0]} seat {seat[1]} and SeatID {seat[0]*8+seat[1]}')
    set_plane(seat[1],seat[0])
    boarding_passes.append(seat)

#Function to find a missing integer in a list 
def find_missing(lst): 
    return [i for x, y in zip(lst, lst[1:])  
        for i in range(x + 1, y) if y - x > 1] 

# Could have just sorted the list and taken last index, eh? 
highest_seatid = max(x*8+y for x,y in boarding_passes)
print(f'Part 1: Highest Seat ID {highest_seatid}')

#Sort the list so we can find the missing seat
seat_ids.sort()
print(f'Part 2: My Seat ID {find_missing(seat_ids)}')

