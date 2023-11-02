def secretCode( n: int, a: List[int] ) -> int:
    
    t = sum( a[ : 3 ] )
    i = 0
    
    if t % 10 == 0:
        return 1

    for j in range( 3, n ):
        t += a[j] - a[i]

        if t % 10 == 0:
            return 1

        i += 1

    return 0
