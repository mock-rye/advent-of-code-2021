with open("input.txt","r") as file:
    lst = [int(f) for f in file]
    
ctr = 0
i = lst[0]
for s in lst:
    if s > i:
        ctr += 1
    i = s

print(ctr)
