with open("input.txt") as file:
    inp = [line.strip() for line in file]

gamma = lambda x: int("".join([str(int(elem[0] < elem[1])) for elem in x]), 2)
epsilon = lambda x: int("".join([str(int(elem[0] > elem[1])) for elem in x]), 2)

d = [[0,0] for i in range(len(inp[0]))]
for line in inp:
    for i in range(len(line)):
        d[i][int(line[i])] += 1

print(gamma(d)*epsilon(d))
