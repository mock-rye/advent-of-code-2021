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

gamma = lambda x: "".join([str(int(elem[0] < elem[1])) for elem in x])
epsilon = lambda x: "".join([str(int(elem[0] > elem[1])) for elem in x])

d = [[0,0] for i in range(len(inp[0]))]
for line in inp:
    for i in range(len(line)):
        d[i][int(line[i])] += 1

g = gamma(d)
e = epsilon(d)
print("gamma =", int(g,2), g)
print("epsilon =", int(e,2), e)
print("p1:", int(g,2)*int(e,2))

o2 = find(inp, 1, 0)
co2 = find(inp, 0, 1)

print("o2 =", int(o2,2), o2)
print("co2 =", int(co2,2), co2)
print("p2:", int(o2,2)*int(co2,2))
