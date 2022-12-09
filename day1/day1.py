# Read values
with open("./input.in", "r") as f:
    lines = f.readlines()

lines = list(map(lambda x: x.rstrip("\n"), lines))

blanks_idxs = list(filter(lambda x: lines[x] == "", range(len(lines))))

# Get ints
for idx in range(len(lines)):
    if lines[idx] != "":
        lines[idx] = int(lines[idx])
    else:
        lines[idx] = int(-1)

# part-1
# max_calories = -1

# prev = 0
# next = blanks_idxs[0]

# for i in blanks_idxs[1:]:
#     max_sum = sum(lines[prev:next])
#     if max_calories < max_sum:
#         max_calories = max_sum
#     prev = next + 1
#     next = i

# print(max_calories)

# part-2:  top 3 elves
N = 3
top_n = [0 for _ in range(N)]

max_calories = -1

prev = 0
next = blanks_idxs[0]

for i in blanks_idxs[1:]:
    max_sum = sum(lines[prev:next])
    # print(max_sum, end=" ")

    # find min index in top_n
    rep_idx = top_n.index(min(top_n))
    

    if max_sum > top_n[rep_idx]:
        top_n[rep_idx] = max_sum

    prev = next + 1
    next = i

print(sum(top_n))
