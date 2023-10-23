from typing import *

def bestLineup( n: int, x: List[int] ) -> int:

    x.sort( reverse = True )

    return sum( ( x[i] - i ) ** 2 for i in range( n ) )
