from typing import *


def bestWorkers( n: int, k: int, a: List[int] ) -> int:
    
    ans = c = sum( a[ : k ] )

    for i in range( k, len( a ) ):
        c += a[i] - a[ i - k ]
        ans = max( ans, c )

    return ans
