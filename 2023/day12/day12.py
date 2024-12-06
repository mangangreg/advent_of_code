from pathlib import Path
from itertools import combinations
import re
HERE = (Path.home()/'pdev/advent_of_code/2023/day12').resolve()

# an enum that maps #:SPRING, .:EMPTY, ?:UNKNOWN
class Cell:
    SPRING = '#'
    EMPTY = '.'
    UNKNOWN = '?'

def read_input(fpath):
    lines = []
    with open(fpath, 'r') as f:
        for raw_line in f:
            row, record = [part.strip() for part in raw_line.strip().split(' ')]
            record = [int(x) for x in record.split(',')]
            lines.append({'row': row, 'record': record})

    return lines

def is_valid(row, record):
    if Cell.UNKNOWN in row:
        raise ValueError('Row contains unknown cells')
    collapsed_row = re.sub(f'\{Cell.EMPTY}+', ' ',row)
    clustered = collapsed_row.split(' ')
    if len(clustered) != len(record):
        return False
    else:
        for i in range(len(record)):
            if len(clustered[i]) != record[i]:
                return False
    return True

def solve():

    # strip empties on either side

    # Cluster the available

    pass


def part1(fpath):
    lines = read_input(fpath)
    
    
    ans = None
    x = is_valid('#..#.###', [1,1,3])
    print(x)

    return ans

# def part2(fpath, scale=1_000_000):
#     lines = read_input(fpath)
#     row_gaps, column_gaps = identify_gaps(lines)
#     distances = get_distances(lines, row_gaps=row_gaps, column_gaps=column_gaps, scale=scale)

#     ans = sum(pair["manhattan_distance"] for pair in distances)

#     return ans

def main():
    res1 = part1(HERE/'sample1.txt')
    # assert res1 == 374
    # print(res1)

    # res1 = part1(HERE/'input.txt')
    # assert res1 == 9522407
    # print(res1)

    # res2 = part2(HERE/'sample1.txt', scale=10)
    # print(res2)

    # res2 = part2(HERE/'input.txt')
    # print(res2)
    
    # pass


if __name__ == '__main__':
    main()