from math import prod
with open("input.txt") as file:
    inp = [[int(x) for x in line.strip()] for line in file]

add = lambda r1, r2: tuple(map(sum, zip(r1, r2)))
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
lowPoints = []
for i in range(len(inp)):
    for j in range(len(inp[i])):
        possible = True
        for (x,y) in [add((i,j),d) for d in dirs]:
            if x in range(len(inp)) and y in range(len(inp[x])):
                if inp[x][y] <= inp[i][j]:
                    possible = False
        if possible:
            lowPoints.append(tuple((i,j)))
            
p1 = sum([1+inp[x][y] for (x, y) in lowPoints])

crush = lambda x: 0 if x == 9 else x
inp = [[crush(x) for x in line] for line in inp]
# crushes locations of height 9 down to 0 so they're always lower than
# any point in any basin, so can't be added to any basin

sizes = []
for center in lowPoints:
    basin = [center]
    for (x,y) in basin:
        height = inp[x][y]
        for newPoint in [add((x,y), d) for d in dirs]:
            possible = True
            xn, yn = newPoint
            if newPoint in basin\
               or xn not in range(len(inp))\
               or yn not in range(len(inp[x])):
                possible = False
            if possible:
                if inp[xn][yn] <= inp[x][y]:
                    possible = False
            if possible:
                basin.append(newPoint)
    sizes.append(len(basin))
        
sizes.sort()
p2 = prod(sizes[-3:])
print("p1:", p1)
print("p2:", p2)
            
