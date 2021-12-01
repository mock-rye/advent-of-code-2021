with open("input.txt","r") as file:
    lst = [int(f) for f in file]
    
sums = [lst[r]+lst[r+1]+lst[r+2] for r in range(len(lst)-2)]
ctr = 0
i = sums[0]
for s in sums:
    if s > i:
        ctr += 1
    i = s

print(ctr)
