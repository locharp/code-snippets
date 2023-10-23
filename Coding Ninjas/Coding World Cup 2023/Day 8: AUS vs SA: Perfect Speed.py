from typing import List
from sortedcontainers import SortedSet

def maxEvenSum( n: int, a: List[int] ) -> int:

    s = SortedSet( { i for i in a if i % 2 == 0 } )
    
    for i in range( len( s ) - 1, -1, -1 ):
        for j in range( i ):
            if s[i] - s[j] in s:
                return s[i]

    return -1
