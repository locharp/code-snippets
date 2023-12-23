def powerOfArray( n: int, k: int, a: List[int] ) -> int:
    
    p = [ 0 ]

    for i in range( n - 1 ):
        p.append( p[-1] + a[i] )
        
    m = q = 0
    
    for i in range( n - 1, -1, -1 ):
        m = max( m, ( a[i] * k ) + p[i] + q )
        q += a[i]
        
    return m
