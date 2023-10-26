from typing import List

def ninjaWantsHoliday( n: int, k: int, a: List[int] ) -> str:
    
    a.sort()
    i, j = 0, 1
    
    while i < n:
        j = i + 1

        while j < n and a[j] - 1 == a[ j - 1 ]:
            j += 1

        if j - i >= k:
            return "YES"

        i = j

    return "NO"
