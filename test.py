#!/usr/bin/python
import unittest
from Shape import *
from MembershipFunction import *
from Ruleset import *

class TestShape(unittest.TestCase):
    def setUp(self):
        self.c = Shape()
        self.ordered = [(20,0),(40,1),(60,0),(80,1),(100,0)]
        self.unordered = [(10.0,0.5),(12,1),(24.000,0),(14.0,0.500),(0,0)]
        self.mftri = MembershipFunction()
        self.mftri.tri(0,2,4)
        self.mftrap = MembershipFunction()
        self.mftrap.trap(0,2,4,6)
        self.mfout = MembershipFunction()
        self.mfout.tri(4,6,8)
        self.mfcold = MembershipFunction()
        self.mfcold.trap(0,0,2,4)
        self.mfdict = {}
        self.mfdict['cold'] = self.mfcold
        self.mfdict['blast'] = self.mfout
        self.rule = Rule(self.mfdict)
        self.cin = {}
        self.cin['temp']=3
    def test_addPoint_presentationValue(self):
        p = [(20,0),(34,0.7),(46,0.7),(54,0.3),(66,0.3),(70,0.5),(100,0.5)]
        for point in p:
            self.c.addPoint(point)
        self.c.solve()
        self.assertEqual(round(self.c.x,3),60.943)
    def test_addPoint_sorted(self):
        p = self.ordered
        for point in p:
            self.c.addPoint(point)
        self.c.solve()
        self.assertEqual(self.c.x,60)
    def test_addPoint_unsorted(self):
        p = self.unordered
        for point in p:
            self.c.addPoint(point)
        self.c.solve()
        self.assertEqual(self.c.x,12)
    def test_setPoints_unsorted(self):
        p = self.unordered
        self.c.setPoints(p)
        self.c.solve()
        self.assertEqual(self.c.x,12)
    def test_resultTri(self):
        self.assertEqual(self.mftri.getResult(0.5).points,[(0,0),(1,0.5),(3,0.5),(4,0)])
    def test_resultTrap(self):
        self.assertEqual(self.mftrap.getResult(0.5).points,[(0,0),(1,0.5),(5,0.5),(6,0)])
    def test_getDegreeTrap(self):
        self.assertEqual(self.mftrap.getDegree(1),0.5)
    def test_getDegreeTri(self):
        self.assertEqual(self.mftri.getDegree(3),0.5)
    def test_heaterRule(self):
        self.rule.addCondition('temp', 'cold')
        self.rule.setResult('heater','blast')
        (feat, shape) = self.rule.getResult(self.cin)
        shape.solve()
        self.assertEqual(shape.x, 6)
    def test_intersects(self):
        s1 = Segment((0,0),(1,1))
        s2 = Segment((0,1),(1,0))
        self.assertTrue(s1.intersects(s2))
    def test_noIntersect(self):
        s1 = Segment((0,0),(1,1))
        s2 = Segment((0,1),(2,3))
        self.assertTrue(not s1.intersects(s2))
    def test_intersect1(self):
        s1 = Segment((0,0),(1,1))
        s2 = Segment((0,1),(1,0))
        self.assertEqual(s1.intersection(s2), (0.5,0.5))
    def test_intersect2(self):
        s1 = Segment((1,3),(3,1))
        s2 = Segment((1,1),(3,3))
        self.assertEqual(s1.intersection(s2), (2.0,2.0))
    def test_addSegment(self):
        s = Shape()
        s.addSegment(Segment((0,0),(1,1)))
        s.addSegment(Segment((1,1),(2,2)))
        s.addSegment(Segment((2,2),(3,0)))
        self.assertEqual(s.points, [(0,0),(1,1),(2,2),(3,0)])
    def test_addShapes(self):
        s1 = Shape()
        s1.setPoints([(0,0),(1,1),(2,1),(3,0)])
        s2 = Shape()
        s2.setPoints([(2,0),(4,2),(5,0)])
        s3 = s1+s2
        self.assertEqual(s3.points, [(0,0),(1,1),(2,1),(2.5,0.5),(4,2),(5,0)])
if __name__ == '__main__':
    unittest.main()
