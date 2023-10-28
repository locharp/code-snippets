from collections import *

def maxGroups( a: List[int] ) -> int:

    d = defaultdict( list )
    g = [ 0, 0 ]
    n = len( a ) - 1
    ans = []

    for i, j in enumerate( sorted( a ) ):
        d[j].append( i )
    
    for i in range( len( a ) ):
        o = d[ a[i] ].pop( 0 )

        if i > g[-1]:
            g.append( o )
        elif o > g[-1]:
            g[-1] = o

        if g[-1] == n:
            break

    return len( g ) - 1
