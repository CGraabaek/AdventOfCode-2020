import re

print("Advent Of Code - Day 8")

PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
ALL_OPERATIONS = []
visited_instructions = set()

instruction_counter = 0
accumulator = 0

regex_pattern = r"([a-z]+) ([+-][0-9]+)"


#Parse the input to operations
for instruction in PUZZLEINPUT:
    match = re.match(regex_pattern,instruction)
    operation = match.group(1)
    argument = int(match.group(2))

    ALL_OPERATIONS.append((operation,argument))

# Part 1
def handle_operations(codes):
    accumulator = 0
    instruction_counter = 0
    visited_instructions = set()
    found_solution = False
    while True:
        if instruction_counter in visited_instructions:
            break
        if instruction_counter >= len(codes):
            found_solution = True
            break
        visited_instructions.add(instruction_counter)
        operation,argument = codes[instruction_counter]
        if operation == "acc":
            accumulator += argument
            instruction_counter += 1
        if operation == "jmp":
            instruction_counter += argument
        if operation == "nop":
            instruction_counter += 1
    return found_solution,accumulator

print(f"Part 1: Accumulator at loop restart {handle_operations(ALL_OPERATIONS)[1] }  ")

# Part 2
for i in range(len(ALL_OPERATIONS)):
    instruction,value = ALL_OPERATIONS[i]
    if instruction== "nop" or instruction == "jmp":
        copy_codes = list()

        for copy_code in ALL_OPERATIONS:
            copy_codes.append(copy_code)

        if instruction == "nop":
            copy_codes.remove(copy_codes[i])
            copy_codes.insert(i, ("jmp", value ))

        if instruction == "jmp":
            copy_codes.remove(copy_codes[i])
            copy_codes.insert(i, ("nop", value ))

        fixed_program,acc = handle_operations(copy_codes)
        if fixed_program:
            print(f"Part 2: Accumulator after fixing program {acc} ")
            