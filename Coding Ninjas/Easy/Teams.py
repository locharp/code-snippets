from math import *
from typing import *

def teams( L: int, R: int ) -> List[ List[int] ]:
    
    ans = []
    s = { i for i in range( L, R + 1 ) }

    while len( s ) > 0:
        p = s.pop()

        for i in s:
            if gcd( p, i ) == 1:
                q = i
                break

        s.remove( q )
        ans.append( [ p, q ] )
    
    return [ 1 ] + ans
