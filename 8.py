import math
a,b=input() 
for i in range(a,b):
    factors = []
    for j in range(1, int(math.floor(i/2)+1)):
        if i%j == 0:
            factors.append(j)
    if sum(factors) == i:
        print i,
