from typing import *
from math import ceil

def ballsAndbats( n: int, s: List[int], m: List[int], x: int, y: int ) -> int:

    p = ceil( x / sum( s ) )
    q = ceil( y / sum( m ) )
    
    return max( p, q )
