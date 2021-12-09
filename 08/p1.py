valid = lambda x: True if len(x) in [2, 3, 4, 7] else False

with open("input.txt") as file:
    inp = [f.strip().split("|")[1].split() for f in file]

out = sum([sum([valid(x) for x in line]) for line in inp])
print(out)
