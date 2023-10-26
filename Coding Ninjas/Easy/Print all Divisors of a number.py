from typing import List

def printDivisors( n: int ) -> List[int]:
    ans = { 1, n }

    for i in range( 2, n ):
        j = n // i

        if n % i == 0:
            ans.add( i )
            ans.add( j )

        if i >= j:
            break

    return sorted( ans )
