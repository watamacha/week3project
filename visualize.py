from lib import optimizer as op

import matplotlib.pyplot as plt


values = op.bruteSearch(op.f2,30,op.f2bounds)
x = [[values[z][k] for z in range(len(values)-1)] for k in range(len(values[0])-1)]
y = [values[z][len(x)] for z in range(len(values)-1)]
bx = [values[len(values)-1][k] for k in range(len(values[0])-1)]
by = values[len(values)-1][len(bx)]

for p in range(len(bx)):
    plt.plot(x[p] ,y, 'r:', bx[p], by, "go")
    plt.ylabel('value')
    plt.xlabel('parameter ' + str(p) )
    plt.show()