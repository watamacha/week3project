from lib import optimizer as op
import matplotlib.pyplot as plt
dataset = [ [0,1.0000000],
            [15,.9743175],
            [25,.9575636],
            [35,.9373807],
            [40,.9241359],
            [45,.9048999],
            [50,.8762306],
            [60,.7698698],
            [70,.5592012],
            [80,.2626372],  ]

#begin by testing robustness of model for f1 using binary bitstring counting


retx = [[],[],[],[],[],[],[],[],[],[]]
rety = [[],[],[],[],[],[],[],[],[],[]]
def bit(a,b):
    return (a // 2**b)%2

for searchindex in range(2**10 - 1):
    data = [dataset[i] for i in range(10) if bit(searchindex, i)]
    values = op.bruteSearch(op.f1, 200, op.f1bounds, data)
    retval = values.pop()
    retx[len(data)].append(retval[0])
    rety[len(data)].append(retval[1])

for i in range(10):
    plt.title("distribution of optimums with data subset of size " + str(i))
    plt.hist(retx[i],200,cumulative = True)#,weights=[1/y for y in rety[i]])
    plt.show()
