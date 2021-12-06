def generatePath(r1, r2):
    x1, y1 = r1
    x2, y2 = r2
    out = []
    if (y2-y1)/(x2-x1) == -1:
        return 0

def prettyPrint(grid):
    [print(line) for line in grid]

with open("input.txt") as file:
    lines = [[[int(x) for x in f.strip().split(",")] for f in line.strip().split("->")] for line in file.readlines()]

grid = [[0 for j in range(1000)] for i in range(1000)]

#prettyPrint(grid)

for line in lines:
    x1, y1 = line[0]
    x2, y2 = line[1]
    if x1 == x2:
        x = x1
        y1, y2 = min(y1,y2), max(y1,y2)
        for y in range(y1, y2+1):
            grid[x][y] += 1
    elif y1 == y2:
        y = y1
        x1, x2 = min(x1,x2), max(x1,x2)
        for x in range(x1, x2+1):
            grid[x][y] += 1
    else:
        if (x1 > x2 and y1 > y2) or (x1 < x2 and y1 < y2):
            x1, x2 = min(x1,x2), max(x1,x2)
            y1, y2 = min(y1,y2), max(y1,y2)
            for it in range(0, x2-x1+1):
                if(x1+it == 1000) or (y1+it == 1000):
                    print(x1, x2, y1, y2)
                    print(it)
                grid[x1+it][y1+it] += 1
        else:
            x1, x2 = min(x1,x2), max(x1,x2)
            y1, y2 = min(y1,y2), max(y1,y2)
            for it in range(0, x2-x1+1):
                grid[x1+it][y2-it] += 1
            

ctr = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] >= 2:
            #print(x, y)
            ctr += 1
#prettyPrint(grid)
print(ctr)
    
