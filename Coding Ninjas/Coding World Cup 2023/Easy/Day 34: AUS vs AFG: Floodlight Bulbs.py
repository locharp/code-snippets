def removeBulbs(a: List[int]) -> int:
    
    i = 0
    j = len( a ) - 1

    while i < j and a[i] < 1:
        i += 1

    while j > i and a[j] < 1:
        j -= 1

    return a[ i : j ].count( 0 )
