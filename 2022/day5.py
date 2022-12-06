import re

RE_INSTRUCTION = 'move (?P<move>\d+) from (?P<from>\d+) to (?P<to>\d+)'
INPATH = 'day5_input.txt'
INPATH_TEST = 'day5_input_test.txt'

def parse_input(inpath):
    crate_rows, instruction_rows = [], []
    found_seperator = False

    # Grab the two chunks
    with open(inpath, 'r') as rfile:
        for line in rfile:
            if not found_seperator and not len(line.strip()):
                found_seperator = True 
                continue
            elif not found_seperator:
                crate_rows.append(line)
            else:
                instruction_rows.append(line)
    
    # Parse crates
    stacks = {}
    n_stacks = n = int(len(crate_rows[0])/4)
    for row in crate_rows[:-1]:
        for ind in range(0,n):
            key = ind+1
            block = row[ind*4 : ind*4 + 4]
            if block.strip():
                letter = re.search('[A-Z]', block).group()
                if not (key) in stacks:
                    stacks[key] = []
                stacks[key] = [letter] + stacks[key]

    # parse instructions
    instructions = []
    for row in instruction_rows:
        instr = re.match(RE_INSTRUCTION, row.strip()).groupdict()
        for key in instr:
            instr[key] = int(instr[key])
        instructions.append(instr)
    
    return stacks, instructions

def move_crates(stacks,instructions, cratemover=9000):
    for instr in instructions:
        if cratemover == 9000:
            for _ in range(instr['move']):
                stacks[instr['to']].append(stacks[instr['from']].pop())
        elif cratemover == 9001:
            temp = []
            for _ in range(instr['move']):
                temp = [(stacks[instr['from']].pop())] + temp
            stacks[instr['to']] = stacks[instr['to']] + temp
        else:
            raise ValueError('Uh oh...')
    return stacks 

def get_message(stacks):
    return ''.join(stacks[key][-1] for key in sorted(stacks.keys()))

def crate_job(inpath, cratemover):
    stacks, instructions = parse_input(inpath)
    stacks = move_crates(stacks, instructions, cratemover=cratemover)
    return get_message(stacks)

def part1():
    return crate_job(INPATH, cratemover=9000)

def part2():
    return crate_job(INPATH, cratemover=9001)

if __name__ == '__main__':
    res1 = part1()
    print(res1)
    res2 = part2()
    print(res2)

