from pathlib import Path
HERE = (Path.home()/'pdev/advent_of_code/2023/day14').resolve()

class Cell:
    CIRCLE = 'O'
    EMPTY = '.'
    ROCK = '#'


def read_input(fpath):
    lines = []
    with open(fpath, 'r') as f:
        lines = [list(line.strip()) for line in f]

    return lines

def resort_column(col,reverse=True):
    og_col = col 
    if type(og_col) is list:
        og_col = "".join(og_col)
    segments = og_col.split(Cell.ROCK)
    segments = ["".join(sorted(segment, reverse=reverse)) for segment in segments]
    new_col = list(Cell.ROCK.join(segments))
    return new_col

def column_load(col):
    n = len(col)
    load = sum(n-i for i in range(n) if col[i]==Cell.CIRCLE)
    return load

def update_lines(lines, ind, col=None, row=None):
    if row is not None:
        lines[ind] = row
    elif col is not None:
        for i, line in enumerate(lines):
            line[ind] = col[i]
    return lines



def part1(fpath):
    lines = read_input(fpath)
    n_cols = len(lines[0])

    ans = 0
    for col_ind in range(n_cols):
        col = [line[col_ind] for line in lines]
        col = resort_column(col)
        load = column_load(col)
        ans+= load 
        lines = update_lines(lines, ind=col_ind, col=col)
    
    # ans = None

    return ans

def part2(fpath, n_cycles=1000000000):
    lines = read_input(fpath)
    og_lines = lines

    n_rows, n_cols = len(lines), len(lines[0])

    seen_hashes = {}
    first_repeat = None
    one_time_skip = False

    i = 1

    while i<n_cycles:
        #tilt north
        new_cols = []
        for col_ind in range(n_cols):
            col = [line[col_ind] for line in lines]
            col = resort_column(col)
            new_cols.append(col)
            # lines = update_lines(lines, ind=col_ind, col=col)
        lines = [list(col) for col in zip(*new_cols)]
        #tile west
        new_lines = []
        for row_ind in range(n_rows):
            row = lines[row_ind]
            row = resort_column(row)
            # lines = update_lines(lines, ind=row_ind, row=row)
            new_lines.append(row)
        
        lines = new_lines
        
        #tilt south
        new_cols = []
        for col_ind in range(n_cols):
            col = [line[col_ind] for line in lines]
            col = resort_column(col, reverse=False)
            # lines = update_lines(lines, ind=col_ind, col=col)
            new_cols.append(col)
        lines = [list(col) for col in zip(*new_cols)]
        
        # tilt east
        new_lines = []
        for row_ind in range(n_rows):
            row = lines[row_ind]
            row = resort_column(row, reverse=False)
            # lines = update_lines(lines, ind=row_ind, row=row)
            new_lines.append(row)
        
        lines = new_lines
        if first_repeat is None:
            post_cycle_hash = hash("".join("".join(row) for row in lines))
            if post_cycle_hash not in seen_hashes:
                seen_hashes[post_cycle_hash] = i
                # print(seen_hashes)
            else:
                print('Found it!')
                first_repeat = (i, seen_hashes[post_cycle_hash])

                cycle_length = first_repeat[0] - first_repeat[1]

                while i+cycle_length<n_cycles:
                    i+=cycle_length
                print(f"Skipped to cycle {i}")
                one_time_skip = True

        print(f"{i=} total_load={total_load(lines)}")
        if one_time_skip:
            one_time_skip = False
        else:
            i+=1

        
    print(f"{i=}")
    print(f"{first_repeat=}")

    # Now get the answer
    ans = total_load(lines)

    return ans

def total_load(lines):
    ans = 0
    n_cols = len(lines[0])
    for col_ind in range(n_cols):
        col = [line[col_ind] for line in lines]
        load = column_load(col)
        ans+= load
    return ans

def main():
    res1 = part1(HERE/'sample1.txt')
    print(res1)
    assert res1 == 136

    res1 = part1(HERE/'input.txt')
    print(res1)
    assert res1 == 113456
    # assert res1 == 9522407

    res2 = part2(HERE/'sample1.txt')
    print(res2)

    res2 = part2(HERE/'input.txt')
    print(res2)
    assert res2 == 118747
    # Returning: 118780
    # Trying: 118779
    
    # pass


if __name__ == '__main__':
    main()