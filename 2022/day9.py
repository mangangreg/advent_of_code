import re
RE_SIGNED_INT = '\-?\d+'

def parse_input(inpath):
    instructions = []
    with open(inpath, 'r') as rfile:
        for line in rfile:
            match = re.search(RE_SIGNED_INT, line)
            if match:
                instructions.append( int(match.group()) )
            else:
                instructions.append(0)
    return instructions


interesting_cycles = [20,60,100,140,180,220]

def sprite_row(pos):
    return '.'*(pos-1) + '#'*3 + '.'*(40-pos-2)

def process(inpath):
    instructions = parse_input(inpath)
    cycle = 1
    x = 1
    waiting = False
    current_instruction = 0

    interesting_data = []
    crt_rows = []
    current_row = ''

    while len(instructions) or waiting:
        print(f'During cycle{cycle} ({x=})')

        if cycle in interesting_cycles:
            interesting_data.append({'x':x, 'cycle': cycle})

        pixel_pos = (cycle % 40) - 1 
        pixel = '#' if pixel_pos in range(x-1,x+2) else '.'
        current_row += pixel

        if current_instruction == 0:
            current_instruction = instructions.pop(0)
            if current_instruction != 0:
                waiting = True
        else:
            if waiting:
                x += current_instruction
                print(f'End of cycle {cycle}: finish adding {current_instruction} ({x=})')
                print(f"Sprite position: {sprite_row(x)}")
                current_instruction = 0
                waiting = False

        cycle += 1
        if len(current_row) >= 40:
            crt_rows.append(current_row)
            current_row = ''

    res = sum(entry['x']*entry['cycle'] for entry in interesting_data)
    return res, crt_rows

INPATH = 'day9_input.txt'
res1, crt_data = process(INPATH)
print(res1)
for row in crt_data:
    print(row)
