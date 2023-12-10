from typing import List
from itertools import product

def goodnessOfArray( n: int, m: int, a: List[int], b: List[int] ) -> List[int]:
    
    ans = []
    i = m
    
    for p, q in product( a, b ):
        if i == m:
            ans.append( 0 )
            i = 0

        ans[-1] = max( ans[-1], p % q )
        i += 1

    return ans
