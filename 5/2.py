# Advent of Code 2022 - Day 5 Part 2
# https://adventofcode.com/2022/day/5
# Courtney Ficker

# 4 spaces per column

def move(num, src, dst):
    for _ in range(num):
        val = src.pop()
        dst.append(val)

def move_multiple(num, src, dst):
    copy = []
    for _ in range(num):
        copy.append(src.pop())
    copy.reverse()
    dst.extend(copy)

with open('input.txt','r') as f:
    # List of lists
    stacks = []
    for _ in range(9):
        stacks.append([])

    donePopulating = False

    for line in f:
        if not donePopulating:
            indices = [i for i in range(len(line)) if line.startswith('[', i)]
            if (len(indices) == 0):
                donePopulating = True
                for stack in stacks:
                    stack.reverse()
                    # print(f'Stack: {stack}')
            else:
                for x in indices:
                    stacks[int(x/4)].append(line[x+1])
        else:
            instr = line.split()
            if not instr: continue
            if (instr[0] == 'move'):
                num = int(instr[1])
                src = stacks[int(instr[3]) - 1]
                dst = stacks[int(instr[5]) - 1]

            move_multiple(num, src, dst)

res = ''
for stack in stacks:
    res += str(stack[-1])

print(res)  # QRQFHFWCL
