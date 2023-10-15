from typing import List

def printDivisors( n: int ) -> List[int]:
    ans = [ 1 ]

    for i in range( 2, n + 1 ):
        if n % i == 0:
            ans.append( i )

    return ans
