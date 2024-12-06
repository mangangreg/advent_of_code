from pathlib import Path
HERE = (Path.home()/'pdev/advent_of_code/2023/dayXX').resolve()

def read_input(fpath):
    lines = []
    with open(fpath, 'r') as f:
        lines = [line.strip() for line in f]

    return lines



def part1(fpath):
    lines = read_input(fpath)
    
    
    ans = None

    return ans

def part2(fpath):
    lines = read_input(fpath)

    pass
def main():
    res1 = part1(HERE/'sample1.txt')
    # print(res1)
    # assert res1 == 374

    # res1 = part1(HERE/'input.txt')
    # print(res1)
    # assert res1 == 9522407

    # res2 = part2(HERE/'sample1.txt')
    # print(res2)

    # res2 = part2(HERE/'input.txt')
    # print(res2)
    
    # pass


if __name__ == '__main__':
    main()