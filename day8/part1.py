def readNode(descr):
	nNode = int(descr.pop(0))
	nProp = int(descr.pop(0))
	res  = sum( [readNode(descr) for i in range(nNode)] )
	res += sum( [descr.pop(0)    for i in range(nProp)] )
	return res
with open("input.txt", 'r') as f:
	print readNode( [int(e) for e in f.read().split(' ') if e != ""] )
