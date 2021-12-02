# list<(string, int)>, dict<string, *int[3](int[4])> -> int
def solve(lst, d):
    (x, y, aim) = (0, 0, 0)
    for (cmd, amt) in lst:
        # thank python for not having switch-case:
        (x, y, aim) = d[cmd](x, y, aim, amt)
    return x*y

d1= {}
d1["up"] = lambda x, y, aim, amt: (x, y-amt, aim)
d1["down"] = lambda x, y, aim, amt: (x, y+amt, aim)
d1["forward"] = lambda x, y, aim, amt: (x+amt, y, aim)

d2= {}
d2["up"] = lambda x, y, aim, amt: (x, y, aim-amt)
d2["down"] = lambda x, y, aim, amt: (x, y, aim+amt)
d2["forward"] = lambda x, y, aim, amt: (x+amt, y+aim*amt, aim)

# driver body:
with open("input.txt") as file:
    inp = [line.split() for line in file]
    inp = [(l[0], int(l[1])) for l in inp]
    # it wouldn't let me do this as a oneliner lol

print("p1: " + str(solve(inp, d1)))
print("p2: " + str(solve(inp, d2)))
