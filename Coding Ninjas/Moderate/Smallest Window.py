from collections import *

def smallestWindow( s, x ):
    
    a = []
    c = Counter( x )
    d = { i: [] for i in c }
    m = u = v = 2147483647
    n = len( x )
    
    for i, j in enumerate( s ):
        if j in c:
            if c[j] > 0:
                n -= 1
                c[j] -= 1
            else:
                a.remove( d[j].pop( 0 ) )

            d[j].append( i )
            a.append( i )

            if n < 1:
                o = a[-1] - a[0]
                
                if o < m:
                    m = o
                    u = a[0]
                    v = a[-1]
                    
    return s[ u : v + 1 ]
