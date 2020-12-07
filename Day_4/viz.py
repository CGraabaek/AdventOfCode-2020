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


def printPassport(full_passport,number,appr):
    if appr:
        approved = bcolors.OKGREEN + "APPROVED" + bcolors.ENDC
    else:
        approved = bcolors.FAIL + "  DENIED" + bcolors.ENDC

    for elem in full_passport:
        key_val = elem.split(':')
        prop = key_val[0]
        val = key_val[1]
        cid = "???"
        if(prop == 'cid'):
            cid = val
        if(prop == 'byr'):
            byr = val
        if(prop == 'iyr'):
            iyr = val
        if(prop == 'eyr'):
            eyr = val
        if(prop == 'hgt'):
            hgt = val
        if(prop == 'hcl'):
            hcl = val
        if(prop == 'ecl'):
            ecl = val
        if(prop == 'pid'):
            pid = val

    print(chr(27) + "[2J")
    print(f'*----------------------------------------*')
    print('| {:<10}          |                    |'.format(approved))
    print('|                   |                    |')
    print(f'|                   |                    |')
    print('|                   |     PID:{:>10} |'.format(pid))
    print(f'|                   |                    |')
    print('|                   |  Y.O.B. : {:<5}    |'.format(byr))
    print(f'|                   |                    |')
    print('|                   |  ISSUED : {:<5}    |'.format(iyr))
    print(f'|                   |                    |')
    print('|                   |  EXPIRE : {:<5}    |'.format(eyr))
    print(f'|                   |                    |')
    print('|                   |  HEIGHT : {:>5}    |'.format(hgt))
    print(f'|                   |                    |')
    print('|                   |  HAIR CLR: {:>7} |'.format(hcl))
    print(f'|                   |                    |')
    print('|                   |  EYE CLR : {:>7} |'.format(ecl))
    print(f"*----------------------------------------*")
    print('')
    print(f'VALID PASSPORTS: {number}')