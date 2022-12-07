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
        else:
            return Path("/".join(self.parts()[:-1]))

    def birth_child(self, name, **kwargs):
        child = Path(path=self/name, **kwargs)
        self.children.append(child)
        return child

    def __truediv__(self, other):
        return Path(f"{self.path if self.path!= '/' else ''}/{other}")

    def __str__(self):
        return self.path

    def __repr__(self):
        return f"<Path({'dir' if self.is_dir else 'file'}): path={self} size={self.size}>"

def get_dir(path, pathmap):
    path = str(path)
    if path not in pathmap:
        new_dir = Path(path, is_dir=True)
        return new_dir, pathmap
    else:
        return pathmap[path], pathmap

def update_pathmap_from_ls_lines(pathmap, ls_lines, pwd):
    for line in ls_lines:
        dir_or_size, name = line.split()
        new_node = pwd / name
        if dir_or_size == 'dir':
            new_node.is_dir = True
        else:
            new_node.size = dir_or_size
        
        pathmap.update({str(new_node): new_node})

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

        while len(lines):
            line = lines.pop(0)

            # instruction
            if is_instruction(line):
                cmd = line.lstrip('$').strip().split()
                
                # list 
                if cmd[0] == 'ls':
                    ls_lines = []
                    line = lines.pop(0)

                    while not is_instruction(line):
                        ls_lines.append(line)

                        if len(lines):
                            line = lines.pop(0)
                        else: 
                            break 
                    pathmap = update_pathmap_from_ls_lines(pathmap, ls_lines, pwd)
                
                elif cmd[0] == 'cd':
                    arg = cmd[1]
                    if arg == '..':
                        pwd = pwd.parent()
                    else:
                        pwd, pathmap = get_dir(pwd/arg, pathmap)
                    
                    continue
    return pathmap

                    


inpath = 'day7_input_example.txt'
res = parse_input(inpath)
print(res)

