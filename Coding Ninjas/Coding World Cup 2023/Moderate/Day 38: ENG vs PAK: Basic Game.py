from typing import *

def basicGame( n: int, k: int, a: List[int] ) -> int:
    
    ans = 0
    a.sort()
    
    for i in range( 1, n ):
        if a[i] - a[ i - 1 ] <= k:
            ans += 1
            
    return ans
