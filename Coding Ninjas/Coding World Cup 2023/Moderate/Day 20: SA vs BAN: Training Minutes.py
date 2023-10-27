from typing import *

def god_of_thunder( n: int, a: List[int] ) -> int:
    
    if len( a ) < 2:
        return -1

    s = m = 0

    for i in a:
        s += i
        m = max( m, i )

    if m * 2 > s or s % 2 == 1:
        return -1
    else:
        return s // 2
