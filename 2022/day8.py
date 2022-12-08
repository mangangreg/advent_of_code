
from operator import truediv


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

    def tree_visible(self, row, col):
        try:
            if self.is_edge(row,col):
                return True

            # from left
            elif self.treemap[row,col] > max(self.treemap[row,x] for x in range(0,col)):
                return True

            # from right
            elif self.treemap[row,col] > max(self.treemap[row,x] for x in range(col+1,self.n_columns)):
                return True
            
            # from top
            elif self.treemap[row,col] > max(self.treemap[x,col] for x in range(0,row)):
                return True
            
            # from bottom
            elif self.treemap[row,col] > max(self.treemap[x,col] for x in range(row+1, self.n_rows)):
                return True

            return False
        except:
            print('problem with', row, col)
            raise


def part1():
    inpath = 'day8_input.txt'
    input_rows = [line.strip() for line in open(inpath).readlines()]
    forest = Forest(input_rows)
    # import pdb;pdb.set_trace()
    res = sum(forest.tree_visible(*coords) for coords in forest.treemap)
    return res


res1 = part1()
print(res1)