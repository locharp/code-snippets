def mxdiflg( a1, a2 ):
    
    if len( a1 ) == 0 or len( a2 ) ==0:
        return -1
    
    m = sorted( len( s ) for s in a1 )
    n = sorted( len( s ) for s in a2 )
    
    return max( abs( m[-1] - n[0] ), abs( n[-1] - m[0] ) 
