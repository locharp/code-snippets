from typing import List

def minimumSubarray( n: int, x: int, y: int, a: List[int] ) -> int:
    
    i = p = q = 0
    ans = n + 1

    for j in range( n ):
        if a[j] == 0:
            continue
        elif a[j] < 0:
            x -= a[j]
        else:
            y -= a[j]

        while x >= 0 and y <= 0:
            ans = min( ans, j - i + 1 )
            if a[i] < 0:
                x += a[i]
            elif a[i] > 0:
                y += a[i]

            i += 1

    return -1 if ans > n else ans
