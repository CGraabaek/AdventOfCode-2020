print("Advent Of Code - Day 14")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
COMMANDS = []    

for line in PUZZLEINPUT:
    plan = {}
    if 'mask' in line:
        plan["mask"]=line
    else: 
        plan["mem"]=line
    COMMANDS.append(plan)


# for comm,col in COMMANDS.items():
#     print(comm + " - " + col)


for comm in COMMANDS:
    print(comm)