def underwaterValves( n: int, a: list ) -> int:
    
    if len( a ) < 2:
        return 0
        
    p = sorted( ( j, i ) for i, j in enumerate( a ) )
    ans = p[0][1]

    for i in range( 1, n ):
        ans += abs( p[i][1] - p[ i - 1 ][1] )
        
    return ans
