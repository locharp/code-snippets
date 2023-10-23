from typing import *

def buildingBuilder( n: int, a: List[int] ) -> int:

    ans = [ 100001 ] + [ 0 ] * 5

    for i in a:
        if ans[i] < ans [ i - 1 ]:
            ans[i] += 1

    return min( ans[ 1 : ] )
