# list<int> -> int
def inc(lst):
    i = lst[0]
    ctr = 0
    for elem in lst:
        if i < elem:
            ctr += 1
        i = elem
    return ctr

with open("input.txt","r") as file:
    lst = [int(f) for f in file]
sums = [lst[r]+lst[r+1]+lst[r+2] for r in range(len(lst)-2)]
print("p1: " + str(inc(lst)))
print("p2: " + str(inc(sums)))
