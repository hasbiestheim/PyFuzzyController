class Centroid:
    def __init__(self):
        self.points = []
        self.x = None
        self.area = None
        self.solved = False
    def addPoint(self,(x,y)):
        self.points.append((x,y))
        self.solved = False
    def solve(self):
        p = self.points
        self.x = 0
        self.area = 0
        for i in range(0,len(p)-1):
            x1,y1 = p[i]
            x2,y2 = p[i+1]
            x1 = float(x1)
            y1 = float(y1)
            x2 = float(x2)
            y2 = float(y2)
            h = x2-x1
            if h>0:
                v = y2-y1
                if y2>y1:
                    y = y2
                else:
                    y = y1
                if v>0:
                    a = h*y/2
                    self.area = self.area + a
                    self.x = self.x + (a*(x2-(h/3)))
                if v<0:
                    a = -1*h*y/2
                    self.area = self.area + a
                    self.x = self.x + (a*(x1+(h/3)))
                if v==0:
                    a = h*y
                    self.area = self.area + a
                    self.x = self.x + (a*(x1+(h/2)))
        self.x = self.x/self.area
        self.solved = True
