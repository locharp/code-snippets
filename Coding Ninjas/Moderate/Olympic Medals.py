from typing import List

def f ( p, i, g, s, b ):

    if g < 0 or s < 0 or b < 0:
        return False
    elif g == s == b == 0:
        return True
    
    for j in range( i, len( p ) ):
        if f( p, j + 1, g - p[j][0], s - p[j][1], b - p[j][2] ):
            return True

    return False



def possibleOrNot( n: int, g: int, s: int, b: int, prizes: List[ List[int] ] ) -> int:

    return 1 if f( prizes, 0, g, s, b ) else 0
