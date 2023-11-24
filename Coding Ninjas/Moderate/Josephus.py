def f( a, i, k ):
    
    if len( a ) < 2:
        return a[0]
    
    j = ( i + k ) % len( a )
    a.pop( j )
    
    return f( a, j % len( a ), k )
    
    
    
def Josephus( n, k ):
    
    return f( [ i for i in range( 1, n + 1 ) ], 0, k - 1 )
