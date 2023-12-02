from typing import *

def minDiff( n : int, arr : List[int] ) -> int:
    
    arr.sort()
    ans = 2147483647
    j = arr[0]
    
    for i in arr[ 1 : ]:
        ans = min( ans, abs( i - j ) )
        j = i
        
    return ans
