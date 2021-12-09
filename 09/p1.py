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
            lowPoints.append((i,j))
ans = sum([1+inp[x][y] for (x, y) in lowPoints])
print(ans)
