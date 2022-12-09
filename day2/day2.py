with open("./input.in", "r") as f:
    lines = f.readlines()

lines = list(map(lambda x: x.split(), lines))
print(lines[:10])

SHAPE_DICT = {
    "X": 1, # A rock
    "Y": 2, # B paper
    "Z": 3, # C scissors
}

RESULT_DICT = {
    "w" : 6,
    "l" : 0,
    "d": 3
}

def pred_win_loss(opp, you):
    if opp == "A":
        if you == "Y":
            return "w"
        elif you == "Z":
            return "l"
        elif you == "X":
            return "d"
    
    if opp == "B":
        if you == "Z":
            return "w"
        elif you == "X":
            return "l"
        elif you == "Y":
            return "d"

    if opp == "C":
        if you == "X":
            return "w"
        elif you == "Y":
            return "l"
        elif you == "Z":
            return "d"

score = 0

for game in lines:
    score += RESULT_DICT[pred_win_loss(*game)] + SHAPE_DICT[game[1]]

print(score)