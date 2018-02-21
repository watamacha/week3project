from lib import optimizer as op

import matplotlib.pyplot as plt


values = op.bruteSearch(op.f1,500,op.f1bounds)
x = [values[z][0] for z in range(len(values)-1)]
y = [values[z][1] for z in range(len(values)-1)]
bx = values[len(values)-1][0]
by = values[len(values)-1][1]



plt.plot(x,y, 'r:', bx, by, "go")
plt.ylabel('value')
plt.xlabel('n')
plt.show()