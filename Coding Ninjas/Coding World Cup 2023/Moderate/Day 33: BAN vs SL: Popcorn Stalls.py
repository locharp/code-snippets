def isAbleToPlace( n: int, k: int, a: List[int] ) -> int:
    
    i = 2
    n -= 1

    while i < n:
        if a[ i - 1 ] < 1 and a[ i + 1 ] < 1 and a[i] < 1:
            a[i] = 1
            k -= 1
            i += 1

        i += 1

    if ( n < 1 or a[1] < 1 ) and a[0] < 1:
        k -= 1

    if ( n < 1 or a[-2] < 1 ) and a[-1] <1:
        k -= 1

    return 0 if k > 0 else 1
