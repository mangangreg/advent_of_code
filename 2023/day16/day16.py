from pathlib import Path
HERE = (Path.home()/'pdev/advent_of_code/2023/day16').resolve()

class Beam:

    def __init__(self, x,y, heading):
        self.x = x
        self.y = y
        self.heading = heading

    def __repr__(self):
        return f"Beam( ({self.x},{self.y}) -> {self.heading})"

class Cell:

    def __init__(self, x,y, label):
        self.x = x
        self.y = y
        self.label = label
        self.beams_seen = set()
        self.energized = False

    def get_next_loc(self, direction):
        if direction == 'n':
            return self.x-1, self.y
        elif direction == 's':
            return self.x+1, self.y
        elif direction == 'w':
            return self.x, self.y-1
        elif direction == 'e':
            return self.x, self.y+1
        
    def reflection_direction(self, heading, forward):
        if heading == 'e':
            return 'n' if forward else 's'
        elif heading == 'w':
            return 's' if forward else 'n'
        elif heading == 'n':
            return 'e' if forward else 'w'
        elif heading == 's':
            return 'w' if forward else 'e'

    def pass_through(self, heading):
        self.energized = True
        if heading in self.beams_seen:
            return []
        else:
            self.beams_seen.add(heading)

        if self.label == '.':
            return [(self.get_next_loc(heading), heading)]
        elif self.label == '|':
            if heading in ('n', 's'):
                return [(self.get_next_loc(heading), heading)]
            else:
                return [(self.get_next_loc('n'),'n'), (self.get_next_loc('s'),'s')]
        elif self.label == '-':
            if heading in ('e', 'w'):
                return [(self.get_next_loc(heading),heading)]
            else:
                return [(self.get_next_loc('e'),'e'), (self.get_next_loc('w'),'w')]
        elif self.label in ('/', '\\'):
            forward = self.label == '/'
            new_direction = self.reflection_direction(heading, forward)
            return [(self.get_next_loc(new_direction), new_direction)]
            
    def __repr__(self):
        return f"Cell( ({self.x},{self.y}) '{self.label}' {str(self.energized)[0]})"


class Board:

    def __init__(self, lines):
        self.cells = []
        self.beams = []
        # self.max_x = len(lines[0])
        # self.max_y = len(lines)
        for row_ind, raw_line in enumerate(lines):
            line = [Cell(row_ind, col_ind, label) for col_ind, label in enumerate(raw_line)]
            self.cells.append(line)

        self.shape = (len(self.cells), len(self.cells[0]))

    def print(self):
        for row in self.cells:
            output = ['#' if cell.energized else '.' for cell in row]
            print("".join(output))

def read_input(fpath):
    # lines = []
    with open(fpath, 'r') as f:
        lines = [list(line.strip()) for line in f]

    return lines


def run_beam(lines, start_x=0, start_y=0, start_heading='e'):
    board = Board(lines)
    beam = Beam(start_x,start_y, start_heading)
    board.beams.append(beam)
    
    step = 1
    while len(board.beams) >0:
        n_beams = len(board.beams)
        new_beams = []
        for i in range(n_beams):
            beam = board.beams.pop(0)
            x,y = beam.x, beam.y
            cell = board.cells[x][y]
            passthroughs = cell.pass_through(beam.heading)
            for loc,heading in passthroughs:
                if(loc[0] < 0 or loc[1] < 0):
                    continue
                elif loc[0] >= board.shape[0] or loc[1] >= board.shape[1]:
                    continue
                else:
                    new_beams.append(Beam(*loc,heading))

        board.beams = new_beams
        step += 1
    
    ans = sum( sum(cell.energized for cell in row) for row in board.cells )

    return ans


def part1(fpath):
    lines = read_input(fpath)
    ans = run_beam(lines)
    return ans

def part2(fpath):
    lines = read_input(fpath)

    n_rows, n_cols = len(lines), len(lines[0])

    possible_answers = []
    # Top line
    for start_y in range(1, n_rows-1):
        ans = run_beam(lines, start_x=0, start_y=start_y, start_heading='s')
        possible_answers.append(ans)

    # bottom line
    for start_y in range(1, n_rows-1):
        ans = run_beam(lines, start_x=(n_rows-1), start_y=start_y, start_heading='n')
        possible_answers.append(ans)

    # left line
    for start_x in range(1, n_cols-1):
        ans = run_beam(lines, start_x=start_x, start_y=0, start_heading='e')
        possible_answers.append(ans)

    # right line
    for start_x in range(1, n_cols-1):
        ans = run_beam(lines, start_x=start_x, start_y=(n_cols-1), start_heading='w')
        possible_answers.append(ans)

    # TOp left corner
    possible_answers.append(run_beam(lines, start_x=0, start_y=0, start_heading='s'))
    possible_answers.append(run_beam(lines, start_x=0, start_y=0, start_heading='e'))

    # Top right corner
    possible_answers.append(run_beam(lines, start_x=0, start_y=(n_cols-1), start_heading='s'))
    possible_answers.append(run_beam(lines, start_x=0, start_y=(n_cols-1), start_heading='w'))

    # Bottom left corner
    possible_answers.append(run_beam(lines, start_x=(n_rows-1), start_y=0, start_heading='n'))
    possible_answers.append(run_beam(lines, start_x=(n_rows-1), start_y=0, start_heading='e'))

    # Bottom right corner
    possible_answers.append(run_beam(lines, start_x=(n_rows-1), start_y=(n_cols-1), start_heading='n'))
    possible_answers.append(run_beam(lines, start_x=(n_rows-1), start_y=(n_cols-1), start_heading='w'))

    ans = max(possible_answers)
    return ans

def main():
    res1 = part1(HERE/'sample1.txt')
    print(res1)
    assert res1 == 46

    res1 = part1(HERE/'input.txt')
    print(res1)
    assert res1 == 7046

    res2 = part2(HERE/'sample1.txt')
    print(res2)
    assert res2 == 51

    res2 = part2(HERE/'input.txt')
    print(res2)
    assert res2 == 7313
    
    # pass


if __name__ == '__main__':
    main()