from pathlib import Path
HERE = (Path.home()/'pdev/advent_of_code/2023/day13').resolve()

def read_input(fpath):
    patterns = []
    current_pattern = []
    with open(fpath, 'r') as f:
        for raw_line in f:
            line = raw_line.strip()
            if not len(line):
                patterns.append(current_pattern)
                current_pattern = []
            else:
                current_pattern.append(line)
    
    patterns.append(current_pattern)
    return patterns

def equal(it_1, it_2, max_diff=0):
    """ Check if two iterators are equal, with a maximum number of differences allowed"""
    n_diff = 0
    try:
        while True:
            val_1, val_2 = next(it_1), next(it_2)
            if val_1 != val_2:
                n_diff += 1 
            if n_diff > max_diff:
                return False, n_diff
    except StopIteration:
        return True, n_diff
    
def potential_reflection_idx(n):
    """ Find potential reflection lines as index pairs, turns out it could be any"""
    return [(i, i+1) for i in range(n-1)]
    
def find_reflection_idx(pattern, n_smudges=0):
    # Horizontal
    is_horizontal = True 
    n_rows = len(pattern) 
    for (top,bottom) in potential_reflection_idx(n_rows):
        
        ptr_top, ptr_bottom = top, bottom 
        is_valid = True
        total_smudge_diffs = 0
        while is_valid and ptr_top >=0 and ptr_bottom <= n_rows-1:
            it_1 = iter(pattern[ptr_top])
            it_2 = iter(pattern[ptr_bottom])
            is_equal, n_diff = equal(it_1, it_2, max_diff=n_smudges)
            if not is_equal:
                is_valid = False
            else:
                total_smudge_diffs += n_diff
            ptr_top -= 1
            ptr_bottom += 1

        if is_valid and total_smudge_diffs==n_smudges:
            return (top, bottom), is_horizontal
        
    # Vertical
    is_horizontal = False
    n_columns = len(pattern[0])
    for (left,right) in potential_reflection_idx(n_columns):
        ptr_left, ptr_right = left, right 
        is_valid = True
        total_smudge_diffs = 0
        while is_valid and ptr_left >=0 and ptr_right <= n_columns-1:
            it_1 = iter([row[ptr_left] for row in pattern])
            it_2 = iter([row[ptr_right] for row in pattern])
            is_equal, n_diff = equal(it_1, it_2, max_diff=n_smudges)
            if not is_equal:
                is_valid = False
            else:
                total_smudge_diffs += n_diff
            ptr_left -= 1
            ptr_right += 1

        if is_valid and total_smudge_diffs==n_smudges:
            return (left, right), is_horizontal
        
        
def pattern_value(index, is_horizontal):
    """ Get the value of a pattern given the index of the 'start' of the reflection, and whether it is horizontal or vertical"""
    if is_horizontal:
        return 100 * (index+1)
    else:
        return (index+1)


def part1(fpath, n_smudges=0):
    patterns = read_input(fpath)
    results = [find_reflection_idx(pattern, n_smudges=n_smudges) for pattern in patterns]
    values = [pattern_value(left, is_horizontal) for ((left,right), is_horizontal) in results]
    ans = sum(values)
    return ans

def part2(fpath):
    return part1(fpath, n_smudges=1)

def main():

    res1 = part1(HERE/'sample1.txt')
    print(res1)
    assert res1 == 405

    res1 = part1(HERE/'input.txt')
    print(res1)
    assert res1 == 33356

    res2 = part2(HERE/'sample1.txt')
    print(res2)
    assert res2 == 400

    res2 = part2(HERE/'input.txt')
    print(res2)
    assert res2 == 28475

if __name__ == '__main__':
    main()