import re
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("Advent Of Code - Day 2")

valid_passwords = 0

PUZZLEINPUT = open('input.txt', 'r').read().strip().split("\n")

regex_pattern = r"([0-9]+)-([0-9]+) ([a-z]+): ([a-z]+)"

def validatePassword(pw,min_limit,max_limit,character,scheme):    
    if scheme == 1:
        formattedpw = ""
        r = range(min_limit, max_limit+1)
        lettercount = password.count(character)

        is_valid = lettercount in r

        if is_valid:
            for letter in pw:
                if letter == character:
                     formattedpw += bcolors.OKGREEN + letter + bcolors.ENDC
                else:
                    formattedpw += letter
            print("[{:<1}] {:<2}-{:<5} {:<3}: {:>15}".format(bcolors.OKGREEN+'PASS'+bcolors.ENDC,min_limit,max_limit,character,formattedpw))
            # print(f'{min_limit}-{max_limit}   {character}: {formattedpw} {bcolors.OKGREEN}PASS{bcolors.ENDC}')
        else:
            error_code = ""
            if lettercount > max_limit:
                for letter in pw:
                    if letter == character:
                        formattedpw += bcolors.WARNING + letter + bcolors.ENDC
                    else:
                        formattedpw += letter
                error_code = bcolors.WARNING+ "TOO MANY (" + str(lettercount) + " > " + str(max_limit)+")"  + bcolors.ENDC
            elif lettercount < min_limit: 
                for letter in pw:
                    if letter == character:
                        formattedpw += bcolors.OKBLUE + letter + bcolors.ENDC
                    else:
                        formattedpw += letter
                error_code = bcolors.OKBLUE +  "TOO FEW (" + str(lettercount) + " < " + str(min_limit)+")" + bcolors.ENDC
            print("[{:<1}] {:<2}-{:<5} {:<3}: {:<2}  {:>30}".format(bcolors.FAIL+'FAIL'+bcolors.ENDC,min_limit,max_limit,character,formattedpw,error_code))
            # print(f'{min_limit}-{max_limit}   {character}: {formattedpw} {bcolors.FAIL}FAIL{bcolors.ENDC} - {error_code}')
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
print('*'*58)
print(f'* {bcolors.WARNING}Part 1{bcolors.ENDC} : Valid Passwords:  {bcolors.OKGREEN}{valid_passwords}{bcolors.ENDC} | Invalid Passwords {bcolors.FAIL}{len(PUZZLEINPUT)- valid_passwords}{bcolors.ENDC} *')
print('*'*58)