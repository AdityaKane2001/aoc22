with open("./input.in", "r") as f:
    lines = f.readlines()

lines = list(map(lambda x: x.split(), lines))

"""
X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
"""

SHAPE_DICT = {
    "X": 1, # A rock
    "Y": 2, # B paper
    "Z": 3, # C scissors
    "A": 1, # A rock
    "B": 2, # B paper
    "C": 3, # C scissors
}

WIN_PAIR = {
    "A": "B", "B": "C", "C":"A"
}

LOSE_PAIR = {v:k for k, v in WIN_PAIR.items()}

DRAW_PAIR = {"A": "A", "B": "B", "C": "C"}

RESULT_DICT = {
    "w" : 6,
    "l" : 0,
    "d": 3,
    "Z" : 6,
    "X" : 0,
    "Y": 3
}

def pred_correct_shape(opp, exp):
    if exp == "X":
        return LOSE_PAIR[opp]
    elif exp == "Y":
        return DRAW_PAIR[opp]
    elif exp == "Z":
        return WIN_PAIR[opp]

score = 0

for game in lines:
    score += SHAPE_DICT[pred_correct_shape(*game)] + RESULT_DICT[game[1]]

print(score)