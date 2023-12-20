def longestDangerousRange( height, n ):
	
	ans = 1
	c = 1
	d = 0

	for i in range( 1, n ):
		e = height[i] - height[ i - 1 ]

		if e > 0 and d <= 0 or e < 0 and d >= 0:
			c += 1
			ans = max( ans, c )
		elif e == 0:
			c = 1
		else:
			c = 2

		d = e

	return ans
