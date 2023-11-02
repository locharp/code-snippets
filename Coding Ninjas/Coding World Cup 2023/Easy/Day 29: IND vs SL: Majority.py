from collections import Counter

def maximumLength( a: list ) -> int:
    
    c = Counter( a )
    k = c.most_common( 1 )
    
    return min( 2 * k[0][1], len( a ) )
