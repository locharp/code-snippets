def posAndNeg( arr ):
	
	p = []
	q = []

	for i in arr:
		if i < 0:
			q.append( i )
		else:
			p.append( i )

	for i in range( len( q ) ):
		arr[ 2 * i ] = p[i]
		arr[ 2 * i + 1 ] = q[i]
		
	if len( p ) > len( q ):
		arr[-1] = p[-1]
