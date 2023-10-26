from typing import *

def bitwise_inclusion( n: int, a: List[int] ) -> int:

    ans = 0

    for i in range( n ):
        j = i + 1
        k = a[i]

        while j < n and k > 0:
            k &= a[j]
            j += 1

        ans += ( j - i ) * a[i]
    
    return ans
