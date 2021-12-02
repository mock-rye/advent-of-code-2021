with open("input.txt") as file:
    inp = [line for line in file]
#print(inp)
x = 0
y = 0
aim = 0
for line in inp:
#    print(line)
    [cmd, amt] = line.split()
    amt = int(amt)
    if cmd == "up":
        aim -= amt
    elif cmd == "down":
        aim += amt
    else:
        x += amt
        y += aim*amt
        
print(str(x*y))
    
