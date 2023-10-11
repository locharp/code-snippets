def lengthOfNumber( k, d = [ 0 ] ):
	
    for i in range( 1, k + 1 ):
        if len( d ) == i:
            d.append( d[-1] * 10 + 1 )
        
        if d[i] % k == 0:
            return i
        
    return -1
