#define dataset, known constant
import math
data = [[0,1.0000000],
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
def f1(n,params):
    return math.exp(n*params[0])
def f2(n,params):
    s = params[0]
    g = params[1]
    c = params[3]
    return (s**n)*(g**((c**n) - 1))

#define inverse value function, sum of error squares to be minimized
def v(funct, params):
    sum = 0
    for i in range(10):
        sum += (funct(data[i][0],params) - data[i][1])**2
    return sum

#define lower and upper bounds for parameters. Write them into a 2xn matrix
lbr = 0-0.01
ubr = 0

lbc = 1.07
ubc = 1.13

lbs = 0.996
ubs = 1

lbg = 0.98
ubg = 1

f1bounds = [[lbr,ubr]]

f2bounds = [[lbs,ubs],
            [lbg,ubg],
            [lbc,ubc]]



#define a brute force by subdividing the boundaries into halves k times








def bruteSearch(funct, iterations, parameterBounds):
    #initialize a coordinate variable, as well as a value list for graphing. here the last thing in pc is the return of the value function and the rest is an ordered list of parameter values
    #values is not gonna be ordered since ordering in higher dimensions is an issue we can deal with afterwards, and if we have enough points to be troublesome to sort for line graphing 
    #they'll be dense enough not to worry about it and just use a scatter
    edge = 2*iterations + 1
    df = len(parameterBounds)
    pc = [0 for x in range(df)]
    pc.append(0)
    best = pc
    pcx = pc
    pcx.pop()
    values = [pc for x in range(edge**df)]
    #next we define some useful information for the iterator
    #the iteration works by moving by stepsize in each direction using modular stuff
    stepsize = pcx
    for p in range(df):
        lb = parameterBounds[p][0]
        ub = parameterBounds[p][1]
        stepsize[p] = (ub-lb)/(2**iterations)
    #now we initialize pc to the first coordinate it must check
    for p in range(df):
        #ayyy james brown hows it goin
        pc[p] = (parameterBounds[p][0])
        pcx[p] = pc[p]

    #here we iterate
    #our index goes up to 2i-1^df, since thats how many points we want
    for index in range(edge**df):
        for d in range(df):
            #every edge times the previous d goes up, this one goes up. done with floor division.
            pcx[d] = stepsize[d] * (index//(edge**(d+1)))
        pc = pcx
        pc.append(v(funct,pcx))
        values[index] = pc
        if pc[df] > best[df]:
            best = pc
           
    #here we return our coordinates, along with the 'best' coordinate. note that append is used instead of extend here.
    #this is because extend stores the entire 'best' array in the last index of values, so values(len(values)-1) is always 'best', regardless of the size of 'best.'
    #effectively we include the length information of 'best' implicitly in the structure of the return array, which also aids in visualization construction.
    values.append(best)
    return values


