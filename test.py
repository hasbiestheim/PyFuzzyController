from Centroid import Centroid
c = Centroid()
p = [(20,0),(34,0.7),(46,0.7),(54,0.3),(66,0.3),(70,0.5),(100,0.5)]
for point in p:
    c.addPoint(point)
c.solve()
print c.x