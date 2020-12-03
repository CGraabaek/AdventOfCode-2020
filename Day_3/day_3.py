print("Advent Of Code - Day 3")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")

def getTreeCount(input,slope):
    STEP_RIGHT,STEP_DOWN = slope
    pos_x = 0
    pos_y= 0
    trees = 0
    for row in PUZZLEINPUT:
        pos_x += STEP_RIGHT
        pos_y += STEP_DOWN

        if (pos_x,pos_y) in tree_map:
            trees += 1
    return trees


#Extend the map 5 --> 
for idx,val in enumerate(PUZZLEINPUT):
    for i in range(0,7):
        PUZZLEINPUT[idx] += PUZZLEINPUT[idx]

x_coor = len(PUZZLEINPUT[0]) 
y_coor = len(PUZZLEINPUT)

#Get a map of where all trees are located
tree_map = [(x,y) for y in range(0,y_coor) for x in range(0,x_coor) if PUZZLEINPUT[y][x] == "#"]



trees_product = 1;
SLOPES = [(1,1),(3,1),(5,1),(7,1),(1,2)]
for slope in SLOPES:
    tree_count = getTreeCount(PUZZLEINPUT,slope)
    print(f'Slope {slope} has {tree_count} trees')
    trees_product *= tree_count

print(f'Part 1: Trees {getTreeCount(PUZZLEINPUT,(3,1))}')
print(f'Part 2: Tree Product {trees_product}')