from math import *

def minimumJumps( x: int, y: int ) -> int:

    if x < 1 or y < 1:
        return max( x, y )
    
    return ( x + y ) // gcd( x, y )
