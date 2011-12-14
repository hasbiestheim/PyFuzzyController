#!/usr/bin/python
import unittest
from Centroid import Centroid

class TestCentroid(unittest.TestCase):
    def test_presentationValue(self):
        c = Centroid()
        p = [(20,0),(34,0.7),(46,0.7),(54,0.3),(66,0.3),(70,0.5),(100,0.5)]
        for point in p:
            c.addPoint(point)
        c.solve()
        self.assertEqual(round(c.x,3),60.943)
    def test_mid1(self):
        c = Centroid()
        p = [(20,0),(40,1),(60,0),(80,1),(100,0)]
        for point in p:
            c.addPoint(point)
        c.solve()
        self.assertEqual(c.x,60)
    def test_mid2(self):
        c = Centroid()
        p = [(0,0),(10.0,0.5),(12,1),(14.0,0.500),(24.000,0)]
        for point in p:
            c.addPoint(point)
        c.solve()
        self.assertEqual(c.x,12)

if __name__ == '__main__':
    unittest.main()
