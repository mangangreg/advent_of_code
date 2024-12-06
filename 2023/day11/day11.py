from pathlib import Path
from itertools import combinations

HERE = (Path.home()/'pdev/advent_of_code/2023/day11').resolve()


def read_input(fpath):
    lines = []
    with open(fpath, 'r') as f:
        lines = [list(line.strip()) for line in f]

    return lines



def expand_lines(lines):
    # expand rows
    new_lines = []
    n_columns = len(lines[0])
    for i in range(len(lines)):
        new_lines.append(lines[i])
        if all(char=='.' for char in lines[i]):
            new_lines.append(['.']*n_columns)

    # Expand columns 
    j = 0 
    while j < len(new_lines[0]):
        if all(line[j]=='.' for line in new_lines):
            for i in range(len(new_lines)):
                new_lines[i].insert(j, '.')
            j+=1
        j+=1

    return new_lines

def identify_gaps(lines):
    row_gaps = []
    for i in range(len(lines)):
        if all(char=='.' for char in lines[i]):
            row_gaps.append(i)
    
    column_gaps = []
    for j in range(len(lines[0])):
        if all(line[j]=='.' for line in lines):
            column_gaps.append(j)
    return row_gaps, column_gaps

def identify_galaxies(lines):
    galaxies = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                galaxies.append((i,j))
    return galaxies

def get_distance(a, b, gaps, scale=1_000_000):
    n_gaps = len(set(step for step in gaps if step>a and step<b))
    distance = (b-a) + n_gaps*scale - n_gaps
    return distance

def get_distances(lines, row_gaps=[], column_gaps=[], scale=1_000_000):
    distances = []
    galaxies = identify_galaxies(lines)

    pairs = list(combinations(galaxies,2))
    for galaxy_a, galaxy_b in pairs:
        if len(row_gaps) > 0 or len(column_gaps) > 0:    
            min_x, max_x = min(galaxy_a[0], galaxy_b[0]), max(galaxy_a[0], galaxy_b[0])
            min_y, max_y = min(galaxy_a[1], galaxy_b[1]), max(galaxy_a[1], galaxy_b[1])
            x_distance = get_distance(min_x, max_x, row_gaps, scale=scale)
            y_distance = get_distance(min_y, max_y, column_gaps, scale=scale)

        else:
            x_distance = abs(galaxy_a[0] - galaxy_b[0])
            y_distance = abs(galaxy_a[1] - galaxy_b[1])
        distances.append(
            {
                "galaxy_a": galaxy_a,
                "galaxy_b": galaxy_b,
                "x_distance": x_distance,
                "y_distance": y_distance,
                "manhattan_distance": x_distance + y_distance,}
        )
    return distances

def part1(fpath):
    lines = read_input(fpath)
    lines = expand_lines(lines)
    distances = get_distances(lines)

    ans = sum(pair["manhattan_distance"] for pair in distances)

    return ans

def part2(fpath, scale=1_000_000):
    lines = read_input(fpath)
    row_gaps, column_gaps = identify_gaps(lines)
    distances = get_distances(lines, row_gaps=row_gaps, column_gaps=column_gaps, scale=scale)

    ans = sum(pair["manhattan_distance"] for pair in distances)

    return ans

def main():
    res1 = part1(HERE/'sample1.txt')
    assert res1 == 374
    print(res1)

    res1 = part1(HERE/'input.txt')
    assert res1 == 9522407
    print(res1)

    res2 = part2(HERE/'sample1.txt', scale=10)
    print(res2)

    res2 = part2(HERE/'input.txt')
    print(res2)
    
    pass


if __name__ == '__main__':
    main()