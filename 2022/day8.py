DIRECTIONS = ['up', 'down', 'left', 'right']
class Forest:
    def __init__(self, input_rows):
        self.n_rows = len(input_rows)
        self.n_columns = len(input_rows[0])
        self.treemap = {}
        for row, input_row in enumerate(input_rows):
            for col, height in enumerate(input_row):
                self.treemap[(row,col)] = int(height)

    def is_edge(self, row, col):
        return row in (0, self.n_rows-1) or col in (0, self.n_columns-1) 

    def trees_in_direction(self, row, col, direction):
        ''' The sequence of tree heights in the given direction'''
        if direction == 'left':
            return reversed([self.treemap[row,x] for x in range(0,col)])
        if direction == 'right':
            return [self.treemap[row,x] for x in range(col+1,self.n_columns)] 
        if direction == 'up':
            return reversed([self.treemap[x,col] for x in range(0,row)])
        if direction == 'down':
            return [self.treemap[x,col] for x in range(row+1, self.n_rows)]

    def tree_visible(self, row, col):
        if self.is_edge(row,col):
            return True
        for direction in DIRECTIONS:
            if self.treemap[row,col] > max(self.trees_in_direction(row,col,direction)):
                return True
        return False
    
    def viewing_distance(self, row, col):
        if self.is_edge(row,col):
            return 0
        viewing_distance = 1

        for direction in DIRECTIONS:
            direction_distance = 0
            for height in self.trees_in_direction(row,col,direction):
                direction_distance += 1
                if height >= self.treemap[row,col]:
                    break 
            viewing_distance *= direction_distance

        return viewing_distance

def part1(forest):
    return sum(forest.tree_visible(*coords) for coords in forest.treemap)

def part2(forest):
    return max(forest.viewing_distance(*coords) for coords in forest.treemap)

inpath = 'day8_input.txt'
forest = Forest( [line.strip() for line in open(inpath).readlines()] )
print(part1(forest))
print(part2(forest))