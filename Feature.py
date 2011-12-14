class Feature:
    def __init__(self):
        self.name = 'InitFeature'
        # membership functions
        self.mf = []

class MembershipFunction:
    def __init__(self):
        self.name = 'InitMF'
        self.f = Shape()
    def trap(self,a,b,c,d):
        self.f.setPoints([(a,0),(b,1),(c,1),(d,0)])
        self.f.sortPoints()
    def tri(self,a,b,c):
        self.f.setPoints([(a,0),(b,1),(c,0)])
        self.f.sortPoints()
        



