from utils import read_input

lines = read_input()


class FileNode:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def get_size(self):
        return self.size


class DirNode:
    def __init__(self, name, top=None) -> None:
        self.name = name
        self.size = 0
        self.directories = []
        self.directories_names = []
        self.files = []
        self.files_names = []
        self.top = top

    def get_size(self):
        if self.size == 0:
            for obj in self.directories + self.files:
                # print("Adding to size: ", obj.name, obj.size)
                self.size += obj.get_size()
        # print("Calculated size:", self.name, self.size)
        return self.size


def parse_line(line):
    if line.startswith("$"):
        line = line.lstrip("$ ")
    parts = line.split()
    return parts


root = DirNode(name="/")

curr = root


def build_system(current, parts):
    if parts[0] == "cd":
        if parts[1] == "/":
            current = root

        elif parts[1] == "..":
            if current.top is not None:
                current = current.top
            else:
                current = root
        elif type(parts[1]) is str:
            current = current.directories[current.directories_names.index(parts[1])]

    elif parts[0] == "ls":
        pass
    elif parts[0] == "dir":
        current.directories.append(DirNode(name=parts[1], top=current))
        current.directories_names.append(parts[1])
    else:
        current.files.append(FileNode(name=parts[1], size=int(parts[0])))
        current.files_names.append(parts[1])
    return current


for line in lines:
    curr = build_system(curr, parse_line(line))


root.get_size()
# print(root.files_names)

# get problem solution

# print(root.size)
# for obj in root.directories + root.files:
#     print(obj.name, obj.size)

def get_filesizes(node, arr=[]):
    for directory in node.directories:
        arr.append(directory.size)
        arr = get_filesizes(directory, arr)
    return arr

all_dirs = get_filesizes(root)

total = 0
for size in all_dirs:
    if size < 1e5:
        total += size

sorted_total = sorted(all_dirs)



current_free = 7e7 - root.size

# print(current_free)

target = 3e7 - current_free

# print(target)

print(sorted_total)

for idx in range(len(sorted_total)):
    if sorted_total[idx] >= target:
        print(sorted_total[idx])
        break