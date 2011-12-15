from Shape import Shape

class MembershipFunction:
    def __init__(self):
        self.name = 'InitMF'
        self.f = Shape()
        self.shape = None
    def trap(self,a,b,c,d):
        self.f.setPoints([(a,0),(b,1),(c,1),(d,0)])
        self.f.sortPoints()
        self.shape = 'trap'
        self.points = (a,b,c,d)
    def tri(self,a,b,c):
        self.f.setPoints([(a,0),(b,1),(c,0)])
        self.f.sortPoints()
        self.shape = 'tri'
        self.points = (a,b,c)
    def getResult(self,deg):
        if deg == 1.0:
            f = Shape()
            for p in self.f.points:
                f.addPoint(p)
            return f
        if self.shape == 'trap':
            f = Shape()
            (a,b,c,d) = self.points 
            dx = (b-a)*deg
            dy = deg
            b = a+dx
            dx = (d-c)*deg
            c = d-dx
            f.setPoints([(a,0),(b,dy),(c,dy),(d,0)])
            return f
        if self.shape == 'tri':
            f = Shape()
            (a,b,c) = self.points 
            dx1 = (b-a)*deg
            dx2 = (c-b)*deg
            b = a+dx1
            d = c
            c = d-dx2
            dy = deg
            f.setPoints([(a,0),(b,dy),(c,dy),(d,0)])
            return f

