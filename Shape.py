from operator import itemgetter

class Segment:
    def __init__(self,p1,p2):
        self.p = [p1, p2]
        x1,y1 = p1
        x2,y2 = p2
        self.x1 = float(x1)
        self.x2 = float(x2)
        self.y1 = float(y1)
        self.y2 = float(y2)
        self.m = (self.y2-self.y1)/(self.x2-self.x1)
        self.b = self.y1 - (self.m*self.x1)
    def y(self, x):
        return x*self.m + self.b
    def intersects(self,other):
        if self.m == other.m:
            return False
        if self.x2 <= other.x1:
            return False
        if other.x2 <= self.x1:
            return False
        s1 = Segment(self.p[0], self.p[1])
        s2 = Segment(other.p[0], other.p[1])
        if s1.x1 < s2.x1:
            s1.y1 = s1.y(s2.x1)
            s1.x1 = s2.x1
        if s1.x2 > s2.x2:
            s1.y2 = s1.y(s2.x2)
            s1.x2 = s2.x2
        if s2.x1 < s1.x1:
            s2.y1 = s2.y(s1.x1)
            s2.x1 = s1.x1
        if s2.x2 > s1.x2:
            s2.y2 = s2.y(s1.x2)
            s2.x2 = s1.x2
        b1 = s1.y1 < s2.y1
        b2 = s1.y2 > s2.y2
        if b1 == b2:
            return True
        return False

class Shape:
    def __init__(self):
        self.points = []
        self.x = None
        self.area = None
        self.sortedPoints = True
        self.solved = False
        self.segments = []
    def __add__(self,other):
        return self
    def addPoint(self,(x,y)):
        self.points.append((x,y))
        if len(self.points)>=2 and x<self.points[-2]:
            self.segments = []
            self.sortedPoints = False
        elif len(self.points)>=2 and self.sortedPoints:
            x1,y1 = self.points[-2]
            x2,y2 = self.points[-1]
            if x1 != x2:
                self.segments.append(Segment(self.points[-2], self.points[-1]))
        self.solved = False
    def setPoints(self,p):
        self.points = p
        self.sortedPoints = True
        for i in range(0,len(p)-1):
            x1,y1 = p[i]
            x2,y2 = p[i+1]
            if x2<x1:
                self.sortedPoints = False
                break
        if self.sortedPoints:
            for i in range(0,len(self.points)-1):
                x1,y1 = self.points[i]
                x2,y2 = self.points[i+1]
                if x1 != x2:
                    self.segments.append(Segment(self.points[i],self.points[i+1]))
        self.solved = False
    def sortPoints(self):
        if not self.sortedPoints:
            self.segments = []
            self.points = sorted(self.points,key=itemgetter(0))
            for i in range(0,len(self.points)-1):
                x1,y1 = self.points[i]
                x2,y2 = self.points[i+1]
                if x1 != x2:
                    self.segments.append(Segment(self.points[i],self.points[i+1]))
            self.sortedPoints = True
    def solve(self):
        self.sortPoints()
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
                    a = h*y/2
                    self.area = self.area + a
                    self.x = self.x + (a*(x1+(h/3)))
                if v==0:
                    a = h*y
                    self.area = self.area + a
                    self.x = self.x + (a*(x1+(h/2)))
        self.x = self.x/self.area
        self.solved = True
