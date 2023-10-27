from typing import *


def equalArrays(n: int, m: int, a: List[int], b: List[int]) -> int:
    
    ans = p = q = 0
    m -= 1
    n -= 1

    while m >= 0 and n >= 0:
        
        if p == 0:
            p += b[m]
            q += a[n]
            m -= 1
            n -= 1
        elif p == q:
            ans += 1
            p = q = 0
        elif p < q:
            p += b[m]
            m -= 1
        else:
            q += a[n]
            n -= 1
    
    while m >= 0:
        p += b[m]
        m -= 1

    while n >= 0:
        q += a[n]
        n -= 1

    if p == q:
        return ans + 1
    else:
        return -1
