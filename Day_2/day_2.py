import re

print("Advent Of Code - Day 2")
valid_passwords = 0
valid_passwords2 = 0

PUZZLEINPUT = open('input.txt', 'r').read().strip().split("\n")

regex_pattern = r"([0-9]+)-([0-9]+) ([a-z]+): ([a-z]+)"

def validatePassword(pw,min_limit,max_limit,character,scheme):    
    if scheme == 1:
        r = range(min_limit, max_limit+1)
        lettercount = password.count(character)

        is_valid = lettercount in r

        return is_valid
    elif scheme == 2:
        letter_at_index1 = pw[min_limit-1] 
        letter_at_index2 = pw[max_limit-1] 

        if (letter_at_index1 == character or letter_at_index2 == character) and letter_at_index1 != letter_at_index2:        
            return True
        else:
            return False
    
for line in PUZZLEINPUT:
    match = re.match(regex_pattern,line)

    min_limit = int(match.group(1))
    max_limit = int(match.group(2))
    letter = str(match.group(3))
    password = str(match.group(4))
    isValid = validatePassword(password,min_limit,max_limit,letter,1)
    if isValid:
        valid_passwords += 1
    if validatePassword(password,min_limit,max_limit,letter,2):
        valid_passwords2 += 1

print(f'Part 1: Valid Passwords: {valid_passwords}')
print(f'Part 2: Valid Passwords: {valid_passwords2}')