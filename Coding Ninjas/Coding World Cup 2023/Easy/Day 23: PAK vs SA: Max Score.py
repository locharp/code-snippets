from typing import *

def max_sum( a: List[int] ) -> int:

    return max( a[ i - 1 ] + a[i] for i in range( 1, len( a ) ) )
