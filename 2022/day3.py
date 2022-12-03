ASCII_OFFSET = ord('a') - 1
INPATH = 'day3_input.txt'

def parse_input(inp_str):
    return [line.strip() for line in inp_str.split('\n')]

def char_value(char):
    return ord(char.lower()) - ASCII_OFFSET + 26*char.isupper()

def compartments_of(rsack):
    midpoint = int(len(rsack)/2)
    return (rsack[:midpoint], rsack[midpoint:])

def in_all(groupings):
    common = set(groupings[0])
    for group in groupings[1:]:
        common.intersection_update(group)
    return list(common)[0]

def part1():
    rucksacks = parse_input( open(INPATH).read() ) 
    return sum(char_value(in_all(compartments_of(rsack))) for rsack in rucksacks) 

def part2():
    rucksacks = parse_input(open(INPATH).read())
    elf_groups = (rucksacks[ind:ind+3] for ind in range(0, len(rucksacks), 3) )
    return sum(char_value(in_all(elf_group)) for elf_group in elf_groups)

if __name__ == '__main__':
    res1 = part1()
    print(res1)
    res2 = part2()
    print(res2)