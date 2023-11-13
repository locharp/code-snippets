from typing import *

def f( ans, a, z, c, j ):
    if c < 0:
        print( -1, c, j )
        return -1

    for i in range( j, len( a ) ):
        if i < len( z ):
            e = len( z[i] )
        else:
            e = 1

        ans = max( ans, f( ans + e, a, z, c - a[i], i + 1 ) )
    print( ans, c, j )
    return ans



def countChildren( n: int, friends: List[ List[int] ], m: int, chocolates: List[int], c: int ) -> int:
    
    a = []
    z = []

    for i, j in friends:
        t = None

        for w in z:
            if i in w or j in w:
                if t is None:
                    t = w
                    w.add( j )
                    w.add( j )
                else:
                    t.update( w )
        
        if t is None:
            z.append( { i, j } )

    a = [ 0 ] * len( z )

    for i, j in enumerate( chocolates ):
        t = True

        for k in range( len( z ) ):
            if i + 1 in z[k]:
                a[k] += j
                t = False
        
        if t:
            a.append( j )
    print( z )
    print( a )
    return f( 0, a, z, c, 0 )
