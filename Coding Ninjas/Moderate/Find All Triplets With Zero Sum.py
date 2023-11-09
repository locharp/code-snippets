from collections import *

def f( a, c, m, n, o, t, ans ):

    if o > 2:
        if n == 0:
            ans.append( t )

        return
    
    for i in range( m, len( a ) ):
        if a[i] + n > 0:
            break

        if c[ a[i] ] > 0:
            c[ a[i] ] -= 1
            f( a, c, i, n + a[i], o + 1, t + [ a[i] ], ans )
            c[ a[i] ] += 1
            

        
def findTriplets( arr, n ):
    
    c = Counter( arr )
    a = sorted( c )
    ans = []
    f( a, c, 0, 0, 0, [], ans )

    return ans
