from collections import *
from itertools import *

def minimumCostsubsets( arr, n, k ):

    if n % k != 0:
        return -1

    m = n // k
    a = [ [] for i in range( k ) ]
    r, s = 0, float( "inf" )
    c= Counter( arr )
    d = []

    for i, j in c.items():
        if j > k:
            return -1
        elif j < k:
            d += [ i ] * j
        else:
            r = max( r, i )
            s = min( s, i )
            m -= 1
    
    if m < 1:
        return ( r - s ) * k

    ans = 2 ** 31

    for p in permutations( d ):
        total = 0
        t = True
        
        for i in range( 0, len( p ), m ):
            u, v = r, s

            if len( set( p[ i : i + m ] ) ) < m:
                t = False
                break
                
            u = max( p[ i : i + m ] + ( u, ) )
            v = min( p[ i : i + m ] + ( v, ) )
            
            total += u - v
        if t:    
            ans = min( ans, total )
        
    return ans
