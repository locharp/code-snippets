def oddToEven( num ):
	
	n = num[0]
	a = []
	c = []
	t = True

	for i in range( len( n ) ):
		j = int( n[i] )
		a.append( n[i] )
		
		if j % 2 == 0:
			c.append( i )
	
	if len( c ) < 1:
		return -1
		
	for i in range( len( c ) ):
		if a[ c[i] ] < a[-1]:
			a[ c[i] ], a[-1] = a[-1], a[ c[i] ]
			t = False
			break

	if t:
		a[ c[-1] ], a[-1] = a[-1], a[ c[-1] ]

	return "".join( a )
