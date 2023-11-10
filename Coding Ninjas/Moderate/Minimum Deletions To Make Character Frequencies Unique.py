from collections import *

def f( n ):
    if n < 2:
        return n
    
    return n + f( n - 1 )



def minDeletions( str ):
    
    c = Counter( str )
    a = sorted( c.values() )
    s = { a[-1] }
    ans = m = n = 0
    
    for i in range( len( a ) - 2, -1, -1 ):
        if a[i] in s:
            n += 1
        else:
            m = min( n, a[ i + 1 ] - a[i] - 1 )
            n -= m
            ans += f( m ) + n * ( a[ i + 1 ] - a[i] )
            s.add( a[i] )
            
    m = min( n, a[0] - 1 )
    n -= m
    
    return ans + f( m ) + n * a[0]
