from typing import *

def andQueries( arr: List[int], n: int ) -> int:
    
    ans = arr[0]

    for i in arr[ 1 : ]:
        ans &= i

    return ans
