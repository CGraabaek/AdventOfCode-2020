import re
import itertools

print("Advent Of Code - Day 4")

valid_passports = []

PUZZLEINPUT = open('input.txt', 'r').read().split("\n\n")

p = re.compile('byr|iyr|eyr|hgt|hcl|ecl|pid')


for line in PUZZLEINPUT:
    match = p.findall(line)
    if(len(match) == 7):
        valid_passports.append(line)

print(f'Part 1: Valid Passports {len(valid_passports)}')


def validate_password(passport):
    valid_passport_count = 0
    for elem in passport:
        key_val = elem.split(':')
    
        prop = key_val[0]
        val = key_val[1]

        if(prop == 'cid'):
            valid=False
        if(prop == 'byr'):
            if int(val) >= 1920 and int(val) <= 2002:
                valid_passport_count += 1
        if(prop == 'iyr'):
            if int(val) >= 2010 and int(val) <= 2020:
                valid_passport_count += 1
        if(prop == 'eyr'):
            if int(val) >= 2020 and int(val) <= 2030:
                valid_passport_count += 1
        if(prop == 'hgt'):
            if "cm" in val:
                height = int(val.split("cm")[0])
                if height >= 150 and height <= 193:
                    valid_passport_count += 1
            elif "in" in val:                
                height = int(val.split("in")[0])
                if height >= 59 and height <= 76:
                    valid_passport_count += 1
            # print(f'hgt {valid} ')
        if(prop == 'hcl'):
            if re.match(r"#([0-9a-z])([0-9a-z])([0-9a-z])([0-9a-z])([0-9a-z])([0-9a-z])", val):
                valid_passport_count += 1
        if(prop == 'ecl'):
            if val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                valid_passport_count += 1
        if(prop == 'pid'):
            if val.isdigit() and len(val) == 9:
                valid_passport_count += 1        
    return valid_passport_count

valid = 0
for passport in valid_passports:
    full_passport = []
    
    partial_passport = passport.split('\n')

    for elem in partial_passport:
        all_elem = elem.split()
        for elem in all_elem:
            full_passport.append(elem)

    print('*********************')
    print(f'Validating passport {full_passport}')
    password_valid = validate_password(full_passport)

    if password_valid == 7:
        valid += 1
    print('*********************')
    
print(f"Valid password {valid} ")


match = re.match(r"#([0-9a-z])([0-9a-z])([0-9a-z])([0-9a-z])([0-9a-z])([0-9a-z])", "456623")
print(match)
