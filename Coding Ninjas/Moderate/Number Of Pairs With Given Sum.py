from collections import Counter

def f( n ):

	if n < 3:
		return n - 1

	return n - 1 + f( n - 1 )



def pairsWithGivenSum( arr, n, target ):
	
	c = Counter( arr )
	ans = 0

	if target % 2 == 0 and target // 2 in c:
		ans += f( c[ target // 2 ] )
		del c[ target // 2 ]

	while len( c ) > 0:
		i, j = c.popitem()

		if target - i in c:
			ans += j * c.pop( target - i )

	return ans
