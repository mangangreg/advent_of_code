from pathlib import Path
from math import gcd

HERE = (Path.home()/'pdev/advent_of_code/2023/day8').resolve()

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_of_list(numbers):
    result = 1
    for num in numbers:
        result = lcm(result, num)
    return result

def parse_input(fpath, only_one = False):
    with open(fpath, 'r') as f:
        lines = f.readlines()

    instructions = lines[0].strip()
    mappings = {}
    for line in lines[2:]:
        node, dest = [x.strip() for x in line.split('=')]
        left, right = [x.strip() for x in dest.strip('()').split(',')]
        mappings[node] = {'L':left, 'R': right}

    return instructions, mappings

# Solution functions
def part1(fpath,):
    instructions, mappings = parse_input(fpath)

    steps = 0
    index = 'AAA'
    while index != 'ZZZ':
        instruction = instructions[steps %len(instructions)]
        index = mappings[index][instruction]
        steps +=1
    return steps

def part2(fpath,):
    instructions, mappings = parse_input(fpath)

    pointers = [ptr for ptr in mappings.keys() if ptr[-1] == 'A']
    steps = [0 for _ in pointers]
    while any(ptr[-1] != 'Z' for ptr in pointers):
        for i in range(len(pointers)):
            if pointers[i][-1] != 'Z':
                instruction = instructions[steps[i] %len(instructions)]
                pointers[i] = mappings[pointers[i]][instruction]
                steps[i] +=1
    
    ans = lcm_of_list(steps)
    return ans

def main():
    res1_s1 = part1(HERE/'sample1.txt')
    print(res1_s1)
    assert res1_s1 == 2

    res1_s2 = part1(HERE/'sample2.txt')
    print(res1_s2)
    assert res1_s2 == 6

    res1_p = part1(HERE/'input.txt')
    print(res1_p)
    assert res1_p == 18673

    res2_s3 = part2(HERE/'sample3.txt')
    print(res2_s3)
    assert res2_s3 == 6

    res2_p = part2(HERE/'input.txt')
    print(res2_p)
    assert res1_p == 17972669116327



if __name__ == '__main__':
    main()