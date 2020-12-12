print("Advent Of Code - Day 11")

PUZZLEINPUT = open('test_input.txt', 'r').read().split("\n")



old_layout = {}
for row_id, row in enumerate(PUZZLEINPUT):
    for seat_id,seat in enumerate(row):
        old_layout[row_id, seat_id] = seat

# for idx,row in enumerate(PUZZLEINPUT):
#     for seat_id,seat in enumerate(row):
        
#         print(f'SeatID {seat_id} - seat {seat}')
#         if seat == 'L' and row[seat_id+1] == 'L' or row[seat_id+1] == '.':
#             #print(PUZZLEINPUT[idx][seat_id])
#             # PUZZLEINPUT[idx][seat_id] = '#'

print(old_layout[2,6])