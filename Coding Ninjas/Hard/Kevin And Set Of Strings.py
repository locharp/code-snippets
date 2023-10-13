def distinctStrings( arr,n ):
    s = set()
    
    for a in arr:
        p = tuple( sorted( i for i in a[ : : 2 ] ) )
        q = tuple( sorted( i for i in a[ 1 : : 2 ] ) )
        s.add( ( p, q ) )
        
    return len( s )
