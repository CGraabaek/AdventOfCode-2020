PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
print("Advent Of Code - Day 7")

all_bags = {}

for bag in PUZZLEINPUT:
    bag.replace("bags"," ")
    bags = bag.replace("bags","").replace("bag","").replace(".","").split('contain')
    bags[0] = bags[0].strip()
    bags[1] = bags[1].strip()
    
    all_bags[bags[0]] = bags[1]

def find_parents(all_bags,child_bag):
    for parent in all_bags:
        contents = all_bags[parent]
        if child_bag in contents:
            find_parents(all_bags,parent)
            confirmed_bags.add(parent)
    return

confirmed_bags = set()
find_parents(all_bags,"shiny gold")
print(f'Part 1: {len(confirmed_bags)} Shiny Gold Bags')

print(all_bags["shiny gold"])