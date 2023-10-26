from math import gcd

def f( n ):

    d = { 1, n }
    j = n

    for i in range( 2, n ):
        j = n // i

        if n % j == 0:
            d.add( i )
            d.add( j )

        if i >= j:
            break

    return d


    
def differentGCDSubsequence( arr ):
    
    a = sorted( set( arr ) )
    d = { i for i in a }

    for i, j in enumerate( a ):
        s = f( j ) - d
        
        for k in a[ i + 1 : ]:
            if len( s ) < 1:
                break
                
            c = gcd( j, k )
            d.add( c )
            s.discard( c )

    return len( d )
