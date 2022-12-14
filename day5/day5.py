from utils import read_input

lines = read_input()

"""
[N]         [C]     [Z]            
[Q] [G]     [V]     [S]         [V]
[L] [C]     [M]     [T]     [W] [L]
[S] [H]     [L]     [C] [D] [H] [S]
[C] [V] [F] [D]     [D] [B] [Q] [F]
[Z] [T] [Z] [T] [C] [J] [G] [S] [Q]
[P] [P] [C] [W] [W] [F] [W] [J] [C]
[T] [L] [D] [G] [P] [P] [V] [N] [R]
 1   2   3   4   5   6   7   8   9 
"""


class Stack:
    def __init__(self, stack) -> None:
        self.stack = stack

    def pop(self):
        elem = self.stack.pop(0)
        return elem

    def push(self, elem):
        self.stack.insert(0, elem)

    def pop_many(self, num):
        popped = [self.pop() for _ in range(num)]
        return popped

    def push_many(self, popped):
        for elem in popped:
            self.push(elem)


stacks = [
    None,
    Stack(
        stack=[
            "N",
            "Q",
            "L",
            "S",
            "C",
            "Z",
            "P",
            "T",
        ]
    ),
    Stack(
        stack=[
            "G",
            "C",
            "H",
            "V",
            "T",
            "P",
            "L",
        ]
    ),
    Stack(
        stack=[
            "F",
            "Z",
            "C",
            "D",
        ]
    ),
    Stack(
        stack=[
            "C",
            "V",
            "M",
            "L",
            "D",
            "T",
            "W",
            "G",
        ]
    ),
    Stack(
        stack=[
            "C",
            "W",
            "P",
        ]
    ),
    Stack(
        stack=[
            "Z",
            "S",
            "T",
            "C",
            "D",
            "J",
            "F",
            "P",
        ]
    ),
    Stack(
        stack=[
            "D",
            "B",
            "G",
            "W",
            "V",
        ]
    ),
    Stack(
        stack=[
            "W",
            "H",
            "Q",
            "S",
            "J",
            "N",
        ]
    ),
    Stack(
        stack=[
            "V",
            "L",
            "S",
            "F",
            "Q",
            "C",
            "R",
        ]
    ),
]

def parse_line(line):
    """move 6 from 2 to 1"""
    words = line.split()
    num = int(words[1])
    from_stack = int(words[3])
    to_stack = int(words[5]) 
    return num, from_stack, to_stack

def op(num, from_stack, to_stack):
    popped = stacks[from_stack].pop_many(num)
    stacks[to_stack].push_many(popped)

for line in lines:
    op(*parse_line(line))

for stack in stacks[1:]:
    print(stack.stack[0], end="")