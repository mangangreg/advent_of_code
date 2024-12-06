from pathlib import Path

HERE = (Path.home()/'pdev/advent_of_code/2023/day10').resolve()
START = 'S'
DIRECTIONS = ['n','s','e','w']
REVERSE_DIRECTION = {
    'n':'s',
    's':'n',
    'e':'w',
    'w':'e'
}

PIPE_MAPPING = {
    '|':('n','s'),
    '-':('e','w'),
    'L':('n','e'),
    'J':('n','w'),
    '7':('s','w'),
    'F':('s','e'),
}

class Board:

    def __init__(self, lines, start):
        self.board = lines
        self.start = start 

    def __getitem__(self, loc):
        return self.board[loc[0]][loc[1]]

class Pipe:

    def __init__(self, loc, board):
        self.loc = loc
        self.label = board[loc]
        if self.label != '.':

            self.connection_dirs = PIPE_MAPPING[self.label] if self.label!= START else []
            self.connected_pipes = []
            self.board = board
        else:
            self.label = None

    def __bool__(self):
        return self.label is not None

    # def connects_to(self, dir):
    #     loc = self.move(dir)
    #     other = Pipe(loc, self.board)
    #     return REVERSE_DIRECTION[dir] in other.conection_dirs
        
    def move(self, direction):
        if direction == 'n':
            return self.loc[0]-1, self.loc[1]
        elif direction == 's':
            return self.loc[0]+1, self.loc[1]
        elif direction == 'e':
            return self.loc[0], self.loc[1]+1
        elif direction == 'w':
            return self.loc[0], self.loc[1]-1
        
    def __repr__(self):
        return f"Pipe({self.label} @ {self.loc})"


def read_input(fpath):
    lines = []
    start = -1,-1
    with open(fpath, 'r') as f:
        for i, line in enumerate(f):
            lines.append(list(line.strip()))
            try:
                start = i, line.index(START)
            except:
                continue

    assert start != -1,-1
    return lines, start

def parse_data(lines):
    board = lines 
    return board


def part1(fpath):
    lines, start = read_input(fpath)
    board = Board(lines, start)
    origin_ptr = Pipe(start, board)

    seen = set()
    seen.add(start)

    # Find the starting directions 
    for dir in DIRECTIONS:
        temp_loc = origin_ptr.move(dir)
        temp = Pipe(temp_loc, board)
        reverse = REVERSE_DIRECTION[dir]
        if temp and reverse in temp.connection_dirs: 
            origin_ptr.connected_pipes.append(temp)
            origin_ptr.connection_dirs.append(dir)
    origin_ptr.connection_dirs = tuple(origin_ptr.connection_dirs)

    # Iterate through the rest of the pipes 
    ptrs = [*origin_ptr.connected_pipes]
    for i in range(2): 
        ptrs[i].connected_pipes.append(origin_ptr)

    steps = 0
    while ptrs[0].loc not in seen or ptrs[1].loc not in seen:
        for i in range(2):
            if ptrs[i].loc not in seen: 
                seen.add(ptrs[i].loc) 
                # print(f"added {ptrs[i]=}")
                investigate_locs = [ptrs[i].move(dir) for dir in ptrs[i].connection_dirs]
                for temp_loc in investigate_locs:
                    if temp_loc not in seen:
                        new_ptr = Pipe(temp_loc, board)
                        new_ptr.connected_pipes.append(ptrs[i])
                        ptrs[i] = new_ptr

        steps +=1

    assert len(origin_ptr.connected_pipes) == 2

    return steps

def expand_lines(lines):
    extended_lines = []
    for line in (lines):
        constructed_line = []
        for ind in range(len(line)-1):
            left, right = line[ind], line[ind+1]
            constructed_line.append(left)
            if left=='.' or right=='.':
                constructed_line.append('.')
            elif left=='S':
                constructed_line.append('S')
            else:
                connected_dirs = PIPE_MAPPING[left]
                future_reverse_dirs = [REVERSE_DIRECTION[dir] for dir in PIPE_MAPPING[right]]
                overlap = set(connected_dirs).intersection(future_reverse_dirs)
                if len(overlap):
                    constructed_line.append('-')
                else:
                    constructed_line.append('.')

        constructed_line.append('.')
        extended_lines.append(constructed_line)
    
    new_inserts = [[] for _ in range(len(extended_lines))]
    for col in range(len(extended_lines[0])):
        for row in range(len(extended_lines)-1):
            up, down = extended_lines[row][col], extended_lines[row+1][col]
            if up=='.' or down=='.':
                new_inserts[row].append('.')
            elif up=='S':
                new_inserts[row].append('S')
            else:
                connected_dirs = PIPE_MAPPING[up]
                future_reverse_dirs = [REVERSE_DIRECTION[dir] for dir in PIPE_MAPPING[down]]
                overlap = set(connected_dirs).intersection(future_reverse_dirs)
                if len(overlap):
                    new_inserts[row].append('|')
                else:
                    new_inserts[row].append('.')
        new_inserts[-1].append('.')


    new_lines = []
    for i in range(len(extended_lines)):
        new_lines.append(extended_lines[i])
        new_lines.append(new_inserts[i])    

    print(len(new_lines))
    for line in new_lines:
        print("".join(line))
    return new_lines
    



def part2(fpath):
    lines, start = read_input(fpath)
    board = Board(lines, start)
    new_lines = expand_lines(lines)
    # print(new_lines)
    

    pass


def main():
    # res1 = part1(HERE/'sample1.txt')
    # print(res1)

    # res1 = part1(HERE/'sample2.txt')
    # print(res1)

    # res1 = part1(HERE/'input.txt')
    # print(res1)

    res2 = part2(HERE/'sample3.txt')
    print(res2)
    
    pass


if __name__ == '__main__':
    main()