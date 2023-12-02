from typing import List

def countMoves( n: int, a: List[int] ) -> int:

    o = n
    t = 0

    for i in a:
        o -= i % 2
        j = ( i % 3 )

        if j > 0:
            t += 3 - j

    return min( o, t )
