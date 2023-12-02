from typing import List
from collections import defaultdict

def f( c, d, o, p, q, s ):

    if p and q:
        return False

    for i in d[o]:
        if i in s:
            continue
        
        if c[i] < 2:
            if f( c, d, i, True, q, s | { i } ):
                return True
        elif c[i] < 3:
            if f( c, d, i, p, True, s | { i } ):
                return True
        else:
            return True

    return False



def goodTree( n: int, color: List[int], edges: List[ List[int] ] ) -> int:
    
    d = defaultdict( set )

    for i, j in edges:
        d[ i - 1 ].add( j - 1 )
        d[ j - 1 ].add( i - 1 )
    
    for i in range( n ):
        if color[i] > 2 and i in d:
            if f( color, d, i, False, False, { i } ):
                return 0

    return 1
