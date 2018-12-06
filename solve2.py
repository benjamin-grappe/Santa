#! /usr/bin/python
# _*_coding:utf8_*_

'''
cd /home/benjamin/Bureau/Santa/day6
python -i solve.py
'''

import pylab
import numpy as np

f = open("input.txt", 'r')
data = np.array([e.split(", ") for e in f.read().split('\n') if e != ""], dtype=int)
xMin, xMax, xSpan = data[:,0].min(), data[:,0].max(), data[:,0].ptp()
yMin, yMax, ySpan = data[:,1].min(), data[:,1].max(), data[:,1].ptp()
nMarkers = len(data)

def man(xp, yp, xm, ym):
	return abs(xp-xm) + abs(yp-ym)

def dist2all(xp, yp, markers):
	return sum([man(xp, yp, xm, ym) for xm, ym in markers])

mapping = np.array([[dist2all(x, y, data) for y in range(xMin, yMax)] for x in range(xMin, xMax)])

mask = mapping < 10000
mapping[:,:] = 0
mapping[     mask] = 1

print "(i) Area of interest is %i large."%mapping.sum()

pylab.matshow(mapping)
pylab.savefig("graphPart2.png")
pylab.show()

print "See you, space cowboy."

