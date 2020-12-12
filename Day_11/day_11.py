import math
print("Advent Of Code - Day 11")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")



floor_plan = {}
for row_id, row in enumerate(PUZZLEINPUT):
    for seat_id,seat in enumerate(row):
        floor_plan[row_id, seat_id] = seat

def print_floor_plan(cell_dimensions, grid):
    for y in range(cell_dimensions):
        print(' '.join(grid[y, x] for x in range(cell_dimensions)))
    print("")

def check_adjacent_seats(floor_plan,row,col,max_occupied):
    max_len = math.sqrt(len(floor_plan))
    adjacent_seats = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
            (row, col - 1),                      (row, col + 1),
            (row + 1, col - 1),  (row + 1, col), (row + 1, col + 1)]
    
    adjacent_list = []
    for neighbor in adjacent_seats:
        r,c = neighbor
        #Check that we are not out of bounds
        if r >= 0 and c >= 0 and r < max_len and c < max_len:
            adjacent_list.append(floor_plan[(r,c)])
        else:
            continue        
    occupied = max_occupied <= adjacent_list.count('#')
    return occupied

new_floor_plan = {}    
while True:
    for (row,col),seat in floor_plan.items():
        if seat == '.':
            new_floor_plan[row,col] = "."
        elif seat == 'L':
            if not check_adjacent_seats(floor_plan,row,col,1):
                new_floor_plan[row,col] = "#"
            else:
                new_floor_plan[row,col] = "L"
        elif seat == '#':
            if not check_adjacent_seats(floor_plan,row,col,4):
                new_floor_plan[row,col] = "#"
            else:
                new_floor_plan[row,col] = "L"
    
    print_floor_plan(int(math.sqrt(len(floor_plan))),new_floor_plan)
    
    if new_floor_plan == floor_plan:
        occupied_seats = [item for item in floor_plan.values() if item=='#']
        print(f'Part 1: Occupied Seats {len(occupied_seats)}')
        break
    floor_plan = {key: value for key, value in new_floor_plan.items()}
    
