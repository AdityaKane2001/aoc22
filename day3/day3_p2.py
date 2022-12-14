from utils import read_input
from string import ascii_lowercase, ascii_uppercase

lines = read_input()

PRIORITY_VALUES = {
    k:v for k, v in zip(ascii_lowercase + ascii_uppercase, range(1, 53))
}

def get_common(three_lines):
    three_lines = list(map(lambda x: list(set(x)), three_lines))

    all_letters = dict()

    for sequence in three_lines:
        for letter in sequence:
            if letter not in all_letters.keys():
                all_letters[letter] = 1
            else:
                all_letters[letter] += 1

    all_letters_inversed = {v:k for k, v in all_letters.items()}

    return all_letters_inversed[3]

three_paired_lines = zip(*(iter(lines),) * 3)

sum_prioirs = 0

for three_lines in three_paired_lines:
    sum_prioirs += PRIORITY_VALUES[get_common(three_lines)]

print(sum_prioirs)