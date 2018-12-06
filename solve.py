#! /usr/bin/python
# _*_coding:utf8_*_

'''
cd /home/benjamin/Bureau/Santa/day4
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

def closest(xp, yp, markers):
	dist = [man(xp, yp, xm, ym) for xm, ym in markers]
	mini = min(dist)
	if dist.count(mini) >1:
		res = -1
	else:
		res = dist.index(mini)
	return res
	return np.array([man(xp, yp, xm, ym) for xm, ym in markers]).argmin()

mapping = np.array([[closest(x, y, data) for y in range(xMin, yMax)] for x in range(xMin, xMax)])
infinite = set()
for i in mapping[ :, 0]: infinite.add(i)
for i in mapping[ :,-1]: infinite.add(i)
for i in mapping[ 0, :]: infinite.add(i)
for i in mapping[-1, :]: infinite.add(i)

flat = list(mapping.flatten())
areas = [flat.count(i) for i in range(nMarkers)]

iMax = -1
aMax = 0
for i in range(nMarkers):
	if i in infinite:
		print "(i) Marker %i area is %i but inifinite."%(i, areas[i])
	else:
		print "(i) Marker %i area is %i."%(i, areas[i])
		if areas[i] > aMax:
			aMax = areas[i]
			iMax = i

print "(i) The greatest finite area is %i, and is associated to marker %i."%(aMax, iMax)

mapping[mapping==iMax] = 100
pylab.matshow(mapping)
pylab.colorbar()
pylab.savefig("graph.png")
pylab.show()

print "See you, space cowboy."

