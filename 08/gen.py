sort = lambda s: "".join(sorted(s))
remove = lambda lst, x: [elem for elem in lst if elem != x]
doDecode = lambda dct, lst: [str(dct[elem]) for elem in lst]
valid = lambda x: True if len(x) in [2, 3, 4, 7] else False

def decode(lst):
    dct = {}
    lst = [set(elem) for elem in lst]
    for elem in lst:
        if len(elem) == 2:
            dct[1] = elem
            lst = remove(lst, elem)
        elif len(elem) == 3:
            dct[7] = elem
            lst = remove(lst, elem)
        elif len(elem) == 4:
            dct[4] = elem
            lst = remove(lst, elem)
        elif len(elem) == 7:
            dct[8] = elem
            lst = remove(lst, elem)
    for elem in lst:
        if len(elem) == 5: # if elem is a 2, 3, or 5
            if elem.intersection(dct[7]) == dct[7]: # elem is a 3
                dct[3] = elem
                lst = remove(lst, elem)
        elif len(elem) == 6: # if elem is a 0, 6, or 9
            if elem.intersection(dct[4]) == dct[4]: # elem is a 9
                dct[9] = elem
                lst = remove(lst, elem)
            elif elem.intersection(dct[7]) == dct[7]: # elem is a 0
                dct[0] = elem
                lst = remove(lst, elem)
            else: # elem is a 6
                dct[6] = elem
                lst = remove(lst, elem)
    for elem in lst:
        if len(elem) == 5: # elem is a 2 or 5
            if elem.intersection(dct[6]) == elem: # elem is a 5
                dct[5] = elem
                lst = remove(lst, elem)
            else: # elem is a 2
                dct[2] = elem
                lst = remove(lst, elem)
    dct = {sort("".join(list(dct[elem]))) : elem for elem in dct}
    return dct

with open("input.txt") as file:
    inp = [line.strip().replace("|","").split() for line in file]

inp = [[sort(x) for x in line] for line in inp]

p1 = sum([sum(valid(x) for x in line[-4:]) for line in inp])
print("p1:", p1)
p2 = sum([int("".join(doDecode(decode(line),line)[-4:])) for line in inp])
print("p2:", p2)
