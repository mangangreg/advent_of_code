from pathlib import Path
from collections import defaultdict
HERE = (Path.home()/'pdev/advent_of_code/2023/day15').resolve()

def read_input(fpath):
    with open(fpath, 'r') as rfile:
        text = rfile.read().strip()

    sequence = text.split(',')

    return sequence

def hash_algo(string):
    current_val = 0
    for char in string:
        current_val += ord(char)
        current_val *= 17
        current_val %= 256
    return current_val


def part1(fpath):
    sequence = read_input(fpath)
    
    # ans = 0 
    # for string in sequence:
    #     ans += hash_algo(string)
    
    vals = [hash_algo(string) for string in sequence]
    print(vals)
    ans = sum(vals)

    return ans

def parse_instruction(chars):
    if chars.endswith('-'):
        label = chars[:-1]
        action = 'subtract'
        focal_length = None
    else:
        label, focal_length = chars.split('=')
        action = 'add'
        focal_length = int(focal_length)
    return label, action, focal_length

def update_boxes(boxes, label, action, focal_length):
    box_id = hash_algo(label)

    if action == 'add':
        found = False
        for i, (existing_label, existing_focal_length) in enumerate(boxes[box_id]):
            if existing_label == label:
                boxes[box_id][i] = (label, focal_length)
                found = True 
        
        if not found:
            boxes[box_id].append((label, focal_length))

    elif action == 'subtract':
        for i, (existing_label, existing_focal_length) in enumerate(boxes[box_id]):
            if existing_label == label:
                boxes[box_id].pop(i)
                break
    
    return boxes

def print_boxes(boxes):
    for box_id, box in boxes.items():
        if len(box):
            contents = " ".join(f"[{label} {focal_length}]" for label, focal_length in box)
            print(f"Box {box_id}: {contents}")
        
def total_lens_power(boxes):
    total_power = 0
    for box_id, box in boxes.items():
        for slot_no,(label, focal_length) in enumerate(box,start=1):
            total_power += (box_id+1)*(slot_no)*focal_length
    return total_power

def part2(fpath):
    sequence = read_input(fpath)
    boxes = {i:[] for i in range(256)}

    for string in sequence:
        instruction = parse_instruction(string)
        boxes = update_boxes(boxes, *instruction)
        # print(f'After "{string}":')
        # print_boxes(boxes)
        # print('\n')

    ans = total_lens_power(boxes)
    return ans
def main():
    res1 = part1(HERE/'sample1.txt')
    print(res1)
    assert res1 == 1320

    # res1 = part1(HERE/'input.txt')
    # print(res1)
    # assert res1 == 519041

    res2 = part2(HERE/'sample1.txt')
    print(res2)

    res2 = part2(HERE/'input.txt')
    print(res2)
    
    pass


if __name__ == '__main__':
    main()