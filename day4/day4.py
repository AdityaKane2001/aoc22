from utils import read_input

lines = read_input()


def parse_line(line):
    first, second = line.split(",")
    first = list(map(int, first.split("-")))
    second = list(map(int, second.split("-")))
    return first, second


def is_contained(first, second):
    if (first[0] <= second[0] and first[1] >= second[1]) or (first[0] >= second[0] and first[1] <= second[1]):
        return 1
    else:
        return 0


num_contained = sum(list(map(lambda x: is_contained(*parse_line(x)), lines)))

print(num_contained)