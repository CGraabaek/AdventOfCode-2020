print("Advent Of Code - Day 3 - Viz")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
print(PUZZLEINPUT[0])
memory = array(map(str, PUZZLEINPUT))



#Extend the map 5 --> 
for idx,val in enumerate(PUZZLEINPUT):
    for i in range(0,5):
        PUZZLEINPUT[idx] += PUZZLEINPUT[idx]


x_coor = len(PUZZLEINPUT[0]) 
y_coor = len(PUZZLEINPUT)
print(f'xLen {x_coor} - yLen {y_coor}')

# Create x by y grid

squares = [[] for i in range(y_coor)]
for i in range(y_coor):
    for j in range(x_coor):
        squares[i].append([])


tree_map = [(x,y) for y in range(0,y_coor) for x in range(0,x_coor) if PUZZLEINPUT[y][x] == "#"]

for trees in tree_map: 
    x,y = trees
    # print(f'x {x} - y {y}')
    memory[x][y] = "X"

print(memory)

