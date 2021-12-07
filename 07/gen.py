import time
start_time = time.time()

def distance1(arr, num):
    return sum([abs(elem-num) for elem in arr])

def distance2(arr, num):
    return sum([abs(elem-num)*(abs(elem-num)+1)//2 for elem in arr])

def minimum(inp, distance): # binary searches through
    first, last = inp[0], inp[-1]
    while first+1 != last:
        midpoint = (first + last)//2
        if distance(inp, midpoint) > distance(inp, midpoint + 1): # just checks the slope lol
            first = midpoint
        else:
            last = midpoint
    return min(distance(inp, midpoint), distance(inp, midpoint+1))


with open("input.txt") as file:
    inp = [int(elem) for elem in file.read().strip().split(",")]

inp.sort() # mostly necessary cause minimum() assumes the list is sorted
print("p1:", minimum(inp, distance1))
print("p1 time: %s seconds" % (time.time() - start_time))
lap_time = time.time()
print("p2:", minimum(inp, distance2))
print("p2 time: %s seconds" % (time.time() - lap_time))
