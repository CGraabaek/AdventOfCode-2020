import functools
print("Advent Of Code - Day 9")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
PUZZLEINPUT = [int(i) for i in PUZZLEINPUT]
FINAL_TARGET = 0

#PART 1
for idx,number in enumerate(PUZZLEINPUT[25:]):
    SUM_CHECK = PUZZLEINPUT[idx:idx+25]
    target = PUZZLEINPUT[idx+25]
    TEMP_SUM = set()
    
    for num in SUM_CHECK:
        for number2 in SUM_CHECK: 
            TEMP_SUM.add(num+number2)

    if target not in TEMP_SUM:
        FINAL_TARGET = target
        print(f'Part 1: XMAS DATA Weak number is {target}')
        break

#PART 2
for start in range(len(PUZZLEINPUT)):
    #The minimum sum has to be at least 2 numbers
    for end in range(start+2, len(PUZZLEINPUT)):
        sub_range = PUZZLEINPUT[start:end]
        if sum(sub_range) == FINAL_TARGET: 
            result2 = min(sub_range) + max(sub_range)
            print(f"Part 2: Found encryption weakness in {result2} in {sub_range}")