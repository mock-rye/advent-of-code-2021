with open("input.txt") as file:
    inp = [line.strip() for line in file]

def find(inp, default, second):
    for i in range(len(inp[0])):
        a = [0,0]
        for elem in inp:
            a[int(elem[i])] += 1
        bit = default
        if a[0] > a[1]:
            bit = second
        inp = [elem for elem in inp if int(elem[i]) == bit]
        if len(inp) == 1:
            return inp[0]

o2 = int(find(inp, 1, 0), 2)
co2 = int(find(inp, 0, 1), 2)

print("o2 =", o2)
print("co2 =", co2)
print(o2*co2)
