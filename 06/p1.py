# this is god-awfully slow, probably something n^3 or maybe even 2^n or whatnot
with open("input.txt") as file:
    inp = [int(x) for x in file.readline().strip().split(",")]

count = [inp.count(i) for i in range(7)]
def fix(it):
    out = []
    for i in it:
        if i == 0:
            out.append(6)
            out.append(8)
        else:
            out.append(i-1)
    return out

def doThings(inp, days):
    for i in range(days):
        inp = fix(inp)
    return inp

inp = doThings(inp, 80)

count = [inp.count(i) for i in range(10)]

print(len(inp))
    
