from collections import defaultdict
from functools import lru_cache

@lru_cache( maxsize = None )
def f( d, m, n, x ):

    if m > x:
        return 2147483647
    elif n == len( d ):
        return x - m
    
    ans = 2147483647

    for i in d[n]:
        ans = min( ans, f( d, m + i, n + 1, x ) )
        
    return ans



def colorfulKnapsack( w, c, m, x ):

    d = defaultdict( set )

    for i in range( len( c ) ):
        d[ c[i] ].add( w[i] )
    
    if len( d ) != m:
        return -1

    e = tuple( tuple( i ) for i in d.values() )
    ans = f( e, 0, 0, x )

    return ans if ans < 2147483647 else -1
