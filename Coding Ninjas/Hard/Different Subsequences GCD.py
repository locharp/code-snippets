from math import gcd

def differentGCDSubsequence( arr ):
    
    a = tuple( set( arr ) )
    d = { i for i in a }

    for i, j in enumerate( a ):
        for k in a[ i + 1 : ]:
            d.add( gcd( j, k ) )

    return len( d )
