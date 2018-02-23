from lib import optimizer as op

import matplotlib.pyplot as plt


values = op.bruteSearch(op.f1,10000,op.f1bounds)
x = [v[0] for v in values]
bx = x.pop()
y = [v[1] for v in values]
by = y.pop()

plt.plot(x ,y, 'r:', bx, by, "go")
plt.ylabel('value')
plt.xlabel('parameter r' )
plt.show()

values = op.bruteSearch(op.f2,50,op.f2bounds)
best = values.pop()
cbgbc = list(filter(lambda x: x[1] == best[1] and x[2] == best[2], values))
sbgbc = [c[0] for c in cbgbc]
vbgbc = [c[3] for c in cbgbc]
plt.plot(sbgbc , vbgbc, 'r:', best[0], best[3], "go")
plt.ylabel('value')
plt.xlabel('parameter s given best g, best c')
plt.show()

cbgbc = list(filter(lambda x: x[0] == best[0] and x[2] == best[2], values))
sbgbc = [c[1] for c in cbgbc]
vbgbc = [c[3] for c in cbgbc]
plt.plot(sbgbc , vbgbc, 'r:', best[1], best[3], "go")
plt.ylabel('value')
plt.xlabel('parameter g given best s, best c')
plt.show()
cbgbc = list(filter(lambda x: x[0] == best[0] and x[1] == best[1], values))
sbgbc = [c[2] for c in cbgbc]
vbgbc = [c[3] for c in cbgbc]
plt.plot(sbgbc , vbgbc, 'r:', best[2], best[3], "go")
plt.ylabel('value')
plt.xlabel('parameter c given best s, best g')
plt.show()