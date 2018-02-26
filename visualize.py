from lib import optimizer as op
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.axes as ax
i1=125000
i2=100
values = op.bruteSearch(op.f1,i1,op.f1bounds)
x = [v[0] for v in values]
bx = x.pop()
y = [v[1] for v in values]
by = y.pop()
print([bx,by])
plt.plot(x ,y, 'r-', bx, by, "go")
plt.ylabel('value')
plt.xlabel('parameter r' )
plt.show()

values = op.bruteSearch(op.f2,i2,op.f2bounds)
best = values.pop()
print(best)
cbgbc = list(filter(lambda x: x[1] == best[1] and x[2] == best[2], values))
sbgbc = [c[0] for c in cbgbc]
vbgbc = [c[3] for c in cbgbc]
plt.plot(sbgbc , vbgbc, 'r-', best[0], best[3], "go")
plt.ylabel('value')
plt.xlabel('parameter s given best g, best c')
plt.show()

cbgbc = list(filter(lambda x: x[0] == best[0] and x[2] == best[2], values))
sbgbc = [c[1] for c in cbgbc]
vbgbc = [c[3] for c in cbgbc]
plt.plot(sbgbc , vbgbc, 'r-', best[1], best[3], "go")
plt.ylabel('value')
plt.xlabel('parameter g given best s, best c')
plt.show()

cbgbc = list(filter(lambda x: x[0] == best[0] and x[1] == best[1], values))
sbgbc = [c[2] for c in cbgbc]
vbgbc = [c[3] for c in cbgbc]
plt.plot(sbgbc , vbgbc, 'r-', best[2], best[3], "go")
plt.ylabel('value')
plt.xlabel('parameter c given best s, best g')
plt.show()

#constant s
plt.title("Heatmap of value versus G and C with best S")
sgvbc = list(filter(lambda v: v[0] == best[0], values))
sgvbc = [[v[1],v[2],v[3]] for v in sgvbc]
sgvbc = sorted(sgvbc, key=lambda v: v[0])
gvbcss = []
for p in sgvbc:
    if len(gvbcss) == 0:
        gvbcss.append([p])
    else:
        if gvbcss[len(gvbcss) - 1][0][0] == p[0]:
            gvbcss[len(gvbcss) - 1].append(p)
        else:
            gvbcss.append([p])
for cluster in gvbcss:
    cluster = sorted(cluster,key=lambda v: v[1])
sgm = [[x[2] for x in cluster] for cluster in gvbcss]
sizes = op.getstepsizes(i2,op.f2bounds)
ar = sizes[2]/sizes[1]
sgmap = np.array([np.array(xi) for xi in sgm])
plt.imshow(sgmap,cmap='hot',origin='lower',aspect=ar,extent=[op.f2bounds[2][0],op.f2bounds[2][1],op.f2bounds[1][0],op.f2bounds[1][1]])
plt.xlabel("parameter c")
plt.ylabel("parameter g")
point = [best[2],best[1]]
plt.plot(point[0], point[1], 'go')
plt.show()

#constant g
plt.title("Heatmap of value versus S and C with best G")
sgvbc = list(filter(lambda v: v[1] == best[1], values))
sgvbc = [[v[0],v[2],v[3]] for v in sgvbc]
sgvbc = sorted(sgvbc, key=lambda v: v[0])
gvbcss = []
for p in sgvbc:
    if len(gvbcss) == 0:
        gvbcss.append([p])
    else:
        if gvbcss[len(gvbcss) - 1][0][0] == p[0]:
            gvbcss[len(gvbcss) - 1].append(p)
        else:
            gvbcss.append([p])
for cluster in gvbcss:
    cluster = sorted(cluster,key=lambda v: v[1])
sgm = [[x[2] for x in cluster] for cluster in gvbcss]
sizes = op.getstepsizes(i2,op.f2bounds)
ar = sizes[2]/sizes[0]
sgmap = np.array([np.array(xi) for xi in sgm])
plt.imshow(sgmap,cmap='hot',origin='lower',aspect=ar,extent=[op.f2bounds[2][0],op.f2bounds[2][1],op.f2bounds[0][0],op.f2bounds[0][1]])
plt.xlabel("parameter c")
plt.ylabel("parameter s")
point = [best[2],best[0]]
plt.plot(point[0], point[1], 'go')
plt.show()


#constant c
plt.title("Heatmap of value versus S and G with best C")
sgvbc = list(filter(lambda v: v[2] == best[2], values))
sgvbc = [[v[0],v[1],v[3]] for v in sgvbc]
sgvbc = sorted(sgvbc, key=lambda v: v[0])
gvbcss = []
for p in sgvbc:
    if len(gvbcss) == 0:
        gvbcss.append([p])
    else:
        if gvbcss[len(gvbcss) - 1][0][0] == p[0]:
            gvbcss[len(gvbcss) - 1].append(p)
        else:
            gvbcss.append([p])
for cluster in gvbcss:
    cluster = sorted(cluster,key=lambda v: v[1])
sgm = [[x[2] for x in cluster] for cluster in gvbcss]
sizes = op.getstepsizes(i2,op.f2bounds)
ar = sizes[1]/sizes[0]
sgmap = np.array([np.array(xi) for xi in sgm])
plt.imshow(sgmap,cmap='hot',origin='lower',aspect=ar,extent=[op.f2bounds[1][0],op.f2bounds[1][1],op.f2bounds[0][0],op.f2bounds[0][1]])
plt.xlabel("parameter g")
plt.ylabel("parameter s")
point = [best[1],best[0]]
plt.plot(point[0], point[1], 'go')
plt.show()

