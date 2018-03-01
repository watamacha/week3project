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

#begin by testing robustness of model for f1
print('beginning robustness analysis on f1')
best = op.bruteSearch(op.f1,200,op.f1bounds).pop()



#first use subsets computed from binary bitstrings
print('analyzing data subsets')
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

mu = [0 for j in range(9)]
for j in range(9):
    i = j+1
    plt.title("distribution of optimums with data subset of size " + str(i))
    plt.hist(retx[i],1+(len(retx[i])//2),histtype='stepfilled',cumulative = False)#,weights=[1/y for y in rety[i]])
    for x in retx[i]:
        mu[j] += x
    mu[j] /= len(retx[i])
    plt.axvline(best[0],color='green')
    plt.axvline(mu[j],color='red')
    plt.show()

mu.append(best[0])
plt.title('mean of optimums versus sample subset size')
plt.plot(range(10),mu,'r-',range(10),mu,'bo')
plt.axhline(best[0],color='green')
plt.show()

