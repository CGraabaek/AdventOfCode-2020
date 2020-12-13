print("Advent Of Code - Day 12")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
# PUZZLEINPUT = open('test_input.txt', 'r').read().split("\n")

def manhattan_distance(pos):
    x,y=pos
    return abs(x) + abs(y)

def get_posistion(instructions):
    x, y = 0, 0
    current_direction = 'E'

    positions = []

    for instruction in instructions:
        direction = instruction[:1]
        distance = int(instruction[1:])
        
        print(f'Current direction {current_direction} Current pos {x,y} New Instruction {direction} with distance {distance}')
        if direction == 'F':
            if current_direction == "N":
                y +=distance
            elif current_direction == "S":
                y -=distance
            elif current_direction == "W":
                x -=distance
            elif current_direction == "E":
                x +=distance

        elif direction == "L":
            if distance == 90:
                if current_direction == "N":
                    current_direction = 'W'
                elif current_direction == "W":
                    current_direction = 'S'
                elif current_direction == "S":
                    current_direction = 'E'
                elif current_direction == "E":
                    current_direction = 'N'
            elif distance == 180: 
                if current_direction == "N":
                    current_direction = 'S'
                elif current_direction == "S":
                    current_direction = 'N'
                elif current_direction == "W":
                    current_direction = 'E'
                elif current_direction == "E":
                    current_direction = 'W'
            elif distance == 270:
                if current_direction == "N":
                    current_direction = 'E'
                elif current_direction == "E":
                    current_direction = 'S'
                elif current_direction == "S":
                    current_direction = 'W'
                elif current_direction == "W":
                    current_direction = 'N'
            distance = 0
        elif direction == "R":
            if distance == 90:
                if current_direction == "N":
                    current_direction = 'E'
                elif current_direction == 'E':
                    current_direction = 'S'
                elif current_direction == "S":
                    current_direction = 'W'
                elif current_direction == "W":
                    current_direction = 'N'
            elif distance == 180: 
                if current_direction == "N":
                    current_direction = 'S'
                elif current_direction == "W":
                    current_direction = 'E'
                elif current_direction == "E":
                    current_direction = 'W'
                elif current_direction == "S":
                    current_direction = 'N'
            elif distance == 270:
                if current_direction == "N":
                    current_direction = 'W'
                elif current_direction == "W":
                    current_direction = 'S'
                elif current_direction == "S":
                    current_direction = 'E'
                elif current_direction == "E":
                    current_direction = 'N'
            distance = 0
        # elif direction == 'N' or direction == 'S' or direction == 'E' or direction == 'W':
        #     current_direction = direction

        elif direction == "N":
            y +=distance
        elif direction == "S":
            y -=distance
        elif direction == "W":
            x -=distance
        elif direction == "E":
            x +=distance
        print(f'New postision is {x},{y} and direction {current_direction}')
        print("")
        positions.append((x, y))
    
    return positions

pos = get_posistion(PUZZLEINPUT)

print(f'Part 1: Manhatten Distance is: {manhattan_distance(pos[-1:][0])}')

# Part 2
#Refactoring part one, since roation is introduced
dirs = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}
def get_posistion_p2(instructions):
    xPos, yPos = 0, 0
    xWay, yWay = 10, 1
    for instruction in instructions:
        direction = instruction[:1]
        distance = int(instruction[1:])
        
        if direction in dirs:
            dx, dy = dirs[direction]
            xWay += distance * dx
            yWay += distance * dy
        elif direction == 'L' or direction == 'R':
            rotation = (distance if direction == 'R' else 360 - distance)
            if rotation == 90 or rotation == 270:
                tmp = yWay
                yWay = xWay * (-1 if rotation == 90 else 1)
                xWay = tmp * (1 if rotation == 90 else -1)
            elif rotation == 180:
                xWay *= -1
                yWay *= -1
        elif direction == 'F':
            xPos += distance * xWay
            yPos += distance * yWay
    return (xPos,yPos)

pos2 = get_posistion_p2(PUZZLEINPUT)


print(f'Part 1: Manhatten Distance is: {manhattan_distance(pos2)}')