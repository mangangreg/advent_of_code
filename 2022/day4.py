import re

RE_INPUT = '(\d+)\-(\d+)\,(\d+)\-(\d+)'
INPATH, INPATH_TEST= 'day4_input.txt', 'day4_input_test.txt'

def parse_input(inpath):
    with open(inpath, 'r') as rfile:
        pairs = []
        for line in rfile:
            match = re.match(RE_INPUT,line.strip())
            a,b,c,d = [int(x) for x in match.groups()]
            pairs.append( ((a,b), (c,d)) )
    return pairs

def has_full_overlap(assignment_1, assignment_2):
    return assignment_1.issubset(assignment_2) or assignment_2.issubset(assignment_1)

def has_any_overlap(assignment_1, assignment_2):
    return len(assignment_1.intersection(assignment_2)) > 0

def assignment(left, right):
    return set(range(left, right+1))

def part_1():
    pairs = parse_input(INPATH)
    true_count = 0
    for elf_1, elf_2 in pairs:
        true_count += has_full_overlap(assignment(*elf_1), assignment(*elf_2))
    return true_count

def part_2():
    pairs = parse_input(INPATH)
    true_count = 0
    for elf_1, elf_2 in pairs:
        true_count += has_any_overlap(assignment(*elf_1), assignment(*elf_2))
    return true_count

res_1 = part_1()
print(res_1)
res_2 = part_2()
print(res_2)