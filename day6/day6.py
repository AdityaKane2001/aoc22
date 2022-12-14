from utils import read_input

lines = read_input()
line = lines[0]

window = []

for idx in range(len(line)):
    if len(list(set(line[idx:idx+4]))) == 4:
        print(idx + 4)
        break
    