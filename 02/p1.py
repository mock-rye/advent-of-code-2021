with open("input.txt") as file:
    inp = [line for line in file]
#print(inp)
x = 0
y = 0
for line in inp:
#    print(line)
    cmd = line.split()[0]
    amt = int(line.split()[1])
    if cmd == "up":
        y -= amt
    elif cmd == "down":
        y += amt
    else:
        x += amt

print(str(x*y))
    
