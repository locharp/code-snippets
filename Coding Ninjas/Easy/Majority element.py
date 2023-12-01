from collections import *

def findMajorityElement( arr, n ):
	
	c = Counter( arr )
	m = n // 2

	for i, j in c.items():
		if j > m:
			return i

	return -1
