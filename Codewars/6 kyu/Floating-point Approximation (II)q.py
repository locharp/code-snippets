from math import floor

def interp( f, l, u, n ):
    ans = []
    d = ( u - l ) / n
    
    for i in range( n ):
        ans.append( floor( f( l + i * d ) * 100 ) / 100 )
        
    return ans
