with open("input.txt") as file:
    lines = [[[int(x) for x in f.strip().split(",")] for f in line.strip().split("->")] for line in file.readlines()]

lines = [line for line in lines if line[0][0] == line [1][0] or line[0][1] == line[1][1]]

grid = [[0 for j in range(1000)] for i in range(1000)]

for line in lines:
    x1, y1 = line[0]
    x2, y2 = line[1]
    x1, x2 = min(x1,x2), max(x1,x2)
    y1, y2 = min(y1,y2), max(y1,y2)
    if x1 == x2:
        x = x1
        for y in range(y1, y2+1):
            grid[x][y] += 1
    elif y1 == y2:
        y = y1
        for x in range(x1, x2+1):
            grid[x][y] += 1
    else:
        print("ya fucked something up ya dingus")

ctr = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        if grid[x][y] >= 2:
            #print(x, y)
            ctr += 1
print(ctr)
    
