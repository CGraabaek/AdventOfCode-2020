from collections import Counter
import itertools

print("Advent Of Code - Day 10")


PUZZLEINPUT = open('input.txt', 'r').read().split("\n")
JOLT_ADAPTERS = [int(i) for i in PUZZLEINPUT]

MAX_RATED_JOLT = max(JOLT_ADAPTERS)+3
CHARGING_OUTLET = 0
#Add max rated jolt and the outlet
JOLT_ADAPTERS.append(MAX_RATED_JOLT)
JOLT_ADAPTERS.append(CHARGING_OUTLET)

JOLT_ADAPTERS = sorted(JOLT_ADAPTERS, reverse=False) 


joltages = [JOLT_ADAPTERS[i+1]-JOLT_ADAPTERS[i] for i in range(len(JOLT_ADAPTERS)-1)]
b = Counter(joltages)
print(f'Part 1 {b[1]*b[3]}')


def combs(a):
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    return cs

def powerSet(items):
    """
    Power set generator: get all possible combinations of a list’s elements

    Input:
        items is a list
    Output:
        returns 2**n combination lists one at a time using a generator 

    Reference: edx.org 6.00.2x Lecture 2 - Decision Trees and dynamic programming
    """

    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo


combis = itertools.combinations(JOLT_ADAPTERS,len(JOLT_ADAPTERS))
for comb in combis:
    print(comb)