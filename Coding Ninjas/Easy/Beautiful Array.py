from typing import List

def maximumRemovals( n: int, v: List[int] ) -> int:
    
    i = v.index( min( v ) )
    j = v.index( max( v ) )
    
    return len( v ) - max( i, j ) - 1
