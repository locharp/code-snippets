from collections import *
from sortedcontainers import *

def minimumCostsubsets( arr, n, k ):

    if n % k != 0:
        return -1

    m = n // k
    a = [ [] for i in range( k ) ]
    r, s = 0, float( "inf" )
    c = Counter( arr )
    d = SortedList()
    
    for i, j in c.items():
        if j > k:
            return -1
        elif j < k:
            d += [ i ] * j
        else:
            for j in a:
                j.append( i )
    
    for i in range( ( k + 1 ) // 2 ):
        s = SortedSet( d )
    
        for j in range( len( a[i] ), m ):
            p = s.pop( 0 )
            d.remove( p )
            a[i].append( p )

        s = SortedSet( d )
        
        for j in range( len( a[ k - i - 1 ] ), m ):
            p = s.pop( -1 )
            d.remove( p )
            a[ k - i - 1 ].append( p )
            
    return sum( max( i ) - min( i ) for i in a )
