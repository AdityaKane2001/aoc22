from utils import read_input

lines = read_input()
line = lines[0]

window = []

for idx in range(len(line)):
    if len(list(set(line[idx:idx+14]))) == 14:
        print(idx + 14)
        break
    