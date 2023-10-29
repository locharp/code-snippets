def maximumPower( n: int, a: list ) -> str:
    
    p = sorted( i for i in a if i < 0 )
    q = sorted( i for i in a if i >= 0 )
    ans = -247483648

    if len( p ) > 1:
        ans = p[0] * p[1]
    elif len( p ) > 0:
        ans = p[0] * q[0]

    if len( q ) > 1:
        ans = max( ans, q[-1] * q[-2] )

    return ans
