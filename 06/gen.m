initial = dlmread("input.txt");
initial = flip(hist(initial, [0:8]))';
transform = [0,0,0,0,0,0,0,0,1;
           1,0,0,0,0,0,0,0,0;
           0,1,0,0,0,0,0,0,1;
           0,0,1,0,0,0,0,0,0;
           0,0,0,1,0,0,0,0,0;
           0,0,0,0,1,0,0,0,0;
           0,0,0,0,0,1,0,0,0;
           0,0,0,0,0,0,1,0,0;
           0,0,0,0,0,0,0,1,0;];
format long;
ans1 = sum(transform^80*initial)
ans2 = sum(transform^256*initial)
