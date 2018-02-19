#define dataset, known constant
import math
a = [[0,1.0000000],
     [15,.9743175],
     [25,.9575636],
     [35,.9373807],
     [40,.9241359],
     [45,.9048999],
     [50,.8762306],
     [60,.7698698],
     [70,.5592012],
     [80,.2626372],]


#define functions to optimize
def f1(n,r):
    return math.exp(r*n)
def f2(n,s,g,c):
    return (s**n)*(g**((c**n) - 1))

#define inverse value function, sum of error squares to be minimized
def v(funct, data, params):
    sum = 0
    for i in xrange(10):
        sum += (funct(data[i][0],params) - data[i][1])**2
    return sum

#define lower and upper bounds for parameters.
lbr = -0.01
ubr = 0

lbc = 1.07
ubc = 1.13

lbs = 0.996
ubs = 1

lb
