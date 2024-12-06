from pathlib import Path
HERE = (Path.home()/'pdev/advent_of_code/2023/day9').resolve()

def parse_input(fpath):
    
    with open(fpath, 'r') as f:
        rows = f.readlines()
    
    data = [[int(x) for x in row.strip().split()] for row in rows]
    return data
   



# Solution functions
def part1(fpath ):
    data = parse_input(fpath)
    next = []
    for row in data:
        last_vals = []

        while any(val!=0 for val in row): 
            last_vals.append(row[-1])
            row = [row[i+1] - row[i] for i in range(len(row)-1)]
        # print(last_vals)
        next.append(sum(last_vals))
    ans = sum(next)
    
    return ans

def part2(fpath ):
    data = parse_input(fpath)
    before = []
    for row in data:
        first_vals = []

        while any(val!=0 for val in row): 
            # print(f"{row=}")
            first_vals.append(row[0])
            row = [row[i+1] - row[i] for i in range(len(row)-1)]

        first_before = 0
        sign = 1
        for val in first_vals:
            first_before += val * sign
            sign *= -1

        before.append(first_before)

        # print(f"{first_before=}")
    ans = sum(before)
    
    return ans

def main():
    res1 = part1(HERE/'sample.txt')
    print(res1)
    assert res1 == 114

    res1 = part1(HERE/'input.txt')
    # assert res1 == 457535844
    print(res1)

    res2 = part2(HERE/'sample.txt')
    print(res2)
    assert res2 == 2

    res2 = part2(HERE/'input.txt')
    print(res2)
    # 41222968



if __name__ == '__main__':
    main()