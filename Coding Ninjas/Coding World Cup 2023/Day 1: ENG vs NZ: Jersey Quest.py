from typing import *

def minDifference( a: List[int] ) -> int:
    a.sort()

    return min( a[i] - a[ i - 1 ] for i in range( 1, len( a ) ) )
