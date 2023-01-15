from utils import read_input

lines = read_input()

heights = []

for line in lines:
    heights.append([])
    for num in line:
        heights[-1].append(int(num))

SIDE_LEN = len(heights)


# left to right

visible = (SIDE_LEN * 4) - 4

for row_idx in range(SIDE_LEN):
    left_to_right_max = -1
    for col_idx in range(SIDE_LEN):
        if heights[row_idx][col_idx] > left_to_right_max:
            if col_idx > 0 and col_idx < SIDE_LEN - 1:
                visible += 1
                left_to_right_max = heights[row_idx][col_idx]
                heights[row_idx][col_idx] = 0