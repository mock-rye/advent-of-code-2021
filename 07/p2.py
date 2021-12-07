def distance(arr, num):
    return sum([abs(elem-num)*(abs(elem-num)+1)//2 for elem in arr])

with open("input.txt") as file:
    inp = file.read().strip().split(",")
    inp = [int(elem) for elem in inp]

inp.sort()
first, last = inp[0], inp[-1]
while first+1 != last:
    midpoint = (first + last)//2
    if distance(inp, midpoint) > distance(inp, midpoint + 1): # just checks the slope lol
        first = midpoint
    else:
        last = midpoint

print(min(distance(inp, midpoint),distance(inp,midpoint+1)))
