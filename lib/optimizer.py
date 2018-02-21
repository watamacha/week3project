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
    c = params[2]
    if math.log(g) > (0-1)/1000000*math.log(c):
        return 0
    return (s**n)*(g**((c**n) - 1))

#define value function, sum of error squares. must be minimized.
def v(funct, params):
    sum = 0.
    for i in range(10):
        sum += (funct(data[i][0],params) - data[i][1])**2
    return sum

#define lower and upper bounds for parameters. Write them into a 2xn matrix
lbr = 0-0.01
ubr = 0.

lbc = 1.07
ubc = 1.125

lbs = 0.996
ubs = 1.

lbg = 0.98
ubg = 1.

f1bounds = [[lbr,ubr]]

f2bounds = [[lbs,ubs],
            [lbg,ubg],
            [lbc,ubc]]



#define a brute force by subdividing the boundaries into halves k times








def bruteSearchold(funct, iterations, parameterBounds):
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

def bruteSearch(funct, stepsperparam, parameterBounds):
    ###INPUT DEFINITION:
    #funct should be a function with args (n, params), where params is excepted to be the same size as parameterBounds. had issues with isinstance(x, function)
    if not True:
        print("ERROR: funct is not a function")
        return []
    #stepsperparam should be an integer greater than 0.
    if not isinstance(stepsperparam, int):
        print ("ERROR: stepsperparam is not an int")
        return []
    if stepsperparam < 1:
        print ("ERROR: invalid number of steps per parameter")
        return []
    #parameterBounds can be a list of any size, and each element must be a list of size 2 containing 2 ordered floats.
    if not isinstance(parameterBounds, list):
        print("ERROR: parameterBounds is not a list")
        return []
    for x in parameterBounds:
        if len(x) != 2:
            print ("ERROR: invalid length member of parameterBounds")
            return []
        if not isinstance(x[0],float):
            print("ERROR: one of the lower bounds is not a float")
            return []
        if not isinstance(x[1],float):
            print("ERROR: one of the upper bounds is not a float")
            return []
        if x[0] >= x[1]:
            print("ERROR:invalid parameter boundary size")
            return []
    #in our case, (fk, any integer greater than 0, fkbounds) is a valid input set if k is 1 or 2.
    ###END INPUT DEFINITION
    
    ###LOCALS DEFINITION:
    #floats should be used for any non-indexing variables. ints/longs (handled automatically by dynamic typing) for any indexing variables.
    #define df, the number of parameters to optimize over
    df = len(parameterBounds)
    print("degrees of freedom: ", df)
    #define co, the current parameter values (a coordinate in our parameter space)
    co = [0. for x in range(df)]
    #define ord, the evaluation of the value function at our current parameter value set (the value of a point in our value field)
    ord = 0.
    #define coord, an array that defines a point in our value field (field in the parameterbounds bounded subset of the parameter space)
    #must be 2 lines since append method does not return the result of the append.
    coord = [0. for x in co]
    coord.append(ord)
    #define our coords array, which is just an array of known coordinates, as well as bco, bord, and bcoord, which are the co, ord, and coord for the current best
    #since we aim to minimize, we initialize bord to a high enough value that we can find something below it.
    values = []
    bco = co
    bord = 999.
    bcoord = bco
    bcoord.append(bord)
    #next we calculate stepsizes using lower and upper bounds
    stepsize = [float((parameterBounds[p][1]-parameterBounds[p][0])/(stepsperparam)) for p in range(df)]
    print("stepsize array: ", stepsize)
    #we also define sco, the same as co but encoded as integer number of steps
    sco = [0 for x in co]
    #next we define our startpoint as the minimum of all parameters
    co = [x[0] for x in parameterBounds]
    #now we define the number of points we will evaluate
    points = (stepsperparam + 1)**df
    ###END LOCALS DEFINITION


    ###FUNCTION DEFINITION:
    #now we begin iterating.
    #from our start coordinate, we move p1 up every step, and reset it every stepsperparam steps.
    #we move p[k] up every stepsperparam^(k-1) steps, and reset it every stepsperparam^k steps
    #incrementing i at every j increments of k is done by i = k//j (floor division)
    #resetting i at every j increments of k is done by i = k%j
    #result is (i//stepsperparam**(p-1))%(stepsperparam**p)
    for i in range(points):
        sco = [(i//((stepsperparam+1)**(p)))%((stepsperparam+1)**(p+1)) for p in range(df)]
        #co = [stepsize[p] * sco[p] for p in range(df)]
        co = [float(((stepsize[p]+0.0)*(sco[p]+0))+parameterBounds[p][0]) for p in range(df)]
        #we define a function to cleanly update ord and coord given co
        ord = v(funct, co)
        coord = co
        coord.append(ord)
        values.append(coord)
        if ord < bord:
            bco = co
            bord = ord
            bcoord = coord
            print("found new optimum of ", bord, " at ", bco)
    values.append(bcoord)
    ###END FUNCTION DEFINITION

    ###RETURN DEFINITION:
    return values
    ###END RETURN DEFINITION

