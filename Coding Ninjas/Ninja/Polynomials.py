from typing import *

def multiply( a: List[int], b: List[int], c: int ) -> List[int]:
    
    ans = [ 0 ] * ( c * 2 - 1 )
    
    for i in range( c ):
        for j in range( c ):
            ans[ i + j ] += a[i] * b[j]

    return ans
