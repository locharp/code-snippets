def countBeautifulPairs( arr, low, high ):

	if len( arr ) < 2:
		return 0

	c = Counter( arr )
	a = list( c.keys() )
	ans = 0

	for i in range( len( a ) ):
		for j in range( i + 1, len( a ) ):
			x = a[i] ^ a[j]

			if x >= low and x <= high:
				ans += c[ a[i] ] * c[ a[j] ]

	return ans
