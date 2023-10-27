def good_subarray( a: List[int] ) -> int:
    
    a.sort()
    i = m = 0
    j = 1

    while j < len( a ):
        if a[j] - a[i] > 10:
            m = max( m, j - i )
            
            while a[j] -a[i] > 10:
                i += 1

        j += 1

    m = max( m, j - i )

    return m
