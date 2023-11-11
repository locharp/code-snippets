from collections import *

def doubleCount( n: int, a: list ) -> int:
    
    c = Counter( a )
    ans = 0
    
    for i, j in c.items():
        if i // 2 in c:
            ans += j
            
    return ans
