from utils import read_input
from string import ascii_lowercase, ascii_uppercase

lines = read_input()

PRIORITY_VALUES = {
    k:v for k, v in zip(ascii_lowercase + ascii_uppercase, range(1, 53))
}

def get_common(line):
    first, second = list(set(line[:len(line)//2])), list(set(line[len(line)//2:]))

    for letter in second:
        if letter in first:
            return letter
    
sum_priorities = 0

for line in lines:
    sum_priorities += PRIORITY_VALUES[get_common(line)]

print(sum_priorities)