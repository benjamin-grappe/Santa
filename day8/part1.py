def readNode(descr):
	'''
	Take a list of integer, with the first elements being the number of nodes and
	the number of metadata to be read.
	Caution : Descr will be shorten while the function reads the node (and its children).
	Returns the sum of the metadata of the higher level node and its children.
	'''
	nNode = descr.pop(0) # number of child nodes
	nMeta = descr.pop(0) # number of properties
	res = 0

	for i in range(nNode):
		res += readNode(descr) # add the result of each child node

	# At this step, no more children nodes are in the list.
	# Next values will be the own node's metadata
	for i in range(nMeta):
		res += descr.pop(0)

	return res

with open("defi.txt", 'r') as f:
	print readNode( [int(e) for e in f.read().split(' ') if e != ""] )
