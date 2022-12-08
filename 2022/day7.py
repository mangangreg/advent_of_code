class Path:
    def __init__(self, path, is_dir=False, size=0, children=[]):
        self.path = path
        self.is_dir = is_dir
        self.size = size
        self.children = children
        
    def parts(self):
        return self.path.split('/')
    
    def parent(self):
        if self.path == '/':
            return None
        elif len(self.parts()) == 2:
            return Path('/', is_dir=True)
        else:
            return Path("/".join(self.parts()[:-1]))

    def __truediv__(self, other):
        return Path(f"{self.path if self.path!= '/' else ''}/{other}")

    def __str__(self):
        return self.path

    def __repr__(self):
        return f"<Path({'dir' if self.is_dir else 'file'}): path={self} size={self.size}>"

    def total_size(self):
        if not self.is_dir:
            return self.size
        else:
            return sum(child.total_size() for child in self.children)

def get_dir(path, pathmap):
    path = str(path)
    if path not in pathmap:
        new_dir = Path(path, is_dir=True)
        return new_dir, pathmap
    else:
        return pathmap[path], pathmap

def update_pathmap_from_ls_lines(pathmap, ls_lines, pwd):
    pwd.children = []
    for line in ls_lines:
        dir_or_size, name = line.split()
        new_node = pwd / name
        if dir_or_size == 'dir':
            new_node.is_dir = True
        else:
            new_node.size = int(dir_or_size)
        
        pathmap.update({str(new_node): new_node})
        pwd.children.append(new_node)

    return pathmap

def is_instruction(line):
    return line.startswith('$')

def parse_input(inpath):
    pathmap = {}
    root = Path('/', is_dir=True)
    pathmap.update({str(root): root})
    pwd = root

    with open(inpath, 'r') as rfile:
        lines = rfile.readlines()
        collecting_ls_lines = False 
        ls_lines = []
        while len(lines):
            line = lines.pop(0).strip()
            # print(line)

            # instruction
            if collecting_ls_lines:
                if is_instruction(line):
                    pathmap = update_pathmap_from_ls_lines(pathmap, ls_lines, pwd)
                    collecting_ls_lines = False
                    ls_lines = []
                else:
                    ls_lines.append(line)

            if is_instruction(line):
                # print('Found an instruction')
                cmd = line.lstrip('$').strip().split()
                print(f"{cmd=}")
                
                # list 
                if cmd[0] == 'ls':
                    collecting_ls_lines = True 
                    continue

                elif cmd[0] == 'cd':
                    # print(f'Changing pwd from {pwd}..')
                    arg = cmd[1]
                    if arg == '..':
                        pwd, pathmap = get_dir(str(pwd.parent()), pathmap)
                    else:
                        new_path = arg if arg.startswith('/') else pwd/arg
                        pwd, pathmap = get_dir(str(new_path), pathmap)
                    # print(f'... to {pwd}')

    if collecting_ls_lines:
        pathmap = update_pathmap_from_ls_lines(pathmap, ls_lines, pwd)
                    
    return pathmap


def part1():
    pathmap = parse_input('day7_input.txt')
    dir_sizes = [x.total_size() for x in pathmap.values() if x.is_dir]
    answer = sum( filter(lambda x: x<100000, dir_sizes))
    return answer
                     
def part2():
    pathmap = parse_input('day7_input.txt')
    dir_sizes = {path: pathobj.total_size() for path, pathobj in pathmap.items() if pathobj.is_dir} 
    free_space = 70000000 - dir_sizes['/']
    space_needed = 30000000 - free_space
    answer = min(filter(lambda x: x>=space_needed, dir_sizes.values()))
    return answer

res1 = part1()
print(res1)
res2 = part2()
print(res2)
print('hello?')