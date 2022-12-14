def read_input(filename="input.in"):
    with open(filename, "r") as f:
        lines = f.readlines()
    lines = list(map(lambda x: x.rstrip("\n"), lines))
    return lines