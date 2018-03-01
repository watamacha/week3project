#define dataset, known constant
import math
dataset = [[0,1.0000000],
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
    return (s**n)*(g**((c**n) - 1))

#define value function, sum of error squares. must be minimized.
def v(funct, params, data = dataset):
    sum = 0.
    for i in range(len(data)):
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
ubg = 0.999

f1bounds = [[lbr,ubr]]

f2bounds = [[lbs,ubs],
            [lbg,ubg],
            [lbc,ubc]]


def getstepsizes(stepsperparam, parameterBounds):
    stepsize = [float((parameterBounds[p][1]-parameterBounds[p][0])/(stepsperparam)) for p in range(len(parameterBounds))]
    #print("stepsize array: ", stepsize)
    return stepsize

#define a brute force by subdividing the boundaries into halves k times
def bruteSearch(funct, stepsperparam, parameterBounds, data = dataset):
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
    #print("degrees of freedom: ", df)
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
    #print("stepsize array: ", stepsize)
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
        if df > 1:
            sco[0] += 1
            for i in range(df-1):
                if sco[i] == stepsperparam+1:
                    sco[i+1] = sco[i+1] + 1
                    sco[i] = 0
        if df == 1:
            sco[0] = i % (stepsperparam + 1)
        #co = [stepsize[p] * sco[p] for p in range(df)]
        co = [float(((stepsize[p])*(sco[p]))+parameterBounds[p][0]) for p in range(df)]
        #we define a function to cleanly update ord and coord given co
        ord = v(funct, co, data)
        coord = co
        coord.append(ord)
        values.append(coord)
        if ord < bord:
            bco = co
            bord = ord
            bcoord = coord
            #print("found new optimum of ", bord, " at ", bco)
    values.append(bcoord)
    ###END FUNCTION DEFINITION

    ###RETURN DEFINITION:
    return values
    ###END RETURN DEFINITION

