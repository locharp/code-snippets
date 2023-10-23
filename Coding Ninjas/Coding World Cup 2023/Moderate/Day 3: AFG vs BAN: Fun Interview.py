from typing import *
from math import ceil

def countOperations( n: int, a: List[int], x: int, q: int, queries: List[List[int]] ) -> List[int]:

    ans = []
    m = sum( a )

    for i, j in queries:
        m -= a[i] - j
        a[i] = j
        ans.append( ceil( m / x ) )

    return ans
