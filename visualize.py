from lib import optimizer as op

import matplotlib.pyplot as plt


values = op.bruteSearch(op.f1,10000,op.f1bounds)
x = [v[0] for v in values]
bx = x.pop()
y = [v[1] for v in values]
by = y.pop()

plt.plot(x ,y, 'r:', bx, by, "go")
plt.ylabel('value')
plt.xlabel('parameter ' + '0' )
plt.show()

values = op.bruteSearch(op.f2,100,op.f2bounds)
best = values.pop()
cbgbc = filter(lambda x: x[1] == best[1] && x[2] = best[2], values)
sbgbc = [c[0] for c in cbgbc]
vbgbc = [c[3] for c in cbgbc]
plt.plot(sbgbc , vbgbc, 'r:', best[0], best[3], "go")
plt.ylabel('value')
plt.xlabel('s given best g, best c')
plt.show()
