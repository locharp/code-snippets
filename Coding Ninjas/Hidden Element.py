from typing import List, Optional

def findHiddenElement( n: int, b: List[ Optional[int] ] ) -> int:

    s = { i for i in range( 1, n + 1 ) }
    curr = 0

    for i in b:
        if i < 0:
            j = curr
        elif curr >= 0:
            s.remove( i - curr )

        curr = i

    return min( s ) + j
