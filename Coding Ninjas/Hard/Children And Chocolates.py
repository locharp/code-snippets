from typing import *

def f( ans, a, c, j ):
    if c < 0:
        return -1
    elif c == 0:
        return ans

    n = 0

    for i in range( j, len( a ) ):
        if c - a[i][1] < 0:
            break
            
        n = max( n, f( a[i][1], a, c - a[i][0], i + 1 ) )
        
    return ans + n



def countChildren( n: int, friends: List[ List[int] ], m: int, chocolates: List[int], c: int ) -> int:
    
    a = []
    z = []

    for i, j in friends:
        t = None
        k = 0
        
        while k < len( z ):
            if i in z[k] or j in z[k]:
                if t is None:
                    t = z[k]
                    z[k].add( i )
                    z[k].add( j )
                else:
                    t.update( z[k] )
                    z.pop( k )
                    continue

            k += 1

        if t is None:
            z.append( { i, j } )

    a = [ [ 0, len( z[i] ) ] for i in range( len( z ) ) ]

    for i, j in enumerate( chocolates ):
        t = True

        for k in range( len( z ) ):
            if i + 1 in z[k]:
                a[k][0] += j
                t = False
        
        if t:
            a.append( [ j, 1 ] )

    a.sort()

    return f( 0, a, c, 0 )
