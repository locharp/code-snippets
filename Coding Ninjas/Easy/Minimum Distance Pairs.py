from typing import *
from collections import defaultdict
from itertools import combinations

def minimumDistancePairs( n: int, arr: List[int] ) -> int:
    
    d = defaultdict( int )

    for i, j in combinations( arr, 2 ):
        d[ abs( i - j ) ] += 1

    return d[ min( d ) ]
