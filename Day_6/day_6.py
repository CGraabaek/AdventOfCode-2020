import re
from collections import Counter

PUZZLEINPUT = open('input.txt', 'r').read().strip().split("\n\n")
question_sum = 0
question_sum_p2 = 0


def get_group_sum(group):
    #Remove special characters from group, see answer: https://stackoverflow.com/questions/46376133/count-of-characters-in-a-string-excluding-special-characters
    content = re.sub('[^a-zA-Z]', '',group, flags=re.M)    
    b = Counter(content)
    
    return len(b)

def get_group_sum_overlap(group):
    #Create a list comprehension to handle all group answers
    group_answers  = [set(x) for x in group.split("\n") ]
    # get the intersection
    inter = set.intersection(*group_answers)

    return len(inter)

for group in PUZZLEINPUT:
    question_sum += get_group_sum(group)
    question_sum_p2 += get_group_sum_overlap(group)


print(f'Part 1: Question Sum is {question_sum}')
print(f'Part 2: Question Sum Overlapped is {question_sum_p2}')