# this is kind of a general solution at this point and
# much faster than anything else I can think of tbh
with open("input.txt") as file:
    inp = [int(x) for x in file.readline().strip().split(",")]

count = [inp.count(i) for i in range(9)]
count.reverse()

# I did the rest in octave/matlab:
# it becomes a matrix exponentiation problem where

# the transformation matrix is:
##    monster = [0,0,0,0,0,0,0,0,1;
##               1,0,0,0,0,0,0,0,0;
##               0,1,0,0,0,0,0,0,1;
##               0,0,1,0,0,0,0,0,0;
##               0,0,0,1,0,0,0,0,0;
##               0,0,0,0,1,0,0,0,0;
##               0,0,0,0,0,1,0,0,0;
##               0,0,0,0,0,0,1,0,0;
##               0,0,0,0,0,0,0,1,0;]

# the initial configuration vector is:
##    initial = count'
# (just transpose it)

# then the exact configuration of fish on day n is:
##    conf = monster^n * initial

# and the amount fish is as simple as:
##    ans = sum(conf)
