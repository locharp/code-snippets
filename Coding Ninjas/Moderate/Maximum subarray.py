from collections import *

def maximumSumSubarray( n, arr ):

	d = defaultdict( list )
	a = []
	i = p = q = 0

	for j in range( n ):
		q += arr[j]

		if q < 0:
			q = 0
			i = j + 1
		elif q > p:
			a = [ [ i, j + 1 ] ]
			p = q
		elif q == p:
			a.append( [ i, j + 1 ] )

	if p < 1:
		return [ max( arr ) ]
	
	ans = arr[ a[0][0] : a[0][1] ]

	for i, j in a[ 1 : ]:
		if j - i > len( ans ):
			ans = arr[ i : j ]

	return ans
