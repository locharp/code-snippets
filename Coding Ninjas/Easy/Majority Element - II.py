from collections import *

def majorityElementII( arr ):
	
	c = Counter( arr )
	n = len( arr ) // 3
	ans = [ i for i, j in c.most_common( 2 ) if j > n ]
	
	return ans
