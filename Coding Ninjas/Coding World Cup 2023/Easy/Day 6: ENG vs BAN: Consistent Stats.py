from typing import *
from itertools import combinations

def p( n ):
    if n < 4:
        return True

    for i in range( 2, n // 2 ):
        if n % i == 0:
            return False

    return True



def primeSum( n: int, m: int, a: List[int] ) -> int:
    
    ans = 0

    for i in combinations( a, 3 ):
        if p( sum( i ) ):
            ans += 1

    return ans
