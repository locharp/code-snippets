def countPairs( n: int, a: list ) -> int:
    
    a.sort()
    p = a.count( a[0] )
    
    if p == len( a ):
        return p * ( p - 1 )

    q = a.count( a[-1] )

    return p * q * 2
