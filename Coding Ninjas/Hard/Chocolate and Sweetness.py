from typing import List
from bisect import bisect_left
from collections import Counter

def chocolatesAndSweetness( n: int, q: int, expiry: List[int], sweetness: List[int], query: List[ List[int] ] ) -> List[int]:

    c = Counter( zip( sweetness, expiry ) )
    a = sorted( c )
    
    return [ sum( c[k] for k in a[ bisect_left( a, ( i, j ) ) : ] if k[0] >= i and k[1] > j ) for i, j in query ]
