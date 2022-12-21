# Advent of Code 2022 - Day 7 Part 1
# https://adventofcode.com/2022/day/6
# Courtney Ficker

# File system
class FileSystem:
    def __init__(self) -> None:
        self.root = Directory('/')
        self.currentDir = self.root
        self.space = 70000000

    def __sizeof__(self) -> int:
        return self.root.__sizeof__()

    def __str__(self) -> str:
        return str(self.root.__str__())

    def cd(self, dirName: str):
        # Go to root
        if (dirName == '/'):
            # print('changing current directory to ROOT')
            self.currentDir = self.root
            return
        # Go up one level if not already at root
        if (dirName == '..'):
            # print('changing current directory to UP ONE LEVEL')
            if (self.currentDir.name != '/'):
                self.currentDir = self.currentDir.parent
            return
        # Go to specified dir, if it exists in this directory
        newDir = self.currentDir.getDir(dirName)
        if (newDir):
            # print(f'changing current directory to {newDir.name}')
            self.currentDir = newDir
        return

    def free_space(self, amt) -> int:
        unused = self.space - self.__sizeof__()
        goal = amt - unused

        if (goal <= 0): return
        print(f'Need to free up at least {goal} space')
        return goal



class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.directories = []
        self.indent = 0
        self.parent = None

    def __sizeof__(self) -> int:
        size = 0
        for file in self.files:
            size += file.__sizeof__()
        for dir in self.directories:
            size += dir.__sizeof__()
        return size

    def __str__(self) -> str:
        return f'{len(self.files)} files, {len(self.directories)} directories: {self.__sizeof__()} bytes'

    def addFile(self, f) -> None:
        self.files.append(f)

    def addDir(self, d) -> None:
        d.indent = self.indent + 2
        d.parent = self
        self.directories.append(d)

    def getDir(self, directoryName):
        for d in self.directories:
            if (d.name == directoryName):
                return d

    def ls(self) -> None:
        indents = ' ' * self.indent
        print(f'{indents}- {self.name} (dir)')
        for dir in self.directories:
            dir.ls()
        for f in self.files:
            print(f'{indents}- {f.name} (file, size={f.size}')

    def calc_answer_a(self, limit) -> int:
        ret = 0
        size = self.__sizeof__()
        if (size <= limit):
            ret += size
        for d in self.directories:
            ret += d.calc_answer()
        return ret

    def getDirs(self):
        if (len(self.directories) == 0):
            return [(self.name, self.__sizeof__())]
        dirs = []
        for d in self.directories:
            dirs.extend(d.getDirs())
        dirs.append((self.name, self.__sizeof__()))
        return dirs


class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size

    def __sizeof__(self) -> int:
        return self.size

    def __str__(self) -> str:
        return f'{self.name}: {self.size} bytes'

fs = FileSystem()

def ls() -> None:
    fs.ls()


# Build the file system
with open('input.txt','r') as f:
    for line in f:
        sp = line.strip().split()
        if (sp[0] == '$'):
            # print(f'command: {sp}')
            cmd = sp[1]
            if (cmd == 'cd'):
                fs.cd(sp[2])
            elif (cmd == 'ls'):
                # ls()
                continue
        elif (sp[0] == 'dir'):
            newDir = Directory(sp[1])
            # print(f'adding new Dir: {newDir}')
            fs.currentDir.addDir(newDir)
        elif (sp[0].isdigit):
            # print(f'creating new file \'{sp[1]}\' with size {sp[0]}')
            newFile = File(sp[1], int(sp[0]))
            fs.currentDir.addFile(newFile)

# Find the answer
# print('Combined size of directories <= 100000:', fs.root.calc_answer_a(100000))

goal = fs.free_space(30000000)

list_of_dirs = fs.root.getDirs()
# print(list_of_dirs)

min = fs.space
for (dir, size) in list_of_dirs:
    if (size >= goal) and (size < min):
        min = size

print('answer:',min)
