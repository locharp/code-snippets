from typing import *
from bisect import *

def whichBowler( n: int, v: List[int], q: int, query: List[int] ) -> List[int]:
    
    a = [ v[0] - 1 ]
    ans = []
    
    for i in v[ 1 : ]:
        a.append( a[-1] + i )

    for i in v[ : : -1 ]:
        a.append( a[-1] + i )
    
    for i in query:
        j = bisect_left( a, i % a[-1] )
        
        if j < n:
            j += 1
        else:
            j = n - ( j - n )
            
        ans.append( j )

    return ans
